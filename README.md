# httprobe 
This is python flavored httprobe version inspire by @tomnomnom httprobe

This script is used to detect the domain is accepting HTTP or HTTPS connection. You can pass Sub-domaina list as input

### Install:
```
git clone https://github.com/securITymania/httprobe.git
cd httprobe
chmod +x httprobe.py

cp httprobe.py /usr/bin

#create --symbolic for easy usage

ln -s /usr/bin/httprobe.py httprob
```

### Usage:
```
usage: httprobe [-h] [-l FILE]

optional arguments:
  -h, --help  show this help message and exit
  -l FILE     Give subdomains list file as input
```
