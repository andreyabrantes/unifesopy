# Escreva um código onde leia a sequência de números e mostre a soma

def main() -> None:
    soma: int = int(input("Digite a quantidade de números que deseja somar: "))
    if soma < 0: 
        print("Por favor, digite um número válido")
    
    else: 
        resultado: int = 0 
        i: int = 0
        
        while i < soma:
            qtdnumero: int = int(input(f"Coloque o número {i+1}: "))
            resultado = resultado + qtdnumero
            i = i + 1
        
        print (f"A soma dos números é {resultado}")
    
if __name__ == "__main__":
    main()
