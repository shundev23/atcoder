def decimal_to_binary_10_digits(n):
    if n >= 0:
        binary_representation = bin(n)[:2]
    else:
        binary_representation = bin(n)[:3]
    
    padded_binary = binary_representation.zfill(10)
    return padded_binary

N = int(input())
binary_representation_ = decimal_to_binary_10_digits(N)
print(binary_representation_)

# Answer

N = int(input())

for x in range(9,-1,-1):
    wari = (2 **x)
    print((N // wari) % 2, end='')
    
print("")