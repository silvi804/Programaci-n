input()
nums = [int(i) for i in input().split(" ")]
for n in nums:
    repeats = []
    while True:
        if n in repeats:
            break
        else:
            repeats.append(n)
            n = n ** 2
            n = (n // 100) % 10000
    print(len(repeats), end=' ')


""" Otro código """


def count_iterations(s):
    numbers = [s]
    while True:
        s = str(int(s) ** 2).zfill(8)[2:6]
        # adds zeros (0) at the beginning of the string, until it reaches the specified length
        if s in numbers:
            return len(numbers)
        numbers.append(s)


input()
numbers = input().split()
print(' '.join([str(count_iterations(number)) for number in numbers]))


"Mi código"
c_valores_iniciales = input("")
valores_iniciales = input("")
cada_valor = valores_iniciales.split(" ")

for valor in cada_valor:
    c = 0
    v = True
    valor = int(valor)
    lista = [valor]
    while v:
        cuadrado = (valor**2)//100
        resultado = round(((cuadrado/10000)-(cuadrado//10000))*10000)
# Aquí falto lógica, pudo ser nada más un (n // 100) % 10000
        resultado = int(resultado)
        c += 1
        for numero in lista:
            if numero == resultado:  # esto es lo mismo que usar in
                v = False
            else:
                valor = resultado

        lista.append(resultado)
    print(c, end=" ")
