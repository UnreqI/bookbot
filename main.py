import sys
from stats import getWordCount, getCharacterCount, sortCharacterDictionaries

def getBookText(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookpath: str = sys.argv[1] # second command line input
    booktext: str = getBookText(bookpath)
    print("---------- Word Count ----------")
    print(f"Found {getWordCount(booktext)} total words")
    print("---------- Character Count ----------")
    sortedCharacterCount: list[dict[str, str], dict[str, int]] = sortCharacterDictionaries(getCharacterCount(booktext))
    for element in sortedCharacterCount:
        if element["name"].isalpha():
            print(f"{element["name"]}: {element["num"]}")

main()
