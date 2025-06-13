import os
from dotenv import load_dotenv
load_dotenv()

class EnvVariables:
    WEB_URL = os.getenv("WEB_URL")
    CORRECT_EMAIL = os.getenv("CORRECT_EMAIL")
    CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
    PASSWORD = os.getenv("CORRECT_PASSWORD")
    RESET_PASSWORD = os.getenv("RESET_PASSWORD")
    CONFIRM_PASSWORD = os.getenv("CONFIRM_PASSWORD")
    TEAM_EMAIL = os.getenv("TEAM_EMAIL")
    TEAM_PASSWORD = os.getenv("TEAM_PASSWORD")

config = EnvVariables()
