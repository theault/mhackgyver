## input
IP: http://54.89.146.217/  
![osint200.png](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/osint200.png)
HINT:- OSINT200 John is so mean, he won't help.  
HINT:- OSINT200 1. Check RFC 7033 2. Check webfinger

## output
Go to http://54.89.146.217/.well-known/webfinger  
You will obtain:  
SSDEEP(523bd1e47b08cfd4d92cddcbff8e541d)  
flag{ssdeep}  

Now go on https://www.vicheck.ca/md5query.php  
And search 523bd1e47b08cfd4d92cddcbff8e541d  

The flag is __flag{3072:uFvAPdnvdoz91j/q2p4N1m1QmKoEe2TE4lvrNh:uFvAPdnvdoz91rq2p4rm1QdoEe2TE4l/}__  
