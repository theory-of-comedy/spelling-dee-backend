from fastapi import APIRouter
from models.wordlists import Wordlist
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/")
async def get_wordlists():
    wordlists = list_serial(collection_name.find())
    return wordlists


@router.post("/")
async def post_wordlist(wordlist: Wordlist):
    collection_name.insert_one(dict(wordlist))
    return dict(wordlist)


@router.put("/{id}")
async def put_wordlist(id: str, wordlist: Wordlist):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(wordlist)})
    return dict(wordlist)


@router.delete("/{id}")
async def delete_wordlist(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
