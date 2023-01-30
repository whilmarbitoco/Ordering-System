import sys, os
from bin.modules import dessert, dish, log, login, signup


def menu():
  print("[1] Dessert")
  print("[2] Main dish")
  print("\n")


def console():
  print("[1] Menu")
  print("[2] Transaction")
  print("[3] Exit")
  print("\n")


def store():
  global username
  menu()
  c = "[Choose]► "
  user = input(c)
  print("\n")

  if user == "1":
    dessert.getall()
    print("\n")
    c = "[Choose]► "
    user = int(input(c))

    if dessert.getid(user):
      fund = int(input("[Money]► "))
      price = dessert.getid(user)

      if price is not None:
        if fund >= price:
          quan = input("[Quantity]► ")
          print("\n")
          quto = int(price) * int(quan)
          print(f"Total: {quto}")
          print("[1] YES")
          print("[2] NO")
          cfm = input("[Confirm]► ")
          print("\n")

          if cfm == "1":
            total = fund - price
            gin = dessert.getnamebyid(user)
            log.log(gin[0], gin[1], quan, total, username)
            print("[!] Transaction successful")
            print(f"[!] Change: {total}")
            print("\n")

          elif cfm == "2":
            print("[!] Order Cancelled")

          else:
            print("[!] Choice in choices")

        else:
          print("[!] Insufficient funds")
          print("\n")

  elif user == "2":
    dish.getall()
    print("\n")
    c = "[Choose]► "
    user = int(input(c))

    if dessert.getid(user):
      fund = int(input("[Money]► "))
      price = dish.getid(user)

      if price is not None:
        if fund >= price:
          quan = input("[Quantity]► ")
          print("\n")
          quto = int(price) * int(quan)
          print(f"Total: {quto}")
          print("[1] YES")
          print("[2] No")
          cfm = input("[Confirm]► ")
          print("\n")

          if cfm == "1":
            total = fund - price
            gin = dessert.getnamebyid(user)
            log.log(gin[0], gin[1], quan, total, username)
            print("[!] Transaction successful")
            print(f"[!] Change: {total}")
            print("\n")

          elif cfm == "2":
            print("[!] Order Cancelled")

          else:
            print("[!] Choice in choices")

        else:
          print("[!] Insufficient funds")
          print("\n")

  else:
    print("[!] Choice in choices")


def main():
  console()
  c = input("[Choose]► ")
  if c == "1":
    store()

  elif c == "2":
    global username
    log.getlog(username)
    print("\n")

  elif c == "3":
    sys.exit()

  else:
    print("[!] Choice in choices")


os.system("clear")
username = None
while True:
  print("[1] Login")
  print("[2] Signup")
  print("[3] Exit")
  print("\n")
  c = input("[Choose]► ")
  if c == "1":
    username = input("username: ")
    password = input("password: ")
    if login.getcred(username, password):
      print(f"[!] Welcome to Uncrowned Kings Market, {username} [!]")
      print("\n")
      while login.getcred(username, password):
        main()

    else:
      print("[!] User not found")
      print("\n")

  elif c == "2":
    username = input("username: ")
    password = input("password: ")
    signup.signup(username, password)
    print("[!] Account Created")

  elif c == "3":
    sys.exit()

  else:
    print("[!] hoice in choices")
