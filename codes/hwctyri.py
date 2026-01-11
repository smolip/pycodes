import string 

with open("raven.txt", "r") as f:
    content = f.read()

dashes = "-–—―" #různý druhy dashů, nějaky mi tam zůstávaly

cleanedText = content.translate(str.maketrans("", "", string.punctuation + string.whitespace + dashes))

def algorithmSplit(text): 
    temp = []
    result = []

    for char in text:
        charLower = char.lower()
        if not temp:
            temp.extend(charLower)
        else:
            if charLower in temp:
                result.append(temp)
                temp = [charLower]
            else:
                temp.extend(charLower)
    return result

splited = algorithmSplit(cleanedText)

def findLongest(splited):
    result = []
    for sp in splited:
        if not result:
            result = sp
        else:
            if len(sp) > len(result):
                result = sp
            
    return print(f"Nejdelší část textu je: {result} a jeho délka je {len(result)}")

findLongest(splited)

print(cleanedText)



            








