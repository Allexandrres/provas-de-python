def adicionar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula: ")
    alunos[matricula] = nome
    print(f"Aluno {nome} adicionado com sucesso.")

def remover_aluno(alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso.")
    else:
        print("Matrícula não encontrada.")

def visualizar_alunos(alunos):
    if alunos:
        print("Alunos cadastrados:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")

def main():
    alunos = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Visualizar todos os alunos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            remover_aluno(alunos)
        elif opcao == "3":
            visualizar_alunos(alunos)
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()