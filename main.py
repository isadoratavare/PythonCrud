from funcoes import Cadastro,alterar,deletar,consultar,inv,atadeexercicio
while True:
    print('     Bem-vindo(a) ao Sistema de Controle Acadêmico!      ')
    n = int(input('\n 1. Professor(es)\n 2. Alunos(as)\n 3. Disciplinas\n 4. Turmas\n 5. Sair\n Acessar:  '))
    if n == 5:
        break
    elif n == 1:
        m = int(input('\n 1.Cadastrar\n 2.Alterar\n 3.Deletar\n 4.Consultar\n 5.Sair\n Ação que deseja executar: '))
        if m == 1:
            Cadastro(n)
        elif m == 2:
            alterar(n)
        elif m == 3:
            deletar(n)
        elif m==4:
            consultar(n)
        elif m==5:
            break
        else:
            inv()
    elif n == 2:
        m = int(input('\n 1.Cadastrar\n 2.Alterar\n 3.Deletar\n 4.Consultar\n 5.Sair\n Ação que deseja executar: '))
        if m == 1:
            Cadastro(n)
        elif m == 2:
            alterar(n)
        elif m==3:
            deletar(n)
        elif m==4:
            consultar(n)
        elif m==5:
            break
        else:
            inv()
    elif n == 3:
        m = int(input('\n 1.Cadastrar\n 2.Alterar\n 3.Deletar\n 4.Consultar\n 5.Sair\n Ação que deseja executar: '))
        if m == 1:
            Cadastro(n)
        elif m == 2:
            alterar(n)
        elif m == 3:
            deletar(n)
        elif m==4:
            consultar(n)
        elif m==5:
            break
        else:
            inv()
    elif n==4:
        m = int(input('\n 1.Cadastrar\n 2.Alterar\n 3.Deletar\n 4.Consultar\n 5.Visualizar Ata\n 6.Sair\n Ação que deseja executar: '))
        if m == 1:
            Cadastro(n)
        elif m == 2:
            alterar(n)
        elif m==3:
            deletar(n)
        elif m==4:
            consultar(n)
        elif m==5:
            atadeexercicio()
        elif m ==6:
            break
    else:
        inv()
