import replit
import second

# variabel för menyval
x = 0
#spara informationen i en lista
class Candy:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    
lionvanlig = Candy("1. Lion vanlig -", 20)
lionwhite = Candy("2.Lion White -", 22)
lionchoco = Candy("3.Lion Choco -", 24)
maraboumjölk = Candy("1.Marabou möjlk choklad -", 20)
maraboumörk = Candy("2.Marabou mörk choklad -", 22)
marabouapelsin = Candy("3.Marabou apelsinkrokant -", 24)
ploppvanlig = Candy("1. Plopp vanlig -", 20)
ploppmint = Candy("2. Plopp mint -", 22)
ploppsalty = Candy("3. Plopp salty -", 24)
daimvanlig = Candy("daim vanlig -", 20)
daimmörk = Candy("daim mörk -", 22)
daimmint = Candy("daim mint -", 24)
while True:
  # rensa meny
  replit.clear()
  # visa meny
  print("Välj ned något av de godis sorterna som finns")
  print("************")
  print("1. Marabou")
  print("2. Plopp")
  print("3. Daim")
  print("4. Lion\n")
  print("5. Avsluta programmet\n")

  # få kundens val
  x = int(input(" Skriv in dit val: "))

  # process att få kundens val
  if x == 1:
    replit.clear()
    print(maraboumjölk.name,maraboumjölk.price)
    print(maraboumörk.name,maraboumörk.price)
    print(marabouapelsin.name,marabouapelsin.price)
    y = int(input(" Skriv in dit val: "))
    if y == 1:
        second.collectcandyinfo(maraboumjölk)
    elif y == 2:
        second.collectcandyinfo(maraboumörk)
    elif y == 3:
        second.collectcandyinfo(marabouapelsin)
    input("Tryck enter för att komma till meny")
  elif x == 2:
    replit.clear()
    print(ploppvanlig.name,ploppvanlig.price)
    print(ploppmint.name,ploppsalty.price)
    print(ploppsalty.name,ploppmint.price)
    y = int(input(" Skriv in dit val: "))
    if y == 1:
        second.collectcandyinfo(ploppvanlig)
    elif y == 2:
        second.collectcandyinfo(ploppmint)
    elif y == 3:
        second.collectcandyinfo(ploppsalty)
    input("Tryck enter för att komma till meny")
  elif x == 3:
    replit.clear()
    print("1. Daim vanlig - 20 kr")
    print("2. Daim mörk - 22 kr")
    print("2. Daim mint - 24 kr")
    y = int(input(" Skriv in dit val: "))
    if y == 1:
        second.collectcandyinfo(daimvanlig)  
    elif y == 2:
        second.collectcandyinfo(daimmörk)
    elif y == 3:
        second.collectcandyinfo(daimmint)
    input("Tryck enter för att komma till meny")
  elif x == 4:
    replit.clear()
    print(lionvanlig.name,lionvanlig.price)
    print("2. Lion White - 22 kr")
    print("2. Lion Choco - 24 kr")
    y = int(input(" Skriv in dit val: "))
    if y== 1:
      listoflion = second.collectcandyinfo(lionvanlig)
      print(listoflion)
    elif y == 2:
       listoflion =  second.collectcandyinfo(lionwhite)
       print(listoflion)
    elif y == 3:
        listoflion = second.collectcandyinfo(lionchoco)
        print(listoflion)
    input("Tryck enter för att komma till meny")
  # avsluta programmet
  elif x == 5:
    replit.clear()
    print("Avsluta programmet")
    input("Tryck enter för att avsluta programmet")
    replit.clear()
    break

  # Om det skrivs något som inte finns i menyvalet
  else:
    print(
      "Du gjorde inte ett giltigt val.\n Gå tillbaka till meny och gör ett nytt val"
    )
    input("Tryck enter för att komma tillbaka till meny")
