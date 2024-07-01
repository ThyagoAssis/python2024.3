def tabuada():
    num = int(input("Tabuada do numero?  "))
    op = input("Informe a aoperação: ")
    for i in range(1,10+1):
      if op == "+":
          resultado = num + i
          print(f"{num} + {i} = {resultado}")
      elif op == "-":
          resultado = num - i
          print(f"{num} - {i} = {resultado}")
      elif op == "*":
          resultado = num * i
          print(f"{num} * {i} = {resultado}")
      elif op == "/":
          resultado = num * i
          print(f"{num} / {i} = {resultado}")
      else:
        print("Valores invalidos!")

tabuada()