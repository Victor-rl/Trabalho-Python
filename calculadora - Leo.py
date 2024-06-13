import os

def titulo():

    print("""CALCULATOR""")
    

def exibir_opcoes():
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Encerrar o progama/n')
    
    
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal:  ')
    main()
    
def finalizando_app():
    print('Finalizando o app')
    
    

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    
def soma():
    x = float(input('Digite o primeiro numero o qual deseja fazer a soma: '))
    y = float(input('Digite o segundo numero o qual deseja fazer a soma: '))
    z = x + y
    print(f'A soma  {x} + {y} é igual a {z}')
    voltar_ao_menu_principal()
    
    
def subtracao():
    x = float(input('Digite o primeiro numero o qual deseja fazer a subtração: '))
    y = float(input('Digite o segundo numero o qual deseja fazer a subtração: '))
    z = x - y
    print(f'A subtração  {x} - {y} é igual a {z}')
    voltar_ao_menu_principal()
     
def multiplicacao():
    x = float(input('Digite o primeiro numero o qual deseja fazer a multiplicação: '))
    y = float(input('Digite o segundo numero o qual deseja fazer a multiplicação: '))
    z = x * y
    print(f'A multiplicação  {x} * {y} é igual a {z}')
    voltar_ao_menu_principal()
    
def divisao():
    x = float(input('Digite o primeiro numero o qual deseja fazer a divisão: '))
    y = float(input('Digite o segundo numero o qual deseja fazer a divisão: '))
    if y == 0:
        print('Não é possível dividir por zero!')
    else:
        z = x / y
        print(f'A divisão {x} / {y} é igual a {z}')
    voltar_ao_menu_principal()

def escolher_opcoes():
    
    opcao_escolhida = None
    while opcao_escolhida != 5:

        try:
            opcao_escolhida = int(input('Escolha uma opção de 1 um a 5 : '))
            
            if opcao_escolhida == 1:
                soma()
            
            elif opcao_escolhida == 2:
                subtracao()
                
            elif opcao_escolhida == 3:
                multiplicacao()
            
            elif opcao_escolhida == 4:
                divisao()
                
            elif opcao_escolhida == 5:
                finalizando_app()
            else:    
                opcao_invalida()
        except:
            opcao_invalida()        
        
        

def main():
    os.system('cls')
    titulo()
    exibir_opcoes()
    escolher_opcoes()   
    
if __name__ == '__main__':
    main()    
    

    
