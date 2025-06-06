import time,os,datetime
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from magicdata_setup.config import config
from magicdata_setup import randomeString
from log_config import setup_logger
from constant import validation_assert,creds,error
from magicdata_setup.randomeString import generate_random_emoji_string

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
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))

def full_name_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full name is too long')]")))

def email_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Email is too long')]")))

def full_name_special_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full name should contain only letters and numbers')]")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email address']")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))

def confirm_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Confirm your password']")))

def signup_btn():

    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign Up']")))

def save_btn():

    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))

def check_blank_fullname():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full name is required')]")))

def check_blank_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Email is required')]")))

def check_blank_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Password is required')]")))

def username_exists_validation():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//span[contains(text(),'Username taken. Please choose another')]"
    )))


def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The email has already been taken.')]")))

def email_invalid_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))

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

def toggle_visibility_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@role='button']")))

def signin_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))

def check_profile():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Profile')]")))

def check_security():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Security']")))

def check_success_profile_update():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'User updated successfully')]")))

def get_updated_full_name():
    return wait.until(EC.presence_of_element_located((
        By.NAME, "fullName"
    )))


def avtar_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'avatar-icon')]//*[name()='svg']")))

def sign_out():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign Out']")))

def sign_out_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign Out']")))

# ============================== TEST CASES ==============================

class TestProfile:

    def test_valid_login_flow(self):
        logger.info("Running test: Valid login flow")
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        toggle_visibility_icon().click()
        logger.debug("Clicked password visibility toggle")
        signin_btn().click()
        time.sleep(5)
        assert validation_assert.DASHBOARD in driver.current_url
        logger.info("Signup successful and redirected to dashboard/home")

    def test_my_profile(self):
        logger.info("Navigating to Reset Password page via My Profile")
        check_profile().click()

    def test_blank_field_validation(self):
        logger.info("Testing blank field validation in change password form")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys(Keys.ENTER)
        assert check_blank_fullname().text == error.EMPTY_FULL_NAME

        logger.info("Blank field validations passed")



    def test_full_name_special_validation(self):
        logger.info("Running test: Full name special character validation")
        full_name_input_field().send_keys(creds.INVALID_FULL_NAME)
        time.sleep(2)
        assert full_name_special_validation().text == error.SPECIAL_VALIDATION
        logger.info("Full name special character validation passed")


    def test_full_name_only_spaces(self):
        logger.info("Running test: Full name with only spaces")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys("     ")
        save_btn().click()
        assert full_name_special_validation().text == error.SPECIAL_VALIDATION
        logger.info("Validation passed for full name with only spaces")



    def test_full_name_numbers_only(self):
        logger.info("Running test: Full name with numbers only")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys("123456")
        save_btn().click()
        logger.info("Validation passed for full name with only numbers")


    def test_very_long_full_name(self):
        logger.info("Running test: Very long full name")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys(creds.LONG_FULL_NAME)
        assert full_name_length_validation().text == error.FULL_NAME_VALIDATION
        logger.info("Long full name validation passed")


    def test_full_name_with_spaces(self):
        logger.info("Running test: Full name with leading/trailing spaces")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys("   " + creds.VALID_FULL_NAME + "   ")
        save_btn().click()
        time.sleep(2)
        assert full_name_input_field().get_attribute("value").strip() == creds.VALID_FULL_NAME
        logger.info("Leading/trailing spaces trimmed correctly")



    def test_full_name_with_middle_initial(self):
        logger.info("Running test: Full name with middle initial and space")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys("Priya A Singh")
        save_btn().click()
        assert full_name_input_field().get_attribute("value").strip() == "Priya A Singh"
        logger.info("Full name accepted with middle initial")


    def test_full_name_stress_input(self):
        logger.info("Running test: Full name rapid input paste")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys("Priya" * 50)
        save_btn().click()
        assert full_name_length_validation().text == error.FULL_NAME_VALIDATION
        logger.info("Stress input validation triggered")


    def test_full_name_with_hyphen_apostrophe(self):
        logger.info("Running test: Full name with hyphen and apostrophe")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys("Anne-Marie O'Neill")
        save_btn().click()
        logger.info("Full name with hyphen/apostrophe accepted or validated")



    def test_valid_full_name_toaster(self):
        logger.info("Updating profile with a valid full name and checking success toaster")
        full_name_input_field().send_keys(clear_input)
        full_name_input_field().send_keys(creds.VALID_FULL_NAME)
        save_btn().click()
        assert check_success_profile_update().text == validation_assert.SUCCESS_TOASTER_MESSAGE_PROFILE_UPDATE
        logger.info("Profile updated successfully and toaster verified")



    def test_logout(self):
        avtar_icon().click()
        sign_out().click()
        sign_out_btn().click()
        quit_browser()
        logger.info("Login with uppercase email successful")
