import psycopg2 as db

class Config:
    
    def __init__(self ):
        
        self._config = {"postgres" : {"host" : "localhost", "user" : "postgres","database" : "Ouvidoria", "password" : "clansofbr1"}}



class connection(Config):
    
    def __init__(self):
        
        Config.__init__(self)
        
        try:
            
            self.conn = db.connect(**self._config["postgres"])
            
            self.cur = self.conn.cursor()
        
        except Exception as e:
            
            print("Erro na conexão", e)
            exit(1)
    
    def __enter__ (self):
        return self
    
    def __exit__(self):
        self.connection.close()

    @property
    def connection (self):
        
        return self.conn

    @property
    def cursor (self):
        
        return self.cur  

    def commit (self):
        
        self.connection.commit()
    
    def fetchall (self):
        
        return self.cursor.fetchall()
    
    def execute (self, sql, params = None):
        
        self.cursor.execute(sql, params or ())
    
    def query (self,sql,params = None):
        
        self.cursor.execute(sql,params or ())
        
        return self.fetchall()


class ManipulacaoDados(connection):

    def __init__(self):
        
        connection.__init__(self)

    def insert (self, *args):

        try:
            sql = f"INSERT INTO usuario (id, nome, senha, reclamação, elogio, sugestão ) VALUES (%s,%s, %s,%s, %s, %s);"

            self.execute(sql, args)

            self.commit()

        except Exception as e:

            print("Erro ao inserir", e)

    def delete (self, id):
        try: 
            sql_s ="SELECT * FROM Usuario WHERE id = %s;"

            if not self.query(sql_s,(id, )):

                return "Registro não encontrado para deletar"

            sql_d = "DELETE FROM Usuario WHERE id = %s;"
            
            self.execute(sql_d,(id, ))
            self.commit()
            print("Conta deletada.")
        except Exception as e:
            
            print("Erro ao deletar", e)
    
 
        
    def atualizar_reclamacao (self,id,reclamacao):
        try:
            self.execute("UPDATE usuario SET reclamação = %s WhERE id = %s;",(reclamacao,id))
            self.commit()
        except Exception as e:
            print("Erro atualizar",e)

    def atualizar_elogio (self,id,elogio):
        try:
            self.execute("UPDATE usuario SET elogio = %s WhERE id = %s;",(elogio,id))
            self.commit()
        except Exception as e:
            print("Erro atualizar",e)
    
    def atualizar_sugestao (self,id,sugestao):
        try:
            self.execute("UPDATE usuario SET sugestão = %s WhERE id = %s;",(sugestao,id))
            self.commit()
        except Exception as e:

            print("\nErro atualizar",e)

    #função para um usuario especifico
    def find_one (self,id):
        sql = "SELECT * FROM Usuario Usuario WHERE id = %s;" 
        
        if not self.query(sql,(id, )):
            
            return "\nO usuario não existe"
        else:
            self.execute(sql,(id, ))
            self.commit()
            return self.fetchall()
    
    #função de busca
    def find_all (self):
        
        self.execute("SELECT * FROM usuario;")
        
        return self.fetchall()
    
    def verificar_usuario (self,id,senha):
        
        sql = "SELECT * FROM Usuario Usuario WHERE id = %s;" 
        
        if not self.query(sql,(id, )):
            
            return "\nUsuario não encontrado"
        else:
            sql_d = "SELECT * FROM Usuario Usuario WHERE senha = %s;"
            
            if not self.query(sql_d,(senha, )):
                
                return "\nSenha incorreta"
            else:
                return True
        self.commit()
    
    def print_user (self):
        
        lista = self.find_all()
        
        for user in lista:
            
            print("Usuario: {}".format(user[0]))
       
    
    def print_feedbacks (self,id):
        
        lista = self.find_one(id)

        print("Reclamação: {}".format(lista[0][3]))

        print("Elogio: {}".format(lista[0][4]))
        
        print("Sugestão: {}".format(lista[0][5]))
