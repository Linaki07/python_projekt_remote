def myPrint(s):
    print(s)

    def printTab(text,n=1):
        print(n*'\t',text)

        printTab('Hallo')
        printTab('Hallo',3)