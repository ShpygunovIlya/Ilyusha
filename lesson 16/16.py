t = int(input("Enter sleep time: "))
h = bool(input('enter if is hungry: '))
if t < 18:
    print('sleepy')
elif t >= 18 and (h):
    print('hungry')
else:
    print('happy')
