# geoguessr2

Category: Level03  
Tag: GEOINT  
Type: Automatic  
Flag: `APT{916154debfb1a3c932e9fa501d2eff53fc3ab6054933a53237e7e35fe9f60a2b}`  
Points: 100  
Requirements: geoguessr  

## Message
One of our contributor went to the small town where the video is taken.  
Below the structure shown in the video, pinned to one of the pillar, he found a picture.  
The sea harmed it a bit but our AI managed to upscale it a lot.  
It seems like this investigation is turning itslef more and more into a treasure hunt. Hope we won't find anything crazy...  
Anyway, once again, your job is to find the location of this picture, we are sure something relevant will appear if you succeed.  

To solve this challenge, submit the flag as follows: APT{sha256(chairlift_name)}  
For exemple if "Pengelstein 1" is the chairlift name (see right side of the photo):  
echo -n "Pengelstein 1" | sha256sum  
94f1755fd09702dfade94d2e848150142c95bbbce4e866d754bb79d93d0a2fe9  
APT{94f1755fd09702dfade94d2e848150142c95bbbce4e866d754bb79d93d0a2fe9}  

## Hint
Mountain in the background is a little famous, try to enumerate.  
We name things the way they look like to us.  

"It is often difficult to wash them" (query in French)

## Solution

echo -n "Chavanette" | sha256sum  
916154debfb1a3c932e9fa501d2eff53fc3ab6054933a53237e7e35fe9f60a2b  
APT{916154debfb1a3c932e9fa501d2eff53fc3ab6054933a53237e7e35fe9f60a2b}  
