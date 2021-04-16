# shoplifter_shoplifting_1

Category: Level03  
Tag: OSINT  
Type: Automatic  
Flag: `APT{23c16fb3fadc2941eb3ccaf4166775ff0b786c4ac12b42ece5c8e773b35a35f2}`  
Points: 100  
Requirements: geoguessr  

## Message
We went talking to the chairlift / ski tracker guys and they told us that someone came with a strange request recently.  
If anybody from APT42 came in this place they had to tell them to check what happened in Strasbourg on February 16, 2021.  
So we did!  
We got the videosurveillance of the train station;  
Someone strange caught our attention, we got him leaving a phone on the ground.  
Minutes later, a tourist grabbed the phone, but got out of the field of view.  
We contacted the tourist and he told us that he handed over the phone to the train station authorities.  
It's probably now waiting for 'le Grand Architecte du Tout' or one of his contacts to get the phone.  
APT42 needs you to get the phone before one of the bad guys do.  

To solve this challenge, submit the SHA-256 hash of the hour:minute of when the phone got handed to the train station authorities.  

Hour:minute of when the phone got handed to the authorities in Europe/Paris time.  

For example, if time is 23:59:
```
echo -n "23:59" | sha256sum
9d16aac260eaa948db79c7b5bffd8f61a7c0c06ea5e934d042f73374f294e2c3
```

Submit the flag as follows:  
`APT{9d16aac260eaa948db79c7b5bffd8f61a7c0c06ea5e934d042f73374f294e2c3}`

## Solution
If the phone is waiting for someone to grab it, it's in the train station, probably at the lost and found office.  
SNCF is the authority ruling the train station, google "lost object sncf".  
Go to the open data website and look for Strabourg february 16: lucky us, there is only one phone this day.  
echo -n "10:13" | sha256sum  
23c16fb3fadc2941eb3ccaf4166775ff0b786c4ac12b42ece5c8e773b35a35f2  
APT{23c16fb3fadc2941eb3ccaf4166775ff0b786c4ac12b42ece5c8e773b35a35f2}  
