from texttransformer import compareTexts, insertText, randomText, removeText, replaceText, searchText


allTests = {}


def test1():
    return None

def executeTests():
    for key in allTests.keys():
        executeTest(key)

def assertThat(statement):
    return statement

def defineTest(testname, test):
    allTests.update({testname: test})

def executeTest(testname):
    test = allTests.get(testname)
    if test() == None or test() == True:
        successfulTest(testname)
    else:
        failedTest(testname)

def successfulTest(testname):
    print("Test " + testname + " was successful")

def failedTest(testname):
    print("Test " + testname + " failed.")

def defineTests():
    def emptyTest():
        return None

    def textCompareTest():
        return assertThat(compareTexts('','') == "Equal")

    def textReplaceTest():
        return assertThat(replaceText('I have your cat', 'cat', 'dog') == "I have your dog")

    def textRemoveTest():
        return assertThat(removeText('I have your cat', 'r cat') == "I have you")

    def textInsertTest():
        return assertThat(insertText('I have you', 'you', ' now') == "I have you now")

    def textSearchTest():
        return assertThat(searchText('I have you now', 'you') == [7])

    def randomTest():
        return assertThat(randomText(randomText(randomText('Hey guys, welcome back! @@@666777'))) != "")

    defineTest('empty test', emptyTest)
    defineTest('empty texts are equal', textCompareTest)
    defineTest('replacing text works', textReplaceTest)
    defineTest('removing text works', textRemoveTest)
    defineTest('inserting text works', textInsertTest)
    defineTest('searching text works', textSearchTest)
    defineTest('random text works', randomTest)

def main():
    defineTests()
    executeTests()

if __name__ == '__main__':
    main()
