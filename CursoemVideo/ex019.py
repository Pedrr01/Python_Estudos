from random import choice
al1 = input('Digite o nome do aluno:')
al2 = input('Digite o nome do aluno:')
al3 = input('Digite o nome do aluno:')
al4 = input('Digite o nome do aluno:')
lista = [al1, al2, al3, al4]
print('O aluno escolhido foi: {}'.format(choice(lista)))
