from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
from dotenv import load_dotenv
import time



def select_shipping_time(driver):
    # Locate all date columns
    date_columns = driver.find_elements(By.XPATH, "//div[contains(@class, 'swiper-slide')]")

    for column_index, column in enumerate(date_columns):
        print(f"Checking date column {column_index + 1}...")

        # Find all time slots in the current column
        time_slots = column.find_elements(By.XPATH, ".//button[contains(@class, 'shipping-time')]")

        for slot in time_slots:
            # Check if the slot is available
            if slot.get_attribute("aria-disabled") == "false":
                print(f"Available time slot found: {slot.text}")
                slot.click()
                return True  # Stop after selecting a valid slot

        # If no slots are available in the current column, continue to the next column
        print(f"No available time slots in column {column_index + 1}.")

        # Handle navigation if columns are not all visible
        next_button = driver.find_element(By.XPATH, "//div[contains(@class, 'swiper-button-next') and @aria-disabled='false']")
        if next_button:
            print("Navigating to the next column...")
            next_button.click()
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'swiper-slide')]")))

    print("No available shipping times found.")
    return False


def choose_credit_card(driver, selectors):
    """
    Selects the 'האשראי שלי' credit card option.
    """
    credit_card_button_xpath = selectors.get("choose_credit_card_button")
    if not credit_card_button_xpath:
        print("Error: 'choose_credit_card_button' selector not found in config.json.")
        return False

    try:
        # Wait until the button with the specific text or label is clickable
        credit_card_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, credit_card_button_xpath))
        )
        credit_card_button.click()
        print("Selected 'האשראי שלי' credit card option.")
        return True
    except Exception as e:
        print(f"Failed to select 'האשראי שלי' credit card option: {e}")
        return False


def confirm_credit_card_payment(driver, selectors):
    """
    Clicks on the 'תשלום בכרטיס זה' button to confirm the credit card selection.
    """
    confirm_button_xpath = selectors.get("confirm_credit_card_button")
    if not confirm_button_xpath:
        print("Error: 'confirm_credit_card_button' selector not found in config.json.")
        return False

    try:
        # Wait until the button is clickable
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, confirm_button_xpath))
        )
        confirm_button.click()
        print("Clicked on 'תשלום בכרטיס זה' button.")
        return True
    except Exception as e:
        print(f"Failed to click on 'תשלום בכרטיס זה' button: {e}")
        return False




def fill_cvv(driver, selectors):
    """
    Fills the CVV in the credit card input field with enhanced debugging.
    """
    try:
        # Load CVV from environment variables
        load_dotenv()
        cvv = os.getenv("CVV")
        if not cvv:
            print("Error: CVV is not set in the environment variables.")
            return False

        print("Looking for CVV input field...")
        
        # Switch to default content first
        driver.switch_to.default_content()
        
        # Add a wait before looking for iframes
        time.sleep(2)
        
        # Find all iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"Found {len(iframes)} iframes")

        # Print iframe details
        for idx, iframe in enumerate(iframes):
            print(f"\nIframe {idx + 1}:")
            print(f"Name: {iframe.get_attribute('name')}")
            print(f"ID: {iframe.get_attribute('id')}")
            print(f"Class: {iframe.get_attribute('class')}")
            print(f"Src: {iframe.get_attribute('src')}")

        # Try each iframe
        for idx, iframe in enumerate(iframes):
            try:
                print(f"\nTrying iframe {idx + 1}")
                driver.switch_to.frame(iframe)
                
                # Print the current iframe's HTML for debugging
                print("Current iframe HTML structure:")
                print(driver.page_source[:500] + "...")  # Print first 500 chars
                
                # Try multiple selector strategies
                selectors_to_try = [
                    (By.ID, "v-card-cvv"),
                    (By.CSS_SELECTOR, "input#v-card-cvv"),
                    (By.CSS_SELECTOR, "input[type='tel'][data-card-field]"),
                    (By.CSS_SELECTOR, ".card-input__input"),
                    (By.XPATH, "//input[@id='v-card-cvv']"),
                    (By.XPATH, "//input[@type='tel' and @data-card-field]")
                ]

                for by, selector in selectors_to_try:
                    try:
                        print(f"Trying selector: {by} - {selector}")
                        cvv_input = WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((by, selector))
                        )
                        
                        # If found, try to interact with it
                        print("Found CVV input, attempting to fill...")
                        driver.execute_script("arguments[0].scrollIntoView(true);", cvv_input)
                        time.sleep(0.5)
                        
                        # Try JavaScript to set value
                        driver.execute_script("arguments[0].value = arguments[1];", cvv_input, cvv)
                        print("Successfully filled CVV using JavaScript")
                        return True
                        
                    except Exception as e:
                        print(f"Selector {selector} failed: {str(e)[:100]}...")
                        continue
                
                driver.switch_to.parent_frame()
                
            except Exception as e:
                print(f"Error with iframe {idx + 1}: {str(e)[:100]}...")
                driver.switch_to.default_content()
                continue

        print("Could not find CVV input in any iframe")
        return False

    except Exception as e:
        print(f"Failed to fill the CVV field: {str(e)[:100]}...")
        return False

    finally:
        # Always switch back to default content
        driver.switch_to.default_content()