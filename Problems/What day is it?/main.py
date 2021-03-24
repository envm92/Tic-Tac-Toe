zone = input()
if zone == '0':
    print('Tuesday')
else:
    sign = zone[1:]
    difference = float(zone)
    if sign == '-':
        difference *= -1
    if 13 >= difference > -11:
        print('Tuesday')
    elif difference > 13:
        print('Wednesday')
    else:
        print('Monday')
