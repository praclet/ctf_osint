# shoplifter_shoplifting_2

Category: Level03  
Tag: OSINT  
Type: Automatic  
Flag: `APT{72612d4a76ddd7e01f7ba41e61a8b6331067cf823789b5bc135b5814b9af90ba}`  
Points: 120  
Requirements: shoplifter_shoplifting_1

## Message
Thanks to the info about the mobile phone you provided,  
Sadly the one that we were intrested in has already been receptionned by someone else.  
We went to the lost objects at the train station, and tricked the receptionnist into giving us the name of the personn that got his hand on the mobile phone we are looking for.  
James Wang, wont be an easy task... or will it?  
Maybe you can try to recon social media ?  

## Solution
Twitter "James Wang phone". Found the James Wang we are looking for.
He says he loves the number 4.
Found the flag which is split in 4 part
1.72612d4a76ddd7e0 //in a tweet
2.1f7ba41e61a8b633 //in a reply to a tweet
3.1067cf823789b5bc //in a list
4.135b5814b9af90ba //in the banner, behind the profile picture

APT{72612d4a76ddd7e01f7ba41e61a8b6331067cf823789b5bc135b5814b9af90ba}
