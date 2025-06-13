from magicdata_setup.randomeString import generate_random_full_name, generate_unique_email

LONG_FULL_NAME = "ABC XYZ 2333333333333333333333333333555555"
LONG_EMAIL = "a" * 245 + "@test.com"
LONG_Ful = "a" * 245
INVALID_FULL_NAME = "ABCD@"
VALID_FULL_NAME = generate_random_full_name()
INVALID_EMAIL_FORMAT = "invalid@gmail"
NON_EXIST_USER = "nonexist@gmail.com"
PASSWORD= "Password@123"
NEW_PASSWORD = "Newpassword@123"
MISMATCH_PASSWORD = "Mismatch@123"
WEAK_PASSWORD = "weakpass1"
VALID_UNIQUE_EMAIL = generate_unique_email()


