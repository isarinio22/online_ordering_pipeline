from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, InvalidSelectorException
import time

def click_to_payment(driver, selectors):
    to_payment_button_xpath = selectors.get('to_payment_button')
    if not to_payment_button_xpath:
        print("Error: 'to_payment_button' selector not found in config.json.")
        return False

    try:
        to_payment_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, to_payment_button_xpath))
        )
        to_payment_button.click()
        print("Clicked on 'לתשלום' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'לתשלום' button: {e}")
        return False


def click_checkout_button(driver, selectors):
    checkout_button_xpath = selectors.get('checkout_button')
    if not checkout_button_xpath:
        print("Error: 'checkout_button' selector not found in config.json.")
        return False

    try:
        checkout_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, checkout_button_xpath))
        )
        checkout_button.click()
        print("Clicked on 'לקופה' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'לקופה' button: {e}")
        return False


def click_payment_button(driver, selectors):
    payment_button_xpath = selectors.get('payment_button')
    if not payment_button_xpath:
        print("Error: 'payment_button' selector not found in config.json.")
        return False

    try:
        payment_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, payment_button_xpath))
        )
        payment_button.click()
        print("Clicked on 'תשלום' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'תשלום' button: {e}")
        return False


def click_skip_button(driver, selectors):
    skip_button_xpath = selectors.get('skip_button')
    if not skip_button_xpath:
        print("Error: 'skip_button' selector not found in config.json.")
        return False

    try:
        skip_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, skip_button_xpath))
        )
        skip_button.click()
        print("Clicked on 'דלג/י' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'דלג/י' button: {e}")
        return False


def check_and_skip(driver, selectors):
    """
    Continuously checks for the 'skip' button and clicks it until no more missing items are detected.
    """
    skip_button_xpath = selectors.get('skip_button')
    if not skip_button_xpath:
        print("Error: 'skip_button' selector not found in config.json.")
        return False

    try:
        while True:
            try:
                # Wait briefly to see if the skip button appears
                skip_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, skip_button_xpath))
                )
                if skip_button:
                    print("Missing item detected. Attempting to click 'Skip' button.")
                    skip_button.click()
                    time.sleep(2)  # Short delay to allow the action to process
            except TimeoutException:
                # No more skip buttons detected
                print("No more missing items detected. Continuing...")
                break
        return True
    except Exception as e:
        print(f"Unexpected error while handling skip: {e}")
        return False

