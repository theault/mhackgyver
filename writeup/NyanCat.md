## input
It looks like my cat is trying to tell me something. Do you speak cat? Meow.

And a streamed video showing a cat with different color filter on it is viewable.

## output
We remark there is 8 different color filters with their HTML code associated:
White (#FFFFFF)
Blue (#0000FF)
Yellow (#FFFF00)
Black (#000000)
Pink (#FF00FF)
Red (#FF0000)
Aqua (#00FFFF)
Lime (#00FF00)

We did manually the list of displayed color filters through the video time:
Green
Pink
Black
[...]
White
Pink

And we took the assumption that we have to extract 3 bits by colors:
White (111)
Blue (001)
Yellow (110)
Black (000)
Pink (101)
Red (100)
Aqua (011)
Lime (010)

That gave us 010101000100100001000011011110110110111001111001011000010110111001111001011000010110111001111001011000010110111001111001011000010110111001111001011000010110111001111001011000010110111001111001011000010110111001111101.
We converted that to ASCII:
__THC{nyanyanyanyanyanyanyan}__
