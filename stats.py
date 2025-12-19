def getWordCount(text: str) -> int:
    return len(text.split())

def getCharacterCount(text: str) -> int:
    characterCount: dict[str,int] = {}
    for character in text:
        character = character.lower() # only consider lowercase
        # get the character count from characterCount, then increment and store
        characterCount.setdefault(character, 0)
        characterCount[character] += 1

    return characterCount

def sortOn(items):
    return items["num"]

def sortCharacterDictionaries(characterCount: dict[str,int]) -> list[dict[str, str], dict[str,int]]:
    dictionaryList: list[dict[str, str], dict[str, int]] = []
    for character, count in characterCount.items():
        dictionaryList.append({"name": character, "num": count})

    dictionaryList.sort(reverse=True, key=sortOn)
    return dictionaryList


