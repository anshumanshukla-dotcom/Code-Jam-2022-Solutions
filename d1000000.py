t = int(input())


for i in range(t):

    n = int(input())

    s = list(int(num) for num in input().strip().split())

    

    s.sort()

    result = 0

    h = 0 # index 

    

    while h < n:

        if s[h] >= result + 1:

            result += 1

        h = h + 1

    print(f"Case #{i+1}: {result}")