s = input('enter a word ')
if " " in s:
    print("multiple words")
elif '.' in s:
    print('one word with dot')
else:
    print("one word without dot")