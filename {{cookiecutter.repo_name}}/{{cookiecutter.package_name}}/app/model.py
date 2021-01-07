def say_hello(name):
    print(f'Hello {name}!')

def say_goodbye(name):
    print(f'Goodbye {name}!')

def Greeting():
    def __init__(self, name='World'):
        self.name = name
    
    def hello(self):
        say_hello(self.name)
    
    def goodbye(self):
        say_goodbye(self.name)