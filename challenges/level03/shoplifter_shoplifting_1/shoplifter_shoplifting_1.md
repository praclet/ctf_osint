# shoplifter_shoplifting_1

Category: Level03  
Tag: OSINT  
Type: Automatic  
Flag: `APT{e09303dfd12fdf74dd19d7eaad222f2a792ccf86bac9bd4a35ae494628721b07}`  
Points: 100  
Requirements: geoguessr  

## Message
We got the videosurveillance of the train station;  
Someone strange caught our attention, we got him leaving a phone on the ground february the 16th in Strasbourg train Station.  
Minutes later a tourist which seems to had good intentions grabbed the phone, but get out of camera view.  
We need you to find info about the phone.  
We contacted the tourist and he told us that he handed over the phone to the train station authorities.  

To solve this challenge, submit the SHA-256 hash of the flag as follows: `APT{object_nature-hour:minute}`. Do not translate the object nature.

For example, if "Optique" is the object nature and time is 23:59:
```
echo -n "Optique-23:59" | sha256sum
c42b07a5d57dc3e89b3cd4dac019f20d5b777d11e3cc6e1f245546c348051d99
```

Submit the flag as follows:  
`APT{c42b07a5d57dc3e89b3cd4dac019f20d5b777d11e3cc6e1f245546c348051d99}`


## Solution
If the tourist had good intention he probably handed the phone over to the lost object  
SNCF is the authority ruling the train station, google "lost object sncf"  
Go to the open data website and look for Strabourg february 16th find out there are 2 phone lost but same timestamp  
echo -n "Téléphone portable protégé (étui, coque,…)-10:13" | sha256sum  
e09303dfd12fdf74dd19d7eaad222f2a792ccf86bac9bd4a35ae494628721b07  
APT{e09303dfd12fdf74dd19d7eaad222f2a792ccf86bac9bd4a35ae494628721b07}  
