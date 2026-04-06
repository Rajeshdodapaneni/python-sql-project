import sqlite3
import openpyxl
import pandas as pd

def analyze_data():
    conn=sqlite3.connect("sales.db")
    df=pd.read_sql("select * from sales",conn)
    df["revenue"]=df["quantity"] * df["price"]

    print("\nTotal Revenue:", df["revenue"].sum())
    print("\nSales by Category:\n", df.groupby("category")["revenue"].sum())
    print("\nTop Product:", df.groupby("product")["quantity"].sum().idxmax())


    # SQL FILTERING

    # 🔹 Load full data
    df = pd.read_sql("SELECT * FROM sales", conn)
    print("\nFull Data:\n", df)

    # 🔹 Step 5: SQL Filtering
    query1 = "SELECT * FROM sales WHERE category = 'Electronics'"
    df1 = pd.read_sql(query1, conn)
    print("\nElectronics Data:\n", df1)

    # 🔹 Step 5: SQL Aggregation
    query2 = """
    SELECT category, SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY category
    """
    df2 = pd.read_sql(query2, conn)
    print("\nRevenue by Category:\n", df2)

     # ✅ Export to CSV
    df.to_csv("full_data.csv", index=False)
    df1.to_csv("electronics_data.csv", index=False)
    df2.to_csv("category_revenue.csv", index=False)

    # ✅ Export to Excel
    with pd.ExcelWriter("sales_report.xlsx") as writer:
        df.to_excel(writer, sheet_name="All Data", index=False)
        df1.to_excel(writer, sheet_name="Electronics", index=False)
        df2.to_excel(writer, sheet_name="Revenue", index=False)

    print("Files exported successfully!")

    conn.close()
