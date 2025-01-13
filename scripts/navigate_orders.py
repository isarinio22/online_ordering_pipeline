# navigate_order.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, InvalidSelectorException


def click_my_cart(driver, selectors):
    my_cart_button_xpath = selectors.get('my_cart_button')
    if not my_cart_button_xpath:
        print("Error: 'my_cart_button' selector not found in config.json.")
        return False

    try:
        my_cart_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, my_cart_button_xpath))
        )
        my_cart_button.click()
        print("Clicked on 'הסל שלי' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'הסל שלי' button: {e}")
        return False


def click_weekly_purchase(driver, selectors):
    weekly_purchase_button_xpath = selectors.get('weekly_purchase_button')
    if not weekly_purchase_button_xpath:
        print("Error: 'weekly_purchase_button' selector not found in config.json.")
        return False

    try:
        weekly_purchase_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, weekly_purchase_button_xpath))
        )
        weekly_purchase_button.click()
        print("Clicked on 'קנייה שבועית' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'קנייה שבועית' button: {e}")
        return False


def click_add_products_to_cart(driver, selectors):
    add_products_to_cart_button_xpath = selectors.get('add_products_to_cart_button')
    if not add_products_to_cart_button_xpath:
        print("Error: 'add_products_to_cart_button' selector not found in config.json.")
        return False

    try:
        add_products_to_cart_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, add_products_to_cart_button_xpath))
        )
        add_products_to_cart_button.click()
        print("Clicked on 'הוספת מוצרים לסל' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'הוספת מוצרים לסל' button: {e}")
        return False

def click_close_popup(driver, selectors):
    close_popup_button_selector = selectors.get('close_popup_button')
    if not close_popup_button_selector:
        print("Error: 'close_popup_button' selector not found in config.json.")
        return False

    try:
        close_popup_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, close_popup_button_selector))
        )
        close_popup_button.click()
        print("Clicked on 'close-popup' button.")
        return True
    except (TimeoutException, InvalidSelectorException) as e:
        print(f"Error clicking 'close-popup' button: {e}")
        return False




def navigate_order(driver, selectors):
    # Step 1: Click on "My Cart"
    success_cart = click_my_cart(driver, selectors)
    if not success_cart:
        print("Failed to click 'My Cart'.")
        return False

    # Step 2: Click on "Weekly Purchase"
    success_weekly_purchase = click_weekly_purchase(driver, selectors)
    if not success_weekly_purchase:
        print("Failed to click 'Weekly Purchase'.")
        return False

    # Step 3: Click on "Add Products to Cart"
    success_add_products = click_add_products_to_cart(driver, selectors)
    if not success_add_products:
        print("Failed to click 'Add Products to Cart'.")
        return False

    # Step 4: Click on "Close Popup"
    success_close_popup = click_close_popup(driver, selectors)
    if not success_close_popup:
        print("Failed to click 'Close Popup'.")
        return False

    print("Navigation through orders completed successfully.")
    return True

