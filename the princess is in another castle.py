possBefore = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes"]
possAfter = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
order = []

print len(possBefore)
print len(possAfter)

while possBefore != ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]:
    check = int(raw_input("Check which room? "))-1
    order.append(check+1)
    possBefore[check] = 'no'
    for i in range(len(possBefore)):
        if possBefore[i] == 'yes':
            if i == 0:
                possAfter[1] = 'yes'
            elif i == (len(possBefore)-1):
                possAfter[i-1] = 'yes'
            else:
                possAfter[i+1] = 'yes'
                possAfter[i-1] = 'yes'
                
    possBefore = possAfter
    possAfter = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]
    print possBefore

print order
