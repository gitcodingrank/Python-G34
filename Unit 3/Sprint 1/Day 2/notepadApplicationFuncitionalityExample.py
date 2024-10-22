#Problem Statement: Creating a Notepad and implementing find, replace and other useful functions


#Solution:

print("--------------WELCOME TO MY APPLICAITON---------------")

str = input("Enter the Text: ")

def notepadMenu():
    print("1. To Find")
    print("2. To Replace")
    print("3. To Count Sepecfic Char/Sequence")
    print("4. Print Text")
    print("5. Re-Enter the Text")
    print("6. Exit")

while True:
    notepadMenu()
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        text = input("Enter Text to Find: ")
        msg = ""
        if str.find(text)!=-1:
            msg = "Text is available in the original text."
        else:
            msg = "Text is not available in the original text."
        print("--------------------------------------------")
        print(msg)
        print("--------------------------------------------")
    elif choice == 2:
        replaceText = input("What to Replace: ")
        msg = ""
        if str.find(replaceText)!=-1:
            replaceValue = input("Text for Replacing: ")
            str = str.replace(replaceText, replaceValue)
            msg = "Text has replaced successfully."
        else:
            msg = "Text is not found in the original string."
        print("--------------------------------------------")
        print(msg)
        print("--------------------------------------------")
    elif choice == 3:
        #Implement the functionality for counting particular char/sequence
        pass
    elif choice == 4:
        print("--------------------------------------------")
        print(str)
        print("--------------------------------------------")
    elif choice == 5:
        #Implement the functionality for re entring the text
        pass
    elif choice == 6:
        res = input("do you want to continue(y/n): ")
        if res in ['n', 'N']:
            print("Thank you for using my application.")
            break
    else:
        print("Invalid choice, please try again.")