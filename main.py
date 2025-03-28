import os
from dotenv import load_dotenv
load_dotenv()
openai = os.environ.get("OPENAI_KEY")
openai_org = os.environ.get("OPENAI_ORG")

# import the app packages
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from dataclasses import dataclass

app = FastAPI()
@app.get("/")
async def root():
    return {"message":"All good"}

# import all AI packages
from pydantic_ai import Agent, RunContext

@dataclass
class SupportDeps:
    customer_id: int
    #db:
agent = Agent(
    'anthropic:claude-3-5-haiku-latest',
    # deps_type=str,
    system_prompt="You are a helpful assistant"
)

