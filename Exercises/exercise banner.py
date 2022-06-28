
def print_banner1(text):
    n = len(text)
    print( '***' + '*' * n + '***' )
    print( '*  ' + text    + '  *' )
    print( '***' + '*' * n + '***' )


print_banner1('Peter')



#%%

def print_banner2(text, c = '*'):
    n = len(text)
    print( c * (n + 6) )
    print( c +'  ' + text    + '  ' + c )
    print( c * (n + 6) )


print_banner2('Peter', '#')


#%%


def banner3(text, c = '*'):
    """Function banner
    input arguments:
        text: the text to surround with stars
        c: the star character
    return: str
    """
    
    n = len(text)
    s = ''
    s += c * (n + 2 * 3) + '\n'
    s += c + '  ' + text + (n - 3) * ' ' + c + '\n'
    s += c * (n + 2 * 3) + '\n'
    return s

def print_banner3(text):
    print( banner3(text, '#') )
    
    
print_banner3('Peter')
