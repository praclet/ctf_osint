# Data from out of space

Category: Level00  
Tag: Forensics  
Type: Automatic  
Flag:  
Points: 40
Requirements: Palmistry, Catch me if you can

## Message

/!\ WIP

Nous avons trouvé un fichier sensible dans la station F. Nous n'avons pas réussis à extraire la moindre information utile. Votre tache est de nous aider à récuperer un indice utile pour la suite.

Note: Le flag attendu sera sous le format => APT{shasum(info)} 


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
