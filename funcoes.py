def inv():  # Codigo Invalido
    print('Código inválido')


def Cadastro(n):
    if n == 1:  # cadastro do professor
        while True:
            professores = open('professores.txt', 'a')  # dados do professor
            nome = str(input('\n Nome:'))  # nome do professor
            cpfdoprofessor = str(input(' CPF(apenas numeros):'))  # cpf do professor
            professores.close()
            professores = open('professores.txt', 'r')
            for linha in professores.readlines():
                if linha.find(str(cpfdoprofessor)) != -1:
                    print('\nCpf já cadastrado. Inicie novamente o cadastro.')  # verificando se o cpf já foi adicionado no sistema
                    break
            else:
                professores = open('professores.txt', 'a')
                departamento = str(input(' Departamento:'))  # departamento do professor
                professores.write('Nome: %s,CPF: %s ,Departamento: %s\r' % (nome, cpfdoprofessor, departamento))  # escrevendo no arquivo professores as informamações
                print('\nO professor foi cadastrado')
                professores.close()
            while True:
                a = int(input('''\n Digite:\n 1.Cadastrar outro professor.\n 2.Voltar.\n'''))
                if a != 1 and a != 2:
                    inv()
                if a == 2 or a == 1:
                    break
            if a==2:
                break

    elif n == 2:  # cadastro de alunos
        while True:
            # dados do aluno
            alunos = open('alunos.txt', 'a+')
            nome = str(input('Nome:'))
            cpfaluno = int(input('CPF(apenas numeros:'))
            # analisando se o cpf ja esta cadastrado
            lista = alunos.readlines()
            for linha in lista:
                if linha.find(str(cpfaluno)) != -1:
                    print('\nCpf já cadastrado.')
                break
            else:
            #adicionando as informações ao arquivo alunos.txt
                alunos.write('Nome: %s,CPF: %s \r' % (nome, cpfaluno))
                alunos.close()
            a = int(input('''\n 1.Cadastrar outro aluno.\n 2.Voltar.\n Digite:'''))
            if a != 1 and a != 2:
                inv()
            if a == 2:
                break

    elif n == 3:  # cadastro de disciplina
        while True:
            disciplinas = open('disciplinas.txt', 'a+')
            #dados da disciplina
            nomed = str(input('Nome da disciplina:'))
            codigod = str(input('Código da disciplina:'))
            lista = disciplinas.readlines()
            for linha in lista:#vereficando se disciplina já foi cadastrada
                if linha.find(str(codigod)) != -1:
                    print('\nCódigo já cadastrado, Inicie novamente.')
                    break
            else:
                #colocando os dados no arquivo disciplinas.txt
                disciplinas.write('Código: %s, Nome da disciplina: %s \r' % (codigod, nomed))
                disciplinas.close()
                while True:
                    a = int(input('''\n 1.Cadastrar mais uma disciplina.\n 2.Voltar.\n Digite: '''))
                    if a == 1 or a == 2:
                        break
                    else:
                        inv()
                if a == 2:
                    break
    elif n == 4:  # cadastro de turma
        while True:
            codigoo = str(input('Código da turma:'))  # codigo da nova turma
            tturmas = open('tturmas.txt', 'a')
            tturmas.close()
            tturmas = open('tturmas.txt', 'r')  # arquivo todas as turmas
            lista = tturmas.readlines()
            for linha in lista:  # verificar se turma ja foi cadastrada
                if linha.find(str(codigoo)) != -1:
                    print('\nTurma já cadastrada.')
                    break
            else:
                tturmas = open('tturmas.txt', 'a')  # Adicionando nova turma
                tturmas.write('%s \n' % codigoo)
                periodo = str(input('Periodo:'))
                coddis = str(input('Código da disciplina:')) #adicionando disciplina a turma
                disciplinas = open('disciplinas.txt', 'r')
                lista = disciplinas.readlines()
                for linha in lista: #verificando se a disciplina já foi adicionada a turma e se ela existe no sistema.
                    if linha.find(str(coddis)) != -1:
                        novaturma = open('%s .txt' % codigoo, 'a')  # abrindo arquivo com nova turma
                        novaturma.write('Código: %s Periodo: %s \n' % (codigoo, periodo))  # adicionando o codigo e o periodo
                        tturmas.close()
                        novaturma.write('Disciplina: %s\n' % coddis)
                        print('\nDisciplina adicionada a turma.')
                        novaturma.close()
                        break
                else:
                    print('\nDisciplina não cadastrada no sistema.')
            while True:
                o = int(input('\n 1.Professor\n 2. Aluno \n 3.Voltar\n Escolha a opção para adicionar a turma:'))
                if o == 1: #Adicionando professor a turma
                    while True:
                        cpfprofessor = str(input('Cpf do professor(apenas numeros):'))  # adicionando o professor a turma por cpf
                        professores = open('professores.txt', 'r')
                        lista = professores.readlines()
                        for linha in lista:
                            if linha.find(str(cpfprofessor)) != -1:#verificando se o professor já ta na turma e se ele exsite no sistema
                                novaturma = open('%s .txt' % codigoo, 'r')
                                lista = novaturma.readlines()
                                for linha in lista:
                                    if linha.find(cpfprofessor) != -1:
                                        print('\nProfessor já cadastrado na turma.')
                                        break
                                else:
                                    novaturma = open('%s .txt' % codigoo, 'a')
                                    novaturma.write('Professor: %s\n' % cpfprofessor)
                                    print('\nProfessor adicionado a turma')
                                    novaturma.close()
                                    break
                        else:
                            print('\nProfessor não cadastrado no sistema.')
                        a = int(input('\n 1.Adicionar mais um professor.\n 2.Voltar.\n Digite:'))
                        if a == 2:
                            break
                        elif a!=1 and a!=2:
                            inv()
                elif o == 2: #Adicionando aluno a turma
                    while True:#dados do aluno
                        cpfdoaluno = str(input('Cpf do aluno(apenas numeros):'))
                        aluno = open('alunos.txt', 'r')
                        lista = aluno.readlines()
                        for linha in lista:
                            if linha.find(str(cpfdoaluno)) != -1: #verificando se o aluno ta cadastrado no sistemae e se ele já esta na turma.
                                novaturma = open('%s .txt' % codigoo, 'r')
                                lista = novaturma.readlines()
                                for linha in lista:
                                    if linha.find(cpfdoaluno) != -1:
                                        print('\nAluno já cadastrado na turma.')
                                        break
                                else:
                                    novaturma = open('%s .txt' % codigoo, 'a')#adicionando dados do aluno a turma
                                    novaturma.write('Aluno: %s \r' % cpfdoaluno)
                                    print('\nAluno adicionado a turma.')
                                    break
                        else:
                            print('\nAluno não cadastrado no sistema.')
                        while True:
                            a = int(input('''\n 1.Cadastrar mais um aluno.\n 2.Voltar.\n Digite:'''))
                            if a == 1 or a == 2:
                                break
                            else:
                                inv()
                        if a == 2:
                            break
                elif o == 3:
                    break
            if o == 3:
                break

