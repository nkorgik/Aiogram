import sqlite3 as sq

async def db_connect() -> None:
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS product(product_id INTEGER PRIMARY KEY, title TEXT, photo TEXT)")

    db.commit()


async def get_all_products():

    products = cur.execute("SELECT * FROM product").fetchall()

    return products  # list


async def create_new_product(state):

    async with state.proxy() as data:
        product = cur.execute("INSERT INTO product (title, photo) VALUES (?, ?)", (data['title'], data['photo']))
        db.commit()

    return product


async def delete_product(product_id: int) -> None:
    cur.execute("DELETE FROM product WHERE product_id = ?", (product_id,))
    db.commit()


async def edit_product(product_id: int, title: str) -> None:
    cur.execute("UPDATE product SET title = ? WHERE product_id = ?", (title, product_id,))
    db.commit()
