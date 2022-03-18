while True:
    try:
        mystr = list(map(str, input().strip().split(',')))
        mystr = sorted(mystr)
        print(','.join(mystr))
    except EOFError:
        break
