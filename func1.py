def hello(nome, idade):
    print(f'olá {nome}!')
    if int(idade) > 15:
        print("voçê pode votar")
    else:
        print("voçê ainda não pode votar!")
    print(" ")

hello("Joca", 17)

hello("Maricleuza", 13 )

hello(idade="19", nome="Julio",)