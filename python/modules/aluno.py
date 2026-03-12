from modules.mysql import MySQL

class Aluno:
    def __init__(self, nome, email, cpf, telefone, endereco):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.matricula = True

    def salvar(self, db: MySQL):
        query = """
        INSERT INTO alunos (
            nome,
            email,
            cpf,
            telefone,
            endereco,
            matricula
        ) VALUES (
            %s, %s, %s, %s, %s, %s
        )
        """

        values = (
            self.nome,
            self.email,
            self.cpf,
            self.telefone,
            self.endereco,
            self.matricula
        )

        return db.execute_query(query, values)

    @staticmethod
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

    def editar(self, db: MySQL, aluno_id: int):
        query = """
        UPDATE alunos SET
            nome = %s,
            email = %s,
            cpf = %s,
            telefone = %s,
            endereco = %s
        WHERE id = %s
        """

        values = (
            self.nome,
            self.email,
            self.cpf,
            self.telefone,
            self.endereco,
            aluno_id
        )

        return db.execute_query(query, values)

    @staticmethod
    def transferir(db: MySQL, aluno_id: int, nova_turma: int):
        query = """
        UPDATE alunos SET
            turma_id = %s
        WHERE id = %s
        """

        values = (nova_turma, aluno_id)
        return db.execute_query(query, values)
