"""Load the demo shop's products into the database.

Run from the backend/ folder (the one that contains app/):

    python seed.py            # seed only if the products table is empty
    python seed.py --reset    # delete ALL products, then seed again

Optional images: put files named 01.jpg, 02.png, ... in backend/seed_images/.
The number is the product's position in seed_data.PRODUCTS (01 = first product).
Supported formats: jpg, jpeg, png, webp.
"""

import argparse
import sys
from pathlib import Path

from app.db import create_product, get_connection, init_db, save_product_image
from seed_data import PRODUCTS

IMAGE_DIR = Path(__file__).parent / "seed_images"
MIMETYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}


def count_products() -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) AS count FROM products")
    n = cur.fetchone()["count"]
    conn.close()
    return n


def delete_all_products() -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("TRUNCATE products RESTART IDENTITY")
    conn.commit()
    conn.close()


def find_image(position: int):
    """Return (bytes, mimetype) for seed_images/NN.<ext>, or None."""
    for ext, mimetype in MIMETYPES.items():
        path = IMAGE_DIR / f"{position:02d}{ext}"
        if path.exists():
            return path.read_bytes(), mimetype
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed the demo shop database.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="delete all products, then seed again",
    )
    args = parser.parse_args()

    init_db()  # safe to run repeatedly; creates tables if they don't exist

    if args.reset:
        answer = input("This deletes ALL products and reseeds them. Type 'yes' to continue: ")
        if answer.strip().lower() != "yes":
            sys.exit("Cancelled.")
        delete_all_products()
    elif count_products() > 0:
        sys.exit("Products already exist, nothing to do. Use --reset to start over.")

    with_images = 0
    for position, p in enumerate(PRODUCTS, start=1):
        product_id = create_product(p["name"], p["price"], p["category"], p["description"])
        image = find_image(position)
        if image:
            save_product_image(product_id, *image)
            with_images += 1

    print(f"Seeded {len(PRODUCTS)} products ({with_images} with images).")


if __name__ == "__main__":
    main()