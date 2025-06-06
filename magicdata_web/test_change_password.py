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
new_password = config.RESET_PASSWORD
confirm_password = config.CONFIRM_PASSWORD

wait = WebDriverWait(driver, 60)
clear_input = Keys.CONTROL + 'a' + Keys.BACKSPACE



def create_an_account_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Account']")))

def full_name_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your full name']")))

def full_name_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full Name is too long')]")))

def email_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Email is too long')]")))

def full_name_special_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full Name should contain only letters and numbers')]")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email address']")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))


def signup_btn():

    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign Up']")))

def check_blank_fullname():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Please enter your full name')]")))

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


def toggle_visibility_icon_password():
    return wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@role='button']"
    )))

def toggle_visibility_icon_current_password():
    elements = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//input[@name='currentPassword']/following::span[@role='button']"
    )))
    return elements[0]


def toggle_visibility_icon_new_password():
    elements = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//input[@name='newPassword']/following::span[@role='button']"
    )))
    return elements[0]

def toggle_visibility_icon_confirm_password():
    elements = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//input[@name='confirmNewPassword']/following::span[@role='button']"
    )))
    return elements[0]

def signin_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))

def check_profile():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Profile')]")))

def check_security():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Security']")))

def update_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']")))

def close_alert():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))

def confirm_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Confirm']")))

def check_blank_current_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Current password is required!')]")))

def check_blank_new_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'New password is required!')]")))

def check_blank_confirm_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Confirm password is required!')]")))

def current_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='currentPassword']")))

def new_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='newPassword']")))

def confirm_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='confirmNewPassword']")))


def get_confirm_password_mismatch_error():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//div[contains(text(),'Passwords do not match')]"
    )))

def get_incorrect_current_password_error():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//span[contains(text(),'Invalid old password')]"
    )))

def get_empty_current_password_error():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//span[contains(text(),'oldPassword should not be empty')]"
    )))
def check_success_message_change_password():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//span[contains(text(),'Password changed successfully')]"
    )))

def get_same_as_current_password_error():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//div[contains(text(),'New password cannot be the same as the current password')]"
    )))

def is_logged_in():
        try:
            return driver.find_element(By.ID, "logout-button").is_displayed()
        except:
            return False


def avtar_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'avatar-icon')]//*[name()='svg']")))

def sign_out():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign Out']")))

def sign_out_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign Out']")))

def check_invalid_credentials():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))

# ============================== TEST CASES ==============================

