#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import threading
import time
import csv
import json
import random
import sqlite3
import re

import urllib2
import requests
import MySQLdb as mdb

import tornado.escape
import tornado.ioloop
import tornado.web

import modd
import const as Const

from datetime import date, datetime
from urllib2 import quote

from kik.error import KikError
from kik import KikApi, Configuration
from kik.messages import messages_from_json, TextMessage, StartChattingMessage, LinkMessage, PictureMessage, StickerMessage, ScanDataMessage, UnknownMessage, VideoMessage, SuggestedResponseKeyboard, TextResponse, CustomAttribution, ReadReceiptMessage

Const.SLACK_TOKEN = 'IJApzbM3rVCXJhmkSzPlsaS9'

Const.DB_HOST = 'external-db.s4086.gridserver.com'
Const.DB_NAME = 'db4086_modd'
Const.DB_USER = 'db4086_modd_usr'
Const.DB_PASS = 'f4zeHUga.age'

Const.MAX_REPLIES = 3
Const.INACTIVITY_THRESHOLD = 12


#=- -=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=- -=#



#--:-- Message UI / Message Part Factories --:--#
#-=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- #

def default_keyboard():
  keyboard = [
    SuggestedResponseKeyboard(
      hidden = False,
      responses = [
        TextResponse(u"Pokémon Go"),
        # TextResponse(u"Pokemon Go"),
        TextResponse("Dota 2"),
        TextResponse("League of Legends"),
        TextResponse("CS:GO"),
        TextResponse("Cancel")
      ]
    )
  ]
  
  return keyboard
  

def default_text_reply(message, delay=0, type_time=500):
  print "default_text_reply(message=%s)" % (message)
  
  return TextMessage(
    to = message.from_user,
    chat_id = message.chat_id,
    body = "Select a game that you need help with. Type cancel anytime to end this conversation.",
    keyboards = default_keyboard(),
    type_time = type_time,
    delay = delay
  )


def default_wait_reply(message):
  print "default_wait_reply(message=%s)" % (message)
  
  topic_name = ""
  if message.from_user in gameHelpList:
    topic_name = gameHelpList[message.from_user]

  
  if message.chat_id in help_convos:
    topic_name = help_convos[message.chat_id]['game']

  
  if len(topic_name) == 0:
    return TextMessage(
      to = message.from_user,
      chat_id = message.chat_id,
      body = "Your message has been receieved, but we don't know what to make of it. Try something else.",
      type_time = 500
    )
  
  else:
    return TextMessage(
      to = message.from_user,
      chat_id = message.chat_id,
      body = "Your message has been routed to the {topic_name} coaches and is in queue to be answered shortly.".format(topic_name=topic_name),
      type_time = 500
    )

 

#--:-- Model / Data Retrieval --:--#
#-=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- #

def fetch_topics():
  print "fetch_topics()"
  _arr = []
  
  try:
    conn = sqlite3.connect("%s/data/sqlite3/kikbot.db" % (os.getcwd()))
    c = conn.cursor()
    c.execute("SELECT display_name FROM topics WHERE enabled = 1;")
    
    for row in c.fetchall():
      _arr.append(row[0])
      key_name = re.sub( '\s+', "_", row[0])
      print "UTF-8 ENCODED : [%s]" % (quote(row[0].key_name.encode('utf-8')).toLower())
    
    conn.close()
  
  except:
    pass
  
  finally:
    pass
  
  print "_arr:%s" % (_arr)
  return _arr
  

def fetch_slack_webhooks():
  print "fetch_slack_webhooks()"
  _obj = {}
  
  try:
    conn = sqlite3.connect("%s/data/sqlite3/kikbot.db" % (os.getcwd()))
    c = conn.cursor()
    c.execute("SELECT topics.display_name, slack_channels.channel_name, slack_channels.webhook FROM slack_channels INNER JOIN topics ON topics__slack_channels.slack_channel_id = topics.id INNER JOIN topics__slack_channels ON topics__slack_channels.topic_id = topics.id AND topics__slack_channels.slack_channel_id = slack_channels.id WHERE slack_channels.enabled = 1;")
    
    for row in c.fetchall():
      _obj[row[0]] = {
        'channel_name'  : row[1],
        'webhook'       : row[2]
      }
    
    conn.close()
  
  except:
    pass
  
  finally:
    pass
  
  print "_obj:%s" % (_obj)
  return _obj
  

