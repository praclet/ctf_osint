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

 To solve this challenge, submit the SHA-256 hash of the flag.

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

Hint qui coûte 190 pts
 - Verryhiden is a nice feature in excel. With BIFF and XLM Macro we can do a lot of things...

## Solution
 
 - Install https://github.com/DissectMalware/XLMMacroDeobfuscator/
 - xlmdeobfuscator --file FILENAMEHERE.xls  --export-json result.json ; cat result.json | grep APT
