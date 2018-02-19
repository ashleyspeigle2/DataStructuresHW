def main(x):
    print(x)
    if x <= 2:
        return 1

    elif x % 2 == 0:
        return 1+main(x/2)

    elif x % 2 != 0:
        return 2+main((3 * x + 1) / 2)

        
