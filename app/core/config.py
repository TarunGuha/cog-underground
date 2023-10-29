import os
from dotenv import load_dotenv

load_dotenv()


APP_ENV = os.environ.get("APP_ENV", "development")

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")