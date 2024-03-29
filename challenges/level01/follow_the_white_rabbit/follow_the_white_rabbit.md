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
Anyway, this call is about your next task. wandre might own a twitter account too. Can you find it? We need to investigate his internet presence.  

Ah! And before I forgot! It seems wandre likes to drink Club Maté. We found a bottle of it at Station F. See the picture attached."

To solve this challenge, submit the SHA-256 hash of the username as a flag (remove the `@`): `APT{username}`

For example, if @my_flag is the username:
```
echo -n my_flag | sha256sum
4d54517a024d0cefa786029a81203fab4f94a86054417fd1b10e77f0be3cf2ca
```

Submit the flag as follows:  
`APT{4d54517a024d0cefa786029a81203fab4f94a86054417fd1b10e77f0be3cf2ca}`

## Solution

![img](linkedin-page.png)
![img](linkedin-header.png)

The Linkedin page leads to Ed Snowcrash's second Twitter account.

Take a loot at the tweets with replies (archived [here](https://web.archive.org/web/20220122132051/https://twitter.com/ed_snowcrash/with_replies)). He commented under a post of adrianakarante2:

![img](screen.png)

There is a Club Maté bottle on [adriana banner picture](https://web.archive.org/web/20220122132909/https://twitter.com/adrianakarante2).

If it is not possible to see the public profile of Ed on Linkedin (no account and so forth), get the profile URL (https://www.linkedin.com/in/edsnowcrash/) and paste it in [Mobile Friendly Test](https://search.google.com/test/mobile-friendly), save the HTML content in a `file.html` and open it in your browser.

```
echo -n adrianakarante2 | sha256sum
8f5475c77714a350ff6180d81edb88ab187edf12d0ad20413f68858772551328
```