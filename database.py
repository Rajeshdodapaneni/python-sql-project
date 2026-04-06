import sqlite3

def create_database():
    conn=sqlite3.connect("sales.db")
    cursor=conn.cursor()

    cursor.execute("""  
    Create table if not exists Sales(
        order_id integer primary key,
        product Text,
        category Text,
        quantity Integer,
        price Real,
        region TEXT
    )""")

    data=[
        (1,'Laptop','Electronics',3,55000,"south"),
        (2,"Mobile","Electronics",5,20000,"North"),
        (3,"Shirt","Clothing",10,1000,"west"),
        (4,"Watches","Electronics",5,2000,"East")
    ]
    cursor.executemany("Insert or ignore into Sales values(?,?,?,?,?,?)",data)
    conn.commit()
    conn.close()