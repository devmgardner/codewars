def unique_in_order(iterable):
    cl = []
    print(iterable)
    for i,c in enumerate(list(iterable)):
        print(i, c)
        if i == 0 : cl.append(c)
        if len(list(iterable)) == 1 : return list(iterable)
        if not i == 0 and not list(iterable)[i-1] == c : cl.append(c)
    return cl
print(unique_in_order(input('')))