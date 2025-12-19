from stats import getWordCount, getCharacterCount

def getBookText(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def main():
    bookpath: str = r"./books/frankenstein.txt"
    print(f"Found {getWordCount(getBookText(bookpath))} total words")
    print(getCharacterCount(getBookText(bookpath)))

main()
