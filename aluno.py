#coding: utf-8

class aluno1:
    def __init__(self, nome, CPF, listaAluno):
        self.nome = nome
        self.CPF = CPF

    def getNome(self):
        return self.nome
    def setNome(self, nome2):
        self.nome = nome2

    def getCPF(self):
        return self.CPF