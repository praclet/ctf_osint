# You know Google?

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{4d0aa736a8bcd9c8557945f1d9d85600d8e2456be079ca17fe6073cd887a41c1}`  
Points: 45  
Requirements: Palmistry

## Message

*bip* \* You answer your phone instantly. You yell at the phone: "DID WE FIND HIM?"  
"Agent, nice to hear you. Sadly, only bad news from over here. The fingerprint you found... is only linked to one thing."  
"What is it?" you reply  
"You won't like it. An e-mail, Edward Snowcrash's e-mail: edwardsnowcrash@gmail.com.
Also, Edward went AWOL, is he a traitor? Who knows... As of now, I need you to find his last location. Some intel suggested he could be on holidays.
We need to get answers from Edward about this potential betrayal. Good luck, Agent."

To solve this challenge, submit the SHA-256 hash of the location where Edward went on holidays. Pay attention to capital letters.

For example, if "My Flag" is the location:
```
echo -n "My Flag" | sha256sum
2b48dba8e6ffa9d6bccc9ec829b8a26a00bfca97736c4bf18181300be7f2df0d
```

Submit the flag as follows:  
`APT{2b48dba8e6ffa9d6bccc9ec829b8a26a00bfca97736c4bf18181300be7f2df0d}`

## Hint (cost: 25 pts)

Have you ever heard of google ID? Have you grabed it yet?  
There are great writeups on how to exploit it, including one from a notorious twitter osint expert :D  

## Solution

1. Get google ID of account, one way is to add the e-mail to your contacts, open dev tools and then click on the contact, check the batchexecute request, scroll all the way to the end and grab the ID  
![contact](contact.png)

2. Check account contribution to gmaps, use https://www.google.com/maps/contrib/ + ID (in this case the link will be https://www.google.com/maps/contrib/112096779393739237909)  
![contribution_gmaps](contribution_gmaps.png)

3. Check the location of the place: Sharm El-Naga
```
echo -n "Sharm El-Naga" | sha256sum
4d0aa736a8bcd9c8557945f1d9d85600d8e2456be079ca17fe6073cd887a41c1
```
APT{4d0aa736a8bcd9c8557945f1d9d85600d8e2456be079ca17fe6073cd887a41c1}
