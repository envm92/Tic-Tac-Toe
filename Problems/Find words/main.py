phrase = input()
phrase = phrase.split()
phrase = [x for x in phrase if x[-1] == 's']
print('_'.join(phrase))
