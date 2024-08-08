def power(k,n):
    if n == 0:
        return 1
    else:
        return k * power(k, n - 1)
k = int(input("Digite k:"))
n = int(input("Digite n:"))
print(power(k, n))