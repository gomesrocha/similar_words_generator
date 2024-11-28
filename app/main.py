from fastapi import FastAPI, HTTPException

import logging

from app.routes.router import router as similar_words_router
from app.schemas.info_requests import InputWord
from app.domain.generate_similar import generate_variations
# Configuração de logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from fuzzywuzzy import fuzz, process  #


app = FastAPI(title="Similar Words Generator", description="A microservice for generating similar words", version="1.0.0")


app.include_router(similar_words_router)

@app.get("/")
def read_root():
    return {"message": "Subfinder API is running!"}
