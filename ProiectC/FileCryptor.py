import os
import sys
import hashlib


def validate_argv():
    if len(sys.argv) != 4:
        raise Exception("Error: You should call the script like this: python FileCryptor.py crypt/decrypt \'path\\to\\file\' password")
    if sys.argv[1] == 'crypt' and os.path.splitext(sys.argv[2])[1] == '.encrypted':
        raise Exception("Error: File is already encrypted!")
    if sys.argv[1] == 'decrypt' and os.path.splitext(sys.argv[2])[1] != '.encrypted':
        raise Exception("Error: This file is not encrypted!")


def hashMD5(fl):
    m = hashlib.md5()
    with open(fl, "rb") as f:
        while True:
            data = f.read(4096)
            if len(data) == 0:
                break
            m.update(data)
    return m.hexdigest()


def encrypt():
    hsh = hashMD5(sys.argv[2])
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
    password = sys.argv[3]
    dec = str()
    ind_pass = 0
    with open(sys.argv[2], "r", encoding='utf-8') as f:
        hsh = f.read(32)
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
    checkhash = hashMD5(newfile)
    if checkhash != hsh:
        os.remove(newfile)
        raise Exception("Password was wrong! File couldn't be decrypted!Retry...")
    os.remove(sys.argv[2])


if __name__ == '__main__':
    validate_argv()
    if sys.argv[1] == "crypt":
        encrypt()
    elif sys.argv[1] == "decrypt":
        decrypt()
