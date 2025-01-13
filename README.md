# Online Ordering Pipeline
Overview
This repository contains a Python script (main.py) that automates the process of buying groceries from the Rami Levy online store. By filling out a simple configuration file, you can provide your Rami Levy login credentials and any other necessary details. Once set up, the script will log into your account, navigate through the store, and perform automated actions (like adding items to your cart and possibly checking out). This can help save time and reduce manual, repetitive tasks.
This project automates the process of placing orders on [Rami Levy](https://www.rami-levy.co.il/he) using Selenium.



## Project Structure

online_ordering_pipeline/ │ ├── config/ │ ├── config.json │ └── credentials.env │ ├── logs/ │ └── automation.log │ ├── scripts/ │ ├── main.py │ ├── login.py │ ├── navigate_orders.py │ ├── handle_purchase.py │ └── payment.py │ ├── utils/ │ ├── browser_setup.py │ ├── helpers.py │ └── logger.py │ ├── requirements.txt └── README.md

## Locate config.json
In the project’s root directory, find the config.json file.

Open config.json
Edit the file in your favorite text editor and replace any placeholder values (like YOUR_USERNAME, YOUR_PASSWORD, etc.) with your actual Rami Levy account credentials and any other required details (e.g., payment info, addresses, item preferences, etc.).


## Running the Script
Open Your Terminal
Navigate to the root directory of this project. For example:

cd path/to/your/rami-levy-automation

## Run main.py
Execute the script by typing:

python main.py

