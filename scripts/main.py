import time
from login import perform_login
from navigate_orders import navigate_order
from payment import click_to_payment, click_checkout_button, click_payment_button, check_and_skip
from handle_purchase import select_shipping_time, choose_credit_card, confirm_credit_card_payment, fill_cvv


def main():
    # Step 1: Perform Login
    driver, selectors = perform_login()
    if not driver or not selectors:
        print("Login failed or selectors not available.")
        return

    # Short delay after login
    time.sleep(2)

    # Step 2: Navigate Orders
    success_navigation = navigate_order(driver, selectors)
    if not success_navigation:
        print("Navigation through orders failed.")
        driver.quit()  # Ensure the browser is closed on failure
        return

    # Short delay after navigation
    time.sleep(2)

    # Step 3: Click on "To Payment"
    success_payment = click_to_payment(driver, selectors)
    if not success_payment:
        print("Failed to click 'To Payment'.")
        driver.quit()
        return

    # Short delay after clicking "To Payment"
    time.sleep(2)
    

    # Step 5: Click on "Payment" (תשלום)
    success_payment_button = click_payment_button(driver, selectors)
    if not success_payment_button:
        print("Failed to click 'Payment' (תשלום).")
        driver.quit()
        return

        # Step 4: Check and Skip if Needed
    skip_handled = check_and_skip(driver, selectors)
    if not skip_handled:
        print("Failed to handle the missing item issue.")
        driver.quit()
        return

    # # Step 6: Select Shipping Time
    # success_shipping_time = select_shipping_time(driver)
    # if not success_shipping_time:
    #     print("Failed to select a shipping time.")
    #     pass


    # Step 7: Choose Credit Card
    success_credit_card = choose_credit_card(driver, selectors)
    if not success_credit_card:
        print("Failed to choose credit card.")
        driver.quit()
        return

    # Step 8: Confirm Credit Card Payment
    success_confirm_payment = confirm_credit_card_payment(driver, selectors)
    if not success_confirm_payment:
        print("Failed to confirm credit card payment.")
        driver.quit()
        return

    # Step 9: Fill CVV
    success_fill_cvv = fill_cvv(driver, selectors)
    if not success_fill_cvv:
        print("Failed to fill CVV.")


    # save_button_xpath = selectors.get('click_on_save')
    # if not save_button_xpath:
    #     print("Error: 'login_button' selector not found in config.json.")
    #     return driver, selectors

    #     try:
    #         save_button_xpath = wait.until(EC.element_to_be_clickable((By.XPATH, save_button_xpath)))
    #         save_button_xpath.click()
    #         print("Clicked on 'התחברות' button.")
    #     except (TimeoutException, InvalidSelectorException) as e:
    #         print(f"Error clicking 'התחברות' button: {e}")
    #         return driver, selectors

    #     return driver, selectors
       
        

    # Pause for observation (optional)
    input("Press Enter to close the browser...")

    # Cleanup: Close the browser
    driver.quit()
    print("Browser closed.")

if __name__ == "__main__":
    main()
