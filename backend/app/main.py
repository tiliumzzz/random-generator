from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from .database import load_quotes
from .models import Quote

app = FastAPI(title="Random Quote Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = load_quotes()


@app.get("/")
def read_root():
    return {"message": "Welcome to Random Quote Generator API"}


@app.get("/random-quote", response_model=Quote)
def get_random_quote():
    return random.choice(quotes)
