
from Usuario import Usuario

from feeddbacks import feedbacks #Importação da class Usuario

from menu import Menu

from Database import ManipulacaoDados, connection,Config

from atendente import Atendente

Atendente1 = Atendente ()

menu1 = Menu ()

Usuario1 = ManipulacaoDados ()

feedbacks1 = feedbacks ()

MenuAtendente = "a"

MenuUsuario = "m"

menu1.boas_vindas()

EncerrarExpediente = "N"

while EncerrarExpediente != "S":

    menu1.menu_principal()
    
    MenuPrincipal = input("Informe o tipo de acesso: ")
    
    if MenuPrincipal == "U":
        
        menu1.menu_acesso ()

        MenuAcesso = input("Informe a opção que deseja: ")

        if MenuAcesso == "Q":

                Cadastro = Usuario ()
                
                Cadastro.id = input("Crie um id: ")
                
                Cadastro.nome = input("Informe seu nome completo: ")
                
                Cadastro.senha = input("Crie uma senha: ")

                Usuario1.insert(Cadastro.id, Cadastro.nome, Cadastro.senha, feedbacks1.reclamcao, feedbacks1.Elogio, feedbacks1.Sugestao)
                
                print("\nvocê foi cadastrado com sucesso.\nAgora acesse como um usuario já cadastrado!")
        
        elif MenuAcesso == "J":
            
            Id_usuario = input("Informe seu id: ")
            
            senha_usuario = input("Informe sua senha: ")
            
            verifica = Usuario1.verificar_usuario (Id_usuario,senha_usuario)
            
            MenuUsuario = "m"
            
            if verifica == True:
                    
                while MenuUsuario != "F":

                    menu1.menu_usuario()

                    MenuUsuario = input("Informe a opção que deseja: ")
                
                    if MenuUsuario == "E":
                        
                        menu1.menu_feedbacks()

                        TipoFeedbacks = input("Informe o tipo de feedbacks: ")

                        if TipoFeedbacks == "R":
                            
                            Reclamacao = input("Digite aqui sua reclamação: ")
                                
                            Usuario1.atualizar_reclamacao(Id_usuario,Reclamacao)
                            
                        elif TipoFeedbacks == "E":
                                
                            Elogio = input("Digite aqui seu elogio: ")
                                
                            Usuario1.atualizar_elogio(Id_usuario, Elogio)
                            
                        elif TipoFeedbacks == "S":

                            Sugestao = input ("Digite aqui sua sugestão: ")

                            Usuario1.atualizar_sugestao (Id_usuario, Sugestao)
                        
                    
                    elif MenuUsuario == "V":
                            
                        Usuario1.print_feedbacks(Id_usuario)                            
                        
                    
                    elif MenuUsuario == "D":

                        Usuario1.delete(Id_usuario)
                            
                        MenuUsuario = "F"
                
            
            else:
                print(verifica)
          

                
    
    elif MenuPrincipal == "A":
        
        SenhaAtendente = input("Digite a senha: ")
        
        MenuAtendente = "a"
        
        if Atendente1.senha_atendente(SenhaAtendente) == True:
        
            while MenuAtendente != "V":
                
                menu1.menu_atendente()

                MenuAtendente = input("Informe  a opção que deseja: ")

                if MenuAtendente == "E":
                    lista = Usuario1.find_all()
                    
                    if len(lista) == 0:
                        
                        print('O sistema não possui usuarios cadastrados.')
                    
                    else:

                        Usuario1.print_user()

                        Id_usuario1 = input("Informe o usuario para vizualiar seus feedbacks: ")
                        
                        Usuario1.print_feedbacks(Id_usuario1)
                    
                elif MenuAtendente == "C":
                    
                    lista = Usuario1.find_all()

                    if len(lista) == 0:
                        
                        print('O sistema não possui usuarios cadastrados.')
                    
                    else:
                        Usuario1.print_user()

                        Id_usuario2 = input("Informe o usuario para vizualiar seus feedbacks: ")
                        
                        Usuario1.print_feedbacks(Id_usuario2)

                        menu1.menu_feedbacks()

                        TipoFeedbacks = input("Informe o feedbacks a ser removido: ")
                        
                        print("")
                        
                        if TipoFeedbacks == "R":
                                
                            Reclamacao = ("")
                                    
                            Usuario1.atualizar_reclamacao(Id_usuario2,Reclamacao)
                                
                        elif TipoFeedbacks == "E":
                                    
                            Elogio = ("")
                                    
                            Usuario1.atualizar_elogio(Id_usuario2, Elogio)
                                
                        elif TipoFeedbacks == "S":

                            Sugestao = input ("")

                            Usuario1.atualizar_sugestao (Id_usuario2, Sugestao)
                
                elif MenuAtendente == "F":
                    
                    MenuAtendente = "V"
                    EncerrarExpediente = "S"  
                    
        else:
            print("\nSenha incorreta.")
Usuario1.__exit__()