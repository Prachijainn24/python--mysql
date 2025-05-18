import mysql.connector
import os

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         # default user
        password="",         # leave blank if no password
        database="employee"  # use your database
    )

    cursor = conn.cursor()

    # Execute query
    cursor.execute("SELECT * FROM empdata")
    rows = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]

    # Define Desktop path
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    file_path = os.path.join(desktop, "empdata_output.txt")

    # Write to file
    with open(file_path, "w", encoding='utf-8') as f:
        f.write("\t".join(columns) + "\n")  # Write headers
        for row in rows:
            f.write("\t".join(str(cell) for cell in row) + "\n")

    print(f"✅ Data successfully saved to {file_path}")

except mysql.connector.Error as err:
    print("❌ MySQL Error:", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
