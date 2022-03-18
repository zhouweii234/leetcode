while True:
    try:
        mystr = list(map(str, input().strip().split()))
        mystr.sort()
        print(' '.join(mystr))
    except EOFError:
        break
