class Atendente:
    
    def __init__(self,senha = "atendente120") -> None:
        
        self.__senha = senha
    
    def senha_atendente (self,senha):
        
        if self.__senha == senha:
            
            return True
        
        return False