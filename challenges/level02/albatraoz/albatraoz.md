# Albatraoz

Category: Level02  
Tag: Steganography  
Type: Automatic  
Flag: `APT{c3094e458a5adf2c2832ee22f71100e2004fdb8873c3c1331a7b3a7e58ab82fb}`  
Points: 35
Requirements: You know Google?, R.D.V, Ok user

## Message

Good job Agent! Electrolab in Nanterre was indeed the place where wandre and Catnity used to meet up.  
Too bad they didn't left the place untouched, all the equipment is gone.  
We managed to get our hands on a usb stick hidden inside Electrolab's post box.  
That key contains a password protected archive. However, we haven't been able to bruteforce the password.  
There seems to be another file can you work with, Agent?

To solve this challenge, submit the SHA-256 hash of the archive_password. Pay attention to capital letters.

For example, if My_Flag is the archive password:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

## Hint (20)
Hey yo what is this ???  
![img](spectrogram.png)

## Solution

Lire le spectogram du fichier.
sT3g4n0_4udi0_Is_fUn => c3094e458a5adf2c2832ee22f71100e2004fdb8873c3c1331a7b3a7e58ab82fb
