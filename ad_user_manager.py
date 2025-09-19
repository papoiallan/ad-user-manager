import csv

def create_user(first_name, last_name, username, password):
    print(f"[OK] Created user: {username} | {first_name} {last_name} | {password}")

def bulk_create(csv_file):
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            create_user(row['FirstName'], row['LastName'], row['Username'], row['Password'])

if __name__ == "__main__":
    CSV_FILE = "users.csv"
    bulk_create(CSV_FILE)