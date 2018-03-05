## input
Just see the [attachment](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/attachment/scream.zip).

## output
When you execute the program, you have to wait 42h. We don't have time for that:
![program_execution](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/Count%20down.png)

So let's have a look inside the exe file:

```
~/Téléchargements$ strings scream.exe | grep -i net | more
s9Net<
NETSCAPE2.0
NET/
unET
NETy
nnet
"NEt
SneT
Netl
.NETFramework,Version=v4.0
.NET Framework 4
```

Ok it's a .NET file, it's easier to use .NET reflector for this:
![.NET_reflector](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/.NET%20Reflector.png)

A bitmap? Don't worry, foremost is your friend:

```
root@kali:/media/sf_challenge/CTF/JuniorsCTF/JuniorsCTF2017/We'vediscoveredanotherplanet!# foremost scream.exe 
Processing: scream.exe
|*|
root@kali:/media/sf_challenge/CTF/JuniorsCTF/JuniorsCTF2017/We'vediscoveredanotherplanet!# ls output/png/
00000005.png
```

That's all:
![flag](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/images/We've_discovered_another_planet!_flag.png)
