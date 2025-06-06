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
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'email must be an email')]")))


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

# ============================== TEST CASES ==============================

class TestSignIn:

    def test_blank_field_validation(self):
        logger.info("Running test: Blank field validation")
        signin_btn().click()
        assert check_blank_email().text == validation_assert.ENTER_SIGNIN_EMAIL
        assert check_blank_password().text == validation_assert.ENTER_SIGNIN_PASSWORD
        logger.info("Blank password validation passed")

    def test_invalid_email(self):
        logger.info("Running test: Invalid email format")
        refresh_page()
        email_input_field().send_keys(creds.INVALID_EMAIL_FORMAT)
        password_input_field().send_keys(password)
        signin_btn().click()
        assert valid_email_validation().text == error.ENTER_VALID_EMAIL
        logger.info("Invalid email format validation passed")

    def test_non_existing_email(self):
        logger.info("Running test: Invalid email")
        refresh_page()
        email_input_field().send_keys(creds.NON_EXIST_USER)
        password_input_field().send_keys(password)
        signin_btn().click()
        assert non_existing_user_error_message().text == error.NON_EXITING_USER_MESSAGE
        logger.info("Invalid password validation passed")

    def test_invalid_password(self):
        logger.info("Running test: Invalid password")
        refresh_page()
        email_input_field().send_keys(email)
        password_input_field().send_keys(creds.WEAK_PASSWORD)
        signin_btn().click()
        assert check_invalid_credentials().text == error.INVALID_PASSWORD_CREDS
        logger.info("Invalid password validation passed")

    def test_password_toggle_visibility(self):
        logger.info("Running test: Password visibility toggle")
        refresh_page()
        email_input_field().send_keys(email)
        password_input_field().send_keys(password)
        toggle_visibility_icon().click()
        visible_type = password_input_field().get_attribute("type")
        assert visible_type == "text", "Password is not visible after toggle"
        logger.info("Password visibility toggle working correctly")

    def test_email_max_length(self):
        logger.info("Running test: Email max length")
        refresh_page()
        long_email = "a" * 250 + "@test.com"
        email_input_field().send_keys(long_email)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        signin_btn().click()
        assert email_format_validation().text == error.VALID_EMAIL_FORMAT_ERROR
        logger.info("Invalid password validation passed")

    def test_email_with_spaces(self):
        logger.info("Running test: Email with leading/trailing spaces")
        refresh_page()
        email_input_field().send_keys("  " + email + "  ")
        password_input_field().send_keys(creds.PASSWORD)
        signin_btn().click()
        assert check_invalid_credentials().text == error.INVALID_PASSWORD_CREDS
        logger.info("Invalid password validation passed")

    def test_invalid_creds(self):
        logger.info("Running test: Invalid creds")
        refresh_page()
        email_input_field().send_keys(creds.INVALID_EMAIL_FORMAT)
        password_input_field().send_keys(creds.WEAK_PASSWORD)
        signin_btn().click()
        assert valid_email_validation().text == error.ENTER_VALID_EMAIL
        logger.info("Invalid password validation passed")

    def test_password_field_type_after_toggle_back(self):
        logger.info("Running test: Password field type toggles back to password")

        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        toggle_visibility_icon().click()
        time.sleep(1)
        toggle_visibility_icon().click()  # toggle back
        visible_type = password_input_field().get_attribute("type")
        assert visible_type == "password", "Password field should toggle back to hidden type"
        logger.info("Password visibility toggle back working")

    def test_login_with_uppercase_email(self):
        logger.info("Running test: Login with uppercase email")

        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL.upper())
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        signin_btn().click()
        time.sleep(3)
        assert validation_assert.DASHBOARD in driver.current_url
        avtar_icon().click()
        sign_out().click()
        sign_out_btn().click()
        logger.info("Login with uppercase email successful")

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
        quit_browser()



