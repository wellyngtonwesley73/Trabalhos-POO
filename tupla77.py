palavras = (
    "compreender", "cozinhar", "ingrediente", "tempero",
    "oficina", "barato", "viajar", "explorar",
    "jornada", "universo", "astronauta", "infinito"
)


for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos: ", end="")
    
  
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(f"{letra} ", end="")