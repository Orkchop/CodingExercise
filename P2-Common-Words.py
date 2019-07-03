# Author: Ian Rosenfield
# This is P2) Common Words
# Write a function that takes in two lists of words and returns a list of the words common to both original lists.

# Here's the list of sample words to run through the function
sampleWords1 = ["hello", "adios", "goodbye", "hola", "au revoir", "bonjour"]
sampleWords2 = ["hello", "welcome","thanks", "goodbye", "please"]

# You can comment out the above sample words and use these, or sub your own into the lists, to test out the function
# sampleWords1 = ["here", "are", "some", "more", "sample", "words"]
# sampleWords2 = ["please", "add", "you're", "own", "sample", "words"]

# Takes in two lists of strings, compares them, and returns a list of the common strings
def commonWords (list1, list2):

    resultsList = []

    for counter in list1:
        if counter in list2:
            # This line checks and prevents duplicate words in the results list
            if counter not in resultsList:
                resultsList.append(counter)

    return resultsList

# Print out the result of the function, so you can tell that it works
print(commonWords(sampleWords1,sampleWords2))