def fetch_faq(topic_name):
  print "fetch_faq(topic_name=%s)" % (topic_name)
  
  _arr = []
  
  try:
    conn = sqlite3.connect("%s/data/sqlite3/kikbot.db" % (os.getcwd()))
    c = conn.cursor()
    c.execute("SELECT faq_content.entry FROM faqs JOIN faq_content ON faqs.id = faq_content.faq_id WHERE faqs.title = \'%s\';" % (topic_name))
    
    for row in c.fetchall():
      _arr.append(row[0])
    
    conn.close()
  
  except:
    pass
  
  finally:
    pass
  
  return _arr


def annul_idle_activity(chat_id):
  print "annul_idle_activity(chat_id={chat_id}) ::{t}".format(chat_id=chat_id, t=help_convos[chat_id]['idle_timer'])

  if help_convos[chat_id]['idle_timer'] is not None:
    t = help_convos[chat_id]['idle_timer']
    t.cancel()


  t = threading.Timer(Const.INACTIVITY_THRESHOLD, annul_idle_activity, [chat_id]).start()

  help_convos[chat_id]['last_message'] = datetime.now()
  help_convos[chat_id]['idle_timer'] = t



#--:-- Session Subpaths / In-Session Seqs --:--#
#-=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- -=:=- #

def welcome_intro_seq(message, is_mention=False):
  print "welcome_intro_seq(message=%s, is_mention=%d)" % (message, is_mention)
  
  modd.utils.sendTracker("bot", "init", "kik")
  
  if is_mention:
    participants = message.participants
    participants.remove(message.from_user)
    
    print ("MENTION PARTICIPANT:%s" % (int(time.time()), participants[0]))
    
    kik.send_messages([
      TextMessage(
        to = message.from_user,
        chat_id = message.chat_id,
        body = u"Welcome to GameBots, looks like a friend has mentioned me!",
        type_time = 500
      ),
    
      TextMessage(
        to = message.from_user,
        chat_id = message.chat_id,
        body = u"Become a better eSports player with GameBots live chat support.",
        type_time = 500,
        delay = 1250
      ),
      default_text_reply(message=message, delay=2750)
    ])
    
    
  else:
    kik.send_messages([
      TextMessage(
        to = message.from_user,
        chat_id = message.chat_id,
        body = u"Welcome to GameBots!",
        type_time = 333
      ),
    
      TextMessage(
        to = message.from_user,
        chat_id = message.chat_id,
        body = u"Become a better eSports player with GameBots live chat support.",
        type_time = 500,
        delay = 1000
      ),
      default_text_reply(message=message, delay=2500)
    ])

  return


def start_help(message):
    print "start_help(message=%s)" % (message)
    modd.utils.sendTracker("bot", "question", "kik")
    gameHelpList[message.from_user] = message.body
    
    kik.send_messages([
      TextMessage(
        to = message.from_user,
        chat_id = message.chat_id,
        body = "Please describe what you need help with. Note your messages will be sent to %s coaches for support." % (message.body),
        type_time = 333
      )
    ])
    
    return


def end_help(to_user, chat_id, user_action=True):
  print "end_help(to_user=\'%s\', chat_id=\'%s\', user_action=%d)" % (to_user, chat_id, user_action)
  
  if not user_action:
    kik.send_messages([
      TextMessage(
        to = to_user,
        chat_id = chat_id,
        body = u"This %s help session is now closed." % (help_convos[chat_id]['game']),
        type_time = 250,
      )
    ])
  
  if chat_id in help_convos:
    if user_action:
      modd.utils.slack_im(help_convos[chat_id], "Help session closed.")
    
    if help_convos[chat_id]['idle_timer'] is not None:
      help_convos[chat_id]['idle_timer'].cancel()
      help_convos[chat_id]['idle_timer'] = None
      
    del help_convos[chat_id]
  
  time.sleep(3)
  cancel_session(to_user, chat_id)
  
  return


