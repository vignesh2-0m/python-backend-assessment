Python Backend Engineer Take-Home Assessment

Overview
This project is a REST API service built using **FastAPI** and **PostgreSQL**.  
It acts as a bridge between a local database and the **GitHub API**, demonstrating data validation, persistence, and external API integration.

The API allows you to create, read, update, and delete GitHub repositories in a local database.
| Method | Endpoint           | Description |
|--------|------------------|-------------|
| POST   | `/repos/`         | Create a repo in the local database by fetching details from GitHub. |
| GET    | `/repos/{id}`     | Get repo details from the local database. |
| PUT    | `/repos/{id}`     | Update the number of stars for a repo in the local database. |
| DELETE | `/repos/{id}`     | Delete a repo from the local database. |
Database Schema

Table: repo

| Column | Type    | Description |
|--------|--------|-------------|
| id     | int    | Primary key, auto-incremented |
| owner  | str    | GitHub username of the repo owner |
| name   | str    | Repository name |
| stars  | int    | Number of stars on GitHub |
| url    | str    | URL of the GitHub repository |

Environment Variables

Create a `.env` file based on `.env.example`:

text
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<db_name>
GITHUB_API_BASE=https://api.github.com
