# Luis Arroyo
# PSID: 2037081
# CIS 2348

word = input()
def remove(word):
    return word.replace(" ", "")

#set reverse
reverse = word.replace(" ", "")[::-1]

#checks and prints
if word.replace(" ", "") == reverse:
    print(word,"is a palindrome")
else:
    print(word, "is not a palindrome")