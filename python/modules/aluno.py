from winreg import QueryValue

from modules.mysql import MySQL

class Aluno:
  def __init__(self, nome, email, cpf, telefone, endereco):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.matricula = True
        
        def self(self, db:MySQL):
         query = """
            INSERT INTO alunos (
                nome,
                email,
                cpf
                telefone,
                endereco,
            ) VALUES (
            
            )
            """
            
        values = (
            self.nome,
            self.email,
            self.cpf,
            self.telefone,
            self.endereco
        )
        
        
        return db.execute_query(Query, values)
    
        def listar(db: MySQL):
          query = """
        SELECT
        id,
        nome,
        email,
        cpf,
        telefone,
        endereco,
        matricula
        
        FROM alunos
        
        """
        
        return db.execute_query(query)
    
        def editar(self):
          pass
    
        def transferir(self):
          pass