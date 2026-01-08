from app.database import get_db
from app.models import Repo
from app.services.github_service import fetch_repo
from dotenv import load_dotenv
load_dotenv()
db = next(get_db())
data = fetch_repo("octocat", "Hello-World")
repo = Repo(**data)
db.add(repo)
db.commit()
db.refresh(repo)
print(repo.id, repo.name, repo.owner)
