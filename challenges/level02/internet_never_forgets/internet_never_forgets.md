# Internet never forgets

Category: Level02  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{3ae38cdf2192d91de5e972a8988b0a5b74b576c81df46447256b716b8d61c31e}`  
Points: 80
Requirements: You know Google?, R.D.V, Ok user

## Message

It seems like wandre had a blog back in the days.  
Thanks to our super powerful quantum computer we managed to bruteforce the hash you found in Github and found a website:  
https://ukrainian-giants.000webhostapp.com/  
Can you find something interesting inside?  

To solve this challenge, submit the SHA-256 hash of the flag.

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

## Solution

> Aller sur le page https://ukrainian-giants.000webhostapp.com/ 

> Trouver un lien mort sur la page principal => https://ukrainian-giants.000webhostapp.com/dogs

> Aller sur waybackmachine => https://web.archive.org/web/20210303121637/https://ukrainian-giants.000webhostapp.com/dogs
 
> Regarder la source pour trouver => W4y_b4rK_M4ch1n3_1s_n1c3 => (sha256 == 3ae38cdf2192d91de5e972a8988b0a5b74b576c81df46447256b716b8d61c31e 

> APT{3ae38cdf2192d91de5e972a8988b0a5b74b576c81df46447256b716b8d61c31e}
