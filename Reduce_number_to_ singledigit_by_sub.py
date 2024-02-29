def RSF(n):
    while n >= 10:
        x = n
        l = 0
        while n > 0:
            n = n // 10
            l += 1
        a = [0] * l
        i = l - 1
        while x > 0:
            a[i] = x % 10
            x = x // 10
            i -= 1
        for j in range(0, l - 1):
            n = n * 10 + abs(a[j] - a[j + 1])
    return n
n = int(input("Enter a number: "))
ans = RSF(n)
print("Result:", ans)