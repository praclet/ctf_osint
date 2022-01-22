# Let the stalk begin

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{7fb0ca4e7a07a2c911dd7446599955d871bfba73fdaa6be50188f2f834cf59ba}`  
Points: 20
Requirements: Data from out of space

## Message

It appears the picture leads to a Twitter account! The owner of this account must be an accomplice of 'le Grand Architecte du Tout'.

Find out who they are! What is their name, their firstname? What do they do?

To solve this challenge, create the flag as the following string in lower-case letters: `APT{name-firstname-job}`. Yes, dashes `-` separate words. The `job` is the job of the accomplice.

And then, submit the SHA-256 hash of the string.

For example, if doe-john-developer is the string:
```
echo -n doe-john-developer | sha256sum
d67322b19b6cf6362589beb528e4ebe6cac4d937a304400695d0b3d671de73d8
```

Submit the flag as follows:  
`APT{d67322b19b6cf6362589beb528e4ebe6cac4d937a304400695d0b3d671de73d8}`

## Solution

This is the Twitter account of Edward Snowcrash.

![img](screen.jpg)

```
echo aHR0cHM6Ly93d3cua2lja3Jlc3VtZS5jb20vY3YvUnlRWnYv | base64 -d
https://www.kickresume.com/cv/RyQZv/
```

(The PDF file is in this directory.)

```
echo -n snowcrash-edward-analyst | sha256sum
7fb0ca4e7a07a2c911dd7446599955d871bfba73fdaa6be50188f2f834cf59ba
```

`APT{7fb0ca4e7a07a2c911dd7446599955d871bfba73fdaa6be50188f2f834cf59ba}`
