from collections import OrderedDict
import math

def print_matrix(matrix,rows):
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")




key = "bugsy".upper()
message = "DF FF AA DG GF GA DA GF DA AD FX DD GX AG XA XX DD FF AF FA XA"
message = "XD AA AD DF XD XD DF FD GA FX XA DF XD DD DF AX GF"

message = message.replace(' ','')

# print(message)

key_length = len(key)
message_length = len(message)

rows = math.ceil(float(message_length)/float(key_length))
short_cols = key_length - (message_length%key_length)

# print(rows)
# print(short_cols)

# print(f"{key_length} {message_length}")

matrix = {}

for k in key:
    matrix[k] = []

i = 0
for m in message:
    matrix[key[i]].append(m)
    i += 1
    i = i % len(key)

#print(matrix)
print_matrix(matrix,rows)

temp_matrix = sorted(matrix.items())

print(temp_matrix)

sorted_matrix = {}

for item in temp_matrix:
    sorted_matrix[item[0]] = item[1]

print_matrix(sorted_matrix,rows)

