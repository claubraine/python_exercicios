print("*********************************")
print("      Ensino  Fundamental")
print("     Sistema de Matriculas")

repetir = True
#Laço de petição, repete sempre que escolher a opção 1 - sim
while(repetir):
  print("*********************************")
  print("\n")
  #Atribui a variavel aluno valor inserido
  aluno = str(input("Entre com o nome do(a) Aluno(a): "))
  #Atribui a variavel idade valor inserido
  idade = int(input("Entre com a idade: "))

  #Verifica a qual ensino o aluno pertence
  #Caso satisfaça as condições será verdadeiro
  educacao_infantil = (idade >= 1 and idade <= 5)
  ensino_fundam_i   = (idade >= 6 and idade <= 10)
  ensino_fundam_ii  = (idade >= 11 and idade <=14)
  ensino_medio = idade >= 15

  print("\n") 

  if(educacao_infantil):
    #Caso Verdadeiro
    print("O Aluno(a) ", aluno ," tem ", idade ," ano(s) e está na Educaçao Infantil.")
  elif(ensino_fundam_i):
    #Caso Verdadeiro
    print("O Aluno(a) ", aluno ," tem ", idade ," anos e está no Ensino Fundamental I.")
  elif(ensino_fundam_ii):
    #Caso Verdadeiro
    print("O Aluno(a) ", aluno ," tem ", idade ," anos e está na Ensino Fundamental II.")
  elif(ensino_medio):
    #Caso Verdadeiro
    print("O Aluno(a) ", aluno ," tem ", idade ," anos e está no Ensino médio.")
  else:
    #Caso idade seja inválida
    print("Idade inválida.")

  repetir_pergunta = True

  #Laço de repetição
  while(repetir_pergunta):
    print("\n")
    #Atribui opçao digita a variavel pergunta
    pergunta = int(input("Deseja continuar? 0 - Não     1 - sim   : "))
    if(pergunta == 0):
      #Finaliza o programa
      repetir = False
      repetir_pergunta = False
    elif(pergunta == 1):
      #Volta ao inicio e pede as informações do novoaluno
      repetir = True
      repetir_pergunta = False

print("\n")      
print("*********************************")
print("   Obrigado por usar nosso Sistema")
print("*********************************")