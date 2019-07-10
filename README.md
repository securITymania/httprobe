# httprobe 
This is python flavored httprobe version inspire by @tomnomnom httprobe

This script is used to detect the domain is accepting HTTP or HTTPS connection. You can pass Sub-domaina list as input

```
cp httprobe.py /usr/bin

#create --symbolic for easy usage

ln -s /usr/bin/httprobe.py httprobe
```

### Usage:
```
usage: httprobe [-h] [-l] file

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit
  -l, --list  Give subdomains list file as input
```

