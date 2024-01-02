import os
import dotenv

dotenv.load_dotenv("var.env")

DEBUG = True  
SECRET_KEY = os.environ['SECRET_KEY']
DB_URL = os.environ['DATABASE_URL']

MAIL_SERVER = 'smtp.gmail.com' # AI
MAIL_PORT = 587 # AI
MAIL_USE_TLS = True # AI
MAIL_USE_SSL = False # AI
MAIL_USERNAME = os.environ['EMAIL_USERNAME'] # AI
MAIL_PASSWORD = os.environ['EMAIL_PASSWORD'] # AI
MAIL_DEFAULT_SENDER = os.environ['EMAIL_USERNAME'] # AI


