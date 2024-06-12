import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Livro:
    def __init__(self, titulo, autor, status='disponível'):
        self.__titulo = titulo
        self.__autor = autor
        self.__status = status

    def __str__(self):
        return f'Título: {self.__titulo}\nAutor: {self.__autor}\nStatus: {self.__status}'

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

class Membro:
    def __init__(self, nome, id_membro, endereco):
        self.__nome = nome
        self.__id_membro = id_membro
        self.__endereco = endereco

    def __str__(self):
        return f'Nome: {self.__nome}\nID: {self.__id_membro}\nEndereço: {self.__endereco}'

    def get_nome(self):
        return self.__nome

    def get_id_membro(self):
        return self.__id_membro

class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao):
        self.__livro = livro
        self.__membro = membro
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = data_devolucao
        self.__estado = 'ativo'

    def __str__(self):
        return f'Livro: {self.__livro.get_titulo()}\nMembro: {self.__membro.get_nome()}\nData de Empréstimo: {self.__data_emprestimo}\nData de Devolução: {self.__data_devolucao}\nEstado: {self.__estado}'

    def get_livro(self):
        return self.__livro

    def get_membro(self):
        return self.__membro

    def get_data_emprestimo(self):
        return self.__data_emprestimo

    def get_data_devolucao(self):
        return self.__data_devolucao

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []
        self.__emprestimos = []

    def cadastrar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.__livros.append(livro)
        print(f'Livro "{titulo}" cadastrado com sucesso.')

    def listar_livros(self):
        if not self.__livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.__livros:
                print(livro)

    def remover_livro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                self.__livros.remove(livro)
                print(f'Livro "{titulo}" removido com sucesso.')
                return
        print(f'Livro "{titulo}" não encontrado.')

    def atualizar_livro(self, titulo_atual, novo_titulo, novo_autor):
        for livro in self.__livros:
            if livro.get_titulo() == titulo_atual:
                livro.__titulo = novo_titulo
                livro.__autor = novo_autor
                print(f'Livro "{titulo_atual}" atualizado para "{novo_titulo}" por {novo_autor}.')
                return
        print(f'Livro "{titulo_atual}" não encontrado.')

    def registrar_membro(self, nome, id_membro, endereco):
        membro = Membro(nome, id_membro, endereco)
        self.__membros.append(membro)
        print(f'Membro "{nome}" registrado com sucesso.')

    def listar_membros(self):
        if not self.__membros:
            print("Nenhum membro registrado.")
        else:
            for membro in self.__membros:
                print(membro)

    def registrar_emprestimo(self, titulo_livro, id_membro, data_emprestimo, data_devolucao):
        livro = next((livro for livro in self.__livros if livro.get_titulo() == titulo_livro), None)
        membro = next((membro for membro in self.__membros if membro.get_id_membro() == id_membro), None)
        if livro and membro and livro.get_status() == 'disponível':
            emprestimo = Emprestimo(livro, membro, data_emprestimo, data_devolucao)
            self.__emprestimos.append(emprestimo)
            livro.set_status('emprestado')
            print(f'Empréstimo registrado: {livro.get_titulo()} para {membro.get_nome()} de {data_emprestimo} a {data_devolucao}.')
        else:
            print('Empréstimo não pode ser registrado. Verifique se o livro está disponível e se o membro existe.')

    def registrar_devolucao(self, titulo_livro, id_membro):
        for emprestimo in self.__emprestimos:
            if emprestimo.get_livro().get_titulo() == titulo_livro and emprestimo.get_membro().get_id_membro() == id_membro and emprestimo.get_estado() == 'ativo':
                emprestimo.set_estado('concluído')
                emprestimo.get_livro().set_status('disponível')
                print(f'Devolução registrada: {titulo_livro} devolvido por {emprestimo.get_membro().get_nome()}.')
                return
        print('Empréstimo não encontrado ou já concluído.')

    def listar_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.__livros:
            if livro.get_status() == 'disponível':
                print(livro)

    def listar_livros_emprestados(self):
        print("Livros emprestados:")
        for livro in self.__livros:
            if livro.get_status() == 'emprestado':
                print(livro)

# Exemplo de uso
biblioteca = Biblioteca()

while True:
    print(
        "1. Cadastrar livro\n"
        "2. Listar livros\n"
        "3. Remover livro\n"
        "4. Atualizar livro\n"
        "5. Registrar membro\n"
        "6. Listar membros\n"
        "7. Registrar empréstimo\n"
        "8. Registrar devolução\n"
        "9. Listar livros disponíveis\n"
        "10. Listar livros emprestados\n"
        "11. Sair"
    )
    
    opcao = int(input("Escolha uma opção: "))

    clear_console()

    if opcao == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        biblioteca.cadastrar_livro(titulo, autor)
    elif opcao == 2:
        biblioteca.listar_livros()
    elif opcao == 3:
        titulo = input("Digite o título do livro a ser removido: ")
        biblioteca.remover_livro(titulo)
    elif opcao == 4:
        titulo_atual = input("Digite o título atual do livro a ser atualizado: ")
        novo_titulo = input("Digite o novo título do livro: ")
        novo_autor = input("Digite o novo autor do livro: ")
        biblioteca.atualizar_livro(titulo_atual, novo_titulo, novo_autor)
    elif opcao == 5:
        nome = input("Digite o nome do membro: ")
        id_membro = input("Digite o ID do membro: ")
        endereco = input("Digite o endereço do membro: ")
        biblioteca.registrar_membro(nome, id_membro, endereco)
    elif opcao == 6:
        biblioteca.listar_membros()
    elif opcao == 7:
        titulo_livro = input("Digite o título do livro a ser emprestado: ")
        id_membro = input("Digite o ID do membro que pegará o empréstimo: ")
        data_emprestimo = input("Digite a data de empréstimo (dd/mm/aaaa): ")
        data_devolucao = input("Digite a data de devolução (dd/mm/aaaa): ")
        biblioteca.registrar_emprestimo(titulo_livro, id_membro, data_emprestimo, data_devolucao)
    elif opcao == 8:
        titulo_livro = input("Digite o título do livro a ser devolvido: ")
        id_membro = input("Digite o ID do membro que devolverá o livro: ")
        biblioteca.registrar_devolucao(titulo_livro, id_membro)
    elif opcao == 9:
        biblioteca.listar_livros_disponiveis()
    elif opcao == 10:
        biblioteca.listar_livros_emprestados()
    elif opcao == 11:
        break
    else:
        print('Opção inválida.')

    input("Pressione Enter para continuar...")
    clear_console()