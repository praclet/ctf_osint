# Internet never forgets

Category: Level02  
Tag: SOCMINT  
Type: Automatic  
Flag: `APT{3ae38cdf2192d91de5e972a8988b0a5b74b576c81df46447256b716b8d61c31e}`  
Points: 80
Requirements: You know Google?, R.D.V, Ok user

## Message
Good job, you found the github account of the hacker !  
Recon his github repositories, look for anything that look suspicious, maybe you can find something interesting...  


#hint ? # some says that wandre had a blog back in the days, maybe vestige of it still remain somewhere...  

## Solution

> Aller sur le page https://ukrainian-giants.000webhostapp.com/ 

> Trouver un lien mort sur la page principal => https://ukrainian-giants.000webhostapp.com/dogs

> Aller sur waybackmachine => https://web.archive.org/web/20210303121637/https://ukrainian-giants.000webhostapp.com/dogs
 
> Regarder la source pour trouver => W4y_b4rK_M4ch1n3_1s_n1c3 => (sha256 == 3ae38cdf2192d91de5e972a8988b0a5b74b576c81df46447256b716b8d61c31e 

> APT{3ae38cdf2192d91de5e972a8988b0a5b74b576c81df46447256b716b8d61c31e}
