memorizer = []

def compareTexts(text1, text2):
    if text1 == text2:
        return "Equal"
    return "Not equal"

def replaceText(text, wordToReplace, replacement):
    return str.replace(text,wordToReplace,replacement)

def removeText(text, wordToRemove):
    return replaceText(text, wordToRemove, '')

def insertText(text, whereToInsert, wordToInsert):
    return replaceText(text, whereToInsert, whereToInsert + wordToInsert)

def removeTextFrom(text, index, endingCharacters):
    return text[:index]+text[:str.find(text, endingCharacters)]

def searchText(text, textToSearch):
    global memorizer
    if str.count(text, textToSearch) <= 0:
        temp = memorizer
        memorizer = []
        return temp
    nextIndex = str.find(text, textToSearch)
    memorizer.append(nextIndex)
    return searchText(removeTextFrom(text, 0, textToSearch), textToSearch)

def randomText(text):
    result = ""
    for character in text:
        result = result + str(searchText(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~', character))
    return result

def main():
    print(randomText(randomText(randomText('Hey guys, welcome back! @@@666777'))))

if __name__ == '__main__':
    main()