"""Seed data for the stationery demo shop.

Prices are integers in Toman. This file only holds data; seed.py loads it
into the database through the template's db.py functions.
"""

CATEGORIES = [
    "Notebooks & Journals",
    "Pens & Accessories",
    "Stickers & Journaling",
]

PRODUCTS = [
    # Notebooks & Journals
    {"category": "Notebooks & Journals", "name": "Nokta Classic Notebook", "description": "Minimal cream hardcover notebook with 120 lined pages.", "price": 189000, "stock": 24},
    {"category": "Notebooks & Journals", "name": "Blush Journal", "description": "Soft pink journal with a floral cover and 160 pages.", "price": 249000, "stock": 18},
    {"category": "Notebooks & Journals", "name": "Daily Planner", "description": "Undated planner for tasks, priorities, and notes.", "price": 279000, "stock": 15},
    {"category": "Notebooks & Journals", "name": "Pocket Notes", "description": "Compact spiral notebook for everyday notes.", "price": 129000, "stock": 30},
    # Pens & Accessories
    {"category": "Pens & Accessories", "name": "Pastel Gel Pen Set", "description": "Set of 6 smooth-writing gel pens in pastel colors.", "price": 169000, "stock": 35},
    {"category": "Pens & Accessories", "name": "Fine Liner Set", "description": "Set of 5 fine-tip pens for writing and journaling.", "price": 189000, "stock": 28},
    {"category": "Pens & Accessories", "name": "Pastel Pencil Case", "description": "Soft fabric pencil case with a minimalist design.", "price": 239000, "stock": 18},
    # Stickers & Journaling
    {"category": "Stickers & Journaling", "name": "Bloom Sticker Pack", "description": "Floral stickers for journals, planners, and gifts.", "price": 89000, "stock": 40},
    {"category": "Stickers & Journaling", "name": "Washi Tape Set", "description": "Set of 4 decorative tapes in pastel patterns.", "price": 149000, "stock": 32},
    {"category": "Stickers & Journaling", "name": "Cloud Sticky Notes", "description": "Set of 3 pastel sticky-note pads in cloud shapes.", "price": 109000, "stock": 27},
]


if __name__ == "__main__":
    # Quick sanity check: every product uses a listed category.
    names = set(CATEGORIES)
    assert all(p["category"] in names for p in PRODUCTS)
    print(f"{len(CATEGORIES)} categories, {len(PRODUCTS)} products OK")