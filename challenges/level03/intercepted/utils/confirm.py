#!/usr/local/bin/python3
def sum_numbers(ticket):
    ret = 0
    for i in ticket:
        if i.isnumeric() == True:
            ret += int(i)
    return ret

def is_valid_ticket(ticket):
    try:
        ticket.index("A")
        return False
    except:
        pass
    try:
        ticket.index("V")
        return False
    except:
        pass

    try:
        ticket.index("E")
        ticket.index("S")
    except:
        return False

    if ticket[4].isnumeric() and ticket[8].isnumeric() and ticket[12].isnumeric():
        pass
    else:
        return False

    if sum_numbers(ticket) % 7 != 0:
        return False

    return True

fd = open("./ticket.txt")
for i in range(0, 5000):
    line = fd.readline()
    linesave = line.replace('\n', '')
    line = line.replace('-', '').replace('\n', '')
    arr = []
    for d in line:
        arr.append(d)
    if is_valid_ticket(arr) == True:
        print(i, linesave)
