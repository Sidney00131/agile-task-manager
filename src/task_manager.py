class Task:
    def __init__(self, title, description, priority="Média"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False


# Lista que armazena as tarefas
tasks = []


# CREATE
def create_task(title, description, priority="Média"):
    task = Task(title, description, priority)
    tasks.append(task)
    return task


# READ
def list_tasks():
    return tasks


# UPDATE
def update_task(index, title, description, priority="Média"):
    if index < len(tasks):
        tasks[index].title = title
        tasks[index].description = description
        tasks[index].priority = priority


# DELETE
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)


# EXECUÇÃO LOCAL
if __name__ == "__main__":
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            title = input("Título: ")
            description = input("Descrição: ")
            priority = input("Prioridade (Baixa/Média/Alta): ")

            create_task(title, description, priority or "Média")
            print("✔ Tarefa criada com sucesso!")

        elif opcao == "2":
            if not tasks:
                print("⚠ Nenhuma tarefa cadastrada.")
            else:
                print("\n--- LISTA DE TAREFAS ---")
                for i, task in enumerate(list_tasks()):
                    print(f"{i} - {task.title} | Prioridade: {task.priority}")

        elif opcao == "3":
            if not tasks:
                print("⚠ Nenhuma tarefa para atualizar.")
            else:
                index = int(input("Informe o índice da tarefa: "))
                title = input("Novo título: ")
                description = input("Nova descrição: ")
                priority = input("Nova prioridade (Baixa/Média/Alta): ")

                update_task(index, title, description, priority or "Média")
                print("✔ Tarefa atualizada com sucesso!")

        elif opcao == "4":
            if not tasks:
                print("⚠ Nenhuma tarefa para remover.")
            else:
                index = int(input("Informe o índice da tarefa: "))
                delete_task(index)
                print("✔ Tarefa removida com sucesso!")

        elif opcao == "5":
            print("Encerrando o programa. 👋")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")
