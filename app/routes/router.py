from fastapi import APIRouter, HTTPException
from fuzzywuzzy import process
from app.schemas.info_requests import InputWord
from app.domain.generate_similar import generate_variations

router = APIRouter()

@router.post("/generate_similar_words/")
def generate_similar_words(input_word: InputWord):
    try:
        word = input_word.word
        max_variations = input_word.max_variations
        if not word.strip():
            raise HTTPException(status_code=400, detail="Word cannot be empty")

        # Gera palavras similares
        variations = generate_variations(word, max_variations)

        results = process.extract(word, variations, limit=input_word.max_variations)

        # Converte resultados em um formato amigável
        matches = [{"word": match[0], "similarity": match[1]} for match in results]

        return {"original_word": word, "matches": matches}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))