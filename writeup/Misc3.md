## input
Key to OPKG is your flag. 
An archive containing some files.  
HINT:- Misc300 I'm not soft, I'm not hard but Firm I am  

## output
$ file *  
misc300.elf: ELF 32-bit LSB executable, MIPS, MIPS32 rel2 version 1 (SYSV), statically linked, stripped  
$ chmod +x misc300.elf  
$ ./misc300.elf  
qemu: uncaught target signal 4 (Illegal instruction) - core dumped  
Instruction non permise (core dumped)  

After some research on the net, [this link](https://wiki.openwrt.org/doc/howto/qemu) was useful.  

$ qemu-system-mipsel -kernel misc300.elf -nographic -m 256

Wait for the booting stuff.  
And go to OPKG file:
![OPKG stuff](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/Misc3.png)

The flag is __flag{RWSvIveoiFjI6WS/h3J8Us0wUEjA53cQLuHJEwOD/sT5JsGvguZjlKmU}__
