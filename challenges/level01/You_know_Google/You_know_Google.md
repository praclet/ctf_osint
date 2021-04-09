# You know Google?

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{ffc678b07a0da80d8749d8ee29436c3fb0c092ceb31306c3b531813c8b98b260}`  
Points: 35  
Requirements: Palmistry

## Message

*bip* \* You answer your phone instantly; You yell at the phone: "DID WE FOUND HIM ?"  
"Agent, nice to hear you, sadly, only bad news from over here, the fingerprint you found... is only linked to one thing"  
"What is it ?" you reply  
"You won't like it, an e-mail, Edward Snowcrash's e-mail, Edward disapeared from all radar, is he a traitor ? Who knows. As of now i need you to find his last location. Some intel suggest he went on holidays, here is his e-mail: edwardsnowcrash@gmail.com  
We need Edward to answer his supposedly betrayal. Good luck agent."

To solve this challenge, submit the SHA-256 hash of the flag.

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

## Hint (qui coute 0 pts)

Have you ever heard of google ID ? Have you grabed it yet ?  
The are great writeup on how to exploit it, especially one from a notorious twitter osint expert :D  

## Solution

1. Get google ID of account, one way is to add the e-mail to your contact, open dev tools and then click on the contact, check the batchexecute request, scroll all the way to the end and grab the ID  
![contact](contact.png)

2. Check account contribution to gmaps, use https://www.google.com/maps/contrib/ + ID (in this case the link will be https://www.google.com/maps/contrib/112096779393739237909)  
![contribution_gmaps](contribution_gmaps.png)

3. Grab the photo and get the exif data, the flag will appear in clear sight  
![exif_data_on_image](exif_data_on_image.png)

`APT{w3ll_n0w_yOu_d0}`
