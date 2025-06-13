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

def get_toggle_button():
    toggle = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "switcher-toggle")))
    return driver.execute_script("arguments[0].click()", toggle)

def get_project_status(driver, wait):
    toggle_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(@class, 'switcher')]/input[@type='checkbox']"))
    )
    is_checked = toggle_input.get_attribute("checked")  # Returns 'true' or None
    status = "Active" if is_checked else "Inactive"
    logger.info(f"Project status: {status}")
    return status

def check_checkbox_status():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(@class, 'switcher')]//input[@type='checkbox']")))

def check_active_msg():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Are you sure you want to activate this project?']")))

def check_inactive_msg():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Are you sure you want to deactivate this project?']")))

def get_all_project_elements():
    """
    Returns a list of all visible project card elements.
    Useful for iterating through projects and performing actions.
    """
    return wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='card card-border']")
    ))


# ============================== TEST CASES ==============================

class TestStatusProject:

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

    def test_toggle_multiple_projects(self):
            checkbox = check_checkbox_status()
            if not checkbox.is_selected():
                project_cards = get_all_project_elements()
                for index, project in enumerate(project_cards[:3]):  # test on first 3 to avoid long run
                    logger.info(f"Processing project #{index + 1}")
                    project.click()
                    time.sleep(1)

                    checkbox = check_checkbox_status()
                    initial_status = get_project_status(driver, wait)
                    get_toggle_button()
                    confirm_btn().click()
                    time.sleep(2)
                    updated_status = get_project_status(driver, wait)

                    assert initial_status != updated_status, "Toggle failed"
                    logger.info(f"Toggle succeeded for project #{index + 1}")
            else:
                logger.info("Project is already active. Skipping popup message test.")
    def test_toggle_for_inactive_project(self):
        logger.info("Checking if project is inactive...")
        checkbox = check_checkbox_status()
        if checkbox.is_selected():
            logger.info("Project is already active. No toggle needed.")
        else:
            logger.info("Project is inactive. Proceeding to toggle...")
            initial_status = get_project_status(driver, wait)
            logger.info(f"Initial status: {initial_status}")
            get_toggle_button()
            assert check_active_msg().text == validation_assert.ACTIVE_POPUP_MSG
            confirm_btn().click()
            logger.info("Waiting for UI to update...")
            time.sleep(3)
            save_screenshot("screenshorts/after_toggle.png")
            updated_status = get_project_status(driver, wait)
            logger.info(f"Status changed from {initial_status} to {updated_status}")
            assert initial_status != updated_status, "Project status did not toggle"

    def test_toggle_activation_for_inactive_project(self):
        logger.info("Checking if project is inactive...")
        checkbox = check_checkbox_status()
        if not checkbox.is_selected():
            logger.info("Project is inactive. Proceeding to toggle...")
            initial_status = get_project_status(driver, wait)
            logger.info(f"Initial status: {initial_status}")

            get_toggle_button()
            assert check_active_msg().text == validation_assert.ACTIVE_POPUP_MSG

            confirm_btn().click()
            time.sleep(3)
            save_screenshot("after_toggle_activation.png")

            updated_status = get_project_status(driver, wait)
            logger.info(f"Status changed from {initial_status} to {updated_status}")
            assert initial_status != updated_status, "Project status did not toggle"
        else:
            logger.info("Project already active. No toggle required.")

    def test_skip_toggle_for_active_project(self):
        checkbox = check_checkbox_status()
        assert checkbox.is_selected(), "Checkbox should be selected (active state)"
        logger.info("Project is active. No toggle should be performed.")

    def test_validate_activation_popup_message(self):
        checkbox = check_checkbox_status()
        if not checkbox.is_selected():
            get_toggle_button()
            popup_text = check_active_msg().text
            logger.info(f"Popup message displayed: {popup_text}")
            assert popup_text == validation_assert.ACTIVE_POPUP_MSG, "Incorrect activation popup message"
            confirm_btn().click()
        else:
            logger.info("Project is already active. Skipping popup message test.")

    def test_status_ui_update_after_toggle(self):
        checkbox = check_checkbox_status()
        if not checkbox.is_selected():
            initial_status = get_project_status(driver, wait)
            get_toggle_button()
            confirm_btn().click()
            time.sleep(3)
            save_screenshot("status_change_ui.png")
            updated_status = get_project_status(driver, wait)
            assert initial_status != updated_status, "Status not updated in UI"
        else:
            logger.info("Project is already active. No status update expected.")


    def test_search_random_project_name_with_status_check(self):
        logger.info("Running: test_search_random_project_name_with_status_check")
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

        logger.info("Search result includes the expected project.")


        checkbox = check_checkbox_status()
        if checkbox.is_selected():
            logger.info(f"Project '{selected_name}' is currently ACTIVE.")
        else:
            logger.info(f"Project '{selected_name}' is currently INACTIVE.")


    def test_search_inactive_project_and_toggle(self):
        logger.info("Searching for a random project...")
        project_names = get_all_project_names()
        assert project_names, "No project names found."

    def test_cancel_toggle_does_not_change_status(self):
        checkbox = check_checkbox_status()
        if not checkbox.is_selected():
            logger.info("Checking status before toggle cancel...")
            initial_status = get_project_status(driver, wait)

            get_toggle_button()
            assert check_active_msg().is_displayed(), "Activation popup not visible"
            cancel_btn().click()

            time.sleep(2)
            updated_status = get_project_status(driver, wait)

            assert initial_status == updated_status, "Status changed even after cancel"
            logger.info("Toggle cancel worked correctly — no status change.")

            project_names = get_all_project_names()
            print("Project Names:", project_names)
            selected_name = random.choice(project_names)
            partial_name = selected_name.split()[0]
            search_box = search_input_field()
            search_box.clear()
            search_box.send_keys(partial_name)
            search_box.send_keys(Keys.ENTER)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='card card-border']//h3"))
            )

            checkbox = check_checkbox_status()
            if not checkbox.is_selected():
                logger.info("Inactive project found. Attempting toggle...")
                get_toggle_button()
                assert check_active_msg().text == validation_assert.ACTIVE_POPUP_MSG
                confirm_btn().click()
                logger.info("Project activated successfully.")
            else:
                logger.info("Project is already active.")
        else:
            logger.info("Project is already active. Skipping popup message test.")

        quit_browser()



