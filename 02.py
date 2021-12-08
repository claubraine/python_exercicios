print("*********************************")
print("     Sistema de Conversão")

repetir = True
#Laço de repetição
while(repetir):

  print("*********************************")
  print("\n")

  #Atribui valor digitado a variavel nome
  nome = str(input("Digite um nome: "))
  #Cria uma varial auxiliar e inicializa vazia
  aux = ""

  #Laço de repetição que vai percorrer cada letra do nome
  for letra in nome:
    #Verefica se a letra é vogal, se sim concatena o simbolo com o valor davarialve aux
    if (letra == "A"):
      aux = aux + "@"
    elif (letra == "a"):
      aux = aux + "@"
    elif (letra == "E"):
      aux = aux + "&"
    elif (letra == "e"):
      aux = aux + "&"
    elif (letra == "I"):
      aux = aux + "!"
    elif (letra == "i"):
      aux = aux + "!"
    elif (letra == "O"):
      aux = aux + "#"
    elif (letra == "o"):
      aux = aux + "#"
    elif (letra == "U"):
      aux = aux + "*"
    elif (letra == "u"): 
      aux = aux + "*"
    else:
      #Se a letra não for vogal, concate ela com o valor da variavel aux
      aux = aux + letra
  print("\n")
  #Imptime o valor original do nome
  print(nome)
  #Imptime o valor do nome  convertido
  print(aux)

  repetir_pergunta = True
  #Laço de petição, pergunta se quer continuar e fornecer um novo nome
  while(repetir_pergunta):
    print("\n")
    pergunta = int(input("Deseja continuar? 0 - Não     1-sim   : "))
    if(pergunta == 0):
      #Finaliza o programa
      repetir = False
      repetir_pergunta = False
    elif(pergunta == 1):
      #Volta ao inicio e perugnta um novo nome
      repetir = True
      repetir_pergunta = False
      
print("\n")  
print("*********************************")
print("FIM")