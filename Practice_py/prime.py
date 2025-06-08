# n = 24
# is_prime = lambda n: all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1
# print("It is prime" if is_prime(n) else "It is not prime")
# prime=list(filter(is_prime,range(2,n+1)))
# print(prime)


# import mysql.connector

# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",  # Replace with your MySQL root password
#     database="ShankerDev"
# )

# cursor = conn.cursor()

# # Create table if not exists
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Teachers (
#     id INT PRIMARY KEY,
#     name VARCHAR(100),
#     address VARCHAR(255),
#     salary INT
# )
# """)

# # Insert 5 records
# records = [
#     (1, 'John Doe', 'New York', 55000),
#     (2, 'Jane Smith', 'California', 48000),
#     (3, 'Alice Johnson', 'Texas', 62000),
#     (4, 'Bob Brown', 'Florida', 51000),
#     (5, 'Eve Adams', 'Nevada', 47000)
# ]

# cursor.executemany("INSERT IGNORE INTO Teachers (id, name, address, salary) VALUES (%s, %s, %s, %s)", records)
# conn.commit()

# # Retrieve teachers with salary > 50000
# cursor.execute("SELECT id, name, salary FROM Teachers WHERE salary > 50000")
# results = cursor.fetchall()

# print("Teachers with salary > 50000:")
# for row in results:
#     print(row)

# cursor.close()
# conn.close()

# import tkinter as tk

# root = tk.Tk()
# root.title("Student Form")

# # Variables
# name = tk.StringVar()
# email = tk.StringVar()
# website = tk.StringVar()
# image = tk.StringVar()
# gender = tk.StringVar(value="Male")
# java = tk.IntVar()
# html = tk.IntVar()
# css = tk.IntVar()

# # Labels and Entries
# for i, text in enumerate(["Name", "Email", "Website", "Image Link"]):
#     tk.Label(root, text=text).grid(row=i, column=0, sticky="w")
#     tk.Entry(root, textvariable=[name, email, website, image][i]).grid(row=i, column=1)

# # Gender Radio Buttons
# tk.Label(root, text="Gender").grid(row=4, column=0, sticky="w")
# tk.Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=4, column=1, sticky="w")
# tk.Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=5, column=1, sticky="w")

# # Skills Checkbuttons
# tk.Label(root, text="Skills").grid(row=6, column=0, sticky="w")
# tk.Checkbutton(root, text="Java", variable=java).grid(row=6, column=1, sticky="w")
# tk.Checkbutton(root, text="HTML", variable=html).grid(row=6, column=2, sticky="w")
# tk.Checkbutton(root, text="CSS", variable=css).grid(row=6, column=3, sticky="w")

# # Buttons
# tk.Button(root, text="Enroll Student").grid(row=7, column=1)
# tk.Button(root, text="Clear").grid(row=7, column=2)

# root.mainloop()

# import requests
# response=requests.get("https://api.example.com/data")
# print(response.json())


def romanToInt(s):
    d= {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(len(s)):
        if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
            result -= d[s[i]]
        else:
            result += d[s[i]]
    
    return result
print(romanToInt('IX'))
