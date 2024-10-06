import time

def main_menu():
  while True:
    print("\n" * 2)
    print("=" * 36)
    print("    School Multitool - By TVEGesd")
    print("=" * 36)
    print("1. Math Calculator")
    print("2. Schedule")
    print("3. Studying")
    print("4. English to Spanish Translator")
    print("5. Exit")
    print("=" * 36)

choice = input("Enter an option!: ")

if choice == "1":
  calculator()
elif choice == "2":
  schedule()
elif choice == "3":
  studying()
elif choice == "4":
  translator()
elif choice == "5":
  exit_program()
else:
  print("Invalid choice, Please try again")
  time.sleep(2)

def calculator():
  print("\n" + "=" * 36)
  print("           Math Calculator")
  print("=" * 36)
  expression = input("Enter an expression: ")

try:
  result = eval(expression)   # Using eval to calculate the expression
    print(f"Result = {result}"|)
  execept Exception as e:
    print("Error in calculation:", e)

    time.sleep(2)

def schdule():
  print(\n" + "=" * 36)
  print("               Schedule")
  print("=" * 36)
  for i in range(1, 10):
    print(f"{i}. Put your {ordinal(i)} period here"
  print("=" * 36)

  time.sleep(2)

def studying():
  print("\nIDK what to put here you just write it yourself")
  time.sleep(2)

def translator():
  english_word = input("Enter the word you want translated: ")

  if english_word == "hello":
    print("Hola")
    print("to translate more select the option again")
    print("I will add more translation words")
    time.sleep(2)

def exit_program():
  print("Exiting program")
  print("ty for using this")
  time.sleep(2)
  exit()

def ordinal(n):
  # Function to return ordinal number
    if 10 <= n % 100 < 20:
        suffix = 'th'
    else:
      suffix = {1: 'st", 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

if __name__ == "__main__":
    main_menu
