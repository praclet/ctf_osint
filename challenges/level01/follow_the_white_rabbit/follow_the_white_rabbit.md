# Follow the white rabbit

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{8f5475c77714a350ff6180d81edb88ab187edf12d0ad20413f68858772551328}`  
Points: 20
Requirements: Let the stalk begin

## Message

The field agent is calling you again:

"Hello again!  
Congratulations! It appears Edward was a traitor and an accomplice of 'le Grand Architecte du Tout'. I now understand why Ed was so bad at taking photographs...  
Anyway, this call is about your next task. The hacker might own a twitter account too. Can you find it? We need to investigate their internet presence.  
Ah! And before I forgot! It seems the hacker likes to drink Club Maté. We found a bottle of it at Station F. See the picture attached."

To solve this challenge, submit the SHA-256 hash of the username as a flag (remove the `@`): `APT{username}`

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

## Solution

The Linkedin page leads to Ed Snowcrash's second Twitter account. He commented under a post of adrianakarante2. There is a Club Maté bottle on adriana banner picture.

If it is not possible to see the public profile of Ed on Linkedin (no account and so forth), get the profile URL (https://www.linkedin.com/in/edsnowcrash/) and paste it in [Mobile Friendly Test](https://search.google.com/test/mobile-friendly), save the HTML content in a `file.html` and open it in your browser.

adrianakarante2 => 8f5475c77714a350ff6180d81edb88ab187edf12d0ad20413f68858772551328
