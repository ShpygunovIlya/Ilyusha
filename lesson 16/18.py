mark = int(input('enter mark: '))
if (mark >= 1) and (mark <= 3):
    print('basic level')
elif (mark >= 4) and mark (mark <= 6):
    print('middle level')
elif (mark >= 7) and mark (mark <= 9):
    print('sufficient level')
elif (mark >= 10) and mark (mark <= 12):
    print('high level')
else:
    print('mark is not correct')