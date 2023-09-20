# Zalando-Beauty-New-Product-Scraper

Zalando Beauty New Product Scraper is a Python script for scraping product information from the [Zalando](https://www.zalando.de/) website and saving it to a CSV file. It allows you to collect and monitor new product arrivals in a specific category over time.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Scraper](#running-the-scraper)
- [Features](#features)
- [Data Storage](#data-storage)
- [Scheduled Execution](#scheduled-execution)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before using the Zalando Product Scraper, ensure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/SilentJMA/Zalando-Beauty-New-Product-Scraper.git
```
# Usage
## Configuration

Modify the url variable in the script to specify the Zalando category URL you want to scrape.
Set the csv_filename variable to specify the name of the CSV file where the data will be saved.
Adjust the product_limit variable to limit the number of products to scrape in each run.
Define the import_interval variable to set the interval for running the import (in seconds).

## Running the Scraper

To run the scraper, simply execute the script using Python:

   ```shell
python zalando_scraper.py
```

The script will scrape the product information, save it to the specified CSV file, and wait for the next scheduled run.

# Features

Scrapes product information including brand name, product name, URL, and price.
Handles German product names and UTF-8 encoding.
Checks for new products and skips existing ones.
Scheduled execution for periodic updates.
Data Storage
Product data is stored in a CSV file named zalando_new_products_XX.csv. The CSV file contains the following columns:

Brand Name
Product Name
Product URL
Product Price
Scheduled Execution
The script runs on a schedule defined by the import_interval variable. It will automatically update the product data at the specified interval.

# Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or create a pull request.
