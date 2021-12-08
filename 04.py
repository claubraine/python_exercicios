#Importa biblioteca
import random
#Inciaializa Lista
lista = []

def inscricao():
  #Formulário de inscrição
  print("\n")
  #Solicitad ados pessoais
  nome = str(input("Digite seu nome: "))
  email = str(input("Digite e-mail: "))
  telefone = str(input("Digite telefone: "))
  curso = str(input("Digite curso: "))
  #Gera um valor aleatorio entre 100 e 400
  voucher = str(random.randrange(100,400))

  #Atribui os valores a um objeto
  dicionario = {
    "voucher" : voucher,
    "nome" : nome,
    "email": email,
    "telefone": telefone,
    "curso": curso
  }

  #Atribui o objeto alista
  lista.append(dicionario) 
  #Chama o muenu novamente
  menu()

def menu():
  #Modulo Menu
  repetir = True
  #Laço de Repetição, repete enquanto não escolher uma opção Válida
  while(repetir):

    print("\n")
    print("**************** MENU ****************")
    print("\n")

    print("1 - Nova inscrição")
    print("2 - Visualização inscrição")
    print("0 - Encerra")

    #Entrada de dados, coloca valor digitado em 'opção'
    opcao = str(input("Opção escolhida: "))

    #Verifica opção escolhida
    if(opcao == "0"):
      #Sai fora do laço de repetição e termina o programa
      repetir = False
    elif(opcao == "1"): 
      #Inserir valores da inscrição 
      inscricao()  
    elif(opcao == "2"):
      #Imprime lista de Inscritos
      
      if (len(lista) == 0):
        #Se não tiver nenhum inscrito
        print("\n")
        print("Nenhuma inscrição cadastrada")
      else:  
        print("------------------ Lista inscritos -------------------")
        #Se tiver inscritos, pecorre a lista com o laço de repetição
        for item in lista:
          #Imprime inscrição
          print("voucher : " + item["voucher"])
          print("nome : " + item["nome"])
          print("email : " + item["email"])
          print("telefone : " + item["telefone"])
          print("curso : " + item["curso"])
       
          print("-------------------------------------------------------") 

    else:
      #Caso digite um valor inválido
      print("\n")
      print("Erro: digite uma opção válida!")      

  #FIM  
  print("\n")      
  print("*********************************")
  print("   Obrigado por usar nosso Sistema")
  print("*********************************")

if(__name__ == "__main__"):
  print("         Sistema de vouchers  ")
  #Chama
  menu()

