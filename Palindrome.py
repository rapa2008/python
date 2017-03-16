def palindrome():
        """This function will check if entered string is palindrome or not."""
        strInput=input('Input a string1: ')
        if len(strInput) == 1:
                print("Its not a palindrome")
        else:
                iFlag = 1
                iFwd, iBack = 0, len(strInput) - 1
                while iFwd < iBack:
                        if strInput[iFwd] != strInput[iBack]:
                                iFlag = 0
                                break
                        else:
                                iFwd, iBack = iFwd + 1, iBack - 1
                if iFlag == 1:
                        print("Its a palindrome")
                else:
                        print("Its not a palindrome")



