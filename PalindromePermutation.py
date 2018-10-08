


def get_hash(key, size):
    hash_index = 0
    for char in str(key):
        hash_index += ord(char)
    hash_index %= size
    return (hash_index)

input = "tactcoa"
size = len(input)
data_map = [None] * size

#Making a hash table
for i in range(0, size):
    hash_value = get_hash(input[i],size)

    if data_map[hash_value] is None:
        data_map[hash_value] = list(input[i])
    else:
        data_map[hash_value].append(input[i])

new_palindromes = [size][10]
odd = 0
flag = 0 # To check multiple odd values
count = 0
index = -1
for values in data_map:
    if values is not None:
        if (len(values)%2 == 1):
            if(odd != 1):
                odd = odd+1
                index = count
            else:
                flag = 1
                break
    count = count + 1



if(flag == 1):
    print("Palindrome is not possible")
else:


