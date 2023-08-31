#val av antal godisar för betalning
def collectcandyinfo(candy):
  selected = False
  while (selected == False): 
    try: 
      x = int(input("Välj antal du vill köpa: "))
    except: 
      print(" Nu blev det fel, skriv ett tal")
      
    else:
      selected = True
      listOfCandy = []
      for n in range(x):
        listOfCandy.append(candy)
      print("Du kommer att få betala: {0} kr ".format(x*candy.price))
      return listOfCandy

  
   
    
    
  





  
