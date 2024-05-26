# mycode
N = int(input("Enter the number of elements in the list :"))
A = list(map(int, input(f"enter {N} integers separeted by spaces:").split()))
X = int(input("Enter the integer to search for :"))

if X in A:
    print("Yes")
else:
    print("No")

# Answer
N,X = map(int, input().split())
A = list(map(int,input().split()))
Answer = False

for i in range(N):
            if A[i] == X:
                        Answer = True
                        break

if Answer == True:
     print("Yes")
else:
     print("No")
