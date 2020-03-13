# Spell Check Starter

import re


def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w']+", textData)


# Load data files into global variables
dictionary = loadWordsFromFile("data-files/dictionary.txt")
aliceWordsCh1 = loadWordsFromFile("data-files/AliceInWonderLandCh1.txt")
aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")

print(aliceWordsCh1)

# Main Menu
loop = True
while loop:
    # Print Main Menu
    print("Main Menu")
    print("1: Linear Search Alice In Wonderland Ch. 1")
    print("2: Binary Search Alice In Wonderland Ch. 1")
    print("3: Linear Search Alice In Wonderland Full")
    print("4: Binary Search Alice In Wonderland Full")
    print("5: Exit")
    selection = input("Enter menu selection (1-5): ")

    # Process selection
    if (selection == "1"):
        # YOUR CODE HERE
        print("Linear Search Alice Ch.1")
    elif (selection == "2"):
        # YOUR CODE HERE
        print("Binary Search Alice Ch.1")
    elif (selection == "3"):
        # YOUR CODE HERE
        print("Linear Search Alice Full")
    elif (selection == "4"):
        # YOUR CODE HERE
        print("Binary Search Alice Full")
    elif (selection == "5"):
        loop = False
# end while loop
print("goodbye")
