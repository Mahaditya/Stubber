from abc import ABC, abstractmethod

class Language(ABC):

    '''Abstract Methods'''

    @abstractmethod
    def loop(self):
        pass
    @abstractmethod
    def function(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def read_array(self):
        pass

    ''' Methods for Static Languages '''

    def declare(self,name,vartype,container='var'):
        return "not_supported"
    def declare_array(self,name,vartype,container='var'):
        return "not_supported"
    def headers(code):
        return "not_supported"











