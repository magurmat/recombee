from dotenv import load_dotenv
import os


load_dotenv()

IMAGE_STORE = os.path.abspath(os.getenv("IMAGE_STORE"))
DATABASE_URL = os.getenv("DATABASE_URL")