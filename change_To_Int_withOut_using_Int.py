# Convert the string "123" into 123, without using the built-api `int()`

def helo(st):
    out = 0
    for item in st:
        for i in range(0, 10):
            if str(i) == item:
                out = out * 10 + i

    return out


print(helo("567465756546"))
