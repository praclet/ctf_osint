# intercepted

Category: Level03  
Tag: evidence investigation  
Type: Automatic  
Flag: `APT{a99d9c2f2ebce18132bbbc18a37498f9083e5dda019d4072244f7a778aad7b05}`  
Points: 100  
Requirements: shoplifter_shoplifting_1 

## Message

While waiting for information about the next step in this case, an e-mail pops up on your screen.  
It's from the APT agency, they have a problem. The agency claims that someone managed to reverse engineer their new secret Kerberos protocol.  
They have found a bunch of custom Kerberos-apt42 tickets in a trashcan near 42school. They are sure those tickets weren't issued by them.  
However, it seems like the machine generating these tickets wasn't working properly, the agency claims only one of the tickets is valid.  
Find out which one and sumbit it, maybe it will help to get the hacker's location in a way...  
You then receive a sms which tells you that the documentation may be found during your other current task.  

To solve this challenge, submit the SHA-256 hash of the valid ticket.  

For example, if the ticket number "0123-4567-89AB-CDEF" is the valid ticket:
```
echo -n "0123-4567-89AB-CDEF" | sha256sum
33d07c717e1889c263cf86b84edd0a5aa3f12826a62da802ca3bf033d87b4f13
```

Submit the flag as follows:  
`APT{33d07c717e1889c263cf86b84edd0a5aa3f12826a62da802ca3bf033d87b4f13}`

## Hint
Have you found the documentation yet? James Wang had some friend that knew a lot about apt42's custom kerberos tickets.  
If yes, check the hint from the documentation :D.  

## Solution
Under one of James Wang's tweet a user posted a link to a documentation.  
Upon looking up the usage page, you will find a set of four rules to check if a ticket is valid.  
Create a script that will loop through all the 5000 images and extract the code.  
Then make another script that will check if the code is valid.  
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
