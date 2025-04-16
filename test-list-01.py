import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://razorpay.com/rize/investors-list/"

# Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage: {response.status_code}")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Debugging: Print the entire HTML content to identify the correct section
print(soup.prettify())

# Find the section containing the investors list using data-testid attributes
investors_section = soup.find('div', {'data-testid': 'investors-list'})

if not investors_section:
    print("Investors section not found!")
    exit()

# Debugging: Print the investors section HTML to verify the content
print(investors_section.prettify())

# Find all investor entries
investors = investors_section.find_all('div', {'data-testid': 'investor-entry'})

# Define the filters
ideal_for_filter = 'Pre-Seed'
industry_filter = 'Consumer'

# Iterate through each investor entry and apply filters
filtered_investors = []
for investor in investors:
    ideal_for = investor.find('div', {'data-testid': 'ideal-for'}).text.strip()
    industry = investor.find('div', {'data-testid': 'industry'}).text.strip()

    if ideal_for == ideal_for_filter and industry == industry_filter:
        name = investor.find('div', {'data-testid': 'name'}).text.strip()
        filtered_investors.append({
            'Name': name,
            'Ideal For': ideal_for,
            'Industry': industry
        })

# Print the filtered investors
for investor in filtered_investors:
    print(f"Name: {investor['Name']}, Ideal For: {investor['Ideal For']}, Industry: {investor['Industry']}")
