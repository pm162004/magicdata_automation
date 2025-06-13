import subprocess

file_order = [
    "magicdata_web/test_signup.py",
    "magicdata_web/test_login.py",
    "magicdata_web/test_change_password.py",
    "magicdata_web/test_profile.py",
    "magicdata_web/test_create_project.py",
    "magicdata_web/test_read_project.py",
    "magicdata_web/test_edit_project.py",
    "magicdata_web/test_delete_project.py",
    "magicdata_web/test_status_project.py",
    "magicdata_web/test_filter_project.py",
    "magicdata_web/test_search_project.py",
    "magicdata_web/test_logout.py"
]

for file in file_order:
    result = subprocess.run(["pytest", file])
    if result.returncode != 0:
        print(f"Test failed: {file}")
        break
