
class Person:
    '''My Person class'''
    
    __slots__ = ['_name','_residence']
    
    def __init__(self, name, residence = 'unknown'):
        self._name = name
        self._residence = residence

    def __repr__(self):
        return f'Person(\'{self._name}\', \'{self._residence}\')'

    def __eq__(self, other):
        return self._name == other.name
        
    def tell(self):
        return(f'I am {self._name} and I live in {self._residence}')

    def move(self, new_residence):
        self._residence = new_residence

#-------------------------------------

if __name__ == '__main__':
    
    p = Person('Trystan', 'Delft')
    
    print( p.tell() )
    
    p.move('Hilversum')
    
    print( p.tell() )


