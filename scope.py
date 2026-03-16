c = None 
d = None
def set_globals(some_int:int,some_str:str)->None:
    global c
    global d
    c = some_int
    d = some_str

def get_globals():
    return (c, d)

