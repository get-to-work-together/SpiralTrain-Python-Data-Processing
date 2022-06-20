class Car:
    
    __slots__ = ['_make', '_model', '_color', '_mileage']
    
    def __init__(self, make, model, color):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = 0
        
    def info(self):
        return f'A {self._color} {self._make} {self._model} with {self._mileage} km on the meter.'

    def drive(self, distance):
        self._mileage += distance 
        
#---------------------------------

if __name__ == '__main__':
    
    car1 = Car('Renault', 'Megane Station', 'metalic brown', )
    
    print( car1.info() )
    
    car1.drive(278)
    
    print( car1.info() )

        
        
        
        
        