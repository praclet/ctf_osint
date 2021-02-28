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
We name things the way they look like to us. (query in French)  

"It is often difficult to wash them" (query in French)

## Solution
Photo is taken towards east, query most known mountain range like the Alps, if you enumerate the mountains you will find the "Dents du Midi".  
Try to find this location in google earth.  
![photo_highlight](solution1.png)  
There arent many place like this in google earth in the west side of the "Dents du Midi", maybe 1 or too location may get your attention  
![photo_highlight_earth](solution2.png)  
You see 3 chairlift that goes as high as the photo on the map, grab photo of the 3 and see that the right one is Chavanette  

echo -n "Chavanette" | sha256sum  
916154debfb1a3c932e9fa501d2eff53fc3ab6054933a53237e7e35fe9f60a2b  
APT{916154debfb1a3c932e9fa501d2eff53fc3ab6054933a53237e7e35fe9f60a2b}  
