asciiLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
asciiUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
newName = []

def listToStr(lst):
  string = ""
  for i in lst:
    string += i
  return string

def cipher(string, shift):
  newString = []
  for i in string:
    if i == i.lower():
      index = asciiLower.index(i) + shift
      letter = asciiLower[(index % len(asciiLower)) - 1]
      newString.append(letter)
    if i == i.upper():
      index = asciiUpper.index(i) + shift
      letter = asciiUpper[(index % len(asciiUpper)) - 1]
      newString.append(letter)
  encryptedString = listToStr(newString)
  return encryptedString

userInName = input("Enter the phrase you want to ") # Jamess
userInShift = int(input("Enter the number of shifts you want the name to go through")) # Guess

cryptName = cipher(userInName, userInShift)
print(cryptName)
