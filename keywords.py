SOURCE_SCORE = 10
MIN_SCORE = 60
MAX_SCORE = 100

CHECK_COUNT = 15

COUNTRY_SCORES = {

    "ایران":35,
    "iran":35,
    "iranian":35,
    "تهران":25,
    "tehran":25,

    "آمریکا":25,
    "usa":25,
    "united states":25,
    "us":25,

    "اسرائیل":25,
    "israel":25,

    "چین":20,
    "china":20,

    "روسیه":20,
    "russia":20,

    "اروپا":20,
    "europe":20,

    "انگلیس":20,
    "uk":20,
    "britain":20,

    "فرانسه":20,
    "germany":20,

    "عراق":15,
    "iraq":15,

    "ترکیه":15,
    "turkey":15,

    "قطر":15,
    "qatar":15,

    "امارات":15,
    "uae":15,

    "عربستان":20,
    "saudi":20,

    "اوپک":35,
    "opec":35,

    "اوپک پلاس":40,
    "opec+":40,

    "فدرال رزرو":45,
    "federal reserve":45,

    "بانک مرکزی":40,
    "central bank":40,

    "IMF":30,
    "imf":30,

    "world bank":30,
    "بانک جهانی":30

}

TOPIC_SCORES = {

    "جنگ":40,
    "war":40,

    "حمله":40,
    "attack":40,

    "موشک":40,
    "missile":40,

    "پهپاد":40,
    "drone":40,

    "آتش بس":50,
    "ceasefire":50,

    "مذاکره":35,
    "negotiation":35,

    "تحریم":40,
    "sanction":40,

    "تحریم جدید":45,

    "برجام":50,
    "jcpoa":50,

    "اقتصاد":25,
    "economy":25,

    "بورس":35,
    "stock":35,
    "market":30

}

CHANGE_WORDS = {

    "قیمت":25,
    "price":25,

    "افزایش":25,
    "increase":25,
    "rise":25,
    "growth":25,

    "کاهش":25,
    "decrease":25,
    "drop":25,
    "fall":25,

    "سقوط":30,
    "crash":30,

    "تورم":35,
    "inflation":35,

    "رکود":30,
    "recession":30,

    "رشد اقتصادی":35,
    "economic growth":35,

    "نرخ بهره":40,
    "interest rate":40,

    "دلار":35,
    "usd":35,

    "یورو":25,
    "euro":25,

    "ارز":30,
    "currency":30,

    "طلا":30,
    "gold":30,

    "نقره":25,
    "silver":25,

    "نقدینگی":35,
    "liquidity":35,

    "بودجه":30,
    "budget":30,

    "کسری بودجه":35,

    "تولید":25,
    "production":25,

    "فروش":25,
    "sales":25,

    "صادرات":30,
    "export":30,

    "واردات":30,
    "import":30,

    "تعرفه":30,
    "tariff":30,

    "سرمایه گذاری":30,
    "investment":30,

    "مالیات":25,
    "tax":25,

    "یارانه":25,
    "subsidy":25,

    "سود":30,
    "profit":30,

    "زیان":30,
    "loss":30

}

INDUSTRY_SCORES = {

    "پالایش":30,
    "پالایشگاه":30,
    "پتروشیمی":35,
    "متانول":30,
    "اوره":30,

    "فولاد":30,
    "سنگ آهن":30,
    "مس":30,
    "آلومینیوم":30,
    "روی":30,
    "سرب":30,

    "معدن":30,

    "سیمان":30,

    "بانک":30,
    "بیمه":30,

    "خودرو":30,
    "قطعه ساز":30,

    "دارو":30,
    "دارویی":30,

    "غذایی":30,

    "کشاورزی":30,
    "زراعت":30,
    "دام":30,
    "طیور":30,

    "برق":30,
    "نیروگاه":30,

    "حمل و نقل":25,
    "کشتیرانی":30,
    "بنادر":25,

    "بورس کالا":35,
    "بورس انرژی":35

}

POSITIVE_PHRASES = {

    "بسته جدید تحریم":45,
    "لغو تحریم":45,
    "تحریم جدید آمریکا":45,
    "تحریم نفتی":45,
    "تحریم بانکی":45,

    "آتش بس":50,
    "آتش بس ایران":50,
    "آتش بس اسرائیل":50,

    "مذاکرات هسته ای":45,
    "توافق هسته ای":50,
    "برجام":50,
    "jcpoa":50,

    "بستن تنگه هرمز":60,
    "تنگه هرمز":45,

    "افزایش قیمت نفت":45,
    "کاهش قیمت نفت":45,
    "افزایش تولید نفت":40,
    "کاهش تولید نفت":40,

    "صادرات نفت":40,
    "صادرات گاز":40,

    "بحران انرژی":40,

    "افزایش نرخ بهره":45,
    "کاهش نرخ بهره":45,

    "افزایش نرخ ارز":45,
    "کاهش نرخ ارز":45,

    "قیمت دلار":40,
    "قیمت طلا":35,

    "افزایش سرمایه":45,
    "عرضه اولیه":40,
    "تقسیم سود":35,

    "قطع برق صنایع":40,
    "قطع گاز صنایع":40,

    "بانک مرکزی ایران":45,
    "فدرال رزرو":45,

    "رشد صادرات":35,
    "کاهش صادرات":35,

    "کسری بودجه":35,
    "بودجه دولت":35

}

