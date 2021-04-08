# Git me im Famous.

Category: Level02  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{0b66ef7ca982a75aa548c74d8d27ee9310ef94f44ccd1400d08782f0468ea729}`  
Points: 80
Requirements: You know Google?, R.D.V, Ok user

## Message

Good job, you found the Github account of the hacker!  
Recon his Github repositories, look for anything that look suspicious, maybe you can find something interesting...  

To solve this challenge, submit the SHA-256 hash of the flag.

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

## Solution

> Aller sur le page https://github.com/0x927 

> Chercher dans la liste des repos fork le repos => https://github.com/0x927/resources 

> Aller à la source de ce fork dans les commits et regarder les commentaires.
 
> Trouver => https://github.com/apt-42/resources/commit/ccb48a6ec53a781bf76ccbaa8945f770db0f4995 

> Copier le flag.
