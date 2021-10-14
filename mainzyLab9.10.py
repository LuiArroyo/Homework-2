# Luis Arroyo
# PSID: 2037081
# CIS 2348

#import external file
import csv
input_file = input()

with open(input_file) as words_file:
    words_reader = csv.reader(words_file)
    for row in words_reader:
        list_of_words = row

no_duplicates = list(dict.fromkeys(list_of_words))
full_list = len(no_duplicates)

for i in range(full_list):
    print(no_duplicates[i], list_of_words.count(no_duplicates[i]))