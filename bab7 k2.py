class Greeter:
    def __init__(self, greeter):
        self.greeter = greeter

    def greet(self):
        return self.greeter.greet()
    

class EnglishGreeter:
    def greet(self):
        return 'Hello!'
    

class SpanishGreeter:
    def greet(self):
        return '¡Hola!'
    

class FrenchGreeter:
    def greet(self):
        return 'Bonjour!'

# Creating greeter objects in various languages
english_greeter = EnglishGreeter()
spanish_greeter = SpanishGreeter()
french_greeter = FrenchGreeter()

# Creating Greeter object and greeting in various languages
greeter = Greeter(english_greeter)
print(greeter.greet()) # Output: Hello!

greeter = Greeter(spanish_greeter)
print(greeter.greet()) # Output: ¡Hola!

greeter = Greeter(french_greeter)
print(greeter.greet()) # Output: Bonjour!