def cancel_session(to_user, chat_id):
  print "cancel_session(to_user=\'%s\', chat_id=\'%s\')" % (to_user, chat_id)
  
  #-- send to kik user
  kik.send_messages([
    TextMessage(
      to = to_user,
      chat_id = chat_id,
      body = "Ok, Thanks for using GameBots!",
      type_time = 250,
    )
  ])
  
  if to_user in gameHelpList:
    del gameHelpList[to_user]
  
  if chat_id in help_convos:
    del help_convos[chat_id]
  
  return
    



# -[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]- #

class KikBot(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
  
  def post(self):
    print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= @%s" % (datetime.now())
    
    #-- missing header
    if not kik.verify_signature(self.request.headers.get('X-Kik-Signature'), self.request.body):
      print "self.request.headers.get('X-Kik-Signature')=%s" % (self.request.headers.get('X-Kik-Signature'))
      print "403 Forbidden"
      self.set_status(403)
      return
    
    
    #-- parse
    data_json = tornado.escape.json_decode(self.request.body)
    messages = messages_from_json(data_json["messages"])
    
    #-- each message
    for message in messages:
      
      # -=-=-=-=-=-=-=-=- UNSUPPORTED TYPE -=-=-=-=-=-=-=-=-
      if isinstance(message, LinkMessage) or isinstance(message, PictureMessage) or isinstance(message, VideoMessage) or isinstance(message, ScanDataMessage) or isinstance(message, StickerMessage) or isinstance(message, UnknownMessage):
        print "=-= IGNORING MESSAGE =-=\n%s " % (message)
        kik.send_messages([
          TextMessage(
            to = message.from_user,
            chat_id = message.chat_id,
            body = "I'm sorry, I cannot understand that type of message.",
            type_time = 250
          ),
          default_text_reply(message=message)
        ])
        
        self.set_status(200)
        return
          
      
      # -=-=-=-=-=-=-=-=- READ RECEIPT MESSAGE -=-=-=-=-=-=-=-=-
      elif isinstance(message, ReadReceiptMessage):
        # print "-= ReadReceiptMessage =-= "
        
        modd.utils.sendTracker("bot", "read", "kik")
        self.set_status(200)
        return
         
      
      # -=-=-=-=-=-=-=-=- START CHATTING -=-=-=-=-=-=-=-=-
      elif isinstance(message, StartChattingMessage):
        print "-= StartChattingMessage =-= "
        
        welcome_intro_seq(message)
        self.set_status(200)
        return
        
      
      # -=-=-=-=-=-=-=-=- TEXT MESSAGE -=-=-=-=-=-=-=-=-
      elif isinstance(message, TextMessage):
        print "=-= TextMessage =-= "
        
        try:
          conn = mdb.connect(Const.DB_HOST, Const.DB_USER, Const.DB_PASS, Const.DB_NAME);
          with conn:
            cur = conn.cursor()
            cur.execute("INSERT IGNORE INTO `kikbot_logs` (`username`, `chat_id`, `body`) VALUES (\'%s\', \'%s\', \'%s\')" % (message.from_user, message.chat_id, quote(message.body.encode('utf-8'))))
        
        except mdb.Error, e:
          print "MySqlError %d: %s" % (e.args[0], e.args[1])
        
        finally:
          if conn:
            conn.close()
        
        
        # print "[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]"
        print "-=- help_convos -=- %s" % (help_convos)
        print "[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]"
        
        
        # -=-=-=-=-=-=-=-=-=- END SESSION -=-=-=-=-=-=-=-
        if message.body.lower() == "!end" or message.body.lower() == "cancel" or message.body.lower() == "quit":
          print "-=- ENDING HELP -=-"
          end_help(message.from_user, message.chat_id)
          self.set_status(200)
          return
        
        
        # -=-=-=-=-=-=-=-=-=- MENTIONS -=-=-=-=-=-=-=-=-
        if message.mention is not None:
          if message.body == "Start Chatting":
            pass
            
          #-- other mention type -- toss messages at 'em
          else:
            welcome_intro_seq(message)
                      
          self.set_status(200)
          return
        else:
          
          
          #-- reset timeout
          if message.chat_id in help_convos:
            annul_idle_activity(message.chat_id)
          
          
          # -=-=-=-=-=-=-=-=- DEFAULT GAME BTNS -=-=-=-=-=-=-=-=-
          if message.body == u"Pokémon Go" or message.body == "CS:GO" or message.body == "Dota 2" or message.body == "League of Legends":
            if len(gameHelpList) == 0:
              start_help(message)
              
              print "SUBSCRIBING \"%s\" TO \"%s\" --> %s" % (message.from_user, quote(message.body.lower().encode('utf-8')), message.chat_id)
              modd.utils.sendTracker("bot", "subscribe", "kik")
              
              _sub = urllib2.urlopen('http://beta.modd.live/api/streamer_subscribe.php?type=kik&channel=%s&username=%s&cid=%s' % (quote(message.body.lower().encode('utf-8')), message.from_user, message.chat_id))
              self.set_status(200)
              return
              
              
              from macostools import findertools
          
          
          # -=-=-=-=-=-=-=-=-=- FAQ BUTTONS -=-=-=-=-=-=-=-=-=-
          elif message.body == u"More Details":
            if message.chat_id in help_convos:
              faq_arr = fetch_faq(help_convos[message.chat_id]['game'])
              print "faq_arr:%s" % (faq_arr)
              
              messages = []
              for entry in faq_arr:
                messages.append(
                  TextMessage(
                    to = message.from_user, chat_id = message.chat_id,
                    body = entry, type_time = 2500, delay = 0
                  )
                )
                
                #-- only get 2 max
                if len(messages) == 2:
                  break;
                  
              
              # send 0ff first faq element
              kik.send_messages([
                messages[0]
              ])
              
              time.sleep(2)
              end_help(message.from_user, message.chat_id)
                            
            
            #-- gimme outta here
            self.set_status(200)
            return
          
          
          # -=-=-=-=-=-=-=-=-=- HELP CONNECT -=-=-=-=-=-=-=-
          if message.from_user in gameHelpList:
            
            #-- data obj/ now in active session
            help_convos[message.chat_id] = {
              'chat_id'       : message.chat_id,
              'username'      : message.from_user,
              'game'          : gameHelpList[message.from_user],
              'ignore_streak' : 0,
              'started'       : int(time.time()),
              'last_message'  : int(time.time()),
              'idle_timer'    : None,
              'messages'      : [],
              'replies'       : [],
              'im_channel'    : ""
            }
  
            kik.send_messages([
              TextMessage(
                to = message.from_user,
                chat_id = message.chat_id,
                body = "Locating %s coaches..." % (gameHelpList[message.from_user]),
                type_time = 250
              ),
              
              TextMessage(
                to = message.from_user,
                chat_id = message.chat_id,
                body = "Pro tip: Keep asking questions, each will be added to your queue! Type Cancel to end the conversation.",
                type_time = 1500,
                delay = 1500
              )
            ])
            
            
            modd.utils.slack_send(help_convos[message.chat_id], message.body, message.from_user)
            
            del gameHelpList[message.from_user]
            self.set_status(200)
            return
            
          
          
          # -=-=-=-=-=-=-=-=-=- HAS EXISTING SESSION -=-=-=-=-=-=-=-
          if message.chat_id in help_convos:
            
            #-- inc message count & log
            help_convos[message.chat_id]['ignore_streak'] += 1
            help_convos[message.chat_id]['messages'].append(message.body)
            help_convos[message.chat_id]['last_message'] = int(time.time())
            
            # -=-=-=-=-=-=-=-=-=- SESSION GOING INACTIVE -=-=-=-=-=-=-=-
            if help_convos[message.chat_id]['ignore_streak'] >= Const.MAX_REPLIES:
              print "-=- TOO MANY UNREPLIED (%d)... CLOSE OUT SESSION -=-" % (help_convos[message.chat_id]['ignore_streak'])
              
              #-- closing out session w/ 2 opts
              kik.send_messages([
                TextMessage(
                  to = message.from_user,
                  chat_id = message.chat_id,
                  body = u"Sorry! GameBots is taking so long to answer your question. What would you like to do?",
                  type_time = 250,
                  keyboards = [
                    SuggestedResponseKeyboard(
                      hidden = False,
                      responses = [
                        TextResponse("More Details"),
                        TextResponse("Cancel")
                      ]
                    )
                  ]
                )
              ])
              
              self.set_status(200)
              return
              
            
            
            # -=-=-=-=-=-=-=-=-=- CONTIUNE SESSION -=-=-=-=-=-=-=-
            else:
              
              #-- respond with waiting msg
              kik.send_messages([default_wait_reply(message)])

              
              #-- route to slack api, guy
              modd.utils.slack_im(help_convos[message.chat_id], message.body)
              
              self.set_status(200)
              return
            
            self.set_status(200)
            return
          
          
          
          # -=-=-=-=-=-=-=-=- BUTTON PROMPT -=-=-=-=-=-=-=-=
          #-- anything else, prompt with 4 topics
          if len(gameHelpList) == 0 and len(help_convos) == 0:
            kik.send_messages([
              default_text_reply(message=message)
            ])
            
            self.set_status(200)
            return
        
      self.set_status(200)
      return
        

# -[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]- #

class Slack(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
  
  def post(self):
    print "=-=-=-=-=-=-=-=-=-=-= SLACK RESPONSE =-=-=-=-=-=-=-=-=-=-= @%d\n%s" % (int(time.time()), self.get_argument('text', ""))
    
    if self.get_argument('token', "") == Const.SLACK_TOKEN:
      _arr = self.get_argument('text', "").split(' ')
      _arr.pop(0)
      
      chat_id = _arr[0]
      _arr.pop(0)
      
      message = " ".join(_arr).replace("'", "")
      to_user = ""
      
      #-- at least 1 msg & last one isn't the same
      # if (len(help_convos[chat_id]['replies']) == 1 and help_convos[chat_id]['replies'][0] == message) or (len(help_convos[chat_id]['replies']) > 1 and help_convos[chat_id]['replies'][-1] == message): 
        # pass
        
      # else:
      try:
        conn = mdb.connect(Const.DB_HOST, Const.DB_USER, Const.DB_PASS, Const.DB_NAME);
        with conn:
          cur = conn.cursor(mdb.cursors.DictCursor)
          cur.execute("SELECT `username`, `body` FROM `kikbot_logs` WHERE `chat_id` = \'{chat_id}\' ORDER BY `added` DESC LIMIT 1;".format(chat_id=chat_id))
        
          if cur.rowcount == 1:
            row = cur.fetchone()
          
            print "help_convos:%s" % (help_convos)
            if chat_id in help_convos and row['body'] != message:
              help_convos[chat_id]['ignore_streak'] = -1
              to_user = row['username']
            
              #print "to_user=%s, to_user=%s, chat_id=%s, message=%s" % (to_user, chat_id, message)
            
              if message == "!end" or message.lower() == "cancel" or message.lower() == "quit":
                print "-=- ENDING HELP -=-"
                end_help(to_user, chat_id, False)
            
              else:
                help_convos[chat_id]['replies'].append(message)
                annul_idle_activity(chat_id)
                
                kik.send_messages([
                  TextMessage(
                    to = to_user,
                      chat_id = chat_id,
                      body = "%s coach:\n%s" % (help_convos[chat_id]['game'], message),
                      type_time = 250,
                    )
                ])
    
      except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
    
      finally:
        if conn:
          conn.close()
    
    self.set_status(200)
    return


# -[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]- #


class InstantMessage(tornado.web.RequestHandler):
  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
  
  def post(self):
    print "=-=-=-=-=-=-=-=-=-=-= SLACK IM =-=-=-=-=-=-=-=-=-=-=" % (int(time.time()))
    data = tornado.escape.json_decode(self.request.body)
    print "payload:%s -(%d)" % (data, data['chat_id'] in help_convos)
    
    if data['chat_id'] in help_convos:
      help_convos[data['chat_id']]['im_channel'] = data['channel']
    

#=- -=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=- -=#
#=- -=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=--=#=- -=#



gameHelpList = {}
help_convos = {}

topics = fetch_topics()
#slack_webhooks = fetch_slack_webhooks()



##Const.KIK_API_CONFIG = {
##   'USERNAME' : "streamcard",
##   'API_KEY'  : "aa503b6f-dcda-4817-86d0-02cfb110b16a",
##   'WEBHOOK'  : {
##     'HOST' : "http://76.102.12.47",
##     'PORT' : 8080,
##     'PATH' : "kik"
##   },
##
##   'FEATURES' : {
##     'receiveDeliveryReceipts'  : True,
##     'receiveReadReceipts'      : True
##   }
## }


# Const.KIK_API_CONFIG = {
#   'USERNAME'  : "game.bots",
#   'API_KEY'   : "0fb46005-dd00-49c3-a4a5-239a0bdc1e79",
#   'WEBHOOK'   : {
#     'HOST'  : "http://159.203.250.4",
#     'PORT'  : 8080,
#     'PATH'  : "kik"
#   },
# 
#   'FEATURES'  : {
#     'receiveDeliveryReceipts' : True,
#     'receiveReadReceipts'     : True
#   }
# }


Const.KIK_API_CONFIG = {
  'USERNAME'  : "gamebots.beta",
  'API_KEY'   : "570a2b17-a0a3-4678-a9cd-fa21edf8bb8a",
  'WEBHOOK'   : {
    'HOST'  : "http://76.102.12.47",
    'PORT'  : 8080,
    'PATH'  : "kik"
  },
  
  'FEATURES'  : {
    'receiveDeliveryReceipts' : True,
    'receiveReadReceipts'     : True
  }
}




# -[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]- #
# -[=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]- #




#-=:=- Start + Config Kik -=:=-#
#-=:=--=:=--=:=--=:=--=:=--=:=--=:=--=:=--=:=--=:=-#

Const.KIK_CONFIGURATION = Configuration(
  webhook = "%s:%d/%s" % (Const.KIK_API_CONFIG['WEBHOOK']['HOST'], Const.KIK_API_CONFIG['WEBHOOK']['PORT'], Const.KIK_API_CONFIG['WEBHOOK']['PATH']),
  features = Const.KIK_API_CONFIG['FEATURES']
)

kik = KikApi(
  Const.KIK_API_CONFIG['USERNAME'],
  Const.KIK_API_CONFIG['API_KEY']
)

kik.set_configuration(Const.KIK_CONFIGURATION)



#-- output what the hell kik is doing
print "\n\n\n# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #"
print "# -= Firing up KikApi WITH =- #"
print "# -= =-=-=-=-=-=-=-=-=-=-=-= =- #"
print "USERNAME : %s\nAPI_KEY : %s\nHOST   : %s\nPORT   : %d\nPATH   : %s\nCONFIG :%s" % (
  Const.KIK_API_CONFIG['USERNAME'],
  Const.KIK_API_CONFIG['API_KEY'],
  Const.KIK_API_CONFIG['WEBHOOK']['HOST'],
  Const.KIK_API_CONFIG['WEBHOOK']['PORT'],
  Const.KIK_API_CONFIG['WEBHOOK']['PATH'],
  kik.get_configuration().to_json())
print "# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #\n\n\n"



#-- url webhooks
application = tornado.web.Application([
  (r"/kik", KikBot),
  # (r"/kikNotify", Notify),
  # (r"/notify", Notify),`
  # (r"/message", Message),
  (r"/slack", Slack),
  (r"/im", InstantMessage)
])


#-- server starting
if __name__ == "__main__":
  application.listen(int(Const.KIK_API_CONFIG['WEBHOOK']['PORT']))
  tornado.ioloop.IOLoop.instance().start()
  print "tornado start" % (int(time.time()))
  
