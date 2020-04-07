def linha(número_linhas=55):
    return "-" * número_linhas  # Estilo


def cabeçalho(texto):
    """Essa função faz seu cabeçalho recebendo o texto que você
    escreveu"""
    print(linha())
    print(texto.center(45))
    print(linha())


def menu(*args):
    """Essa Função cria o menu com as opção de escolha"""
    Numero_opcao = 1
    Lista_Menu = args
    for elementos in Lista_Menu:
        print(f"[{Numero_opcao}] - {elementos}")
        Numero_opcao += 1


def CheckBancoDeDados(Banco_de_Dados):
    """Essa função verifica se há um banco de dados, se não tiver ela
    cria"""
    try:
        Arquivo = open(Banco_de_Dados, "r")
        Arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriadorDeArquivos(Banco_de_dados):
    """Essa função chama a função CheckBancoDeDados e caso não haver
    arquivos ela cria um
    arquivo chamdo BandoDeDados.txt"""
    if CheckBancoDeDados("BancoDeDados.txt") == True:
        return None
    else:
        Arquivo = open(Banco_de_dados, "w+")
        Arquivo.close()


def CriarEvento(Banco, Nome_evento, Preço_Evento):
    """Essa função cria um novo evento recbendo o nome e o preço do
    evento"""
    try:
        Arquivo = open(Banco, "a")
    except:
        print("Erro ao abrir arquivo")
    else:
        Arquivo.write(f"{Nome_evento}:{Preço_Evento}\n")
        print(linha())
        print(f"O evento {Nome_evento} foi adicionado com sucesso.")
        Arquivo.close()


def LerArquivo(Banco_de_dados):
    """Essa função le o banco de dados"""
    try:
        Arquivo = open(Banco_de_dados, "rt")
    except:
        print(linha())
        print("Erro ao ler o Banco de Dados")
    else:
        for Elementos in Arquivo:
            Dados = Elementos.split(":")
            Dados[1] = Dados[1].replace("\n", " ")
            print(f"Nome do evento: {Dados[0]:<20}Preço R$: {Dados[1]}")
    Arquivo.close()


def AlterarEvento(nome_do_evento, valor_do_evento, novo_valor):
    # Essa função coloca os elementos do arquivo em uma lista e faz uma
    # troca para novo valor
    Arquivo = open("BancoDeDados.txt", "r")
    Lista = Arquivo.readlines()
    Evento = str(nome_do_evento) + ":" + str(valor_do_evento) + "\n"
    new_evento = str(nome_do_evento) + ":" + str(novo_valor) + "\n"
    Index = ProcuraIndice(nome_do_evento, valor_do_evento)
    for c in Lista:
        if c == Evento:
            Trocado = c.replace(Evento, new_evento)
            Lista.insert(Index, Trocado)
            Lista.pop(Index + 1)
            return Lista
    return False
    Arquivo.close()


def TrocarEvento(nome_do_evento, valor_do_evento, novo_valor):
    """Esssa função pega os dados de AlterarEvento e coloca no novo
    arquivo atualizado"""
    Novo_evento = AlterarEvento(nome_do_evento, valor_do_evento, novo_valor)
    if Novo_evento == False:
        print(linha())
        return "Erro...Evento não existe ou Valor do evento é incorreto"
    else:
        Arquivo = open("BancoDeDados.txt", "w")
        for Elemento in Novo_evento:
            Arquivo.write(Elemento)
        print(linha())
        return "Evento alterado com sucesso"
        Arquivo.close()


def ProcuraIndice(nome_do_evento, valor_do_evento):
    """Essa função analisa o indice do evento"""
    Arquivo = open("BancoDeDados.txt", "r")
    Lista = Arquivo.readlines()
    Evento_modificado = str(nome_do_evento) + ":" + str(valor_do_evento) + "\n"
    try:
        Index = Lista.index(Evento_modificado, 0, len(Lista))
        return Index
    except ValueError:
        return "Erro"


def Deleta():
    Arquivo = open("BancoDeDados.txt", "w")
    Arquivo.close()
