from named_constants import Constants

class Const(Constants):
    FB_APP_ID = "267184583696625"
    FB_PAGE_ID = "177712676037903"

    VERIFY_TOKEN = "AC7F552BD16A775B653F6EF6CD3902E6"
    ACCESS_TOKEN = "EAADzAMIzYPEBAJGk5P18ibMeEBhhdvUzZBsMoItnuB19PEzUGnNZALX5MN1rK0HKEfSG4YsmyVM2NmeK3m9wcmDvmwoB97aqfn1U0KOdvNtv6ZCgPLvqPFr2YbnlinuUUSrPtnphqafj6ad73wIPVBCOhCaiLGfvEZCUr7CxcAZDZD"

    MYSQL_HOST = '138.197.216.56'
    MYSQL_NAME = 'prebot_marketplace'
    MYSQL_USER = 'pre_usr'
    MYSQL_PASS = 'f4zeHUga.age'

    STRIPE_DEV_API_KEY = "sk_test_3QTHaM9IjN2g3AI91Gqqaoxo"
    STRIPE_LIVE_API_KEY = "sk_live_XhtvWeK1aZ1ggqLrJ4Z0SOZZ"

    SLACK_TOKEN = "DdWzzWFEAqAnK9loyaIFvaFK"

    SLACK_ORTHODOX_CHANNEL = "pre"
    SLACK_ORTHODOX_HANDLE = "lemon8-fb"
    SLACK_ORTHODOX_AVATAR = "https://scontent.fsnc1-4.fna.fbcdn.net/t39.2081-0/p128x128/15728018_267940103621073_6998097150915641344_n.png"
    SLACK_ORTHODOX_WEBHOOK = "https://hooks.slack.com/services/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"

    SLACK_SHOPS_WEBHOOK = "https://hooks.slack.com/services/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"
    SLACK_PURCHASES_WEBHOOK = "https://hooks.slack.com/services/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"

    WEB_SERVER_IP = "192.241.212.32"
    PACIFIC_TIMEZONE = "America/Los_Angeles"
    RATE_GLYPH = u'\u2605'.encode('utf8')
    IGNORED_NAME_PATTERN = r'[\,\'\"\`\~\ \:\;\^\%\#\&\*\$\@\!\/\?\=\+\-\|\(\)\[\]\{\}\\\<\>]'

    SQLITE_ID_START = 524288
    SUBSCRIBERS_MAX_FREE_TIER = 100
    PREMIUM_SHOP_PRICE = 4.99

    PRODUCT_TYPE_PHYSICAL = 2
    PRODUCT_TYPE_VIRTUAL = 1

    POINT_AMOUNT_VIEW_PRODUCT = 25
    POINT_AMOUNT_SHARE_PRODUCT = 50
    POINT_AMOUNT_SUBMIT_STOREFRONT = 100
    POINT_AMOUNT_SUBMIT_PRODUCT = 200
    POINT_AMOUNT_PURCHASE_PRODUCT = 300

    COIN_FLIP_API = "http://beta.modd.live/api/coin_flip.php"

    ORTHODOX_GREETING = "Hi, this is Lemonade. The fastest way to sell on Messenger."
    GOODBYE_MESSAGE = "Ok, Thanks. Goodbye!"
    UNKNOWN_MESSAGE = "I'm sorry, I cannot understand that type of message."

    ATTACHMEMENT_ID_GREETING = "216350262174144"
    IMAGE_URL_GREETING = "http://i.imgur.com/QocV5nc.gif"
    IMAGE_URL_CREATE_STOREFRONT = "https://i.imgur.com/aShmYBR.png"
    IMAGE_URL_REMOVE_STOREFRONT = "https://i.imgur.com/0EbJPhk.png"
    IMAGE_URL_ADD_PRODUCT = "https://i.imgur.com/arjLQFV.png"
    IMAGE_URL_SHARE_STOREFRONT = "https://i.imgur.com/MvZR73I.png"
    IMAGE_URL_SHARE_MESSENGER = "https://i.imgur.com/FLmisom.png"
    IMAGE_URL_MARKETPLACE = "https://i.imgur.com/oeDnbGx.png"
    IMAGE_URL_GIVEAWAYS = "https://i.imgur.com/huwkiVo.png"
    IMAGE_URL_PURCHASES = "https://i.imgur.com/Bd8H09A.png"
    IMAGE_URL_NOTIFY_SUBSCRIBERS = "https://i.imgur.com/Bd8H09A.png"
    IMAGE_URL_SUPPORT = "https://i.imgur.com/tQ9mBeG.png"

    IMAGE_URL_NEW_SUBSCRIBER = "http://i.imgur.com/JurzrAB.gif"
    IMAGE_URL_PRODUCT_PURCHASED = "https://i.imgur.com/jj72JHz.gif"

    MARKETPLACE_GREETING = 'MARKETPLACE_GREETING'
    STOREFRONT_AUTO_GEN = 'STOREFRONT_AUTO_GEN'
    STOREFRONT_ADMIN = 'STOREFRONT_ADMIN'
    CUSTOMER_EMPTY = 'CUSTOMER_EMPTY'
    CUSTOMER_REFERRAL = 'CUSTOMER_REFERRAL'
    CUSTOMER_STOREFRONT = 'CUSTOMER_STOREFRONT'
    CUSTOMER_PRODUCT = 'CUSTOMER_PRODUCT'

    CARD_TYPE_STOREFRONT = 'CARD_STOREFRONT'
    CARD_TYPE_STOREFRONT_PREVIEW = 'CARD_STOREFRONT_PREVIEW'
    CARD_TYPE_STOREFRONT_SHARE = 'CARD_STOREFRONT_SHARE'
    CARD_TYPE_STOREFRONT_ACTIVATE_PRO = 'CARD_STOREFRONT_ACTIVATE_PRO'
    CARD_TYPE_STOREFRONT_FEATURE = 'CARD_STOREFRONT_FEATURE'
    CARD_TYPE_PRODUCT = 'CARD_PRODUCT'
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
    CARD_TYPE_CUSTOMER_PURCHASES = 'CARD_CUSTOMER_PURCHASES'

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

    PB_PAYLOAD_ORTHODOX = 'ORTHODOX_PAYLOAD'
    PB_PAYLOAD_GREETING = 'WELCOME_MESSAGE'
    PB_PAYLOAD_RANDOM_STOREFRONT = 'RANDOM_STOREFRONT'
    PB_PAYLOAD_HOME_CONTENT = 'HOME_CONTENT'
    PB_PAYLOAD_CANCEL_ENTRY_SEQUENCE = 'CANCEL_ENTRY_SEQUENCE'

    PB_PAYLOAD_MAIN_MENU = 'MAIN_MENU'
    PB_PAYLOAD_PREBOT_URL = "PREBOT_URL"

    PB_PAYLOAD_PAYMENT_YES = 'PAYMENT_YES'
    PB_PAYLOAD_PAYMENT_NO = 'PAYMENT_NO'
    PB_PAYLOAD_PAYMENT_CANCEL = 'PAYMENT_CANCEL'

    PB_PAYLOAD_CREATE_STOREFRONT = 'CREATE_STOREFRONT'
    PB_PAYLOAD_DELETE_STOREFRONT = 'DELETE_STOREFRONT'
    PB_PAYLOAD_SUBMIT_STOREFRONT = 'SUBMIT_STOREFRONT'
    PB_PAYLOAD_REDO_STOREFRONT = 'REDO_STOREFRONT'
    PB_PAYLOAD_CANCEL_STOREFRONT = 'CANCEL_STOREFRONT'
    PB_PAYLOAD_ACTIVATE_PRO_STOREFRONT = 'ACTIVATE_PRO_STOREFRONT'
    PB_PAYLOAD_PRO_STOREFRONT_PURCHASE = 'PRO_STOREFRONT_PURCHASE'

    PB_PAYLOAD_ADD_PRODUCT = 'ADD_PRODUCT'
    PB_PAYLOAD_DELETE_PRODUCT = 'DELETE_PRODUCT'
    PB_PAYLOAD_SUBMIT_PRODUCT = 'SUBMIT_PRODUCT'
    PB_PAYLOAD_REDO_PRODUCT = 'REDO_PRODUCT'
    PB_PAYLOAD_CANCEL_PRODUCT = 'CANCEL_PRODUCT'

    PB_PAYLOAD_PRODUCT_TYPE_PHYSICAL = 'PRODUCT_TYPE_PHYSICAL'
    PB_PAYLOAD_PRODUCT_TYPE_VIRTUAL = 'PRODUCT_TYPE_VIRTUAL'
    PB_PAYLOAD_PRODUCT_TAG_SKIP = 'PRODUCT_TAG_SKIP'

    PB_PAYLOAD_PRODUCT_RELEASE_NOW = 'PRODUCT_RELEASE_0_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_30_DAYS = 'PRODUCT_RELEASE_30_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_60_DAYS = 'PRODUCT_RELEASE_60_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_90_DAYS = 'PRODUCT_RELEASE_90_DAYS'
    PB_PAYLOAD_PRODUCT_RELEASE_120_DAYS = 'PRODUCT_RELEASE_120_DAYS'

    PB_PAYLOAD_PAYOUT_BITCOIN = 'PAYOUT_BITCOIN'
    PB_PAYLOAD_PAYOUT_PAYPAL = 'PAYOUT_PAYPAL'
    PB_PAYLOAD_MESSAGE_CUSTOMERS = 'MESSAGE_CUSTOMERS'

    PB_PAYLOAD_PRODUCT_RATE_1_STAR = 'PRODUCT_RATE_1_STAR'
    PB_PAYLOAD_PRODUCT_RATE_2_STAR = 'PRODUCT_RATE_2_STAR'
    PB_PAYLOAD_PRODUCT_RATE_3_STAR = 'PRODUCT_RATE_3_STAR'
    PB_PAYLOAD_PRODUCT_RATE_4_STAR = 'PRODUCT_RATE_4_STAR'
    PB_PAYLOAD_PRODUCT_RATE_5_STAR = 'PRODUCT_RATE_5_STAR'

    PB_PAYLOAD_CHECKOUT_PRODUCT = 'CHECKOUT_PRODUCT'
    PB_PAYLOAD_CHECKOUT_BITCOIN = 'CHECKOUT_BITCOIN'
    PB_PAYLOAD_CHECKOUT_CREDIT_CARD = 'CHECKOUT_CREDIT_CARD'
    PB_PAYLOAD_CHECKOUT_PAYPAL = 'CHECKOUT_PAYPAL'
    PB_PAYLOAD_PURCHASE_PRODUCT = 'PURCHASE_PRODUCT'
    PB_PAYLOAD_SHARE_PRODUCT = 'SHARE_PRODUCT'
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
    PB_PAYLOAD_DM_REQUEST_INVOICE = 'DM_REQUEST_INVOICE'
    PB_PAYLOAD_DM_REQUEST_PAYMENT = 'DM_REQUEST_PAYMENT'
    PB_PAYLOAD_DM_CANCEL_PURCHASE = 'DM_CANCEL_PURCHASE'
    PB_PAYLOAD_DM_CLOSE = 'DM_CLOSE'

    PB_PAYLOAD_AFFILIATE_GIVEAWAY = 'GIVEAWAY'
    PB_PAYLOAD_ADD_GIVEAWAYS = 'ADD_GIVEAWAYS'
    PB_PAYLOAD_GIVEAWAYS_YES = 'GIVEAWAYS_YES'
    PB_PAYLOAD_GIVEAWAYS_NO = 'GIVEAWAYS_NO'

    PB_PAYLOAD_FLIP_COIN_NEXT_ITEM = 'FLIP_COIN_NEXT_ITEM'
    PB_PAYLOAD_FLIP_COIN_DO_FLIP = 'FLIP_COIN_DO_FLIP'

    PAYMENT_SOURCE_UNDEFINED = 'PAYMENT_UNDEFINED'
    PAYMENT_SOURCE_BITCOIN = 'PAYMENT_BITCOIN'
    PAYMENT_SOURCE_CREDIT_CARD = 'PAYMENT_CREDIT_CARD'
    PAYMENT_SOURCE_PAYPAL = 'PAYMENT_PAYPAL'

    RESERVED_ADMIN_REPLIES = "admin"#|main|main menu|menu"
    RESERVED_CUSTOMER_REPLIES = "shop"#main|main menu|menu"
    RESERVED_SUPPORT_REPLIES = "help|support"
    RESERVED_STOP_REPLIES = "cancel|end|quit|stop"
