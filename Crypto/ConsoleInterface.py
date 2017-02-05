from CipherAdjustable import CipherAdjustable as CC
from CipherMonoalphabetic import CipherMonoalphabetic as CA
from CipherVigenere import CipherVigenere as CV
import sys

def choose_cipher(choise):
    try:
        if choise=='1':
            create_cipher_adjustable()
            return
        if choise=='2':
            create_cipher_monoalphabetic()
            return
        if choise=='3':
            create_cipher_vigenere()
            return
        else:
            choise = input(
                "Choose cryptosystem (1 - Adjustable cipher1; 2 - Monoalphabetic cipher; 3- Vigenere's cipher):")
            choose_cipher(choise)
    except Exception as exception:
        print(exception)
    except:
        print("Unexpected error.", sys.exc_info()[0])

def read_from_file(str):
    file=open(str,'r')
    line=file.read()
    file.close()
    return line

def read_from_key():
    return read_from_file("key.txt")

def read_from_in():
    return read_from_file("in.txt")

def write_to_file(str,line):
    file=open(str,'w')
    file.write(line)
    file.close()
    return

def write_to_crypt(line):
    return write_to_file("crypt.txt",line)

def write_to_decrypt(line):
    return write_to_file("decrypt.txt",line)

def create_cipher_adjustable():
    key = read_from_key()
    line = read_from_in()
    cs = CC(key)
    encrypt_line=cs.encrypt(line)
    write_to_crypt(encrypt_line)
    write_to_decrypt(cs.decrypt(encrypt_line))
    return

def create_cipher_monoalphabetic():
    key = read_from_key()
    line = read_from_in()
    cs = CA(key)
    encrypt_line = cs.encrypt(line)
    write_to_crypt(encrypt_line)
    write_to_decrypt(cs.decrypt(encrypt_line))
    return

def create_cipher_vigenere():
    key = read_from_key()
    line = read_from_in()
    cs = CV(key)
    encrypt_line = cs.encrypt(line)
    write_to_crypt(encrypt_line)
    write_to_decrypt(cs.decrypt(encrypt_line))
    return

choise=input("Choose cryptosystem (1 - Adjustable cipher1; 2 - Monoalphabetic cipher; 3- Vigenere's cipher):")
choose_cipher(choise)
