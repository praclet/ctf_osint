# shoplifter_shoplifting_1

Category: Level03  
Tag: OSINT  
Type: Automatic  
Flag: `APT{e09303dfd12fdf74dd19d7eaad222f2a792ccf86bac9bd4a35ae494628721b07}`  
Points: 100  
Requirements: geoguessr  

## Message
We went talking to the chairlift / ski tracker guys and they told us that someone came with a strange request recently.  
If anybody from APT42 came in this place they to tell them to check what happened in Strasbourg the 16th february in 2021.  
So that's what we did !  
We got the videosurveillance of the train station;  
Someone strange caught our attention, we got him leaving a phone on the ground.  
Minutes later a tourist grabbed the phone, but get out of camera view.  
We contacted the tourist and he told us that he handed over the phone to the train station authorities.  
It's probably now waiting for le Grand Architecte du Tout or one of his contact to get the phone.  
APT42 need you to get back the phone before one of the bad guy do.  

To solve this challenge, submit the SHA-256 hash of the flag as follows: `APT{object_nature-hour:minute}`.  

Object nature in french.  
Hour:minute of when the phone got handed back to the authorities in Europe/Paris time.  

For example, if "Optique" is the object nature and time is 23:59:
```
echo -n "Optique-23:59" | sha256sum
c42b07a5d57dc3e89b3cd4dac019f20d5b777d11e3cc6e1f245546c348051d99
```

Submit the flag as follows:  
`APT{c42b07a5d57dc3e89b3cd4dac019f20d5b777d11e3cc6e1f245546c348051d99}`

## Solution
If the phone is waiting for someone to grab it, it's in the train station so probably the lost object  
SNCF is the authority ruling the train station, google "lost object sncf"  
Go to the open data website and look for Strabourg february 16th, lucky us, there is only one phone this day  
echo -n "Téléphone portable protégé (étui, coque,…)-10:13" | sha256sum  
e09303dfd12fdf74dd19d7eaad222f2a792ccf86bac9bd4a35ae494628721b07  
APT{e09303dfd12fdf74dd19d7eaad222f2a792ccf86bac9bd4a35ae494628721b07}  
