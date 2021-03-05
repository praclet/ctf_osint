# intercepted

Category: Level03  
Tag: evidence investigation  
Type: Automatic  
Flag: `APT{a99d9c2f2ebce18132bbbc18a37498f9083e5dda019d4072244f7a778aad7b05}`  
Points: 100  
Requirements: shoplifter shoplifting 2  

## Message
While relaxing after finding out the phone, and while the forensic team is investigating it, an e-mail pops up on your screen.  
It's from the APT agency, they have a problem. The agency claims that someone managed to reverse engineer their new secret Kerberos protocol.  
They have found a bunch of custom Kerberos-apt42 tickets in a trashcan nearby 42school. They are sure those tickets arent issued by them.  
However it seems like his machine to generate tickets isnt working properly, only one of the ticket is working properly.  
Find out which one and sumbit it.  

To solve this challenge, submit the flag as follows: APT{sha256(ticket_value)}  
For exemple if the ticket number "0123-4567-89AB-CDEF" is the valid ticket:  
echo -n "0123-4567-89AB-CDEF" | sha256sum  
33d07c717e1889c263cf86b84edd0a5aa3f12826a62da802ca3bf033d87b4f13  
APT{33d07c717e1889c263cf86b84edd0a5aa3f12826a62da802ca3bf033d87b4f13}  

## Hint
Have you found the documentation yet ? James Wang had some friend that knew a lot about custom apt42 kerberos ticket.  

## Solution
Under one of James Wang's tweet a use posted a link to a documentation  
Upon looking up the usage page, you will find a set of 4 rules to see if a ticket is valid or not  
Create a script that will loop through all the 5000 image and extract the code  
Then do an other script that will check if the code is valid  
(download ticket.tar.gz at the root of the docker folder)  
build & run  
```
tar -xf ticket.tar.gz
bash script.sh
python3 confirm.py
DRDG-9Y69-8EDS-9Y1Y
```
echo -n DRDG-9Y69-8EDS-9Y1Y | sha256sum  
a99d9c2f2ebce18132bbbc18a37498f9083e5dda019d4072244f7a778aad7b05  
APT{a99d9c2f2ebce18132bbbc18a37498f9083e5dda019d4072244f7a778aad7b05}  
