#importação de lista de alunos e professores
from listas import alunos, professores
# criando objetos
class Escola():
    def __init__(self, nome, email, turma, turno):
        self.nome = nome.title()
        self.email = email
        self.turma = turma
        self.turno = turno.title()

    def __str__(self):
        return f' nome:  {self.nome.__str__()} \n email: {self.email.__str__()} \n turma: {self.turma.__str__()} \n turno: {self.turno.__str__()}'
#validação de email escolar
    def validacao(self):

        indice_base = self.email.find('@')
        indice_parametro = self.email[indice_base:]
        parametro_email = '@escola.pr.gov.br'
        if parametro_email != indice_parametro:
            while parametro_email != indice_parametro:
                print('Email inválido')
                print('exemplo de email escolar: xxxxxx@escola.pr.gov.br')
                self.email = input('Este email não é escolar,por gentileza ensira o email escolar: ')
                indice_base = self.email.find('@')
                indice_parametro = self.email[indice_base:]
            return self.email
        else:
            return self.email

# criando dados do aluno
class Aluno(Escola):
    def __init__(self, nome, email, turma, turno, cgm, status):

        super().__init__(nome, email, turma, turno)
        self.cgm = cgm
        self.status = status
        self.email = super().validacao()

    def __str__(self):
        return f'\n ---Aluno--- \n' + super().__str__() + f'\n CGM: {self.cgm} \n Status: {self.status} '

# criando dados do professor
class Professor(Escola):
    def __init__(self, nome, email, turma, turno):

        super().__init__(nome, email, turma, turno)
        self.email = super().validacao()

    def __str__(self):
        return f'\n ---Professor--- \n' + super().__str__()

#fazendo cadastramento do úsuario (professor ou aluno)
def Cadastramento():
    print('Cadastramento de Aluno(1) Cadastramento de Professor(2)')
    servico_escolhido = int(input('Digite o número do serviço desejado :'))
    if servico_escolhido == 1:
        cadastrado = Aluno(input('Nome Completo: '),
                input('Email Escolar: '),
                input('Série atual: '),
                input('Turno (Matuino , Vespertino , Noturno) :'),
                input('Número de CGM: '),
                input('Ativo ou Inativo:'))
        alunos.append(cadastrado)

    else:
         cadastrado = Professor(input('Nome Completo: '),
                input('Email Escolar: '),
                input('Série atual que atua : '),
                input('Turno (Matuino , Vespertino , Noturno) :'))

    print(cadastrado)
    return cadastrado
#abertura da plataforma
def Bemvindo():
    print('------Seja Bem-Vindo a Alura-----')
    print('      Serviços disponiveis       ')
    print(f'Cadastro em Geral (1)\ninformações sobre alunos (2)\ninformações sobre professores (3): \n')

#informações dos alunos matriculados
def lista_alunos():
    print('----Alunos Matriculados---- ')
    print(f' 1 - Renan Tonon    4 - Laura Sandres - 7 - Amanda Rodrigues\n'
          f' 2 - Lucas Gomes    5 - Marcos Vinicius 8 - Sergio Passos\n' 
          f' 3 - Maria Vitoria  6 - Kauan Teodoro \n')
    num = int(input('selecione o número do aluno para mais informações :\n '))
    for n in range(0, num):
        x = 0
        while x != 1:
            estudantes = Aluno(alunos[n][x], alunos[n][x+1], alunos[n][x+2], alunos[n][x+3], alunos[n][x+4], alunos[n][x+5] )
            x = x + 1
    print(estudantes)
    modifica_status(estudantes)
    print(estudantes)
#informações sobre os professores
def lista_professores():
    print('----Professores Matriculados---- ')
    print(f' 1 - Matheus Yamada 2 - Yumi kurumi \n')
    numr = int(input(f'Selecione o número do professor para mais informações : '))
    for n in range(0, numr):
        x = 0
        while x != 1:
            funcionarios = Professor(professores[n][x], professores[n][x + 1], professores[n][x + 2], professores[n][x + 3])
            x = x + 1
    print(funcionarios)
    print(f'-------Professores-------\nMatheus yamada(1) Yumi kurumi(2)')
    qual_professor = int(input('Listar a turmas de qual professor: \n'))
    if qual_professor == 1:
        for c in alunos:
            if c[3] == 'Matutino':
                print(f'Nome: {c[0]} Turma:{c[2]}')
            else:
                continue
    elif qual_professor == 2:
        for c in alunos:
            if c[3] == 'Vespertino':
                print(f'Nome: {c[0]} Turma:{c[2]}')
            else:
                continue
    else:
        print('Encerrando......')
#alteração de status do aluno
def modifica_status(self):
    aluno_stutus = input('\ndeseja Alterar o Status desse aluno s/n : ')
    if aluno_stutus == 's':
        alterar = int(input('Alterar status do aluno para ativo(1) ou inativo(2): '))
        if alterar == 1:
            self.status = 'Ativo'
        else:
            self.status = 'Inativo'
    else:
        print('saindo do perfil......')
#unificando serviços
def plataforma():
    proceguir = 0
    while proceguir != 1:
        Bemvindo()
        opcao_escolhida = int(input('Digite o numero da opção escolhida: '))
        if opcao_escolhida == 1:
            Cadastramento()
            print('\nFinalizando cadastramento.....')
            proceguir = int(input('Deseja continuar na plataforma Sim(0) Não(1): '))

        elif opcao_escolhida == 2:
            lista_alunos()
            print('\nEncerrando leitura de informação.....')
            proceguir = int(input('Deseja continuar na plataforma Sim(0) Não(1): '))
        else:
            lista_professores()
            print('\nEncerrando informação.....')
            proceguir = int(input('Deseja continuar na plataforma Sim(0) Não(1): '))
    print('\nFinalizando Serviços.....')
plataforma()