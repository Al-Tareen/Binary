#This program retrieves 2 binary numbers and outputs its sum.

binary_1 = input("Please enter the first binary number.")
binary_2 = input("Please enter the second binary number.")

#used to store place values during addition
extra = []

#used to store sum of each index in the binary
answer = []

while binary_1[0] == '0':
    binary_1 = binary_1[1:]
    continue
while binary_2[0] == '0':
    binary_2 = binary_2[1:]
    continue

while len(binary_1) and len(binary_2):
    print("starting over")
    if binary_1[-1] + binary_2[-1] == "11":
        if extra:
            answer.append(1)
            print("added 1")
            binary_1 = binary_1[:-1]
            binary_2 = binary_2[:-1]
            continue
        else:
            extra.append(1)
            answer.append(0)
            print("added 0")
            binary_1 = binary_1[:-1]
            binary_2 = binary_2[:-1]
            continue
    elif binary_1[-1] + binary_2[-1] == "00":
        if extra:
            answer.append(1)
            print("addedd 1")
            extra.pop(1)
            binary_1 = binary_1[:-1]
            binary_2 = binary_2[:-1]
            continue
        else:
            answer.append(0)
            print("addedd 0")
            binary_1 = binary_1[:-1]
            binary_2 = binary_2[:-1]
            continue
    else:
        if extra:
            answer.append(0)
            print("Added 0")
            binary_1 = binary_1[:-1]
            binary_2 = binary_2[:-1] 
            continue
        else:
            answer.append(1)
            print("Added 1")
            binary_1 = binary_1[:-1]
            binary_2 = binary_2[:-1] 
            continue

while binary_1: 
    print(binary_1)
    print("last flush")
    if extra:
        if len(binary_1) > 1:
            if binary_1[-1] == '1':
                answer.append(0)
                print("ADDED 0")
                binary_1 = binary_1[:-1]
                continue
            else:
                answer.append(1)
                print("ADDED 1")
                extra.pop()
                extra = ""
                binary_1 = binary_1[:-1]
                continue
        else:
            if binary_1 == '1':
                answer.append(0)
                answer.append(1)
                print("ADDED 1")
                extra.pop()
                extra = ""
                binary_1 = ""
            else: 
                answer.append(0)
                print("ADDED 0")
                binary_1 = ""
    else:
        for element in binary_1:
            print(answer)
            answer.append(element)
        binary_1 = ""

if extra:
    print("added final 1")
    answer.append(1)

print("Your final answer is: ", answer[::-1])