def alterar(n):
    if n == 1:  # Alterar dados do professor
        while True:
            cpf = str(input('\nDigite o numero do cpf para pesquisar:')) #dados do professor para pesquisar
            professores = open('professores.txt', 'r')
            b = professores.readlines()
            for linha in b:
                if linha.find(str('CPF: %s' % cpf)) != -1: #procurando professor no sistema
                    print(linha)
                    print('\nCpf encontrado.')
                    professores = open('professores.txt', 'r')
                    listab = professores.readlines() #vendo a posição da linha com os dados do professor
                    linha = listab.index(linha)
                    listab.pop(linha) #excluindo linha antiga
                    professores.close()
                    atualizar = open('atualizar.txt', 'w') #limpando o arquivo
                    novonome = str(input('Digite o novo nome:')) #novas informações
                    novocpf = str(input('Digite novo cpf:'))
                    novodepartamento = str(input('Digite novo departamento:'))
                    atualizar.write('Nome: %s,CPF: %s ,Departamento: %s \r' % (novonome, novocpf, novodepartamento)) #adicionando novos dados em arquivo auxiliar
                    atualizar.close()
                    atualizar = open('atualizar.txt', 'r')
                    linhaatualizar = atualizar.readlines()
                    atualizar.close()
                    listab.insert(linha, linhaatualizar[0]) #mudando linha que queria no arquivo antigo
                    professores = open('professores.txt', 'w')
                    for i in listab: #adicionando todas as linhas com a linha alterada no arquivo anterior novamente
                        professores.write(i)
                    print('\nAlteração feita!')
                    break
            else:
                print('\nCpf não encontrado')

            while True:
                opcao = int(input('\n 1.Alterar novamente\n 2.Voltar'))
                if opcao == 2 or opcao ==1 :
                    break
                if opcao != 1 and opcao != 1:
                    print('\nOpção inválida.')
            if opcao == 2:
                break
    elif n == 2:  # Alterar dados do aluno
        while True:
            cpf = str(input('\nDigite seu cpf para pesquisarmos:')) #dados do aluno
            alunos = open('alunos.txt', 'r')
            b = alunos.readlines()
            for linha in b: #verificando se o aluno esta no sistema
                if linha.find(str('CPF: %s' % cpf)) != -1:
                    print('\nCadastro encontrado.')
                    alunos = open('alunos.txt', 'r')
                    listab = alunos.readlines()
                    linha = listab.index(linha) #vendo posição do cadastro do aluno
                    listab.pop(linha) # eliminando linha com o cadastro no aluno
                    alunos.close()
                    atualizar = open('atualizar.txt', 'w') #abrindo o arquivo atualizar limpo
                    novonome = str(input('Novo nome:')) #novos dados
                    novocpf = str(input('Novo cpf:'))
                    atualizar.write('Nome: %s CPF: %s \r' % (novonome, novocpf)) #adicionando novos dados ao arquivo atualizar
                    atualizar.close()
                    atualizar = open('atualizar.txt', 'r') #buscando linha atualizada
                    linhaatualizar = atualizar.readlines()
                    listab.insert(linha, linhaatualizar[0]) #colocando ela no arquivo anterior
                    alunos = open('alunos.txt', 'w') #abrindo o arquivo alunos limpos
                    for i in listab: #adicionando as linhas novamente com a linha atualizada
                        alunos.write(i)
                    print('\nAlteração feita.')
                    break
                else:
                    print('\nCpf não encontrado')
                    break
            while True:
                opcao = int(input('\n Digite\n 1.Alterar novamente\n 2.Voltar\n'))
                if opcao == 2 or opcao == 1:
                    break
                else:
                    inv()
            if opcao == 2:
                break

    elif n == 3:  # alterar disciplina
        while True:
            codigo = str(input('\nDigite o codigo da disciplina que deseja alterar:')) #dados da disciplina
            disciplinas = open('disciplinas.txt', 'r')
            b = disciplinas.readlines()
            for linha in b:
                if linha.find(codigo) != -1: #verificiando se disciplina está no sistema
                    print(linha)
                    print('\nDisciplina encontrada')
                    disciplinas = open('disciplinas.txt', 'r')
                    listad = disciplinas.readlines()
                    linha = listad.index(linha) #pegando posição da linha com os dados a serem alterados
                    listad.pop(linha) #apagando linha com dados antigos
                    disciplinas.close()
                    atualizar = open('atualizar.txt', 'w') #abrindo o arquivo atualizar vazio
                    novonome = str(input('Nome da disciplina(novo):')) #novos dados
                    novocodigo = str(input('Codigo(novo):'))
                    atualizar.write('Nome da disciplina: %s Codigo: %s\n' % (novonome, novocodigo)) #adicionando novos dados ao arquivo atualizar
                    atualizar.close()
                    atualizar = open('atualizar.txt', 'r')
                    linhaatualizar = atualizar.readlines()
                    listad.insert(linha, linhaatualizar[0]) #adicionando linha atualizada ao arquivo anterior
                    disciplinas = open('disciplinas.txt', 'w') #abrindo o arquivo disciplinas
                    for i in listad: # escrevendo linhas no arquivo disciplinas , com a linha atulizada.
                        disciplinas.write(i)
                    print('\nAlteração feita!')
                    break
            else:
                print('\nCodigo não encontrado')
            while True:
                opcao = int(input('\n 1.Alterar novamente\n 2.Voltar'))
                if opcao == 2:
                    break
                if opcao != 1 and opcao != 1:
                    print('\nOpção inválida.')
            if opcao == 2:
                break

    elif n == 4:  # alterar turma
        while True:
            tturmas = open('tturmas.txt', 'r')
            codigo = str(input('Digite o codigo da turma que deseja alterar:')) #dados da turma
            b = tturmas.readlines()
            for linha in b:
                if linha.find(codigo) != -1:
                    print('\nTurma encontrada')
                    tturmas = open('tturmas.txt', 'r')
                    listat = tturmas.readlines()
                    linha = listat.index(linha)
                    listat.pop(linha)
                    novocodigo = str(input('Código da turma(novo):'))
                    tturmas=open('tturmas.txt','w')
                    for i in listat:
                        tturmas.write(i)
                    novoperiodo = str(input('Periodo(novo):'))
                    novadisciplina = str(input('Codigo da Disciplina(nova):'))
                    disciplinas = open('disciplinas.txt', 'r')
                    lista = disciplinas.readlines()
                    for linha in lista:
                        if linha.find(novadisciplina) != -1:
                            novaturma = open('%s .txt'%codigo, 'w')
                            novaturma.write('Código: %s  Periodo: %s\n' % (novocodigo, novoperiodo))
                            novaturma.write('Disciplina: %s\n'%novadisciplina)
                            novaturma.close()
                            break
                    else:
                        print('\nDisciplina não cadastrada no sistema.')
                        break
                    while True:
                        o = int(input('\n 1.Adicionar professor.\n 2.Adicionar aluno.\n 3.Voltar\n Digite:\n'))
                        if o == 1:
                                    novaturma=open('%s .txt'%codigo,'a')
                                    cpfdoprofessor = str(input('Cpf do professor:'))
                                    professores = open('professores.txt', 'r')
                                    lista = professores.readlines()
                                    for linha in lista:
                                        if linha.find(cpfdoprofessor) == -1:
                                            print('\nProfessor não cadastrado no sistema.')
                                            break
                                    else:
                                        novaturma.write('Professor: %s\n' % cpfdoprofessor)
                                        novaturma.close()

                                    professores.close()
                        elif o == 2:
                                    novaturma=open('%s .txt'%codigo,'a')
                                    cpfdoaluno = str(input('Cpf do aluno:'))
                                    alunos = open('alunos.txt', 'r')
                                    lista = alunos.readlines()
                                    for linha in lista:
                                        if linha.find(cpfdoaluno) != -1:
                                            novaturma.write('Aluno: %s\n' % cpfdoaluno)
                                            novaturma.close()
                                            break
                                    else:
                                        print('\nAluno não cadastrado no sistema')
                        elif o == 3:
                            break
            while True:
                a=int(input('\n 1.Alterar outra turma.\n 2.Voltar\n'))
                if a==1 or a==2:
                    break
                else:
                    inv()
            if a==2:
                break

