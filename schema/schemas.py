def individual_serial(wordlist) -> dict:
    return {
        "id": str(wordlist["_id"]),
        "word": wordlist["word"],
        "description": wordlist["description"]
    }


def list_serial(wordlists) -> list:
    return [individual_serial(wordlist) for wordlist in wordlists]
