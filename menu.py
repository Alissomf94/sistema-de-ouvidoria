import time

class Menu ():
    def __init__(self) -> None:
        pass
 

    def boas_vindas (self):
        #Mensagem de boas vinda ao usuário
        print("\n")
        print("-" * 65)
        print ("     \033[34mSEJA BEM-VINDO A OUVIDORIA MUNICIPAL DE CAMPINA GRANDE   \033[m")
        print("-" * 65)
        
        #função sleep a qual irá simular um pequeno "delay" ao muda de tela e emissão de mensagens aos usuários
        time.sleep(2)
        
        #Intruções para excutar o sistema 
        print("-" * 72)
        print("                             \033[34mINSTRUÇÃO\033[m                                 ")
        print("\n1- Para selcionar uma opção digite a letra que esta a frente dela.")
        print("2-Será permitido armazenar apenas 3 feedbacks, sendo um de cada categoria.")
        print("-" * 72)

    def menu_principal (self):
        time.sleep(4)
        #exibição do menu principal
        print("-" * 65)
        print ("                          \033[34mMENU PRINCIPAL         \033[m")
        print("-" * 65)
            
        #opções do menu principal
        print("\nU-Usuário\nA-Atendente\n")

    def menu_acesso (self):
    
        #execução da função append esta salvando um registro de um usuário na lista
        print("\n")
                
        time.sleep(2)
                
        #Apresentação do atendente para o usuario
        print("-" * 65)
        print("\033[34mOlá, Me chamo Alisson e hoje realizarei seu atendimento!\033[m     ")
        print("-" * 65)
                
        #exibição e pedido do tipo de acesso do usuário
        print("\nJ-Ja possuo cadastro\nQ-Quero me cadastrar\n")
    
    def menu_usuario (self):
    
        #exibição do menu de opções do usuário
        print("-" * 65)
        print("                     \033[34mMENU DE OPÇÕES\033[m                     ")
        print("-" * 65)
        print("\nE- Enviar um feedback\nV- Visualizar seus feedbacks\nD- Deletar conta\nF- Finalizar atendimento\n")
    
    def menu_feedbacks (self):
    
        #exibição do menu de opções dos tipos de feedbacks
        print("-" * 65)
        print("                   \033[34mOPÇÕES DE FEEDBACK\033[m               ")
        print("-" * 65)
        print("\nR- Reclamações\nE- Elogios\nS- Sugestões para melhorias\n")
    
    def menu_atendente (self):
        
        time.sleep(3)
                        
        print("-" * 65)
        print("                     \033[34mMENU DE OPÇÕES\033[m                      ")
        print("-" * 65) 
        print("\nE-Exibir lista de feedbacks por usuário.\nC-Concluir processo de feedback.\nv-Voltar ao menu principal.\nF-Finalizar expediente.\n")