def deletar(n):
    if n == 1:  # PROFESSOR
        while True:
            cpfdoprofessor = str(input('Cpf do professor: '))
            professores = open('professores.txt', 'r')
            lista = professores.readlines()
            for linha in lista:
                if linha.find(cpfdoprofessor) != -1:
                    lista.pop(linha.index(linha))
                    professores=open('professores.txt','w')
                    for linha in lista:
                        professores.write(linha)
                    print('\nCadastro do professor removido.')
                    break
            else:
                print('\nProfessor não encontrado')
            professores.close()
            while True:
                a = int(input(' 1.Remover outro professor.\n 2.Voltar.\n Digite: '))
                if a == 1 or a == 2:
                    break
                else:
                    inv()
            if a==2:
                break
    elif n == 2:  # Aluno #concluido e testado
        while True:
            cpfdoaluno = str(input(' Cpf do aluno: '))
            alunos = open('alunos.txt', 'r')
            lista = alunos.readlines()
            for linha in lista:
                if linha.find(cpfdoaluno) != -1:
                    lista.pop(linha.index(linha))
                    alunos = open('alunos.txt', 'w')
                    for linha in lista:
                        alunos.write(linha)
                    print('\nCadastro de aluno removido')
                    break
            else:
                print('\nAluno não encontrado.')
            while True:
                a = int(input(' 1.Remover outro aluno.\n 2.Voltar\n Digite: '))
                if a == 1 or a == 2:
                    break
                else:
                    inv()
            if a==2:
                break
    elif n==3: #DISCIPLINA
        while True:
            codigodis= str(input('Codigo da disciplina: '))
            disciplinas = open('disciplinas.txt', 'r')
            lista = disciplinas.readlines()
            for linha in lista:
                if linha.find(codigodis) != -1:
                    lista.pop(linha.index(linha))
                    disciplinas = open('disciplinas.txt', 'w')
                    for linha in lista:
                        disciplinas.write(linha)
                    print('\n Cadastro de disciplina removido.')
                    break
            else:
                print('\n Disciplina não encontrada.')
            while True:
                a=int(input(' 1.Remover outra disciplina.\n 2.Voltar.\n Digite: '))
                if a==1 or a==2:
                    break
                else:
                    inv()
            if a==2:
                break
    elif n==4: #TURMA
        while True:
            codigotur= str(input('Codigo da turma: '))
            tturmas= open('tturmas.txt', 'r')
            lista = tturmas.readlines()
            for linha in lista:
                if linha.find(codigotur) != -1:
                    lista.pop(linha.index(linha))
                    tturmas = open('tturmas.txt', 'w')
                    for linha in lista:
                        tturmas.write(linha)
                    print('\n Turma excluída.')
                    break
            else:
                print('\n Turma não encontrada.')
            while True:
                a=int(input('\n Digite:\n 1.Remover outra turma.\n 2.Voltar: \n'))
                if a ==1 or a==2:
                    break
                else:
                    inv()
            if a==2:
                break

