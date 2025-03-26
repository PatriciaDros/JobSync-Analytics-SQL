import pandas as pd
import mysql.connector
from mysql.connector import Error

# Database connection function
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="greyson",
            database="jobsync"
        )
        print("Connected to MySQL database!")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Load Excel data into MySQL
def load_data_to_db(file_path, table_name):
    try:
        # Read Excel file
        df = pd.read_excel(file_path)
        print(f"Loaded Excel file: {file_path}")
        print(f"Original columns: {df.columns.tolist()}")

        # Sanitize column names
        df.columns = [col.lower().strip().replace(" ", "_").replace("-", "_").replace(".", "").replace("(", "").replace(")", "") for col in df.columns]
        print(f"Sanitized columns: {df.columns.tolist()}")

        # Replace NaN with empty string
        df = df.fillna("")

        # Connect to database
        connection = connect_db()
        if connection is None:
            return

        cursor = connection.cursor()

        # Create table with sanitized columns
        column_defs = ", ".join([f"`{col}` VARCHAR(255)" for col in df.columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"
        print(f"Executing CREATE TABLE query: {create_table_query}")
        cursor.execute(create_table_query)

        # Insert data row by row
        for i, row in df.iterrows():
            placeholders = ", ".join(["%s"] * len(row))
            insert_query = f"INSERT INTO {table_name} ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({placeholders})"
            cursor.execute(insert_query, tuple(row))

        # Commit changes
        connection.commit()
        print(f"Data loaded into {table_name} successfully! Rows inserted: {len(df)}")

    except Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

# Main execution
if __name__ == "__main__":
    base_path = "/home/tricia/Desktop/JobSync-Analytics-SQL/"
    files = [
        ("ALL CONTRACT JOBS.xlsx", "contract_jobs"),
        ("JOB INFO.xlsx", "job_info"),
        ("LABS.xlsx", "labs"),
        ("LOGS.xlsx", "logs"),
        ("Monthly Status.xlsx", "monthly_status"),
        ("NAMED RANGES.xlsx", "named_ranges"),
        ("REOCCUPANCY.xlsx", "reoccupancy")
    ]
    for file_name, table_name in files:
        file_path = f"{base_path}{file_name}"
        print(f"\nProcessing {file_name}...")
        load_data_to_db(file_path, table_name)
