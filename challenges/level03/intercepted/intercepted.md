# intercepted

Category: Level03  
Tag: evidence investigation  
Type: Automatic  
Flag: `APT{}`  
Points: 50  
Requirements: shoplifter shoplifting 2  
Max number of try: 3

## Message
While relaxing after finding out the phone, and while the forensic team is investigating it, an e-mail pops up on your screen.  
It's from the APT agency, they have a problem. The agency claims that someone managed to reverse engineer their new secret Kerberos protocol.  
They have found a bunch of custom Kerberos-apt42 tickets in a trashcan nearby 42school. They are sure those tickets arent issued by them.  
However it seems like his machine to generate tickets isnt working properly, only one of the ticket is working properly.  
Find out which one and sumbit it.  

WARNING: This challenge has a maximum number of try, do not submit randomly as you won't be able to get to the end of the ctf, if in doubt pm admin.  

To solve this challenge, submit the flag as follows: APT{sha256(ticket_number)}  
For exemple if the ticket number "3" is the valid ticket:  
echo -n "3" | sha256sum  
4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce  
APT{4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce}  

## Hint
Have you found the documentation yet ? James Wang had some friend that knew a lot about custom apt42 kerberos ticket.  

## Solution
