from pathlib import Path
from dotenv import load_dotenv
import os


env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

db_url = os.getenv('DATABASE_URL')
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'