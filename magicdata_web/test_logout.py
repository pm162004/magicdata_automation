import time,os,datetime
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from magicdata_setup.config import config
from magicdata_setup import randomeString
from log_config import setup_logger
from constant import validation_assert,creds,error
logger = setup_logger()
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument('--headless')
driver.maximize_window()
logger.info("Opening signup page")
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.CORRECT_PASSWORD
confirm_password = config.CONFIRM_PASSWORD
wait = WebDriverWait(driver, 60)
clear_input = Keys.SPACE+ Keys.CONTROL + 'a' + Keys.BACKSPACE



def create_an_account_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Account']")))

def full_name_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your full name']")))

def full_name_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full Name is too long')]")))

def email_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Email is too long')]")))

def email_format_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid email address')]")))


def full_name_special_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full Name should contain only letters and numbers')]")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email address']")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))

def confirm_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Confirm your password']")))

def signup_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign Up']")))

def signin_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))

def sign_out():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign Out']")))

def sign_out_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign Out']")))

def check_blank_fullname():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter your full name')]")))

def check_blank_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter your email address')]")))

def check_blank_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter your password')]")))

def username_exists_validation():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//span[contains(text(),'Username taken. Please choose another')]"
    )))


def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The email has already been taken.')]")))

def check_password_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password field must be at least 8 characters')]")))

def check_strong_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password Must include uppercase, lowercase, number, and special character')]")))

def success_signup_message():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been successfully created!')]")))

def refresh_page():
    logger.info("Refreshing page")
    time.sleep(1)
    return driver.refresh()

def quit_browser():
    logger.info("Quitting browser")
    return driver.quit()

def overlay_spinner():
    return WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))

def save_screenshot(filename, use_timestamp=True, folder="screenshorts"):
    os.makedirs(folder, exist_ok=True)

    if use_timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = "{}_{}.png".format(filename, timestamp)
    else:
        filename = "{}.png".format(filename)

    full_path = folder, filename
    driver.save_screenshot(f"{folder}/{filename}")
    return full_path

def valid_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter a valid email address')]")))  # Adjust text if needed

def password_mismatch_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),\"Confirm Password doesn't match with Password.\")]")))

def password_pattern_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Password must contain at least: 1 uppercase letter,1 lowercase letter, 1 number and 1 special character.')]")))

def signup_success_message():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Signup successful')]")))

def existing_user_error_message():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email already registered')]")))

def non_existing_user_error_message():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'User not found')]")))

def toggle_visibility_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@role='button']")))

def check_invalid_credentials():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))

def is_logged_in():
        try:
            return driver.find_element(By.ID, "logout-button").is_displayed()
        except:
            return False
def avtar_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'avatar-icon')]//*[name()='svg']")))
def verify_avtar_email():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-xs']")))


# ============================== TEST CASES ==============================

class TestSignOut:

    def test_valid_login_flow(self):
        logger.info("Running test: Valid login flow")
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        toggle_visibility_icon().click()
        logger.debug("Clicked password visibility toggle")
        signin_btn().click()
        time.sleep(3)
        assert validation_assert.DASHBOARD in driver.current_url
        logger.info("Signup successful and redirected to dashboard/home")

    def test_logout(self):
        logger.info("Running test: Valid logout  flow")
        refresh_page()
        avtar_icon().click()
        sign_out().click()
        time.sleep(2)
        sign_out_btn().click()
        quit_browser()



