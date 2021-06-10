# Macro démission

Category: Level02  
Tag: Forensics  
Type: Automatic  
Flag: `APT{77b16ea5b9d1da0eec772831111afd6f9ec1e2c370c339ef3f116874a1cc586e}`  
Points: 70
Requirements: Mail Bomb

## Message

Nice job finding out the email we were looking for.  
An attachment caught our attention.  
Be careful if oppening this document though, the data it contains may harm you.  

To solve this challenge, submit the flag you will find along the challenge.

## Hint (Cost: 60 pts)
Verryhiden is a nice feature in excel. With BIFF and XLM Macro we can do lots of things...

## Solution
 
 - Install https://github.com/DissectMalware/XLMMacroDeobfuscator/
 - xlmdeobfuscator --file FILENAMEHERE.xls  --export-json result.json ; cat result.json | grep APT
