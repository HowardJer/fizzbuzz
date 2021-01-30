for (i) in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print ( str(i) + ' is multiple of 3 and 5')
    elif i % 3 == 0:
        print ( str(i) + ' is multiple of 3')
    elif i % 5 == 0:
        print ( str(i) + ' is multiple of 5')
    else:
        print ( str (i) )
    