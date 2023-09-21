# Zalando-Beauty-New-Products-Scraper

Zalando Beauty New Product Scraper is a Python script for scraping product information from the [Zalando](https://www.zalando.de/) website and saving it to a CSV file. It allows you to collect and monitor new product arrivals in a specific category over time.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Scraper](#running-the-scraper)
- [Features](#features)
  - [Scraping Product Data](#scraping-product-data)
  - [CSV Data Storage](#csv-data-storage)
  - [Monitoring New Products](#monitoring-new-products)
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

 ```bash
   git clone https://github.com/SilentJMA/Zalando-Beauty-New-Product-Scraper.git
```
2. Change to the project directory:

```bash
cd Zalando-Beauty-New-Product-Scraper
```

3. Install the required Python packages:

 ```bash
   pip install -r requirements.txt
```

# Usage
## Configuration
<li>Modify the <b>url</b> variable in the script to specify the Zalando category URL you want to scrape.</li>
<li>Define the <b>csv_directory</b> variable to specify the directory where CSV files will be saved.</li>
<li>Set the <b>product_limit</b> variable to limit the number of products to scrape in each run.</li>
<li>Define the <b>import_interval</b> variable to set the interval for running the import (in seconds).</li>

## Running the Scraper

To run the scraper, simply execute the script using Python:

 ```bash
python zalando_beauty_scraper.py
```

The script will scrape the product information, save it to the specified CSV file, and wait for the next scheduled run.

# Features
<p><li>Scrapes product information including brand name, product name, URL, and price.</li>
<li>Handles German product names and UTF-8 encoding.</li>
<li>Checks for new products and skips existing ones.</li>
<li>Scheduled execution for periodic updates.</li>

# CSV Data Storage
<p>Each import creates a new CSV file with a timestamp in the filename.
Previous CSV files are retained in the specified directory.
The CSV files contain data for new products found during each import.</p>

# Scraping Product Data
The scraper extracts the following product information:

<li>Brand Name</li>
<li>Product Name (German product names are supported)</li>
<li>Product URL</li>
<li>Product Price</li>
<li>Premium Delivery Status</li>

# Monitoring New Products
<p>The script checks for new products by comparing product names with previous imports.<br>
Only new products are saved to the CSV files.<br>
You can monitor product arrivals over time and track changes.</p>

# Scheduled Execution
The script runs on a schedule defined by the import_interval variable. It will automatically update the product data at the specified interval.

# Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or create a pull request.