NEGATIVE_WORDS = [

    "football",
    "soccer",
    "basketball",
    "tennis",
    "volleyball",
    "cricket",

    "movie",
    "cinema",
    "music",
    "concert",
    "actor",
    "actress",
    "celebrity",

    "recipe",
    "cooking",
    "food recipe",

    "horoscope",
    "astrology",

    "game",
    "gaming",

    "wedding",
    "marriage",

    "festival",
    "showbiz",

    "entertainment",
    "tv show",

    "fashion",
    "makeup",

    "tourism",
    "travel"

]

ENGLISH_SCORES = {

# اقتصاد
"economy":25,
"economic":25,
"inflation":35,
"interest rate":40,
"interest rates":40,
"recession":35,
"economic growth":35,
"gdp":30,
"budget":30,
"budget deficit":35,
"liquidity":35,
"investment":30,
"tax":25,
"tariff":30,
"subsidy":25,

# بورس
"stock":30,
"stocks":30,
"stock market":40,
"stock exchange":40,
"equity":25,
"share":25,
"shares":25,
"ipo":40,
"earnings":35,
"dividend":35,
"financial report":35,

# ارز
"usd":35,
"dollar":35,
"currency":30,
"exchange rate":40,
"forex":30,
"euro":25,

# انرژی
"oil":35,
"crude oil":35,
"brent":35,
"wti":35,
"gas":30,
"lng":30,
"petrochemical":35,
"methanol":30,
"urea":30,

# فلزات
"steel":30,
"iron ore":30,
"copper":30,
"aluminum":30,
"zinc":30,
"lead":30,
"nickel":30,

# بانک
"bank":30,
"central bank":40,
"federal reserve":45,
"ecb":35,
"imf":30,
"world bank":30,

# ژئوپلیتیک
"iran":35,
"israel":25,
"usa":25,
"united states":25,
"china":20,
"russia":20,
"war":40,
"attack":40,
"missile":40,
"drone":40,
"ceasefire":50,
"sanction":40,
"opec":35,
"opec+":40,
"strait of hormuz":60

}

SMART_BONUS = [

(
["ایران","iran"],
["اقتصاد","economy","تورم","inflation","نرخ بهره","interest rate"],
20
),

(
["ایران","iran"],
["بورس","stock","stock market","شاخص کل"],
20
),

(
["ایران","iran"],
["دلار","usd","ارز","currency"],
20
),

(
["ایران","iran"],
["نفت","oil","گاز","gas","پتروشیمی","petrochemical"],
20
),

(
["ایران","iran"],
["تحریم","sanction"],
25
),

(
["ایران","iran"],
["جنگ","war","حمله","attack","موشک","missile","پهپاد","drone"],
25
),

(
["بورس","stock market"],
["افزایش","increase","کاهش","decrease","رشد","growth"],
15
),

(
["نفت","oil"],
["قیمت","price","افزایش","increase","کاهش","decrease"],
15
),

(
["دلار","usd"],
["قیمت","price","افزایش","increase","کاهش","decrease"],
15
),

(
[
"فولاد","steel",
"مس","copper",
"پالایش","oil",
"پتروشیمی","petrochemical",
"بانک","bank",
"خودرو","automotive"
],
[
"قیمت","price",
"افزایش","increase",
"کاهش","decrease",
"تعرفه","tariff"
],
15
),

(
[
"گزارش",
"report",
"کدال",
"earnings",
"financial report"
],
[
"سود",
"profit",
"زیان",
"loss",
"فروش",
"sales",
"تولید",
"production"
],
15
),

(
[
"بانک مرکزی",
"central bank",
"فدرال رزرو",
"federal reserve"
],
[
"تورم",
"inflation",
"بهره",
"interest",
"نقدینگی",
"liquidity"
],
20
)

]

SMART_AI_SETTINGS = {

    "allow_multiple_hits": False,

    "count_same_keyword_once": True,

    "use_positive_phrases": True,

    "use_smart_bonus": True,

    "use_industry_scores": True,

    "use_change_scores": True,

    "use_country_scores": True,

    "use_topic_scores": True,

    "use_english_scores": True,

    "ignore_negative_news": True,

    "negative_words_stop_processing": True,

    "source_score": SOURCE_SCORE,

    "min_publish_score": MIN_SCORE,

    "max_score": MAX_SCORE

}

LEVELS = {

95: "🚨🔥🔥🔥",
80: "🔥🔥",
60: "🔥"

}
