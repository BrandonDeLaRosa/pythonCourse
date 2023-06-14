#  TIENDA BLACK FRIDAY

# todo si el precio es de 300 o mas aplica 30% desc.
# todo si el precio es entre 200 y 300 aplica 20%
# todo si el precio esta entre 100 y 300 aplica un 10% de desc
# todo  si el precio es menos que 100 aplica 5%
# todo si el precio es negativo no hay descuento.



producto = 400
desc = 0

if producto > 100: 
    desc = producto * 0.30
elif producto >= 200 and producto < 300: 
    desc = producto * 0.20
elif producto >= 100 and producto < 300:
    desc = producto * 0.10
elif producto < 100:
    desc = producto * 0.05 
elif producto < 0:
    print("Sorry this product has no discount")                   


print(producto - desc)
   

if producto >= 300:
    producto *= .30
elif producto >= 200 and producto < 300:
    producto *= .20
elif producto >= 100 and producto < 300:
    producto *= .10
elif producto < 100 and  producto > 0:
    producto *= .05        

print(producto)