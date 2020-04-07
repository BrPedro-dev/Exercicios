from Exercicios.Lib.funçoes import *

Banco = "BancoDeDados.txt"
CriadorDeArquivos(Banco)  # Faz a checagem se não houver, cria
cabeçalho("Sistema 1.0 para Eventos")  # Chama a função cabeçalho

while True:  # Main
    print(linha())
    menu("Cadastrar Novo Evento", "Listar Eventos", "Alterar Eventos",
         "Deletar todos eventos", "Sair")
    print(linha())
    Resposta = int(input("Qual é opção: "))
    print(linha())

    if Resposta == 1:

        cabeçalho("Novo Cadastro de Evento")
        nome_evento = str(input("Qual é nome do evento? "))
        preço_evento = str(input("Qual é o valor do ingresso em reais? "))
        CriarEvento(Banco, nome_evento, preço_evento)

    elif Resposta == 2:

        cabeçalho("Lista de eventos")
        print(linha())
        LerArquivo(Banco)
        print(linha())

    elif Resposta == 3:

        cabeçalho("Alterar Evento")
        print(linha())
        nome_do_evento = input("Digite o nome do Evento: ")
        valor_do_evento = input("Digite o valor atual do Evento: ")
        novo_valor = input("Digite o novo valor do evento: ")
        print(TrocarEvento(nome_do_evento, valor_do_evento, novo_valor))

    elif Resposta == 4:
        Deleta()

    elif Resposta == 5:
        break

    else:
        print("Erro...Resposta invalida")
