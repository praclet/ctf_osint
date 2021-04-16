# Macro démission

Category: Level02  
Tag: Forensics  
Type: Automatic  
Flag: `APT{77b16ea5b9d1da0eec772831111afd6f9ec1e2c370c339ef3f116874a1cc586e}`  
Points: 200
Requirements: Mail Bomb

## Message

Nice job finding out the e-mail we were looking for.  
An attachment in the e-mail attracted our minds.  
Be careful if oppening this document though, the data it contains may harm you.  

To solve this challenge, submit the flag you will find along the challenge.

Hint qui coûte 190 pts
 - Verryhiden is a nice feature in excel. With BIFF and XLM Macro we can do a lot of things...

## Solution
 
 - Install https://github.com/DissectMalware/XLMMacroDeobfuscator/
 - xlmdeobfuscator --file FILENAMEHERE.xls  --export-json result.json ; cat result.json | grep APT
