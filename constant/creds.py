from magicdata_setup.randomeString import generate_random_full_name, generate_unique_email

LONG_FULL_NAME = "ABC XYZ 2333333333333333333333333333555555"
INVALID_FULL_NAME = "ABCD@"
VALID_FULL_NAME = generate_random_full_name()
INVALID_EMAIL = "invalid@"
PASSWORD= "Password@123"
MISMATCH_PASSWORD = "Mismatch@123"
WEAK_PASSWORD = "weakpass1"
VALID_UNIQUE_EMAIL = generate_unique_email()