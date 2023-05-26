# Você recebe um array A de tamanho N. Você precisa imprimir os elementos de A em
# ordem alternada (começando do índice 0).
while True:
    print(f"{'=' * 50}")
    print("ESCOLHA O EXEMPLO A EXECUTAR")
    print("0 - SAIR dos exemplo")
    print(
        "1 - Você recebe um array A de tamanho N. Você precisa imprimir os elementos de A em ordem alternada (começando do índice 0).")
    print(
        "2 - Dado um número N. Encontre os dois últimos dígitos do enésimo número de fibonacci. Nota: Se os dois últimos dígitos forem 02, retorne 2.")
    opcao = int(input("Opção: "))
    print(f"{'='*50}")
    if opcao == 0:
        break
    elif opcao != 1 and opcao != 2:
        print("\nDigite uma opção valida!")


    match opcao:
        case 1:
            quant = int(input('Digite a quantidade de elementos: '))
            a = []
            for x in range(1, quant + 1):
                a.append(x)
            print("Lista: ", a)
            print("Resultado: ", a[::2])

        case 2:
            n = int(input("Que termo deseja encontrar: "))
            ultimo = 1
            penultimo = 1

            lista = []
            termina02 = []

            if (n == 1) or (n == 2):
                print("1")
            else:
                count = 3
                lista = ['1', '1']
                for count in range(n - 2):
                    termo = ultimo + penultimo
                    penultimo = ultimo
                    ultimo = termo
                    count += 1
                    lista.append(f'{termo}')
                    if '02' in f'{termo}':
                        x = str(termo)
                        if x[-2:] == '02':
                            termina02.append(termo)

            ultimo_text = str(lista[-1])

            if ultimo_text[-2:] == '02':
                print(2)
            elif ultimo < 10:
                print(f'{n}º elemento: {ultimo_text}\nUltimo digito: {ultimo_text[-1]}')
            else:
                print(f'{n}º elemento: {ultimo_text}\nDois ultimos digitos: {ultimo_text[-2]} e {ultimo_text[-1]}')
    print()