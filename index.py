
exit = 0

def exibir_menu():
    while True:
        print("  Petshop Bom Amiguinho")
        print("1 - Cadastrar Dados.")
        print("2 - Listar Dados.")
        print("3 - Alterar Dados.")
        print("4 - Excluir Dados.")
        print("5 - Realizar backup do arquivo.")
        print("0 - Para encerrar o atendimento.")
        escolha = int(input("Escolha a opção que deseja realizar: "))
        
        if (escolha == 1):
            cadastrarDados()
        elif (escolha == 2):
            listar_dados()
        elif (escolha == 3):
            alterar_dados()
        elif (escolha == 4):
            excluirDados()
        elif (escolha == 5):
            realizarBackup()
        elif (escolha == exit):
            break
        else:
            print("Opção inválida. Digite um número corresponde ao menu.")
          
#CADASTRAR DADOS:
def cadastrarDados():
    try:
        #criando um arquivo txt
        with open("Dados.txt","a") as arquivo:
            #solicitar ao usuário as opções que ele deseja 
            codigo = int(input("Código do Cliente: "))
            nome = input("Nome do Responsável: ")
            contato =int(input("Contato: ")) #no caso do telefone ele define um numero x de caracteres e consegue colocar alem de numeros inteiros(pode colocar hifen)
            endereço = input("Endereço: ")
            pet = input("Nome do pet: ")
            print(nome, contato, endereço, pet)

            #formatar os dados do cliente em uma string
            clientes = f"{codigo}, {nome},{contato},{endereço},{pet}\n"
            print(clientes)

            #escrever os dados formatados no arquivo txt
            arquivo.write(clientes)

            #exibir uma mensagem de sucesso
            print("Ação realizada com sucesso!")
    except ValueError:
        #captar um erro, caso os dados informados pelo usuario não sejam condizentes com o input desejado
        print("Valor inválido! Certifique-se de digitar um valor condizente com o input desejado.")
    except Exception as e:
        #capturar qualquer outro erro que possa ecorrer em algum momento da aplicação 
        print("Ocorreu um erro ao realizar a ação desejada",str(e))

#ALTERAR DADOS
def alterar_dados():
    try:
        # Abrir o arquivo 'Dados.txt' em modo de leitura 'r'
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum dado de cliente cadastrado.")
            return

        # Aqui vai solicitar ao usuário o código do aluno que deseja alterar
        codigo_cliente = int(input("Digite o código do cliente que deseja alterar: "))
        encontrado = False

        for i in range(len(linhas)):
            # Dividir a linha em partes separadas por vírgulas e remover os espaços em branco
            dados = linhas[i].strip().split(', ')

            # aqui vai verificar se o código do cliente na linha atual corresponde ao código fornecido pelo usuário
            if int(dados[0]) == codigo_cliente:
                novo_codigo_cliente = int(input("Digite o novo código do cliente: "))
                novo_nome = input("Digite o novo nome do responsável: ")
                novo_contato =int(input("Digite o novo contato: "))
                novo_endereço =input("Digite a novo endereço: ")
                novo_pet = input("Digite o novo nome do pet: ")

                # aqui vai criar uma nova linha listando os novos dados do aluno selecionado
                nova_linha = f"{novo_codigo_cliente}, {novo_nome}, {novo_contato}, {novo_endereço}, {novo_pet}\n"
                print(nova_linha)
                # Substituir a linha no arquivo de dados velhos pelos dados novos
                linhas[i] = nova_linha

            # Abrir o arquivo 'Dados.txt' novamente em modo de escrita 'w', para conseguir alterar e substituir os dados velhos pelos novos dados
            with open('Dados.txt', 'w') as arquivo:
                arquivo.writelines(linhas)
            

    except ValueError:
        print("Valor inválido. Certifique-se de digitar um valor numérico para o código do cliente.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao alterar os dados:", str(e))

#REALIZAR BACKUP
def realizarBackup():
    try:
        with open('Dados.txt', 'r') as arquivo_origem:
            with open('backup_dados.txt', 'w') as arquvio_backup:
                conteudo = arquivo_origem.read()
                arquvio_backup.write(conteudo)
        print("Backup do arquvio realizado com sucesso!")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao realizar o backup: ", str(e))

#EXCLUIR DADOS
def excluirDados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum dado de cliente cadastrado.")
            return

        codigo_cliente = int(input("Digite o código do cliente que deseja excluir: "))
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(', ')
                if int(dados[0]) == codigo_cliente:
                    encontrado = True #esse encontrado é para, se o dado nao foi encontrado Flase, e se for encontrado true
                    print("Dados do cliente excluído com sucesso!")
                else:
                    arquivo.write(linha)
        if not encontrado:
            print("Nenhum cliente encontrado com código fornecido.")
    except ValueError:
        print("Valor inválido. Certifique-se de digitar um valor número para o código do cliente.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao excluir os dados:", str(e))
#LISTAR DADOS
def listar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            print(linhas)

        if not linhas:
            print("Nenhum dado de cliente cadastrado.")
            return

    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao executar a função desejada:", str(e))
listar_dados()