import string

# 1. Načtení textu
with open("raven.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 2. Odstranění interpunkce, mezer a všech typů pomlček
dashes = "-–—―"  # spojovník, en dash, em dash, horizontal bar
cleanedText = content.translate(str.maketrans("", "", string.punctuation + string.whitespace + dashes))

# 3. Funkce pro hledání všech nejdelších unikátních podřetězců
def findLongestUniqueSubstrings(text):
    text = text.lower()
    start = 0
    seen = {}
    max_len = 0
    results = []

    for end, char in enumerate(text):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        curr_len = end - start + 1
        if curr_len > max_len:
            max_len = curr_len
            results = [text[start:end+1]]
        elif curr_len == max_len:
            results.append(text[start:end+1])
    
    return results, max_len

# 4. Vyhledání a výpis výsledků
longest_substrings, length = findLongestUniqueSubstrings(cleanedText)
print(f"Nejdelší délka: {length}")
print("Nejdelší části textu:")
for s in longest_substrings:
    print(s)
