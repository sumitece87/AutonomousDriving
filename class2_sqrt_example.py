def my_sqrt_for_int(num, range1):
    sqrt1 = -1
    r = num
    rangeee = range1
    for x in range(rangeee + 1):
        if x*x == r:
            sqrt1 = x
            print(sqrt1)
            break
    if sqrt1 == -1:
        print("Not found")
