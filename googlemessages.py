from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Google Messages for Web
driver.get('https://messages.google.com/web')

# Wait for QR code scanning
input("Scan the QR code with your Android device and press Enter...")

def send_text_via_google_messages(phone_number, message):
    # Click on the 'New Message' button
    new_message_btn = driver.find_element_by_xpath('//button[contains(@aria-label, "Start chat")]')
    new_message_btn.click()
    time.sleep(2)

    # Enter the phone number
    to_input = driver.find_element_by_xpath('//input[@type="text"]')
    to_input.send_keys(phone_number)
    to_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Enter the message
    message_box = driver.find_element_by_xpath('//div[@aria-label="Text message"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

# Example usage
# send_text_via_google_messages('+1234567890', 'Hello from Python!')