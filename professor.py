from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, id_pessoa):
        super().__init__(nome, id_pessoa)
        self.turmas = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)