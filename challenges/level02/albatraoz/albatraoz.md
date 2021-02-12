# Albatraoz

Category: Level02  
Tag: Steganography  
Type: Automatic  
Flag: `APT{}`  
Points: 80
Requirements: You know Google?, R.D.V, Ok user

## Message
Good job agent, Electrolab was indeed the place where wandre and Catnity used to meet up.  
Too bad they didnt left the place untouch, every equipement, gone.  
We managed to get our hands on a usb stick hidden inside Electrolab post box;  
The usb key contains a password protected archive, however, we didnt managed to bruteforce the password.  
There seems to be another file can you work with that agent ?

To solve this challenge, submit the flag as follows: APT{sha256(archive_password)}  
For exemple if "My_Flag" is the archive password:  
echo -n "My_Flag" | sha256sum  
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404  
APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}

## Solution

