import csv

# Demo version: Simulates AD user creation from a CSV file
# CSV Format: FirstName,LastName,Username,Password

CSV_FILE = "users.csv"
DOMAIN = "MYDOMAIN"

def create_user(first_name, last_name, username, password):
    # Instead of running PowerShell, just print what would happen
    command = (
        f"New-ADUser -Name '{first_name} {last_name}' "
        f"-GivenName '{first_name}' -Surname '{last_name}' "
        f"-SamAccountName '{username}' -UserPrincipalName '{username}@{DOMAIN}.local' "
        f"-AccountPassword (ConvertTo-SecureString '{password}' -AsPlainText -Force) "
        f"-Enabled $true"
    )
    print(f"SIMULATION: {command}")

def bulk_create(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            create_user(row['FirstName'], row['LastName'], row['Username'], row['Password'])

if __name__ == "__main__":
    bulk_create(CSV_FILE)