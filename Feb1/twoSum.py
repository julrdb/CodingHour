#This is a LeetCode problem provided by jalexakos. Link: https://leetcode.com/problems/two-sum/description/


def main():
    arrayThis = [3,1,5,0,4,2,11]
    target = 9
    for x in range(len(arrayThis)):
        for y in range(x+1, len(arrayThis)):
            print((x,y))
        # since the inner is initiating with x+1, it only iterates 21x, like a factorial; no repeated pairs.
            if arrayThis[x] + arrayThis[y] == target:
                print('Integers:',(arrayThis[x],arrayThis[y]))
                print('Indices: ',[x,y])
                break
    print("-----------------------------------------------------------------------------------------------------")
    for x in arrayThis: 
        for y in arrayThis:
            print((x,y))
        # while this nested loop works, it iterates 49x, which is comprised of already scanned int. pairs.
            if x + y == target:
                print("Int here: ", x, y)
                print("Ind here: ", arrayThis[x], arrayThis[y])
                return      
main()


# Leetcode solution:
# def main():
#     arrayThat = [3,1,5,0,4,2,11]
#     target = 9
#     scannedInt = {}
#     for i in range(len(arrayThat)):
#         firstNum = target - arrayThat[i]
#         # print(scannedInt)
#         if firstNum in scannedInt:
#             # return[scannedInt[firstNum], i]
#             print([scannedInt[firstNum], i])
#             break
#             # print(x,",",arrayThat[i]) 
#         else:
#             scannedInt[arrayThat[i]] = i
# main()



'''
# Chatgpt explained:

def main():
    arrayThis = [3,1,5,0,4,2,11]
    target = 9
    for i in range(len(arrayThis)):
        for j in range(i+1, len(arrayThis)):
            if arrayThis[i] + arrayThis[j] == target:
                print("Index here: ", i, j)
                print("Int here: ", arrayThis[i], arrayThis[j])
                return      
main()

i = 0, j = 1: [3, 1]
i = 0, j = 2: [3, 5]
i = 0, j = 3: [3, 0]
i = 0, j = 4: [3, 4]
i = 0, j = 5: [3, 2]
i = 0, j = 6: [3, 11]
i = 1, j = 2: [1, 5]
i = 1, j = 3: [1, 0]
i = 1, j = 4: [1, 4]
i = 1, j = 5: [1, 2]
i = 1, j = 6: [1, 11]
i = 2, j = 3: [5, 0]
i = 2, j = 4: [5, 4]
i = 2, j = 5: [5, 2]
i = 2, j = 6: [5, 11]
i = 3, j = 4: [0, 4]
i = 3, j = 5: [0, 2]
i = 3, j = 6: [0, 11]
i = 4, j = 5: [4, 2]
i = 4, j = 6: [4, 11]
i = 5, j = 6: [2, 11]
'''