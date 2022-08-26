def party_people(lst):
    ppl = len(lst)
    if ppl != 0:
        b = biggest(lst)
        if ppl < b:
            return party_people(deletion(lst, b))
        else:
            return ppl
    else:
        return 0

def biggest(a):
    largest = a[0]
    for i in a[:]:
        if i > largest:
            largest = i
    return largest

def deletion(lst, target):
    for e in lst:
        if e == target:
            lst.remove(e)
    return lst

print(party_people([4, 5 ,4 ,1]))
print(party_people([10, 12, 15, 15, 5]))
print(party_people([2, 1, 2, 0]))