def consultar(n):
    if n == 1: #PROFESSOR
        while True:
            cpfdoprofessor = str(input('Cpf do professor: '))
            professor = open('professores.txt', 'r')
            lista = professor.readlines()
            for linha in lista:
                if linha.find(cpfdoprofessor) != -1:
                    print(linha)
                    break
            else:
                print('\nProfessor não encontrado')
            while True:
                a = int(input(' 1.Consultar outro professor.\n 2.Voltar.\n Digite: '))
                if a == 1 or a == 2:
                    break
                else:
                    inv()
            if a==2:
                break
    elif n==2: #Aluno
        while True:
            cpfdoaluno = str(input('Cpf do aluno: '))
            aluno = open('alunos.txt', 'r')
            lista = aluno.readlines()
            for linha in lista:
                if linha.find(cpfdoaluno) != -1:
                    print(linha)
                    break
            else:
                print('\nAluno não encontrado.')
            while True:
                a = int(input('\n 1.Consultar outro aluno.\n 2.Voltar\n Digite: '))
                if a == 1 or a == 2:
                    break
                else:
                    inv()
            if a==2:
                break

    elif n==3: #Disciplina
        while True:
            codigodis=str(input(' Codigo da disciplina: '))
            disciplinas=open('disciplinas.txt','r')
            lista= disciplinas.readlines()
            for linha in lista:
                if linha.find(str(codigodis)) !=-1:
                    print(linha)
                    break
            else:
                print('\nDisciplina não encontrada.')
            while True:
                a=int(input('\n 1.Consultar outra disciplina.\n 2.Voltar.\n Digite:\n '))
                if a==1 or a==2:
                    break
                else:
                    inv()
            if a ==2:
                break
    elif n==4: #Turma
        while True:
            codigotur = str(input('\nCodigo da turma:'))
            tturmas = open('tturmas.txt', 'r')
            lista = tturmas.readlines()
            for linha in lista:
                if linha.find(codigotur) != -1:
                    turma= open('%s .txt'%codigotur)
                    lista=turma.readlines()
                    for linha in lista:
                        print(linha)
                    break
            else:
                print('\nTurma não encontrada.')

            while True:
                a = int(input('\n 1.Consultar outra turma.\n 2.Voltar\n Digite: '))
                if a == 1 or a == 2:
                    break
                else:
                    inv()
            if a ==2:
                break

def atadeexercicio():
    while True:
        codigo=str(input('Codigo da Turma:')) #codigo da turma
        tipodeata=str(input('Tipo de Ata: '))
        tturmas=open('tturmas.txt','r')
        t=tturmas.readlines()
        for linha in t:
            if linha.find(codigo)!=-1:
                turma=open('%s .txt'%codigo,'r') #abrindo o arquivo turma
                lista=turma.readlines()
                print('Ata de %s'%tipodeata)
                for i in lista:
                    print(i)
            break
        else:
            print('Turma não encontrada')
        while True:
            a = int(input('''\n Digite:\n 1.Visualizar outra Ata.\n 2.Voltar.\n'''))
            if a != 1 and a != 2:
                inv()
            if a == 2 or a == 1:
                break
        if a==2:
            break

