# Project 1
import random

print("🎮 Welcome to Rock-Paper-Scissors Game!")

# Step 1: Player input
player = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()

# Step 2: Computer random choice
options = ["Rock", "Paper", "Scissors"]
computer = random.choice(options)

print("Computer chose:", computer)

# Step 3: Determine the winner
if player == computer:
    print("It's a Tie! 🤝")
elif (player == "Rock" and computer == "Scissors") or \
     (player == "Scissors" and computer == "Paper") or \
     (player == "Paper" and computer == "Rock"):
    print("🎉 YOU WON!")
elif player in options:
    print("😞 YOU LOST! Better luck next time.")
else:
    print("❌ Invalid choice! Please choose Rock, Paper, or Scissors.")



print('------------------------------------------------------')
# Project 2

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # find the middle index

        if arr[mid] == target:
            return mid  # target found, return its index
        elif arr[mid] < target:
            low = mid + 1  # search right half
        else:
            high = mid - 1  # search left half

    return -1  # target not found


# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18]
target = int(input("Enter the number to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"✅ Target found at index {result}")
else:
    print("❌ Target not found in the list.")



print('------------------------------------------------------')
# Project 3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Sender details
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"  # Use an App Password, not your normal password

# Step 2: Recipients (can be one or multiple)
recipients = ["person1@example.com", "person2@example.com"]

# Step 3: Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = ", ".join(recipients)
msg["Subject"] = "Test Email from Python"

# Step 4: Add email body
body = "Hello!\n\nThis is a test email sent using Python.\n\nBest regards,\nYour Python Script"
msg.attach(MIMEText(body, "plain"))

# Step 5: Connect to Gmail's SMTP server and send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, msg.as_string())
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", e)



print('------------------------------------------------------')
# Project 4
import pandas as pd

# Function to determine Zodiac sign
def get_zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"


# Step 1: Take user input
name = input("Enter your name: ")
birthdate = input("Enter your birthdate (DD-MM-YYYY): ")

# Step 2: Extract day and month
day, month, year = map(int, birthdate.split("-"))

# Step 3: Determine Zodiac sign
zodiac = get_zodiac_sign(day, month)

print(f"\n{name}, your Zodiac sign is: {zodiac}")

# Step 4: Store in Pandas DataFrame
data = {
    "Name": [name],
    "Birthdate": [birthdate],
    "Zodiac Sign": [zodiac]
}

df = pd.DataFrame(data)

# Step 5: Save to file
df.to_csv("zodiac_data.csv", index=False)

print("\nData saved successfully to 'zodiac_data.csv'.")




print('------------------------------------------------------')
# Project 5
import os

# Step 1: Get user input
directory = input("Enter the directory path: ")
pattern = input("Enter the file extension or pattern to match (e.g., .txt, .jpg): ")
new_name = input("Enter the new base name for the files: ")

# Step 2: Change to target directory
try:
    os.chdir(directory)
except FileNotFoundError:
    print("❌ Directory not found! Please check the path.")
    exit()

# Step 3: Get list of files matching the pattern
files = [f for f in os.listdir() if f.endswith(pattern)]

# Step 4: Rename files
if not files:
    print("⚠ No files found matching the pattern.")
else:
    for index, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]   # Extract extension
        new_filename = f"{new_name}_{index}{file_ext}"
        os.rename(filename, new_filename)
        print(f"Renamed: {filename} → {new_filename}")

    print("\n✅ All matching files have been renamed successfully.")


    
print('------------------------------------------------------')
    # Project 6
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Step 1: Download page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find the table with company info
table = soup.find("table", {"class": "wikitable"})

# Step 3: Extract rows
data = []
rows = table.find_all("tr")

for row in rows[1:]:  # Skip header
    cols = row.find_all("td")
    
    if len(cols) >= 6:
        rank = cols[0].text.strip()
        name = cols[1].text.strip()
        industry = cols[2].text.strip()
        revenue = cols[3].text.strip()
        revenue_growth = cols[4].text.strip()
        headquarters = cols[5].text.strip()

        data.append([rank, name, industry, revenue, revenue_growth, headquarters])

# Step 4: Create DataFrame
df = pd.DataFrame(data, columns=[
    "Rank", "Company", "Industry", "Revenue", "Revenue Growth", "Headquarters"
])

# Step 5: Save results
df.to_csv("largest_us_companies.csv", index=False)

print("Scraping completed successfully!")

