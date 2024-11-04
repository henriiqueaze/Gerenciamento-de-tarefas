from time import sleep

class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def marcarConcluida(self):
        self.concluida = True

    def __str__(self):
        if self.concluida:
            status = "Concluida"
        else:
            status = "Pendente"

        return f"Tarefa: {self.titulo} | Status: {status}"


class GerenciadorTarefas:
    tarefas = []

    @staticmethod
    def adicionarTarefa(titulo):
        novaTarefa = Tarefa(titulo)
        GerenciadorTarefas.tarefas.append(novaTarefa)

    @staticmethod
    def listarTarefas():
        for indice, tarefa in enumerate(GerenciadorTarefas.tarefas, start=1):
            print(f"{indice}. {tarefa}")

    @staticmethod
    def concluirTarefa(indice):
        try:
            GerenciadorTarefas.tarefas[indice].marcarConcluida()

        except IndexError:
            print("Índice da tarefa inválido")


def main():
    while True:
        print("Menu:")
        print("1 - Adicionar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Concluir Tarefa")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ")
            GerenciadorTarefas.adicionarTarefa(titulo)
            print("Tarefa adicionada com sucesso.")
            sleep(3)  

        elif opcao == "2":
            GerenciadorTarefas.listarTarefas()
            sleep(3)  

        elif opcao == "3":
            indice = int(input("Digite o índice da tarefa a concluir: ")) - 1
            GerenciadorTarefas.concluirTarefa(indice)
            if indice < len(GerenciadorTarefas.tarefas):
                print("Tarefa concluída com sucesso.")

            else:
                print("")
                
            sleep(3)  

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")
            sleep(3)  

if __name__ == "__main__":
    main()
