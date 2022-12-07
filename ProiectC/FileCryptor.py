import os
import sys
import hashlib


def validate_argv():
    if len(sys.argv) != 4:  #eroare argumente prea multe/ putine
        raise Exception("Error: You should call the script like this: python FileCryptor.py encrypt/decrypt \'path\\to\\file\' password")
    if os.path.exists(sys.argv[2]) is False:
        raise Exception(f"Error: There is no such file at {sys.argv[2]}...")
    if os.path.isfile(sys.argv[2]) is False:
        raise Exception(f"Error: The {sys.argv[2]} is not a file!")
    if sys.argv[1] == 'encrypt' and os.path.splitext(sys.argv[2])[1] == '.encrypted':  #eroare pentru încercare de criptare pe fisier deja criptat
        raise Exception("Error: File is already encrypted!")
    if sys.argv[1] == 'decrypt' and os.path.splitext(sys.argv[2])[1] != '.encrypted':  #eroare pentru încercare de decriptare pe fisier care nu este criptat
        raise Exception("Error: This file is not encrypted!")


def hashSHA256(fl):
    """

    :param fl: primeste fișierul pe care se face hash sha256
    :return: functia hash a fișierului
    """
    m = hashlib.sha256()
    with open(fl, "rb") as f:
        while True:
            data = f.read(4096)
            if len(data) == 0:
                break
            m.update(data)
    return m.hexdigest()


def encrypt():
    """
    Cand se criptează se generează hash-ul fișierului, apoi se citește din fisier caracter cu caracter,
    pentru fiecare se aduna codul ASCII cu cel al caracterului din iteratia curenta a parolei
    Apoi se pune hash-ul pe 64 de caractere si sirul criptat in noul fisier creat ".encrypted".

    """
    hsh = hashSHA256(sys.argv[2])
    password = sys.argv[3]
    enc = str()
    ind_pass = 0
    with open(sys.argv[2], "r", encoding='utf-8') as f:
        byte = f.read(1)
        while byte != '':
            enc += chr((ord(byte) + ord(password[ind_pass])) % 256)
            ind_pass += 1
            if ind_pass == len(password):
                ind_pass = 0
            byte = f.read(1)
    with open(sys.argv[2] + ".encrypted", "w", encoding='utf-8')as f:
        f.write(hsh)
        f.write(enc)
    os.remove(sys.argv[2])


def decrypt():
    """
    Se ia fișierul criptat din care se citește si se fac operatii pe fiecare caracter similar cu functia de criptare,
    doar ca se scad valorile ASCII. Primii 64 de octeti sunt citiți odata, deoarece reprezinta hash-ul fișierului
    decriptat. Dupa ce se decriptează, se creaza hash pe sirul decriptat si se compara cu cel al fișierului initial.
    Daca hash-urile nu se potrivesc înseamna ca parola a fost greșita si se anulează operatia de decriptare. Altfel
    se va crea fișierul decriptat.
    """
    password = sys.argv[3]
    dec = str()
    ind_pass = 0
    with open(sys.argv[2], "r", encoding='utf-8') as f:
        hsh = f.read(64)
        byte = f.read(1)
        while byte != '':
            dec += chr(((ord(byte) - ord(password[ind_pass])+256) % 256))
            ind_pass += 1
            if ind_pass == len(password):
                ind_pass = 0
            byte = f.read(1)
    newfile = os.path.splitext(sys.argv[2])[0]
    with open(newfile, "w", encoding='utf-8') as f:
        f.write(dec)
    checkhash = hashSHA256(newfile)
    if checkhash != hsh:
        os.remove(newfile)
        raise Exception("Password was wrong! File couldn't be decrypted!Retry...")
    os.remove(sys.argv[2])


if __name__ == '__main__':
    validate_argv()
    if sys.argv[1] == "encrypt":
        encrypt()
    elif sys.argv[1] == "decrypt":
        decrypt()
