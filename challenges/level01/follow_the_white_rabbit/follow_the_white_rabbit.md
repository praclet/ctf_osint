# Follow the white rabbit

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{adrianakarante2}`  
Points: 30
Requirements: Let the stalk begin

## Message

The field agent is calling you again:

"Hey again!  
Congratulations! It appears Edward was a traitor and an accomplice of 'le Grand Architecte du Tout'. I now understand why Ed was so bad at taking photographs...  
Anyway, this call is about your next task. We suppose the hacker owns a twitter account too. Can you find it? We need to investigate their internet presence.  
Ah! And before I forgot! It seems the hacker likes to drink Club Maté. We found a bottle of it at Station F. See the picture attached."

To solve this challenge, submit the username as a flag (remove the `@`): `APT{username}`

## Solution

The Linkedin page leads to a second Twitter account of Ed Snowcrash. He commented under a post of adrianakarante2. There is a Club Maté bottle on adriana banner picture.

If it is not possible to see the public profile of Ed on Linkedin (no account and so forth), get the profile URL and paste it in [Mobile Friendly Test](https://search.google.com/test/mobile-friendly), save the HTML content in a `file.html` and open it in your browser.
