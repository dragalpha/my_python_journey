# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

d={
    "Chabi":"Keys",
    "Amm":"Mango",
    "Kola":"Banana",
    "Jam":"Wine",
    "Apel":"Apple",
    "Jal":"Water",

}

for n in range(1,7):
    a=input(f"Which English meaning You Wanna Know about the hindi word {d.keys()}:")
    print(d.get(a))