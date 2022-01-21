<p align="center">
  <img src="assets/apt42_logo.png" alt="APT42 logo" width="250" />
</p>

<h1 align="center">
  CTF OSINT
</h1>
<h3 align="center">
  Conduct an online investigation and discover OSINT techniques
</h3>

### Table of Contents

- [Project](#project)
- [Acknowledgements](#acknowledgements)
- [How to contribute](#how-to-contribute)
- [License](#license)

## Project

This project is a CTF hosted by APT42.

It runs as a Capture the Flag format where students have to collect flags to validate levels. Learn OSINT basics by solving challenges that focus on GEOINT, IMINT, SOCMINT and investigative journalism techniques.

APT42 is a student organization of the Paris campus of the school 42. We aim to foster interest in information security and to provide a safe and inclusive space for everyone to learn and improve their cybersecurity skills.

## Play

Have a running ctfd instance (see https://github.com/CTFd/CTFd)  
(`docker run --name ctfd -p 8000:8000 -d ctfd/ctfd`)

Then go to your newly created ctfd instance web page (its on port `8000`), create a new ctf (only `Administration` category is needed, otherwise, click on the `Next` button)

Go to Admin Panel > Config > Backup > import and import https://github.com/apt-42/ctf_osint/releases/download/v1.0.0/CTF.OSINT.2021-12-01_14_50_18.zip  

For a better experience, git clone https://github.com/apt-42/apt42_ctfd_themes and run:  
`docker cp watchdogs <ctfd_container>:<path_to_ctfd>/CTFd/themes` from the cloned directory.  

Else, if you have used the above command to run the instance, you can do:  
`docker cp watchdogs ctfd:/opt/CTFd/CTFd/themes` from the cloned directory.  


Then go to Admin Panel > Config > Theme and choose `watchdogs` as the the theme in the Theme section, click `Update` at the bottom of the page to save this setting.


## Intended audience

Students who aim to work as:

- OSINT analysts
- Online investigators
- Penetration testers
- Data journalists
- Investigative journalists

## Prerequisites

Basic knowledge of the internet, computers, search engines, and social networks.

## Acknowledgements

### Creators

* avan-pra
* mboivin
* therbret
* wandre

### Beta-testers

* agoomany
* agranger (Congrats!! :1st_place_medal:)
* macosta
* nargouse

## How to contribute

You are a 42 student and willing to contribute? Follow these [guidelines](CONTRIBUTING.md).

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
