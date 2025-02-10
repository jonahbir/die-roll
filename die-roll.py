from fractions import Fraction

    

def die_roll():
    y,w=tuple(map(int,input().split()))
    atleast=max(y,w)
  
    chance=7-atleast
    if chance==6:
        return "1/1"
    elif chance==0:
        return "0/6"
   
    return Fraction(chance,6)
print(die_roll())
        
    

