import mysql.connector
#to install pip install mysql.connector.python

# 1. Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="std_2082"
)
cursor = conn.cursor()

# 2. Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS sudip (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    roll INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# 3. Insert 5 records
people = [
    (1, 'Sudip', 21),
    (2, 'Amit', 22),
    (3, 'Rekha', 23),
    (4, 'Binod', 24),
    (5, 'Sneha', 25)
]

# Prevent duplicate ID insertion
cursor.execute("SELECT COUNT(*) FROM sudip")
row_count = cursor.fetchone()[0]
if row_count == 0:
    cursor.executemany("INSERT INTO sudip (id, name, roll) VALUES (%s, %s, %s)", people)
    conn.commit()
    print("✅ 5 records inserted.\n")
else:
    print("⚠️ Records already exist. Skipping insert.\n")

# 4. Retrieve and display all records
print("📋 All Records:")
cursor.execute("SELECT * FROM sudip")
for row in cursor.fetchall():
    print(row)

# 5. Update a record (e.g., change 'Amit's roll to 99)
cursor.execute("UPDATE sudip SET roll = 99 WHERE name = 'Amit'")
conn.commit()
print("\n🔁 Record updated: Amit's roll changed to 99")

# 6. Delete a record (e.g., delete 'Binod')
cursor.execute("DELETE FROM sudip WHERE name = 'Binod'")
conn.commit()
print("❌ Record deleted: Binod")

# 7. Alter the table (e.g., add 'city' column)
cursor.execute("ALTER TABLE sudip ADD COLUMN city TEXT")
conn.commit()
print("🛠️ Table altered: 'city' column added")

# 8. Update city values
cursor.execute("UPDATE sudip SET city = 'Kathmandu' WHERE name = 'Sudip'")
cursor.execute("UPDATE sudip SET city = 'Pokhara' WHERE name = 'Amit'")
cursor.execute("UPDATE sudip SET city = 'Biratnagar' WHERE name = 'Rekha'")
cursor.execute("UPDATE sudip SET city = 'Lalitpur' WHERE name = 'Sneha'")
conn.commit()
print("🌍 City values added.")

# 9. Display final records
print("\n✅ Final Table Data:")
cursor.execute("SELECT * FROM sudip")
for row in cursor.fetchall():
    print(row)

# Cleanup
cursor.close()
conn.close()
