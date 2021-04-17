# Data from out of space

Category: Level00  
Tag: Forensics  
Type: Automatic  
Flag: `APT{e850a491c61d9ae2bda26d8d05ae49394830fbd1e9bff54935cf9dee491a77a9}`  
Points: 40  
Requirements: Catch me if you can

## Message

Unfortunately, the Special Operation Forces couldn't catch the hacker! However, they dropped something while escaping Station F. We retrieved this sensitive file but we were not able to extract any useful data from it.  
Can you help us to find any clue that might lead us to the hacker?

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

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
