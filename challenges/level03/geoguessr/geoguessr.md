# geoguessr

Category: Level03  
Tag: GEOINT  
Type: Automatic  
Flag: `APT{}`  
Points: 100  
Requirements: macro demission, ghost in the shell, internet never forgets  

## Message
Wow agent, thats a lot of info you managed to get us recently,  
The secret behind the xls file, the ghostbin info with the help you provided to 42school and last but not least wandre's old blog.  
Now its time to step up the level and dive deep into wandre's life and to try getting as close as possible to him.  
With the recent info you provided we found out there was a video/photo hidden in *REDACTED*  
Something seems to have been happening in this place.  
First things first, we need you to find out where is the picture taken.  

To solve this challenge, submit the flag as follows: APT{sha256(what3words_location)}  
For exemple if "owns.doing.estate" is the what3words location of the photo/video:  
echo -n "owns.doing.estate" | sha256sum  
e620e8e50ff1d30631544c4a1acd879acf1d992ed8535709b25a91a5e84dacde  
APT{e620e8e50ff1d30631544c4a1acd879acf1d992ed8535709b25a91a5e84dacde}  

## Solution

