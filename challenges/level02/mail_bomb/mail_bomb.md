# Mail Bomb

Category: Level02  
Tag: Data science  
Type: Automatic  
Flag: `APT{9fbb38c2b63244203cf502b8df99bc032aff45ba853e494e0e7ccf9272b4e9fe}`  
Points: 80
Requirements: Albatraoz

## Message

You just received an email from the field agent. Let's open it!

```
From: Diana Arkly <darkly@aptagency.com>

Agent, congratulations for finding the password! Thanks to it, you are now able to unzip the archive. Have you seen all this data?  
Too bad most of it looks like spam emails. Maybe with a secret trick of yours, you can find something interesting?  
Like an e-mail addressed to Edward for example?
```

To solve this challenge, submit the SHA-256 hash of the flag.

For example, if My_Flag is the flag:
```
echo -n My_Flag | sha256sum
f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404
```

Submit the flag as follows:  
`APT{f8fa66e084281bb87f40b2f7048ceb93c28dd6e282f98f43a2cd4396245a7404}`

## Solution

They get a zip file containing 200 email screenshots with many duplicated screenshots both in Russian and English.

There are only 5 unique emails:

- screenshot_00053.jpg
- screenshot_00073.jpg
- screenshot_00092.jpg
- screenshot_00140.jpg
- screenshot_00158.jpg

Use OCR techniques (online converter or simple tool like tesseract) to get the text. Write a script to find targeted words (in English).

As Edward works at APT Agency, try to filter emails by targeting "aptagency.com". You will get 4 emails that are hints. They have to be read in this order:

- screenshot_00092.jpg
- screenshot_00073.jpg
- screenshot_00053.jpg
- screenshot_00158.jpg

In the 2nd email, Edward says he must be contacted by his other email address. Then Cat asks about it. In the last email, Edward says it's an address named after Marvin, the robot in The Hitchhiker's Guide to the Galaxy.

Try to target "marvin" and you will get screenshot_00140.jpg. The latter is in Russian. Upload the file into [Yandex OCR translator](https://translate.yandex.com/ocr) and get:

```
Good afternoon
From: me <adriana@evilevil.com>
Sent 31/10/2020
To: m <marvin@paranoid.com>
Show details
Well, Edward!
What's up?
I can give you a job.
Well done!
Here's the flag: capture the flag
Bye
```

Get the flag:

```sh
echo -n capture the flag | sha256sum
9fbb38c2b63244203cf502b8df99bc032aff45ba853e494e0e7ccf9272b4e9fe
```
