import nltk
from nltk.tokenize import word_tokenize

"""verbReplace
Parses a text and moves it to an output file, 
except with all the verbs changed to corresponding tenses of yeet. 

TODO: better documentation 
"""

# VB verb, base form – take
# VBD verb, past tense – took
# VBG verb, gerund/present participle – taking
# VBN verb, past participle – taken
# VBP verb, sing. present, non-3d – take
# VBZ verb, 3rd person sing. present – takes
VERBS = {
    "VB": "yeet",
    "VBD": "yote",
    "VBG": "yeeting",
    "VBN": "yoten",
    "VBP": "yeet",
    "VBZ": "yeets",
}


def main():
    # clear output file by opening in write mode. with statement automatically unloads the file from RAM
    with open("output.txt", "w") as outputFile:
        print("Output file cleared")

    text: str = ""

    with open("Manifesto.txt", "r", encoding="utf-8") as inputFile:
        # save the text from inputFile into string variable text
        text = inputFile.read()
        print("Input text read")

        tokenized = word_tokenize(text)

        tagged = nltk.pos_tag(tokenized)

        text: str = ""
        for i in tagged:
            if i[1] in VERBS:  # if the word is a verb
                text += VERBS[i[1]]  # add corresponding verb tense of yeet
            else:
                text += i[0]  # add word
            text += " "

    with open("output.txt", "a", encoding="utf-8") as outputFile:
        outputFile.write(text)
        # print(text)
        print("Text replaced")

    print("Done")


# in python, this block tells a programmer that this file is a driver script that is meant to be run
if __name__ == "__main__":
    main()
