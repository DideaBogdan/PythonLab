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


def crypt(encrypt):
    """
    Cand se criptează se generează hash-ul fișierului, apoi se citește din fisier caracter cu caracter,
    pentru fiecare se aduna codul ASCII cu cel al caracterului din iteratia curenta a parolei
    Apoi se pune hash-ul pe 64 de caractere si sirul criptat in noul fisier creat ".encrypted".

    """
    if encrypt is True:
        hsh = hashSHA256(sys.argv[2])
    password = sys.argv[3]
    h = hashlib.sha256()
    h.update(password.encode('ascii'))
    hshpass = h.hexdigest()
    enc = str()
    ind_pass = 0
    with open(sys.argv[2], "r", encoding='utf-8') as f:
        if encrypt is False:
            check = f.read(6)
            if check != 'Bogdan':
                raise Exception("Error: This file is not encrypted!")
            verify_pass = f.read(64)
            if verify_pass != hshpass:
                raise Exception("Password was wrong! File couldn't be decrypted!Retry...")
            hsh = f.read(64)
        already_encrypted = f.read(6)
        if encrypt is True and already_encrypted == 'Bogdan':
            raise Exception("Error: File is already encrypted!")
        if encrypt is False:
            f.seek(134)
        else:
            f.seek(0)
        byte = f.read(1)
        while byte != '':
            if encrypt is True:
                enc += chr((ord(byte) + ord(password[ind_pass])) % 256)
            else:
                enc += chr(((ord(byte) - ord(password[ind_pass]) + 256) % 256))
            ind_pass += 1
            if ind_pass == len(password):
                ind_pass = 0
            byte = f.read(1)
    if encrypt is True:
        with open(sys.argv[2], "w", encoding='utf-8')as f:
            f.write("Bogdan")
            f.write(hshpass)
            f.write(hsh)
            f.write(enc)
    else:
        with open(sys.argv[2], "w", encoding='utf-8') as f:
            f.write(enc)



if __name__ == '__main__':
    validate_argv()
    if sys.argv[1] == "encrypt":
        crypt(True)
    elif sys.argv[1] == "decrypt":
        crypt(False)
