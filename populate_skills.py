import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dtu_website.settings")  # Update with your project name
django.setup()

from core.models import SkillCategory, Skill

# Data from PDF
skills_data = {
    "DETERGENTS": [
        "Liquid soap", "Powder detergent", "Jik", "Shampoo", "Bar soap",
        "Bathing soap", "Shower gel", "Toilet detergent", "Jezz disinfectants",
        "Hand wash", "Hand sanitizer", "Tile cleaner"
    ],
    "COSMETOLOGY": [
        "Petroleum jelly", "Herbal Jelly", "Body creams", "Body Lotion", "Body perfumes",
        "Lip balm", "Lip scrub", "Facial serum", "Facial Tonner", "Facial wash",
        "Lip glosses", "Stain remover", "Nail remover"
    ],
    "BAKERY & PASTRY": [
        "Cakes", "Donuts", "Bread", "Pizza", "Cookies", "Muffins"
    ],
    "NUTRITION & FOOD TECHNOLOGY": [
        "Snacks (Chapatis/samosa/Mandazi)", "Daddies", "Crisps", "Cocktail juice",
        "Soya Milk", "Ice cream", "Yogurt", "Peanut butter", "Tooth paste"
    ],
    "ART & CRAFT": [
        "Craft shoes", "Craft bags", "Gift bags & paper bags", "Door marts",
        "Jewelry", "Charcoal lighters", "Charcoal Briquettes", "Plastic decoration"
    ],
    "ENTREPRENEURSHIP": [
        "Candles", "Shoe polish", "Counter Books", "Chalk production"
    ]
}

# Insert data into database
for category_name, skills in skills_data.items():
    category, created = SkillCategory.objects.get_or_create(name=category_name)
    for skill_name in skills:
        Skill.objects.get_or_create(category=category, name=skill_name)

print("✅ Skills data has been successfully populated!")
