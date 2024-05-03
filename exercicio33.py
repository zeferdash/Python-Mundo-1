a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
menor = a
## Verifica o menor valor digitado.
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
print(f"O menor valor digitado foi: {menor}")

## Verifica o maior valor digitado.
maior = a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior = c
print(f"O maior valor digitado foi: {maior}")