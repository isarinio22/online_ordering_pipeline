# login.py

import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from selenium.common.exceptions import TimeoutException, InvalidSelectorException
import time


def perform_login():
    # Determine the absolute path to the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))

    # Path to credentials.env
    dotenv_path = os.path.join(project_root, 'config', 'credentials.env')

    # Check if credentials.env exists
    if not os.path.exists(dotenv_path):
        print(f"Error: credentials.env file not found at {dotenv_path}")
        return None, None

    # Load environment variables from credentials.env
    load_dotenv(dotenv_path=dotenv_path)

    # Retrieve credentials from environment variables
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    # Debugging: Print the loaded credentials (Masking Password)
    print(f"Loaded EMAIL: {email}")
    if password:
        print(f"Loaded PASSWORD: {'*' * len(password)}")
    else:
        print("Loaded PASSWORD: None")

    if not email or not password:
        print("Error: EMAIL and PASSWORD must be set in the environment variables.")
        return None, None

    # Path to config.json
    config_path = os.path.join(project_root, 'config', 'config.json')

    if not os.path.exists(config_path):
        print(f"Error: config.json file not found at {config_path}")
        return None, None

    # Load configuration from JSON
    with open(config_path, 'r', encoding='utf-8') as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing config.json: {e}")
            return None, None

    website_url = config.get('website_url')
    selectors = config.get('selectors', {})

    if not website_url or not selectors:
        print("Error: website_url or selectors not defined in config.json.")
        return None, None

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Start maximized for better visibility
    # chrome_options.add_argument("--headless")  # Uncomment to run in headless mode (no browser UI)

    # Initialize WebDriver
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return None, None

    try:
        # Step 1: Navigate to the Rami Levy website
        driver.get(website_url)
        print(f"Navigated to {website_url}")
        time.sleep(5)

        # Initialize WebDriverWait
        wait = WebDriverWait(driver, 30)  # Increased timeout

        # Step 2: Click on "התחברות" button
        login_button_xpath = selectors.get('login_button')
        if not login_button_xpath:
            print("Error: 'login_button' selector not found in config.json.")
            return driver, selectors

        try:
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
            login_button.click()
            print("Clicked on 'התחברות' button.")
        except (TimeoutException, InvalidSelectorException) as e:
            print(f"Error clicking 'התחברות' button: {e}")
            return driver, selectors

        # Step 3: Enter Email
        email_field_selector = selectors.get('email_field')
        if not email_field_selector:
            print("Error: 'email_field' selector not found in config.json.")
            return driver, selectors

        try:
            email_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, email_field_selector)))
            email_field.clear()
            email_field.send_keys(email)
            print("Entered email.")
            time.sleep(5)
        except (TimeoutException, InvalidSelectorException) as e:
            print(f"Error interacting with email field: {e}")
            return driver, selectors

        # Step 4: Enter Password
        password_field_selector = selectors.get('password_field')
        if not password_field_selector:
            print("Error: 'password_field' selector not found in config.json.")
            return driver, selectors

        try:
            password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_field_selector)))
            password_field.clear()
            password_field.send_keys(password)
            print("Entered password.")
        except (TimeoutException, InvalidSelectorException) as e:
            print(f"Error interacting with password field: {e}")
            return driver, selectors

        # Step 5: Click on Submit/Login button
        submit_login_selector = selectors.get('submit_login')
        if not submit_login_selector:
            print("Error: 'submit_login' selector not found in config.json.")
            return driver, selectors

        try:
            submit_login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, submit_login_selector)))
            submit_login_button.click()
            print("Clicked on submit 'התחברות' button.")
        except (TimeoutException, InvalidSelectorException) as e:
            print(f"Error clicking submit 'התחברות' button: {e}")
            return driver, selectors

        # Optional: Verify Successful Login
        # Example: Wait for a user-specific element to appear
        # username_dropdown_xpath = selectors.get('username_dropdown')
        # if username_dropdown_xpath:
        #     try:
        #         username_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, username_dropdown_xpath)))
        #         print("Login successful.")
        #     except TimeoutException:
        #         print("Login might have failed; username dropdown not found.")
        # else:
        #     print("Login button clicked, but username dropdown selector not provided.")

    

    except Exception as e:
        print(f"An unexpected error occurred during the login process: {e}")
        return driver, selectors

    return driver, selectors

# This block is optional and can be used for standalone testing
if __name__ == "__main__":
    perform_login()
