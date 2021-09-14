#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    longueur = len(string)
    return True
    pass


def remove_third_char(string: str) -> str:
    caracteres = list(string)
    print(caracteres)
    caracteres[2] = ""
    print(caracteres)
    string ="".join(caracteres)
    return string
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    caract = list(string)
    print(caract)
    caract[6] = "z"
    print(caract)
    string = "".join(caract)
    return string
    pass


def get_number_of_char(string: str, char: str) -> int:
    counter = 0
    for letter in string:
        if letter == char:
         counter = counter + 1
    return counter

    pass


def get_number_of_words(sentence: str, word: str) -> int:
    counter = 0
    liste = sentence.split()
    print(liste)
    for mot in liste:
        if mot == word:
            counter = counter + 1
    return counter



    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
