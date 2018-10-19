


A = [1, 2, 1, 2, 1, 2, 1]
print(A)



def solution(A):
    # write your code in Python 3.6
    #print(max(A))
    count_list = [0]*2
    fruit_type = [-1]*2
    fruit_type[0] = A[0]
    count_list[0]+=1
    print(len(A))
    for i in range(1,len(A)):
        print(fruit_type)
        print(i)
        if(A[i] == fruit_type[0]):
            count_list[0]+=1
        elif( fruit_type[1] == -1):
            fruit_type[1] = A[i]
            count_list[1] += 1
        elif(fruit_type[1] == A[i]):
            count_list[1] += 1
        else:
            break
    return(count_list[0] + count_list[1])



print(solution(A))