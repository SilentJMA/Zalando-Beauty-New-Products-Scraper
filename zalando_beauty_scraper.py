import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime, timedelta

# Define the URL of the zalando.de category you want to scrape.
url = 'https://en.zalando.de/beauty-women/?order=activation_date'

# Define the CSV filename to save the results.
current_date = datetime.now().strftime("%d%m%Y%H%M%S")
csv_filename = f'Zalando_new_products_{current_date}.csv'

# Define the limit of products to collect (84 products).
product_limit = 31

# Define the interval for running the import (in seconds, set to 24 hours).
import_interval = 24 * 60 * 60  # 24 hours

# Function to scrape and save the data to a CSV file
def scrape_and_save_to_csv():
    # Send an HTTP GET request to the URL.
    response = requests.get(url)

    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing product information (adjust this based on website structure).
        product_elements = soup.find_all('div', class_='_5qdMrS w8MdNG cYylcv BaerYO _75qWlu iOzucJ JT3_zV _Qe9k6')

        # Create a list to store the product data.
        products_data = []

        # Load the previous products from the CSV file
        previous_products = load_previous_products()

        # Loop through each product element and extract the name and price.
        for product in product_elements[:product_limit]:
            # Extract product brand name
            product_brand_name = product.find('h3', class_='FtrEr_ lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2')
            product_brand_name = product_brand_name.text.strip() if product_brand_name else ''

            # Extract product name (German product names)
            product_name_element = product.find('h3', class_='sDq_FX lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2')
            product_name = product_name_element.get_text(strip=True) if product_name_element else ''

            # Extract product URL
            product_url = product.find('a', class_='q84f1m CKDt_l LyRfpJ JT3_zV CKDt_l _2dqvZS')
            product_url = product_url['href'] if product_url else ''

            # Extract product price
            product_price = product.find('span', class_='sDq_FX lystZ1 FxZV-M HlZ_Tf')
            product_price = product_price.text.strip() if product_price else ''

            # Check for Premium Delivery tag and class
            premium_delivery = product.find('p', class_='sDq_FX lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7')
            premium_delivery_text = "Premium Delivery" if premium_delivery else "No"

            # Check if the product is new
            if is_new_product(product_name, previous_products):
                products_data.append([product_brand_name, product_name, product_url, product_price, premium_delivery_text])

        # Save the data to a CSV file with UTF-8 encoding
        if products_data:
            with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Brand Name', 'Product Name', 'Product URL', 'Product Price', 'Premium Delivery'])
                csv_writer.writerows(products_data)

            print(f"Data saved to '{csv_filename}'")
        else:
            print("No new products found.")

# Function to load previous products from the CSV file
def load_previous_products():
    previous_products = set()
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                product_name = row[1]  # Assuming product name is in the second column
                previous_products.add(product_name)
    except FileNotFoundError:
        pass  # The CSV file doesn't exist yet, no previous products

    return previous_products

# Function to check if a product is new
def is_new_product(product_name, previous_products):
    return product_name not in previous_products

# Infinite loop to run the import every 24 hours
while True:
    scrape_and_save_to_csv()
    # Calculate the next import time
    next_import_time = datetime.now() + timedelta(seconds=import_interval)
    print(f"Next import will occur at: {next_import_time}")
    # Sleep until the next import time
    time.sleep(import_interval)
