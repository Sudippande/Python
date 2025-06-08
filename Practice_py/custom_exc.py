class NotJoke(Exception):
    def __init__(self, message):
        self.message=f"Custom Error"
        super().__init__(self.message)
try:
    raise NotJoke("oops you  have got an exception here !")
except NotJoke as n:
    print("error:",n)
