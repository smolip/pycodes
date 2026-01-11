def reverse_ascending(items):
    result = []
    temp = []

    for num in items:
        if not temp:
            temp.append(num)
        else:
            if num > temp[-1]:
                temp.append(num)
            else:
                result.extend(reversed(temp))
                temp = [num]
    if temp:
        result.extend(reversed(temp))

    return result

print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))
            
