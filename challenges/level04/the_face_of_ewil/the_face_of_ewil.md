# The face of ewil

Category: Level04  
Tag: Sysadmin  
Type: Automatic  
Flag: `APT{2713e1f94bf398c3bcc971e7b8fb2b2f4d49820a2cc54ffac3697cab9e47b4b7}`  
Points: 199  
Requirements: follow me

## Message

Upon meeting the barman of the Black Dog pub, you are told that wandre is indeed currently in the bar.  
Too bad he took refuge in the back store, a padlock on the door is preventing us from arresting him.  
As usual, he left something behind, a usb stick containing a weird file, can you work with this?  

To solve this challenge, submit the flag you will find along the challenge.  

## Solution

Mount the file as an usb key (`sudo mount -t auto -o loop file.bin /media/usb_mount_point`) and read the message.

Catch me if you can (well you can't) => APT{9fbf261b62c1d7c00db73afb81dd97fdf20b3442e36e338cb9359b856a03bdc8} => 9  
let_the_stalk_begin (finally?) => APT{76266e243bdc5a467eecc37d633af4dc0feb0c7c0edbe905c49582fd87122731} => 7  
albatraoz (I love that song) => APT{c3094e458a5adf2c2832ee22f71100e2004fdb8873c3c1331a7b3a7e58ab82fb} => c  
git_me_im_famous (this can be useful) => APT{0b66ef7ca982a75aa548c74d8d27ee9310ef94f44ccd1400d08782f0468ea729} => 0  
macro_demission (I wish...) => APT{77b16ea5b9d1da0eec772831111afd6f9ec1e2c370c339ef3f116874a1cc586e} => 7  
intercepted (you wish...) => APT{a99d9c2f2ebce18132bbbc18a37498f9083e5dda019d4072244f7a778aad7b05} => a  

Check commit => https://github.com/matboivin/wandroulette => 1312  
http://www.apt42.fr/97c07a1312 there is an image you exif it and gg.
