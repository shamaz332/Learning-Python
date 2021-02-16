
# Given an array of integers, find the pair of adjacent elements
# that has the largest product and return that product.

def mult(inputArr):
    length = int(len(inputArr))

    maxAns = inputArr[0]*inputArr[1]
    product = 1

    for i in range(1, length-1):
        product = inputArr[i]*inputArr[i+1]

        if product > maxAns:
            maxAns = product

    return maxAns


print(mult([2, 23, 6, 23, 7]))
