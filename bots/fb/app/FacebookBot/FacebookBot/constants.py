from named_constants import Constants

class Const(Constants):
    FB_APP_ID = "267184583696625"
    FB_PAGE_ID = "177712676037903"

    # toofus|jason|kalvin|bryan|charles
    ADMIN_FB_PSIDS = "1448213991869039|996171033817503|1108749299253610|1263941553690055|888707194565351"

    VERIFY_TOKEN = "AC7F552BD16A775B653F6EF6CD3902E6"
    ACCESS_TOKEN = "EAADzAMIzYPEBADsgmDY8laRqc4QjcZAtZAEat2fJ19Qan779WqV0ZCgPe0GkIVFwgZAeEAYG6sfzmkKEyiV09ByNQXYqcYcG9KOGu5dXz79BBuEXqNZB0sCQXxSJGRbCGA72JnjTi4rVQNMB1MznmZA6nV7CwUOZB9ZABcaD1ZBm1zwZDZD"

    MYSQL_HOST = '138.197.216.56'
    MYSQL_NAME = 'prebot_marketplace'
    MYSQL_USER = 'pre_usr'
    MYSQL_PASS = 'f4zeHUga.age'

    STRIPE_DEV_API_KEY = "sk_test_3QTHaM9IjN2g3AI91Gqqaoxo"
    STRIPE_LIVE_API_KEY = "sk_live_XhtvWeK1aZ1ggqLrJ4Z0SOZZ"

    SLACK_TOKEN = "L8u66hlTDtzl9Hp6aK9gKkKZ"
    STEAM_TOKEN = "0e8c3c25db9d52139ef41be8acffd194"
    TRADER_TOKEN = "ef273536b112776fb137916807783bcc"
    PAYPAL_TOKEN = "882499ef6be6c2575a7a8b2be032e42f"
    IMPORT_STOREFRONT_TOKEN = "07f5057bb7d5be65101cb251bc26c748"
    REFUND_TOKEN = "7f47d7d76f9ddbf30b671040779ab787"
    USER_ADD_POINTS_TOKEN = "7da9c27d7ea2ed899df79bcb71de72db"
    MYSTERY_FLIP_TOKEN = "476b5353b4ea9a12e778ea445d0a4043"
    GAMEBOTS_POINTS_TOKEN = "457a7fa6c8319c5e6c2fcc990b423981"

    SLACK_ORTHODOX_CHANNEL = "pre"
    SLACK_ORTHODOX_HANDLE = "lemon8-fb"
    SLACK_ORTHODOX_AVATAR = "https://scard.tv/static/images/logo-paypal.jpg"
    SLACK_ORTHODOX_WEBHOOK = "https://hooks.slack.com/services/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"

    SLACK_SHOPS_WEBHOOK = "https://hooks.slack.com/services/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"
    SLACK_PURCHASES_WEBHOOK = "https://hooks.slack.com/services/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"
    SLACK_PIZZA_WEBHOOK = "https://hooks.slack.com/services/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"
    SLACK_SUPPORT_WEBHOOK = "https://hooks.slack.com/services/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"


    WEB_SERVER_IP = "192.241.212.32"
    PACIFIC_TIMEZONE = "America/Los_Angeles"
    RATE_GLYPH = u'\u2605'.encode('utf8')
    IGNORED_NAME_PATTERN = r'[\,\'\"\`\~\ \:\;\^\%\#\&\*\$\@\!\/\?\=\+\-\|\(\)\[\]\{\}\\\<\>]'

    GA_TRACKING_ID = "UA-79705534-2"
    GA_TRACKING_URL = "http://www.google-analytics.com/collect"

    MIN_POINTS_THRESHOLD = 1250000
    SQLITE_ID_START = 524288
    SUBSCRIBERS_MAX_FREE_TIER = 100
    PREMIUM_SHOP_PRICE = 4.99
    POINTS_PER_DOLLAR = 250000
    FLIPS_PER_24_HOUR = 100

    STOREFRONT_TYPE_OWNER_GEN = 0
    STOREFRONT_TYPE_CUSTOM = 1
    STOREFRONT_TYPE_AUTO_GEN = 2
    STOREFRONT_TYPE_IMPORT_GEN = 3
    STOREFRONT_TYPE_PHYSICAL = 4


    PRODUCT_TYPE_SKIPPED = 0
    PRODUCT_TYPE_GAME_ITEM = 1
    PRODUCT_TYPE_STICKER = 2
    PRODUCT_TYPE_CARD = 3

    POINT_AMOUNT_NEXT_SHOP = 20
    POINT_AMOUNT_VIEW_PRODUCT = 5
    POINT_AMOUNT_SHARE_APP = 10
    POINT_AMOUNT_REFFERAL = 500
    POINT_AMOUNT_FLIP_STOREFRONT_WIN = 100
    POINT_AMOUNT_SUBMIT_STOREFRONT = 50
    POINT_AMOUNT_RESELL_STOREFRONT = 1000
    POINT_AMOUNT_SUBMIT_PRODUCT = 50
    POINT_AMOUNT_PURCHASE_PRODUCT = 200

    COIN_FLIP_API = "http://beta.modd.live/api/coin_flip.php"

    #ORTHODOX_GREETING = "Welcome to Lemonade. The world's largest virtual mall."
    ORTHODOX_GREETING = "Hi {first_name}, Welcome to Lemonade. The world's largest virtual mall."
    GOODBYE_MESSAGE = "Ok, Thanks. Goodbye!"
    UNKNOWN_MESSAGE = "I'm sorry, I cannot understand that type of message."

    IMAGE_URL_GREETING = "https://media.giphy.com/media/3o6wrlOBmtEI8OUi5y/giphy.gif" #"https://i.imgur.com/sdV0hkv.png"
    IMAGE_URL_NEW_SUBSCRIBER = "https://media.giphy.com/media/MaxKN8dORncpG/giphy.gif" #"http://i.imgur.com/zBTx8Xy.gif"
    IMAGE_URL_PRODUCT_PURCHASED = "https://media.giphy.com/media/VUie5h5B1NDfq/giphy.gif" #"http://i.imgur.com/vdMdrVT.gif"
    IMAGE_URL_PRODUCT_CREATED = "http://i.imgur.com/WsjHWej.gif"
    IMAGE_URL_SAY_THANKS = "http://i.imgur.com/XRG8fHa.gif"

    IMAGE_URL_CREATE_STOREFRONT_CARD = "https://i.imgur.com/dT2KO63.png"
    IMAGE_URL_ADD_PRODUCT_CARD = "https://i.imgur.com/rrEWTrd.png"
    IMAGE_URL_SHARE_STOREFRONT_CARD = "https://i.imgur.com/D7qNhRa.png"
    IMAGE_URL_SHARE_MESSENGER_CARD = "https://i.imgur.com/D7qNhRa.png"
    IMAGE_URL_PURCHASES_CARD = "https://i.imgur.com/j5GbuHS.png"
    IMAGE_URL_FLIP_SPONSOR_CARD = "https://i.imgur.com/eOaYJ0G.png"
    IMAGE_URL_REFERRAL_CARD = "https://i.imgur.com/PQgFYSG.png"

    IMAGE_URL_HELP_COMMAND = "https://i.imgur.com/Sv26pNs.gif"
    IMAGE_URL_CANCEL_COMMAND = "https://i.imgur.com/KChXWd4.gif"
    IMAGE_URL_SUPPORT_COMMAND = "https://i.imgur.com/lt1YMOC.gif"
    IMAGE_URL_SUBS_COMMAND = "https://i.imgur.com/Q8YI9YV.gif"
    IMAGE_URL_LEMONADE_COMMAND = "https://i.imgur.com/W65TYHj.gif"
    IMAGE_URL_MAIN_MENU_COMMAND = "https://i.imgur.com/2q1eEGP.gif"
    IMAGE_URL_MENU_COMMAND = "https://i.imgur.com/2q1eEGP.gif"

    IMAGE_URL_FLIP_START = "https://i.imgur.com/EXev63l.gif"
    IMAGE_URL_FLIP_WIN = "http://i.imgur.com/TAayas0.gif"
    IMAGE_URL_FLIP_LOSE = "http://i.imgur.com/CdwqcSD.gif"

    IMAGE_URL_PIZZA_GIF = "https://i.imgur.com/aaiiSj3.gif"


    ENTRY_MARKETPLACE_GREETING = 'ENTRY_MARKETPLACE_GREETING'
    ENTRY_STOREFRONT_AUTO_GEN = 'ENTRY_STOREFRONT_AUTO_GEN'
    ENTRY_CUSTOMER_REFERRAL = 'ENTRY_CUSTOMER_REFERRAL'

    CARD_TYPE_STOREFRONT_ENTRY = 'CARD_STOREFRONT_ENTRY'
    CARD_TYPE_STOREFRONT_PREVIEW = 'CARD_STOREFRONT_PREVIEW'
    CARD_TYPE_STOREFRONT_SHARE = 'CARD_STOREFRONT_SHARE'
    CARD_TYPE_STOREFRONT_FEATURE = 'CARD_STOREFRONT_FEATURE'
    CARD_TYPE_PRODUCT_ENTRY = 'CARD_PRODUCT_ENTRY'
    CARD_TYPE_PRODUCT_PREVIEW = 'CARD_PRODUCT_PREVIEW'
    CARD_TYPE_PRODUCT_SHARE = 'CARD_PRODUCT_SHARE'
    CARD_TYPE_PRODUCT_CHECKOUT = 'CARD_PRODUCT_CHECKOUT'
    CARD_TYPE_PRODUCT_CHECKOUT_CC = 'CARD_PRODUCT_CHECKOUT_CC'
    CARD_TYPE_PRODUCT_INVOICE_PAYPAL = 'CARD_PRODUCT_INVOICE_PAYPAL'
    CARD_TYPE_PRODUCT_RECEIPT = 'CARD_PRODUCT_RECEIPT'
    CARD_TYPE_PRODUCT_PURCHASED = 'CARD_PRODUCT_PURCHASED'
    CARD_TYPE_PRODUCT_RATE = 'CARD_PRODUCT_RATE'
    CARD_TYPE_SUPPORT = 'CARD_SUPPORT'
    CARD_TYPE_NOTIFY_SUBSCRIBERS = 'CARD_NOTIFY_SUBSCRIBERS'
    CARD_TYPE_PRODUCT_PURCHASES = 'CARD_PRODUCT_PURCHASES'
    CARD_TYPE_PRODUCTS_PURCHASED = 'CARD_CUSTOMER_PURCHASES'

    CARD_BTN_PAYMENT = 'payment'
    CARD_BTN_POSTBACK = 'postback'
    CARD_BTN_URL = 'web_url'
    CARD_BTN_URL_COMPACT = 'web_url_compact'
    CARD_BTN_URL_TALL = 'web_url_tall'
    CARD_BTN_URL_FULL = 'web_url_full'
    CARD_BTN_INVITE = 'element_share'
    KWIK_BTN_TEXT = 'text'
    KWIK_BTN_LOCATION = 'location'

    PAYLOAD_TYPE_QUICK_REPLY = 'PAYLOAD_QUICK_REPLY'
    PAYLOAD_TYPE_POSTBACK = 'PAYLOAD_POSTBACK'

    PB_PAYLOAD_PIZZA_FAQ = "PIZZA_FAQ"
    PB_PAYLOAD_PIZZA_CLAIM = "PIZZA_CLAIM"
    PB_PAYLOAD_PIZZA_TRY_AGAIN = "PIZZA_TRY_AGAIN"
    PB_PAYLOAD_PIZZA_CONFIRM = "PIZZA_CONFIRM"
    PB_PAYLOAD_PIZZA_REENTER = "PIZZA_REENTER"

    PB_PAYLOAD_ORTHODOX = 'ORTHODOX_PAYLOAD'
    PB_PAYLOAD_GREETING = 'WELCOME_MESSAGE'
    PB_PAYLOAD_HOME_CONTENT = 'HOME_CONTENT'
    PB_PAYLOAD_CANCEL_ENTRY_SEQUENCE = 'CANCEL_ENTRY_SEQUENCE'
    PB_PAYLOAD_LMON8_FAQ = "LMON8_FAQ"

    PB_PAYLOAD_RND_FLIP_STOREFRONT = 'RND_FLIP_STOREFRONT'
    PB_PAYLOAD_PRODUCT_PURCHASES = 'PRODUCT_PURCHASES'
    PB_PAYLOAD_PRODUCTS_PURCHASED = 'PRODUCTS_PURCHASED'

    PB_PAYLOAD_MAIN_MENU = 'MAIN_MENU'
    PB_PAYLOAD_PREBOT_URL = "PREBOT_URL"
    PB_PAYLOAD_RND_STOREFRONT = 'RND_STOREFRONT'
    PB_PAYLOAD_SAY_THANKS = 'SAY_THANKS'
    PB_PAYLOAD_SHARE_APP = 'SHARE_APP'
    PB_PAYLOAD_FEATURE_STOREFRONT = 'FEATURE_STOREFRONT'

    PB_PAYLOAD_PAYMENT_YES = 'PAYMENT_YES'
    PB_PAYLOAD_PAYMENT_NO = 'PAYMENT_NO'
    PB_PAYLOAD_PAYMENT_CANCEL = 'PAYMENT_CANCEL'

    PB_PAYLOAD_AUTO_GEN_STOREFRONT = 'AUTO_GEN_STOREFRONT'
    PB_PAYLOAD_SEARCH_STOREFRONT = 'SEARCH_STOREFRONT'
    PB_PAYLOAD_BUILD_STOREFRONT = 'BUILD_STOREFRONT'
    PB_PAYLOAD_RESELL_STOREFRONT = 'RESELL_STOREFRONT'
    PB_PAYLOAD_CREATE_STOREFRONT = 'CREATE_STOREFRONT'
    PB_PAYLOAD_DELETE_STOREFRONT = 'DELETE_STOREFRONT'
    PB_PAYLOAD_SUBMIT_STOREFRONT = 'SUBMIT_STOREFRONT'
    PB_PAYLOAD_REDO_STOREFRONT = 'REDO_STOREFRONT'
    PB_PAYLOAD_CANCEL_STOREFRONT = 'CANCEL_STOREFRONT'
    PB_PAYLOAD_ACTIVATE_PRO_STOREFRONT = 'ACTIVATE_PRO_STOREFRONT'
    PB_PAYLOAD_PRO_STOREFRONT_PURCHASE = 'PRO_STOREFRONT_PURCHASE'
    PB_PAYLOAD_RESELLER_CAROUSEL = 'RESELLER_CAROUSEL'

    PB_PAYLOAD_ADD_PRODUCT = 'ADD_PRODUCT'
    PB_PAYLOAD_DELETE_PRODUCT = 'DELETE_PRODUCT'
    PB_PAYLOAD_SUBMIT_PRODUCT = 'SUBMIT_PRODUCT'
    PB_PAYLOAD_REDO_PRODUCT = 'REDO_PRODUCT'
    PB_PAYLOAD_CANCEL_PRODUCT = 'CANCEL_PRODUCT'

    PB_PAYLOAD_PRODUCT_TYPE_GAME_ITEM = 'PRODUCT_TYPE_GAME_ITEM'
    PB_PAYLOAD_PRODUCT_TYPE_STICKER = 'PRODUCT_TYPE_STICKER'
    PB_PAYLOAD_PRODUCT_TYPE_SKIP = 'PRODUCT_TYPE_SKIP'
    PB_PAYLOAD_PRODUCT_TAG_SKIP = 'PRODUCT_TAG_SKIP'

    PB_PAYLOAD_PRODUCT_RELEASE_NOW = 'PRODUCT_RELEASE_0_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_30_DAYS = 'PRODUCT_RELEASE_30_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_60_DAYS = 'PRODUCT_RELEASE_60_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_90_DAYS = 'PRODUCT_RELEASE_90_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_120_DAYS = 'PRODUCT_RELEASE_120_DAYS'

    PB_PAYLOAD_PAYOUT_BITCOIN = 'PAYOUT_BITCOIN'
    PB_PAYLOAD_PAYOUT_PAYPAL = 'PAYOUT_PAYPAL'
    PB_PAYLOAD_MESSAGE_CUSTOMERS = 'MESSAGE_CUSTOMERS'
    PB_PAYLOAD_REFERRAL_FAQ = 'REFERRAL_FAQ'
    PB_PAYLOAD_CUSTOMER_POINTS = 'CUSTOMER_POINTS'
    PB_PAYLOAD_MYSTERY_FLIP = 'MYSTERY_FLIP'

    PB_PAYLOAD_PRODUCT_RATE_1_STAR = 'PRODUCT_RATE_1_STAR'
    PB_PAYLOAD_PRODUCT_RATE_2_STAR = 'PRODUCT_RATE_2_STAR'
    PB_PAYLOAD_PRODUCT_RATE_3_STAR = 'PRODUCT_RATE_3_STAR'
    PB_PAYLOAD_PRODUCT_RATE_4_STAR = 'PRODUCT_RATE_4_STAR'
    PB_PAYLOAD_PRODUCT_RATE_5_STAR = 'PRODUCT_RATE_5_STAR'

    PB_PAYLOAD_CHECKOUT_PRODUCT = 'CHECKOUT_PRODUCT'
    PB_PAYLOAD_CHECKOUT_BITCOIN = 'CHECKOUT_BITCOIN'
    PB_PAYLOAD_CHECKOUT_CREDIT_CARD = 'CHECKOUT_CREDIT_CARD'
    PB_PAYLOAD_CHECKOUT_PAYPAL = 'CHECKOUT_PAYPAL'
    PB_PAYLOAD_CHECKOUT_POINTS = 'CHECKOUT_POINTS'
    PB_PAYLOAD_CHECKOUT_FB = 'CHECKOUT_FB'
    PB_PAYLOAD_PURCHASE_POINTS_PAK = 'PURCHASE_POINTS_PAK'
    PB_PAYLOAD_PURCHASE_POINTS_PAK_5 = 'PURCHASE_POINTS_PAK_5'
    PB_PAYLOAD_PURCHASE_POINTS_PAK_10 = 'PURCHASE_POINTS_PAK_10'
    PB_PAYLOAD_PURCHASE_POINTS_PAK_20 = 'PURCHASE_POINTS_PAK_20'
    PB_PAYLOAD_PURCHASE_POINTS_YES = 'PURCHASE_POINTS_YES'
    PB_PAYLOAD_PURCHASE_POINTS_NO = 'PURCHASE_POINTS_NO'
    PB_PAYLOAD_PURCHASE_PRODUCT = 'PURCHASE_PRODUCT'
    PB_PAYLOAD_VIEW_PRODUCT = 'VIEW_PRODUCT'
    PB_PAYLOAD_VIEW_MARKETPLACE = 'VIEW_MARKETPLACE'
    PB_PAYLOAD_SUPPORT = 'SUPPORT'
    PB_PAYLOAD_CUSTOMERS = 'CUSTOMERS'
    PB_PAYLOAD_RATE_PRODUCT = 'RATE_PRODUCT'
    PB_PAYLOAD_NOTIFY_STOREFRONT_OWNER = 'NOTIFY_STOREFRONT_OWNER'

    DM_ACTION_PURCHASE = 'DM_ACTION_PURCHASE'
    DM_ACTION_SEND = 'DM_ACTION_SEND'
    DM_ACTION_CLOSE = 'DM_ACTION_CLOSE'

    PB_PAYLOAD_DM_OPEN = 'DM_OPEN'
    PB_PAYLOAD_DM_SEND_FB_NAME = 'DM_SEND_FB_NAME'
    PB_PAYLOAD_DM_SEND_URL = 'DM_SEND_URL'
    PB_PAYLOAD_DM_REQUEST_INVOICE = 'DM_REQUEST_INVOICE'
    PB_PAYLOAD_DM_REQUEST_PAYMENT = 'DM_REQUEST_PAYMENT'
    PB_PAYLOAD_DM_CANCEL_PURCHASE = 'DM_CANCEL_PURCHASE'
    PB_PAYLOAD_DM_CLOSE = 'DM_CLOSE'

    PB_PAYLOAD_AFFILIATE_GIVEAWAY = 'GIVEAWAY'
    PB_PAYLOAD_ADD_GIVEAWAYS = 'ADD_GIVEAWAYS'
    PB_PAYLOAD_MOD_TASK_YES = 'MOD_TASK_YES'
    PB_PAYLOAD_MOD_TASK_NO = 'MOD_TASK_NO'

    PB_PAYLOAD_TRADE_URL = 'TRADE_URL'
    PB_PAYLOAD_TRADE_URL_KEEP = 'TRADE_URL_KEEP'

    PB_PAYLOAD_ALT_SOCIAL = 'ALT_SOCIAL'
    PB_PAYLOAD_ALT_SOCIAL_KEEP = 'ALT_SOCIAL_KEEP'

    PB_PAYLOAD_DISNEY_YES = 'DISNEY_YES'
    PB_PAYLOAD_DISNEY_NO = 'DISNEY_NO'

    PAYMENT_SOURCE_UNDEFINED = 'PAYMENT_UNDEFINED'
    PAYMENT_SOURCE_BITCOIN = 'PAYMENT_BITCOIN'
    PAYMENT_SOURCE_CREDIT_CARD = 'PAYMENT_CREDIT_CARD'
    PAYMENT_SOURCE_PAYPAL = 'PAYMENT_PAYPAL'
    PAYMENT_SOURCE_POINTS = 'PAYMENT_POINTS'
    PAYMENT_SOURCE_FB = 'PAYMENT_FB'
    PAYMENT_SOURCE_PIZZA = 'PAYMENT_PIZZA'

    RESERVED_COMMAND_REPLIES = "lmon8|admin|main|main menu|menu"
    RESERVED_APPNEXT_REPLIES = "f1xgb"
    RESERVED_AUTO_GEN_STOREFRONTS = "autogen"
    RESERVED_OPTOUT_REPLIES = "cancel|end|quit|stop"
    RESERVED_SUPPORT_REPLIES = "support|help"
    RESERVED_FAQ_REPLIES = "faq"
    RESERVED_KIK_REPLIES = "kik"
    RESERVED_POINTS_REPLIES = "points"
    RESERVED_BONUS_AUTO_GEN_REPLIES = "bonus"
    RESERVED_TRADES_REPLIES = "trades"
    RESERVED_STEAM_REPLIES = "steam"
    RESERVED_MODERATOR_REPLIES = "mod"
    RESERVED_TASKS_REPLIES = "tasks"
    RESERVED_GIAVEAWAY_REPLIES = "ga|giveaway|snap|twitter|ig|twitch|yt"
    RESERVED_FBPSID_REPLIES = "id|referral"
    RESERVED_PROTECTED_REPLIES = "4x78"
    RESERVED_PIZZA_CODES = "p1zza|152dd|c84e6|56aeb|b95b2|90d6a|5dac8|a561e|a2e9d|df301|e5618|b272e|70b01|befb2|96466|c112f|e2587|7b16a|36d25|393de|c445f|38809|4fa71|a9f19|c3ddd|8fdb7|6874f|69624|3f8e7|09dbb|2d8c3|f483a|ade96|770a3|77823|6db3a|45336|4b11d|835f5|86a38|f087c|b2360|fc2a0|3df83|81374|ae3ed|15c01|3d0d5|84da0|c7add|9a323|7d3ae|06162|85a2c|f4e15|b10e9|ad47f|cb27b|94a1c|7204d|6d17a"

