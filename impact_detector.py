IMPACT_WORDS = {

    "افزایش",
    "کاهش",
    "رشد",
    "افت",
    "صعود",
    "سقوط",

    "نرخ",
    "قیمت",
    "تعرفه",
    "مالیات",

    "تحریم",
    "لغو تحریم",

    "صادرات",
    "واردات",

    "تولید",
    "فروش",

    "کمبود",
    "مازاد",

    "بحران",
    "آتش بس",
    "جنگ",
    "حمله",

    "بستن",
    "بازگشایی",

    "قطع",
    "وصل",

    "بانک مرکزی",
    "فدرال رزرو",
    "اوپک",

    "interest",
    "inflation",
    "oil",
    "gas",
    "sanction",
    "tariff",
    "budget",
    "export",
    "import",
    "production",
    "sales",
    "war",
    "attack",
    "ceasefire"

}


def has_impact(text):

    text = text.lower()

    for word in IMPACT_WORDS:
        if word.lower() in text:
            return True

    return False
