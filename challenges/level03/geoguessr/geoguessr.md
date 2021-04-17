# geoguessr

Category: Level03  
Tag: GEOINT  
Type: Automatic  
Flag: `APT{ac1ab44acefe486538fb18b886268cbbd7bd3566e9dd574ec7c324b8831549c3}`  
Points: 100  
Requirements: macro demission, ghost in the shell, internet never forgets  

## Message

Wow agent, thats a lot of info you managed to get us recently.  
The secret behind the xls file, the ghostbin info with the help you provided to 42school, and last but not least wandre's old blog.  
Now its time to step up and dive deep into wandre's life and to try getting as close as possible to him.  
With the recent info you provided we found out there was a video or picture hidden in one of the email you parsed earlier.  
It seems like something has been happening in this place.  
First things first, we need you to find out where the video was taken.  

ps: If that can help you (it won't), yes, it's located in France.  

To solve this challenge, submit the SHA-256 hash of the town where the video was taken.  

For example, if "Saint-Jean-de-Luz" is the name of the town:
```
echo -n "Saint-Jean-de-Luz" | sha256sum
df198b8313a00d11c0551672477a5438b80a1518c62f97c57e2d853b0ce523c1
```

Submit the flag as follows:  
`APT{df198b8313a00d11c0551672477a5438b80a1518c62f97c57e2d853b0ce523c1}`

## Hint (Cost: 20 pts)
"it is what it is", but maybe there's a different term to name it, look for synonyms maybe ?  

## Solution
When looking at the video you will be able to see something which seems like a "ponton".  
Upon looking up on google, not even half the pictures that show up will look like what you are looking for.  
Its because the term you are looking for isn't "ponton" but "estacade", upon googling it you will rapidily find the one in the video: "Le Havre estacade".  
When you google it, the real location is not "Le Havre" but "Sainte-Adresse".  
echo -n "Sainte-Adresse" | sha256sum  
ac1ab44acefe486538fb18b886268cbbd7bd3566e9dd574ec7c324b8831549c3  
APT{ac1ab44acefe486538fb18b886268cbbd7bd3566e9dd574ec7c324b8831549c3}  
