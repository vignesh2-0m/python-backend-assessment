from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

print(">>> ENV PATH:", ENV_PATH)

load_dotenv(dotenv_path=ENV_PATH)

DATABASE_URL = os.getenv("DATABASE_URL")
GITHUB_API_BASE = os.getenv("GITHUB_API_BASE")

print(">>> DATABASE_URL VALUE:", DATABASE_URL)
print(">>> GITHUB_API_BASE:", GITHUB_API_BASE)
