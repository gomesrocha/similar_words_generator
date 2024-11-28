from pydantic import BaseModel


class InputWord(BaseModel):
    word: str
    max_variations: int = 10