import psycopg2
from psycopg2 import sql

def get_ahmed_salary():
    try:
        # Connect to your friend's PostgreSQL database
        conn = psycopg2.connect(
            host="192.168.200.86",  # Replace with the IP address of your friend's server
            database="postgres",  # Replace with the actual database name
            user="postgres",  # Replace with your PostgreSQL username
            password="123456789",  # Replace with your PostgreSQL password
            port="5432"  # PostgreSQL port (default is 5432)
        )

        cursor = conn.cursor()

        # Query to search for Ahmed's salary
        query = sql.SQL("SELECT name, salary FROM employees WHERE name = %s")
        cursor.execute(query, ('ahmed',))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print(f"Ahmed's salary: {result[1]}")
        else:
            print("Ahmed not found in the database.")

        # Close connection
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    get_ahmed_salary()

""""
import psycopg2
from psycopg2 import sql

def get_ahmed_salary():
    try:
        # Connect to your friend's PostgreSQL database
        conn = psycopg2.connect(
            host="192.168.200.86",  # Replace with the IP address of your friend's server
            database="postgres",  # Replace with the actual database name
            user="postgres",  # Replace with your PostgreSQL username
            password="123456789",  # Replace with your PostgreSQL password
            port="5432"  # PostgreSQL port (default is 5432)
        )

        cursor = conn.cursor()

        # Query to search for Ahmed's salary
        query = sql.SQL("SELECT name, salary FROM employees WHERE name = %s")
        cursor.execute(query, ('khaled',))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print(f"khaled's salary: {result[1]}")
        else:
            print("Ahmed not found in the database.")

        # Close connection
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    get_khaled_salary()
"""
#print("Hello, World! from onemin.py")
