__import__('sys').stdout = open('res7.txt', 'w')

art = {
    "0": [".####..","##..##.","##..##.","##..##.",".####.."],
    "1": ["###.",".##.",".##.",".##.",".##."],
    "2": [".####..","##..##.","...##..",".##....","######."],
    ",": ["......","......","......","##....",".#...."],
    ".": ["......","......","......","##....","##...."],
    "9": [".####..","##..##.",".#####.","....##.",".####.."]
    }

def ternary(n):
    s = ''
    while n: s+= str(n%3); n//= 3
    return s

def artlen(s):
    return sum(len(art[c][0]) for c in s)

class gen7:
    def __init__(_): _.i = 0; _.j = 0; _.n = 1; _.grid = [['.']*1000 for i in range(492)]
    def writenum(_, c):
        pic = art[c]
        for i in range(_.i, _.i+5):
            for j in range(_.j, _.j+len(pic[0])): _.grid[i][j] = pic[i-_.i][j-_.j]
        _.j+= len(pic[0])
    def writestr(_, s):
        for c in s: _.writenum(c)
    def write(_):
        s = ternary(_.n)+","
        if artlen(s) + _.j > 1000: _.i+= 6; _.j = 0
        for c in s: _.writenum(c)
    def gen(_):
        while _.i < 461: _.write(); _.n*= 2
        _.writestr("0.")
        _.i+= 7; _.j = 0; _.writestr("01020102001020021020001020010200120000120001200102010200120120012001200102012001020102012001020102010102010201200120012012001220100200012002010201020102010200")
        _.i+= 6; _.j = 0; _.writestr("120012012001200120012001200120012001200120012012001201002000102001201200020020010020102001200001020102000120002010200102020000102001202002102001200202010201")
        _.i+= 6; _.j = 0; _.writestr("0201020010020201020201020200120010001200201200102012001200120102012002100002010200010200012022020012020102020102020102010909909990999909999902010200120012")
        _.i+= 6; _.j = 0; _.writestr("0012010201020102012001201201020120102012002001020012001200120012000120012001200210200120000120012001201200120102001001001001010100101000020102010200102001020001")
        print('\n'.join(''.join(row) for row in _.grid))

q = gen7()
q.gen()
assert open('gen7.out').read().rstrip() == open('res7.txt').read().rstrip()