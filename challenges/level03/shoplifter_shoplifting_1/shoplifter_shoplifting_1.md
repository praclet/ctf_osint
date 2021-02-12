# shoplifter_shoplifting_1

Category: Level03  
Tag: OSINT  
Type: Automatic  
Flag: `APT{}`  
Points: 0  
Requirements: geoguessr  

## Message
We got the videosurveillance of the train station;  
Someone strange caught our attention, we got him giving a MODIFY_HERE to the lost objects between 00:00 and 00:00.  
We need you to find out the object nature and the exact time the item got handed over the lost objects.

To solve this challenge, submit the flag as follows: APT{sha256(object_nature-hour:minute)}  
For exemple if "Optique" is the object nature and time is 23:59
echo -n "Optique-23:59" | sha256sum  
c42b07a5d57dc3e89b3cd4dac019f20d5b777d11e3cc6e1f245546c348051d99  
APT{c42b07a5d57dc3e89b3cd4dac019f20d5b777d11e3cc6e1f245546c348051d99}  

## Solution

