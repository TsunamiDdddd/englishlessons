from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = str(os.environ.get("DB_HOST"))
DB_PORT = str(os.environ.get("DB.HOST"))
DB_NAME = str(os.environ.get("DB_NAME"))
DB_USER = str(os.environ.get("DB_USER"))
DB_PASS = str(os.environ.get("DB_PASS"))