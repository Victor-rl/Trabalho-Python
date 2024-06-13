class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


class AgendaTelefonica:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        print(f"Contato {nome} adicionado.")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido.")
                return
        print(f"Contato {nome} não encontrado.")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print("Contato encontrado:")
                print(contato)
                return
        print(f"Contato {nome} não encontrado.")

    def exibir_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for contato in self.contatos:
                print(contato)


def main():
    agenda = AgendaTelefonica()
    while True:
        print("\nMenu da Agenda Telefônica:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Exibir Contatos")
        print("5. Sair")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            agenda.adicionar_contato(nome, telefone, email)
        elif escolha == '2':
            nome = input("Digite o nome para remover: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome para buscar: ")
            agenda.buscar_contato(nome)
        elif escolha == '4':
            agenda.exibir_contatos()
        elif escolha == '5':
            print("Saindo da agenda telefônica. Até logo!")
            break
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()
