from presentatie import presenteer
from helper import som_inkomsten

inkomsten = {"Aardbeien-ijs-totaal" : 1000, "Vanille-ijs-totaal" : 2000, "Chocolade-ijs-totaal" : 1500, "Waterijsjes-totaal" : 750}

som1 = inkomsten["Aardbeien-ijs-totaal"]
som2 = inkomsten["Vanille-ijs-totaal"]
som3 = inkomsten["Chocolade-ijs-totaal"]
som4 = inkomsten["Waterijsjes-totaal"]

print(som_inkomsten(som1, som2, som3, som4))
print("============================")
print("Aardbeien-ijs-totaal" , som1)
print("Vanille-ijs-totaal" , som2)
print("Chocolade-ijs-totaal" , som3)
print("Waterijsjes-totaal" , som4)
print("============================")
print("totaal", som_inkomsten(som1, som2, som3, som4))