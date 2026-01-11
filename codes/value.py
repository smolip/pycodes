word = "monty"
char = list(word)
  
one = ["e","a","i","o","n","r","t","l","s","u"]
two = ["d","g"]
three = ["b","c","m","p"]
four = ["f","h","v","w","y"]
five = ["k"]
six = ["j","x"]
seven = ["q","z"]

value = 0

for c in char:
    if one.__contains__(c):
        value = value + 1
    if two.__contains__(c):
        value = value + 2
    if three.__contains__(c):
        value = value + 3
    if four.__contains__(c):
        value = value + 4
    if five.__contains__(c):
        value = value + 5
    if six.__contains__(c):
        value = value + 6
    if seven.__contains__(c):
        value = value + 7

print(value)
    