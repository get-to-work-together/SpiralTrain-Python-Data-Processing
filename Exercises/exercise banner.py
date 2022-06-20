
def print_banner1(text):
    n = len(text)
    print( '***' + '*' * n + '***' )
    print( '*  ' + text    + '  *' )
    print( '***' + '*' * n + '***' )


def print_banner2(text, c = '*'):
    n = len(text)
    print( c * (n + 6) )
    print( c +'  ' + text    + '  ' + c )
    print( c * (n + 6) )




def banner3(text, c = '*'):
    """Function banner
    input arguments:
        text: athe text to surround with stars
        c: the star character
    return: str
    """
    lines = text.split('\n')
    n = max(map(len, lines))
    s = ''
    s += c * (n + 2 * 3) + '\n'
    for line in lines:
        s += c + '  ' + line + (n - 3) * ' ' + c + '\n'
    s += c * (n + 2 * 3) + '\n'
    return s


def print_banner(text):
    print( banner3(text, '#') )
    
    
# --------------------------------------------


if __name__ == '__main__':
    print_banner('Peter')
