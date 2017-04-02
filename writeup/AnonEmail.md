## input
Hey man. My flag got kidnapped, can you help me get it back?  
Warning: do not use yopmail.com w/ this service.
[Attachment](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/attachment/challenge.eml)

## output
We tried to send an email with the 5ymail.com service. We received the following credentials:  
Username = 115261-eQAWO / Password = eQAWOBI6  

By looking through the mail headers from our anonymous mail sent to ourself, we remarked this line:  
Your_FAKE_Name.eQAWOBI6Y9255397-115261-EN@5ymail.com  

So we retrieved this line from the [attachment](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/attachment/challenge.eml) of the challenge:  
Bad_Guy.nUWAQuXA8i253005-114196-EN@5ymail.com  

And we deduced the Bad Guy credentials:  
Username = 114196-nUWAQ / Password = nUWAQuXA  

We connected to the service with these credentials and we obtained:  
![flag](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/AnonEmail.png)
