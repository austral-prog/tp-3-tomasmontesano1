def slice_simple():
    texto = "Awesome"
    texto = texto.lower()
    print(texto[0:3])
    a = int((len(texto)/2)-1)
    b = int((len(texto)/2)+2)
    print(texto[a:b])
    print(texto[0:7])

