def calculator(num1,num2,operation):
    if operation== "+":
      return num1+num2
    elif operation== "-":
        return num1-num2
    elif operation== "*":
        return num1*num2
    elif operation== "/":
        return num1/num2
    else:
        return "Invalid num"
history=[]
while True:
    command = input("Type 'exit' to quit or Enter to continue: ")
    if command.lower() == "exit":
        print("Ta-ta! Bye!")
        break
    if command.lower()== "history":
        print(history)
        continue
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    operation = input("Select operation (+, -, *, /): ")
    result = calculator(num1, num2, operation)
    print("Result:", result)
    history.append(f"{num1} {operation} {num2}={result}")