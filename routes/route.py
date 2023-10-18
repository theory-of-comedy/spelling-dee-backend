from fastapi import APIRouter
from utils.words_dfa import isAccepted

router = APIRouter()


@router.get("/word/check")
async def check_word(word: str):
    return (isAccepted(word.lower()))
