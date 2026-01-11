import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="password@123",
    port=5432
)

cur = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT,
    name TEXT,
    department TEXT
);
"""

cur.execute(create_table_query)
conn.commit()

print("Table created successfully ✅")

cur.close()
conn.close()
