def palindrome(N):
    for i in range(1, N + 1):
        print(int('1' * i)**2)

palindrome(int(input()))



5
1
121
12321
1234321
123454321


#or second method


n=int(input("enter a numbr"))
i=0
while i<=n+1:
    i=i+1
    
    print(int('1' * i)**2)
