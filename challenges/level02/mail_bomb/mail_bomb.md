# Mail Bomb

Category: Level02  
Tag: Data science  
Type: Automatic  
Flag: `APT{}`  
Points: 120
Requirements: Albatraoz

## Message

Agent, congratulations for finding the password! Thanks to it, we have been able to unzip the archive. Have you seen all this data?  
Too bad most of it are spam-like e-mail. Maybe with a secret trick of yours, you can find something interesting?  
Like an e-mail addressed to Edward for example?

TODO

To solve this challenge, submit the flag as follows: APT{sha256(mail subject)}  
For exemple if My_Flag is the mail subject:  
echo -n My_Flag | sha256sum  
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404  
APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}  

## Solution

Use OCR techniques (online converter or simple tool like tesseract) to get the text. Write a script to find words such as: Edward/edward or Snowcrash/snowcrash.

TODO
