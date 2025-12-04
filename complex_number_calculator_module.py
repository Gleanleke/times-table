def calculator(x,y,o):
    
    operator=o
    
    if operator== "+": 
        return x + y
    elif operator== "-":
        return x - y
    elif operator== "*": 
        return x * y
    elif operator== "/":
        return x / y
    elif operator== "%": 
        return x % y  
    
    ''' match o:
        case "+": 
            return x + y
        case "-":
            return x - y
        case "*": 
            return x * y
        case "/":
            return x / y
        case "%": 
            return x % y
        case _:
            return "maths error"  
            
            '''