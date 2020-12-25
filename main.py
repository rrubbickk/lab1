import csv
import re

symbols = 0
spaces = 0
marks = 0
words = 0
sentences = 0

with open('steam_description_data.csv', encoding='utf-8') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        string = ','.join(line)
        symbols += len(string)
        spaces += string.count(" ")
        marks += string.count(".") - 2 * string.count("...") + string.count("!") + string.count("?")
        marks += string.count("\"") + string.count("\'") + string.count(":") + string.count(",")
        marks += string.count("-") - string.count("--") + string.count("(") + string.count(")") + string.count(";")
        words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", string))
        sentences += len(re.findall(r"([A-Z][^.!?]*[.!?])", string))

print("символов : ", symbols)
print("символов (без пробелов): ", symbols - spaces)
print("символов (без знаков препинания): ", symbols - marks)
print("слов: ", words)
print("предложений: ", sentences)