class TestChangePassword:

    def test_valid_login_flow(self):
        logger.info("Running test: Valid login flow")
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        toggle_visibility_icon_password().click()
        logger.debug("Clicked password visibility toggle")
        signin_btn().click()
        time.sleep(5)
        assert validation_assert.DASHBOARD in driver.current_url
        logger.info("Signup successful and redirected to dashboard/home")


    def test_my_profile(self):
        logger.info("Navigating to Reset Password page via My Profile")
        check_profile().click()
        check_security().click()



    def test_blank_field_validation(self):
        logger.info("Testing blank field validation in change password form")
        update_btn().click()
        assert check_blank_current_password().text == validation_assert.ENTER_CURRENT_PASSWORD
        assert check_blank_new_password().text == validation_assert.ENTER_NEW_PASSWORD
        assert check_blank_confirm_password().text == validation_assert.ENTER_CONFIRM_PASSWORD
        logger.info("Blank field validations passed")



    def test_confirm_password_mismatch_validation(self):
        logger.info("Testing confirm password mismatch validation")
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(new_password)
        confirm_password_input_field().send_keys(password)
        toggle_visibility_icon_current_password().click()
        toggle_visibility_icon_new_password().click()
        toggle_visibility_icon_confirm_password().click()
        assert get_confirm_password_mismatch_error().text == error.DIFFERENT_PASSWORD_ERROR
        logger.info("Confirm password mismatch validation passed")




    def test_incorrect_current_password_validation(self):
        logger.info("Testing Wrong current password validation rules")
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(creds.PASSWORD)
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(creds.NEW_PASSWORD)
        confirm_password_input_field().send_keys(clear_input)
        confirm_password_input_field().send_keys(creds.NEW_PASSWORD)
        toggle_visibility_icon_current_password().click()
        toggle_visibility_icon_new_password().click()
        toggle_visibility_icon_confirm_password().click()
        update_btn().click()
        confirm_btn().click()
        close_alert().click()
        assert get_incorrect_current_password_error().text == error.INVALID_CURRENT_PASSWORD
        logger.info("Wrong Current password validation passed")



    def test_validation_new_password(self):
        logger.info("Testing new password validation rules")
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(creds.WEAK_PASSWORD)
        assert password_pattern_validation().text == error.PASSWORD_PATTERN_VALIDATION
        confirm_password_input_field().send_keys(clear_input)
        confirm_password_input_field().send_keys(creds.WEAK_PASSWORD)
        toggle_visibility_icon_current_password().click()
        toggle_visibility_icon_new_password().click()
        toggle_visibility_icon_confirm_password().click()
        logger.info("New password validation passed")



    def test_new_password_as_current_password(self):
        logger.info("Testing validation when new password is same as current password")
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(password)
        confirm_password_input_field().send_keys(clear_input)
        confirm_password_input_field().send_keys(password)
        toggle_visibility_icon_current_password().click()
        toggle_visibility_icon_new_password().click()
        toggle_visibility_icon_confirm_password().click()
        update_btn().click()
        logger.info("New password same as current password validation passed")
        assert get_same_as_current_password_error().text == error.OLD_PASSWORD_ERROR




    def test_copy_paste_new_password(self):
        logger.info("Testing copy-paste functionality in new password fields")
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(clear_input)
        confirm_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(new_password)
        toggle_visibility_icon_new_password().click()
        new_password_input_field().send_keys(Keys.CONTROL + 'A' + Keys.CONTROL + 'C')
        confirm_password_input_field().send_keys(Keys.CONTROL + 'v')
        logger.info("Copy-paste test completed")



    def test_change_password_flow(self):
        logger.info("Testing full password change flow")
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(new_password)
        confirm_password_input_field().send_keys(clear_input)
        confirm_password_input_field().send_keys(new_password)
        toggle_visibility_icon_current_password().click()
        toggle_visibility_icon_new_password().click()
        toggle_visibility_icon_confirm_password().click()
        time.sleep(1)
        update_btn().click()
        time.sleep(1)
        confirm_btn().click()
        close_alert().click()
        assert check_success_message_change_password().text == validation_assert.CHANGE_PASSWORD_SUCCESS_MESSAGE
        overlay_spinner()
        time.sleep(5)
        logger.info("Password change successful")



    def test_old_password_login(self):
        logger.info("Testing login with old password (should fail)")
        avtar_icon().click()
        sign_out().click()
        sign_out_btn().click()
        email_input_field().send_keys(email)
        password_input_field().send_keys(password)
        assert check_invalid_credentials().text == error.INVALID_PASSWORD_CREDS
        toggle_visibility_icon_password().click()
        logger.debug("Clicked password visibility toggle")
        signin_btn().click()
        time.sleep(3)
        logger.info("Old password login test passed (login failed as expected)")



    def test_new_password_login(self):
        refresh_page()
        logger.info("Testing login with new password")
        email_input_field().send_keys(email)
        password_input_field().send_keys(new_password)
        signin_btn().click()
        time.sleep(3)
        assert validation_assert.DASHBOARD in driver.current_url
        check_profile().click()
        check_security().click()
        current_password_input_field().send_keys(new_password)
        new_password_input_field().send_keys(password)
        confirm_password_input_field().send_keys(password)
        toggle_visibility_icon_current_password().click()
        toggle_visibility_icon_new_password().click()
        toggle_visibility_icon_confirm_password().click()
        update_btn().click()
        confirm_btn().click()
        close_alert().click()
        assert check_success_message_change_password().text == validation_assert.CHANGE_PASSWORD_SUCCESS_MESSAGE
        overlay_spinner()
        time.sleep(5)
        quit_browser()

        logger.info("Password reset to original and browser closed")