from stats import getWordCount, getCharacterCount, sortCharacterDictionaries

def getBookText(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    bookpath: str = r"./books/frankenstein.txt"
    booktext: str = getBookText(bookpath)
    print("---------- Word Count ----------")
    print(f"Found {getWordCount(booktext)} total words")
    print("---------- Character Count ----------")
    sortedCharacterCount: list[dict[str, str], dict[str, int]] = sortCharacterDictionaries(getCharacterCount(booktext))
    for element in sortedCharacterCount:
        if element["name"].isalpha():
            print(f"{element["name"]}: {element["num"]}")

main()
