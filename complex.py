class ComplexNumber(object):
    def __init__(self, real, imaginary):
        if (isinstance(real, float) | isinstance(real, int)):
            self.real = real
        else:
            raise RuntimeError("The real component of your ComplexNumber is not a number.")
        if (isinstance(imaginary, float) | isinstance(imaginary, int)):
            self.imag = imaginary
        else:
            raise RuntimeError("The imaginary component of your ComplexNumber is not a number.")
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real==other.real) & (self.imag==other.imag):
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not self==other