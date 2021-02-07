# Ok user

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{4a52132263f898dd28098e11f493cf182ee78bfa916122237df0646ccf8730ad}`  
Points: 30
Requirements: Follow the white rabbit

## Message

Good job! You discovered what seems to be the Twitter account of 'le Grand Architecte du Tout'. We need more information to identify them. We asked school 42 staff to start searching in their database. The hacker could be a former student. What do you think? Can you check if they have an account on any code hosting platform?

To solve this challenge, submit the account URL without `https://` and without terminating slash.
For exemple if My_Flag is the name:
echo -n My_Flag | sha256sum  
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
Then the flag is:
> APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}

## Solution

Find the HTB accound of adriana in a twitter thread. A Github account is linked on the HTB profile.

github.com/0x927 => 4a52132263f898dd28098e11f493cf182ee78bfa916122237df0646ccf8730ad
