'''
Created on Dec 10, 2014

@author: cienet
'''

class FooClass(object):
    '''
    My First class: FooClass
    '''

    version = 0.1  # class(data) attribute

    def __init__(self, nm='seashell'):
        '''
        Constructor
        '''
        self.name = nm  # class instance attribute
        print 'Created a class instance for', nm
        
    def showname(self):
        print 'Your name is ', self.name
        print 'Class name is ', self.__class__.__name__
        
    def showver(self):
        print self.version  # reference FooClass.version
        
if __name__ == '__main__':
    foo = FooClass()
    foo.showname()
    foo.showver()
