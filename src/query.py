import mysql.connector
import csv
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Fetch user data by user ID and save to CSV.")
parser.add_argument("-u", "--user_id", type=int, required=True, help="The user ID to fetch data for.")
args = parser.parse_args()

# mysql -h user-expenditure-data.c38ogckoido2.ca-central-1.rds.amazonaws.com -P 3306 -u admin -p
# Database connection parameters (replace with your credentials)
db_config = {
    "host": "user-expenditure-data.c38ogckoido2.ca-central-1.rds.amazonaws.com",
    "user": "admin",
    "password": "CloudComputing",
    "database": "test"
}

try:
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Execute the query
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (args.user_id,))
    rows = cursor.fetchall()

    # If no data is found
    if not rows:
        print(f"No data found for user ID {args.user_id}.")
    else:
        # Save the result to a CSV file
        output_file = f"user_data_{args.user_id}.csv"
        with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([desc[0] for desc in cursor.description])  # Write header
            writer.writerows(rows)  # Write data

        print(f"Data saved to {output_file}")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Clean up
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
