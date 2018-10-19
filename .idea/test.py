b = "ab-cdef-ghij"

b =b.replace('-','').upper()
print(len(b))
x = range(10, 2)
j = len(b)
temp = b
count = 1
for i in range(len(b),0,-1):
    #print(b[i])
    print("j >>", j, "||i >>", i, "temp >>",temp, "|| b>>", b)
    if count%3 == 0 and b[:i-1] != '':
        print("I'm here , count == ", count)

        temp =   b[:i-1] + "-" + temp[j-1:]

    count = count + 1
    j = j - 1
print(temp)
#print("AButu".capitalize())


print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
d = {'dog': ['milo','otis','laurel','hardy'],'cat': ['bob','joe'],'milo': ['otis','laurel','hardy','dog'], 'bob': ['cat','joe'], 'hardy': ['dog']}
seen = set()
unique = []
for key, values in d:
    if key not in seen:
        unique.append(key)
    seen = seen.union(values)
print(len(unique))