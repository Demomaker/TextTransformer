from texttransformer import compareTexts


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

def failedTest(testname, expected, actual):
    print("Test " + testname + "failed.\nExpected : " + expected + "\nActual :" + actual)

def defineTests():
    def emptyTest():
        return None

    def textCompareTest():
        return assertThat(compareTexts('','') == "Equal")

    defineTest('empty test', emptyTest)
    defineTest('empty texts are equal', textCompareTest)

def main():
    defineTests()
    executeTests()

if __name__ == '__main__':
    main()
