from pydantic import BaseModel


class Wordlist(BaseModel):
    word: str
    description: str
