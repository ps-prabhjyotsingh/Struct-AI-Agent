import os
from dotenv import load_dotenv

from app.common.Database import Database

load_dotenv()

#connect to DB
db = Database(
    os.environ.get("DB_DRIVER"),
    os.environ.get("DB_HOST"),
    os.environ.get("DB_NAME"),
    os.environ.get("DB_USERNAME"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("DB_PORT")
)

# openai = os.environ.get("OPENAI_KEY")
# openai_org = os.environ.get("OPENAI_ORG")

# init the app
from fastapi import FastAPI

# routes
from app.routes import app as app_routes, ai as ai_routes
app = FastAPI()

app.include_router(app_routes.router)
app.include_router(ai_routes.router)


# import all AI packages
#
# @dataclass
# class SupportDeps:
#     customer_id: int
#     #db:

# agent = Agent(
#     'anthropic:claude-3-5-haiku-latest',
#     # deps_type=str,
#     system_prompt="You are a helpful assistant"
# )



