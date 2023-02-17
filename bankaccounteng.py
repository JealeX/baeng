print("""**************************
Mobile Bank App              
**************************""")

import datetime

current_date=datetime.date.today()
print(current_date)

while True:
  card = input("Please enter your card number:")
  if (card != "5899 6588 3354 2265") and (card !="4566 4487 5894 5588"):
    print("This card number isn't valid. Please try again.")
    continue
  accountbalance = int(9000)
  accountbalance1 = int(5000)
  process = input("What do you want to do?\n1. Account Balance Inquiry\n2. Withdraw Money\n3. Money Transfer\n")
  if (card == "5899 6588 3354 2265"):
    print("MasterCard Papara")
    if (process == "1"):
      print("Your account balance is",accountbalance, "$.")
      q = input("Do you wanna make another process?  If your answer is yes please dial 1. If your answer is no please dial 2.")
      if (q == "1"):
        print("You are being redirected to the home page...")
        exit
      elif (q == "2"):
        print("Thank you for using our app. See you later!")
        break
    elif (process == "2"):
      withdrawmoney = int(input("Enter the amount:"))
      if (withdrawmoney > accountbalance):
        print("Your account balance is isn't enough for do this process.")
        exit
      elif (withdrawmoney <= accountbalance):
        print("Your transaction has been confirmed. You can draw your money on closest ATM machine by reading a QR Code .")
      q = input("Do you wanna make another process?  If your answer is yes please dial 1. If your answer is no please dial 2.")
      if (q == "1"):
        print("You are being redirected to the home page...")
        exit
      elif (q == "2"):
        print("Thank you for using our app. See you later!")
        break
      elif (process == "3"):
        transfer = input("Please write the card number you wanna transfer money:")
        if (transfer != "4566 4487 5894 5588"):
          print("This card number isn't valid. Please try again.")
          exit(61)
        elif(transfer=="4566 4487 5894 5588"):
          print("İşlem gerçekleştirildi. Para başarıyla karşı tarafa aktarıldı.")
          q = input("Do you wanna make another process?  If your answer is yes please dial 1. If your answer is no please dial 2.")
          if (q == "1"):
            ("You are being redirected to the home page...")
            exit
          elif (q == "2"):
            ("Thank you for using our app. See you later!")
            break 
  elif (card == "4566 4487 5894 5588"):
    print("Visa BankAmericard")
    if (process == "1"):
      print("Your account balance is",accountbalance, "$.")
      q = input("Do you wanna make another process?  If your answer is yes please dial 1. If your answer is no please dial 2.")
      if (q == "1"):
        print("You are being redirected to the home page...")
        exit
      elif (q == "2"):
        print("Thank you for using our app. See you later!")
        break
    elif (process == "2"):
      withdrawmoney = int(input("Çekmek istediğiniz tutarı giriniz:"))
      if (withdrawmoney > accountbalance1):
       print("Your account balance is isn't enough for do this process.")
       exit
      elif (withdrawmoney <= accountbalance1):
       print("Your transaction has been confirmed. You can draw your money on closest ATM machine by reading a QR Code .")
    elif (process == "3"):
        transfer = input("Please write the card number you wanna transfer money:")
        if (transfer != "5899 6588 3354 2265"):
          print("Hatalı numara girdiniz. Lütfen tekrar tuşlayınız.")
          exit(57)
        elif(transfer=="5899 6588 3354 2265"):
          print("İşlem gerçekleştirildi. Para başarıyla karşı tarafa aktarıldı.")
          q = input("Do you wanna make another process?  If your answer is yes please dial 1. If your answer is no please dial 2.")
          if (q == "1"):
            ("You are being redirected to the home page...")
            exit
          elif (q == "2"):
            ("Thank you for using our app. See you later!")
            break 