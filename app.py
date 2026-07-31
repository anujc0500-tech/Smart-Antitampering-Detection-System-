import sqlite3
import hashlibdef connect():

DB_NAME = "products.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        product_code TEXT UNIQUE,

        product_name TEXT,

        brand TEXT,

        batch TEXT,

        manufacturing_date TEXT,

        expiry_date TEXT,

        status TEXT,

        qr_data TEXT

    )
    """)

    conn.commit()
    conn.close()


def add_product(
        product_code,
        product_name,
        brand,
        batch,
        manufacturing_date,
        expiry_date,
        status):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""

    INSERT INTO products(

    product_code,
    product_name,
    brand,
    batch,
    manufacturing_date,
    expiry_date,
    status,
    qr_data

    )

    VALUES(?,?,?,?,?,?,?,?)

    """,

    (

    product_code,
    product_name,
    brand,
    batch,
    manufacturing_date,
    expiry_date,
    status,
    product_code

    ))

    conn.commit()
    conn.close()


def verify_product(code):

    conn = connect()

    cur = conn.cursor()

    cur.execute(

    "SELECT * FROM products WHERE product_code=?",

    (code,)

    )

    data = cur.fetchone()

    conn.close()

    return data


def get_all_products():

    conn = connect()

    cur = conn.cursor()

    cur.execute("SELECT * FROM products")

    data = cur.fetchall()

    conn.close()

    return data


def delete_product(code):

    conn = connect()

    cur = conn.cursor()

    cur.execute(

    "DELETE FROM products WHERE product_code=?",

    (code,)

    )

    conn.commit()

    conn.close()


def update_status(code,status):

    conn=connect()

    cur=conn.cursor()

    cur.execute("""

    UPDATE products

    SET status=?

    WHERE product_code=?

    """,(status,code))

    conn.commit()

    conn.close()


if __name__=="__main__":

    create_table()

    try:

        add_product(

        "SAFE123",

        "Potato Chips Classic Salted",

        "SafeExpiry",

        "A1B2C3D4",

        "01/05/2024",

        "01/05/2025",

        "Authentic"

        )

    except:

        pass

    try:

        add_product(

        "SAFE456",

        "Orange Juice 1L",

        "SafeExpiry",

        "B9C8D7E6",

        "15/08/2024",
DB_NAME = "products.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_users_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password, role="user"):

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("""
        INSERT INTO users(username,password,role)
        VALUES(?,?,?)
        """,
        (
            username,
            hash_password(password),
            role
        ))

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:

        conn.close()

        return False


def login(username, password):

    conn = connect()

    cur = conn.cursor()

    cur.execute("""

    SELECT role

    FROM users

    WHERE username=?

    AND password=?

    """,

    (

    username,

    hash_password(password)

    ))

    result = cur.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def user_exists(username):

    conn = connect()

    cur = conn.cursor()

    cur.execute("""

    SELECT *

    FROM users

    WHERE username=?

    """,

    (username,))

    result = cur.fetchone()

    conn.close()

    return result is not None


if __name__ == "__main__":

    create_users_table()

    if not user_exists("admin"):

        register(

            "admin",

            "admin123",

            "admin"

        )

    print("Authentication system ready.")

        "15/08/2025",

        "Authentic"

        )

    except:

        pass

    print(get_all_products())
