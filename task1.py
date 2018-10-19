
import numpy as np
L = ["a.b@example.com", "x@example.com", "x@exa.mple.com", "ab@example.com","x+abcd@example.com"]


def unique(lval):

    ul = []
    for i in lval:

        if i not in ul:
            ul.append(i)

    return(ul)
def solution(L):
    local = [None]* len(L)
    domain = [None]* len(L)
    item = []

    for i in range(0, len(L)):
        temp = ""
        #print("$$$$$", L[i])
        temp = L[i]
        l = ""
        #print("*****", temp)
        local[i], domain[i] = temp.split("@")
        l = str(local[i])
        local[i] = local[i].replace(".","")
        if(l.find('+')>=0):
            print("I'm here")
            print("1st time :", local[i])
            print(l[:l.find('+')])
            local[i] = l[:l.find('+')]
            print("2nd :", local[i])
        item.append((domain[i], local[i]))
    print(item)
    y = np.unique(item, axis = 0)
    y = unique(item)
    z = []
    for i in y:
        print("****", len(i[1]))
        if(len(i[1]) > 1):
            z.append(tuple(i))
            print(z)
    print("^^^^^^", len(z))
   # print("&&&&&", item)
    #print("&&&&&", np.unique(item))
    #print("&&&&&", len(np.unique(item)))
    return(local, domain)



print(solution(L))
a, b = "a.b@example.com".split("@")
print(a,">>>",b)
print(len(L))
print(L[0])


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def unique(lval):
    ul = []
    for i in lval:
        if i not in ul:
            ul.append(i)
    return (ul)


def solution(L):
    local = [None] * len(L)
    domain = [None] * len(L)
    item = []

    for i in range(0, len(L)):
        temp = ""
        # Formatting the data loop
        temp = L[i]
        l = ""
        # Splitting the local and domain names
        local[i], domain[i] = temp.split("@")
        l = str(local[i])
        # Removing the .characters in local names
        local[i] = local[i].replace(".", "")
        if (l.find('+') >= 0):
            # Ignoring data after + sign
            local[i] = l[:l.find('+')]

        item.append((domain[i], local[i]))
    # Finding unique addresses - passing unique y would give only the unique mail ids
    # y = unique(item)
    # Without finding the unique adresses - to find the number of groups
    y = item
    z = []
    for i in y:
        # Checking if the adresses are greater than 1
        if (len(i[1]) > 1):
            z.append(tuple(i))

    return (len(z))
    pass