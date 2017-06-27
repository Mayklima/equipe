#coding: utf-8

from aluno import aluno1

class equipe1:
    def __int__(self, projeto):
        self.projeto = projeto

    def cadastrarAluno(self):
        self.listaAluno = []

        while True:

            print("\n===== seja bem vindo =====")

            print("\n1 - adicionar(aluno)")
            print("2 - remove(aluno)")
            print("3 - imprimir(cadastrados)")
            print("4 - sair")


            p = int(raw_input("\ndigite uma das opcoes acima: "))

            if p == 1:
                while True:
                    print("\n===== adicionar aluno ======")

                    nome1 = raw_input("\ninforme o nome do aluno: ")
                    cpf1 = int(raw_input("informe o CPF do aluno: "))

                    existe = False
                    if len(self.listaAluno) == 0:
                        alu = aluno1(nome1,cpf1,self.listaAluno)
                        self.listaAluno.append(alu)

                        print("\n%s cadastrado(a) com sucesso" % (nome1))
                    else:
                        for x in range(len(self.listaAluno)):
                            if self.listaAluno[x] == nome1:
                                existe = True
                                print("\nja cadastrado")
                        if existe == False:
                            alu = aluno1(nome1, cpf1, self.listaAluno)
                            self.listaAluno.append(alu)

                            print("\n%s cadastrado(a) com sucesso" % (nome1))

                    p1 = raw_input("\ndeseja adicionar outro aluno? Sim/Nao: ")

                    if p1.upper() == "SIM":
                        continue
                    elif p1.upper() == "NAO":
                        break
                    else:
                        print("invalido")
                        continue

            elif p == 2:
                while True:
                    print("\n===== remover aluno =====")

                    nome2 = raw_input("\ninforme o nome do aluno: ")

                    for y in range(len(self.listaAluno) + 1):
                        if self.listaAluno[y].getNome() == nome2:
                            self.listaAluno.remove(self.listaAluno[y])
                            print("\nremovido com sucesso")
                            break

                    p2 = raw_input("\ndeseja remover outro aluno? Sim/Nao: ")

                    if p2.upper() == "SIM":
                        continue
                    elif p2.upper() == "NAO":
                        break
                    else:
                        print("invalido")
                        continue

            elif p == 3:
                print("\n====== alunos cadastrados =====")
                for x in range(len(self.listaAluno)):
                    print("\n%d) Nome: %s | CPF: %d" %(x+1, self.listaAluno[x].getNome(), self.listaAluno[x].getCPF()))
            else:
                print("invalido")
                continue

eq = equipe1()
eq.cadastrarAluno()