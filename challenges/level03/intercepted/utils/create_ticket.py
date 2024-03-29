#!/usr/local/bin/python3
import random

def alpha_num():
    an = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return (random.choice(an))

def sum_numbers(ticket):
    ret = 0
    for i in ticket:
        if i.isnumeric() == True:
            ret += int(i)
    return ret

def unpresent_char(ticket):
    for a in range(0, 16):
        while ticket[a] == "V" or ticket[a] == "A":
            ticket[a] = alpha_num()
    return (ticket)

def present_char(c):
    try:
        ind = ticket.index("E")
        if ind == 8 or ind == 4 or ind == 12:
            ticket[ind + 1] = "E"
    except:
        ind = random.randint(0, 15)
        if ind == 8 or ind == 4 or ind == 12:
            ind += 1
        ticket[ind] = "E"
    try:
        ind = ticket.index("S")
        while ind == 8 or ind == 4 or ind == 12 or ticket[ind] == "E":
            ind = random.randint(0, 15)
        ticket[ind] = "S"
    except:
        ind = random.randint(0, 15)
        while ind == 8 or ind == 4 or ind == 12 or ticket[ind] == "E":
            ind = random.randint(0, 15)
        ticket[ind] = "S"
    return (ticket)

def add_number(ticket):
    if ticket[4].isnumeric() == False:
        ticket[4] = chr(random.randint(48, 57))
    if ticket[8].isnumeric() == False:
        ticket[8] = chr(random.randint(48, 57))
    if ticket[12].isnumeric() == False:
        ticket[12] = chr(random.randint(48, 57))
    return (ticket)

def add_modulo(ticet):
    if sum_numbers(ticket) % 7 != 0:
        nbr = sum_numbers(ticket) % 7
        nbr = 7 - nbr
        for i in range(0, 16):
            if ticket[i].isnumeric() == True:
                while nbr > 0 and int(ticket[i]) < 9:
                    nbr -= 1
                    ticket[i] = str(int(ticket[i]) + 1)
    return (ticket)

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

def make_valid_ticket(ticket):
    rule = random.randint(0, 3)
    dic_rule = [unpresent_char, present_char, add_number, add_modulo]
    for i in range(0, 4):
        if (i != rule):
            ticket = dic_rule[i](ticket)
    #ticket = unpresent_char(ticket)
    #ticket = present_char(ticket)
    #ticket = add_number(ticket)
    #ticket = add_modulo(ticket)
    if is_valid_ticket(ticket) == True:
        raise

i = 0
while i < 10000:
    ticket = []
    str_ticket = ""
    for a in range(0, 16):
        ticket.append(alpha_num())
    try:
        make_valid_ticket(ticket)
        for k in range(0, 16):
            if k % 4 == 0 and k != 0:
                str_ticket += "-"
            str_ticket += ticket[k]
        print(str_ticket)
    except:
        i -= 1
    i += 1
