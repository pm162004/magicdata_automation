from magicdata_setup.randomeString import get_random_word_from_api, generate_random_project_names

VALID_PROJECT = get_random_word_from_api()
LONG_PROJECT_NAME = "PROJECT " * 245
INVALID_PROJECT_NAME = "PROJECT@"
VALID_DESCRIPTION = "Test Description"
EXISTING_PROJECT_NAME = "EXISTING PROJECT"
LONG_DESCRIPTION_NAME = "Description " * 500
EDIT_PROJECT = generate_random_project_names(1)[0]
DELETE_PROJECT = generate_random_project_names(1)[0]
EXACT_PROJECT_NAME = "c"
PARTIAL_PROJECT_NAME = "ro"
VALID_SINGLE_EMAIL = "user1@yopmail.com"
VALID_MULTIPLE_EMAIL = "user2@yopmail.com,user3@yopmail.com"
MIXED_EMAIL_CASE ="UsErMiXeD@yopmail.com"
INVALID_EMAIL = "invalidemail.com"
MULTIPLE_INVALID_EMAIL = "wrong,alsoWrong@,bad.com"
ALREADY_INVITED_EMAIL = "user1@yopmail.com"