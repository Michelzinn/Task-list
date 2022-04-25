list = []

def add_task(list):
    task = input("Adicione o nome da sua tarefa!")
    list.append(task)
    return list

def show_list(list):
    print(list)

def undo(list):
    list.pop()
    return

def redo(list,deleted_task):
    list.append(deleted_task)
    return

option = 0
print('Seja bem vindo ao task manager!')
while option != '5':
    option = input('Digite uma opção!\n 1 para adicionar uma tarefa\n 2 para mostrar a sua lista de tarefas\n 3 para excluir o ultimo item \n 4 para desfazer a exclusão  \n 5 para encerrar!')

    if option == '1':
        add_task(list)
        print("\n" * 130)

    elif option == '2':
        print("\n" * 130)
        print("Aqui esta sua lista!")
        show_list(list)

    elif option == '3':
        if list == []:
            print("sua lista esta vazia, adicione um item")
            continue
        deleted_task = list[-1]
        undo(list)

    elif option == '4':
        print("\n" * 130)
        redo(list, deleted_task)

print('programa encerrado, aqui esta sua lista de task final!')
print(list)

