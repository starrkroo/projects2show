def digital_root(n):
    #while n:
    pass

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10

    if s>10:
        return sum_digits(s)
    else:
        return s

print(sum_digits(132189))