import time,os,datetime
import random
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from magicdata_setup.config import config
from magicdata_setup import randomeString
from log_config import setup_logger
from constant import validation_assert,creds,error,input_field


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
valid_project_name = input_field.VALID_PROJECT
wait = WebDriverWait(driver, 60)
clear_input = Keys.CONTROL + 'a' + Keys.BACKSPACE
edit_project = input_field.EDIT_PROJECT
delete_project = input_field.DELETE_PROJECT

def create_an_account_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Account']")))

def full_name_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your full name']")))

def project_name_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Project Name']")))

def description_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Describe your project']")))

def full_name_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full Name is too long')]")))

def project_name_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Project Name is too long')]")))

def description_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Description is too long')]")))

def email_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Email is too long')]")))

def full_name_special_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Full Name should contain only letters and numbers')]")))

def project_name_special_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Project Name should contain only letters and numbers')]")))

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

def check_projects():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Projects')]")))

def check_security():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Security']")))

def update_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']")))

def close_alert():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))

def confirm_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Confirm']")))

def cancel_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']")))

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

def new_projects_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New Project']")))
def edit_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'flex') and contains(@class, 'gap-2')]//a//*[name()='svg'][contains(@class, 'lucide-pencil')]")))
def delete_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and contains(@class, 'lucide-trash2')]")))


def check_invalid_credentials():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))

def save_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))

def check_blank_projectname():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Project Name is required')]")))

def check_blank_description():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Description is required')]")))

def check_success_profile_update():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'User updated successfully')]")))

def check_success_msg_project_update():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Project updated successfully')]")))


def check_success_msg_project_delete():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Project deleted successfully')]")))




def verify_valid_project_name():
    return wait.until(EC.element_to_be_clickable((By.XPATH, f"//h3[normalize-space(text())='{selected_name}']")))

def verify_valid_project_edit():
    return wait.until(EC.element_to_be_clickable((By.XPATH, f"//h3[normalize-space(text())='{edit_project}']")))

def existing_project_error_message():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Project already exists')]")))

def search_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search projects...']")))


def search_results_container():
    return  wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6']")))

def project_cards():
    return  wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'card card-border')]")))

def get_all_project_names():
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card card-border']//h3"))
    )
    elements = driver.find_elements(By.XPATH, "//div[@class='card card-border']//h3")
    return [el.text.strip() for el in elements if el.text.strip()]

def check_success_msg_project_create():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Project created successfully')]")))

# ============================== TEST CASES ==============================

class TestReadProject:

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
        logger.info("Login successful and redirected to dashboard/home")


    def test_my_project(self):
        logger.info("Navigating to My Project")
        check_projects().click()
        time.sleep(2)


    def test_search_random_project_name(self):
        logger.info("Running: test_search_random_project_name")

        project_names = get_all_project_names()

        assert project_names, "No project names found on the dashboard."
        global selected_name

        selected_name = random.choice(project_names)
        partial_name = selected_name.split()[0]
        logger.info(f"🔍 Searching for random project name: {selected_name}")
        search_box = search_input_field()
        search_box.clear()
        search_box.send_keys(partial_name)
        search_box.send_keys(Keys.ENTER)


        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card card-border']//h3"))
        )
        visible_names = get_all_project_names()

        logger.info(f"Visible project names after search: {visible_names}")
        assert any(selected_name in name for name in visible_names), \
            f"Search result does not include the selected project: {selected_name}"


        logger.info("Search result correctly includes the expected project.")


    def test_read_project(self):
        logger.info("Deleting project with a valid project name and checking success toaster")
        verify_valid_project_name().click()
        quit_browser()




