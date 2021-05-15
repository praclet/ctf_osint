# Data from out of space

Category: Level00  
Tag: Forensics  
Type: Automatic  
Flag: `APT{e850a491c61d9ae2bda26d8d05ae49394830fbd1e9bff54935cf9dee491a77a9}`  
Points: 30  
Requirements: Catch me if you can

## Message

Unfortunately, the Special Operation Forces couldn't catch wandre! However, he dropped something while escaping Station F. We retrieved this sensitive file but we were not able to extract any useful data from it.

Can you help us to find any clue that might lead us to the hacker?

You're now in charge of investigating this evidence:

To solve this challenge, submit the SHA-256 hash of the flag.

For example, if my_flag is the flag:
```
echo -n my_flag | sha256sum
4d54517a024d0cefa786029a81203fab4f94a86054417fd1b10e77f0be3cf2ca
```

Submit the flag as follows:  
`APT{4d54517a024d0cefa786029a81203fab4f94a86054417fd1b10e77f0be3cf2ca}`

## Hint (cost: 5 pts)
`man file`

## Solution

```sh
# file uknown
# unknown: POSIX tar archive (GNU)
# tar -xf uknown
# fcrackzip -u -D -p test.bin my_secret_files.bin 
# PASSWORD FOUND!!!!: pw == liecu7chahrohqu0aiX4eeph7ho6chae
# unzip my_secret_files.bin 
# file my_akka
# #Get the flag ! => axx compte twitter.
# echo -n marvin_at_42 | sha256sum                                                                                                
# e850a491c61d9ae2bda26d8d05ae49394830fbd1e9bff54935cf9dee491a77a9
# APT{e850a491c61d9ae2bda26d8d05ae49394830fbd1e9bff54935cf9dee491a77a9}
# We can get the same result with => https://emn178.github.io/online-tools/sha256.html "marvin_at_42'
```
