import sqlite3 as sq

async def db_connect() -> None:
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS product(title TEXT, photo TEXT)")

    db.commit()


async def get_all_products():

    products = cur.execute("SELECT * FROM product").fetchall()

    return products


async def create_new_product(title, photo_id):

    product = cur.execute("INSERT INTO product VALUES (?, ?)", (title, photo_id))
    db.commit()

    return product
