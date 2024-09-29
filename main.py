from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pync import Notifier

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Google Messages
driver.get("https://messages.google.com/web/authentication")

# Wait for the QR code to be visible
try:
    qr_code = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "mw-qr-code[data-e2e-qr-code]"))
    )
    print("QR code is visible. Please scan it with your phone to pair the device.")
except Exception as e:
    print("QR code not found:", e)
    driver.quit()

# Wait for the user to complete the pairing process
try:
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.banner-container"))
    )
    print("Device paired successfully.")
except Exception as e:
    print("Pairing failed or took too long:", e)
    driver.quit()

# Now you can create event listeners for new message alerts
def check_new_messages():
    try:
        new_message = driver.find_element(By.CSS_SELECTOR, "a.list-item[data-e2e-conversation][data-e2e-is-unread='true']")
        if new_message:
            sender = new_message.find_element(By.CSS_SELECTOR, "span[data-e2e-conversation-name]").text
            message_content = new_message.find_element(By.CSS_SELECTOR, "mws-conversation-snippet span.ng-star-inserted").text
            print(f"New message received from {sender}: {message_content}")
            
            # Send notification
            Notifier.notify(message_content, title='New message from: ' + sender, sound='default')
            
            # Modify the attribute to mark the message as read
            driver.execute_script("arguments[0].setAttribute('data-e2e-is-unread', 'false')", new_message)
            print(f"Marked message from {sender} as read.")
    except Exception as e:
        print("No new messages or error occurred:", str(e))

# Example: Polling for new messages every 5 seconds
try:
    while True:
        check_new_messages()
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopping the script.")
finally:
    driver.quit()