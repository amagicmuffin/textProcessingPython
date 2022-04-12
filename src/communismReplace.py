"""communismReplace
when ran, this script copies input.txt into output.txt but replaces every fourth word with "communism"
all whitespace is converted into spaces (including newlines)

only works when input.txt and output.txt are in the same directory (aka folder) as this script

"""


def main():
    # clear output file by opening in write mode. with statement automatically unloads the file from RAM
    with open("output.txt", "w") as outputFile:
        print("Output file cleared")

    text: str = ""

    with open("input.txt", "r") as inputFile:
        # save the text from inputFile into string variable text
        text = inputFile.read()
        print("Input text read")

    with open("output.txt", "a") as outputFile:
        # split text by whitespace into a list
        splittedText: [str] = text.split()

        # one by one, add words from splittedText into outputFile. every fourth word is instead "communism"
        for index, word in enumerate(splittedText):
            if index % 4 != 0:
                outputFile.write(word + " ")
            else:
                outputFile.write("communism ")

        print("Text replaced")

    print("Done")


# in python, this block tells a programmer that this file is a driver script that is meant to be run
if __name__ == "__main__":
    main()
