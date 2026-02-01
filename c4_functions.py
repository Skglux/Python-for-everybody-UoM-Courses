while True:
    
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    
    try:
        
        fhrs = float(hrs)
        frate = float(rate)
        break 
        
    except:
        print("Please input numbers")

def computepay(h, r):
    
    if h > 40:
        
       pay = (40*r)+(h-40)*(1.5*r)
    else:
        pay = h * r 
    
    
    return pay  
    
p = computepay(fhrs, frate)

print("Pay", p)