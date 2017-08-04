## input  
Decode [ME](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/attachment/enc.txt) faster !

## output
When we open the file, it looks like base64 encoded. So we try to decode the file:

```
~/Documents/challenge/CTF/Bugs_Bunny/Crypto-50$ cat enc.txt | base64 -d > output.txt
```

It looks like, again, a base64 encoded file... So:
```
~/Documents/challenge/CTF/Bugs_Bunny/Crypto-50$ cat enc.txt | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d 
Bugs_Bunny{N0T_H4Rd_4T_4ll}
```
