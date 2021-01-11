# Data from out of space

Category: Level00  
Tag: Forensics  
Type: Automatic  
Flag:  
Points: 40
Requirements: Palmistry, Catch me if you can

## Message

Unfortunately, the Special Operation Forces couldn't catch the hacker! However, they dropped something while escaping Station F. We retrieved this sensitive file but we were not able to extract any useful data from it.  
Can you help us to find any clue that might lead us to the hacker?

To solve this challenge, submit the flag as follows: `APT{shasum(info)}`


## Solution

```sh
# mkdir /meda/usb_mount_point
# mount -t auto -o loop data.bin /media/usb_mount_point
# cd /media/usb_mount_point
# mkdir /tmp/n
# find -iname '*.txt' -exec cp {} /tmp/n \;
# cd /tmp/n 
# edit file MySecret42.txt ligne 42 remove =>  WW91IGtub3cgd2hhdCB0byBkbyB3aXRoIHRoaXM= + tab => md5sum file edit valid = 27f341520644abdcaa5387d62c9d9c1c
# cat MySecret* | tr -d '\n' | base64 -d > test.jpg
# open test.jpg (md5sum test.jpg  de9ee7028f94f5053faf36562e985a5e ) 
# #Get the flag ! => APT{shasum(marvin_at_42)} => axx compte twitter.
```
