# Let the stalk begin

Category: Level01  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{76266e243bdc5a467eecc37d633af4dc0feb0c7c0edbe905c49582fd87122731}`  
Points: 20
Requirements: Data from out of space

## Message

It appears the picture leads to a Twitter account! The owner of this account must be an accomplice of 'le Grand Architecte du Tout'.

Find out who they are!

To solve this challenge, create the flag as the following string: `APT{Name-Firstname-Job-COMPANY}`. Yes, dashes `-` separate words. Pay attention to capitals.

And then, submit the SHA-256 hash of the string.

For example, if Doe-John-Hacker-FOO is the string:
```
echo -n Doe-John-Hacker-FOO | sha256sum
2c502311b1a3be6d52ce18c1757bafb40dbb5b9e4c39d1bb93d0aa5ee808e61d
```

Submit the flag as follows:  
`APT{2c502311b1a3be6d52ce18c1757bafb40dbb5b9e4c39d1bb93d0aa5ee808e61d}`

## Solution

This is the Twitter account of Edward Snowcrash.

Snowcrash-Edward-Analyst-APT => 76266e243bdc5a467eecc37d633af4dc0feb0c7c0edbe905c49582fd87122731
