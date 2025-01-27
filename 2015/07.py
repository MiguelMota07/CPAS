n = int(input())
texts = []
for j in range(n):
    text = str(input())
    letras = []
    nLetras = []
    for letra in text:
        if letra == " ":
            continue
        elif letra in letras:
            nLetras[letras.index(letra)] += 1
        else:
            letras.append(letra)
            nLetras.append(1)
    output = ""
    for letra in letras:
        for i in range(nLetras[letras.index(letra)]):
            output += letra
    texts.append(output)
for text in texts:
    print(text)