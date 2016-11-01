from СipherCaesar import CipherCaesar as CC
from CipherAffine import CipherAffine as CA
from CipherVigenere import CipherVigenere as CV
import sys

def choose_cipher(choise):
    try:
        if choise=='1':
            create_cipher_caesar()
            return
        if choise=='2':
            create_cipher_affine()
            return
        if choise=='3':
            create_cipher_vigenere()
            return
        else:
            choise = input("Choose cryptosystem (1 - Caesar's cipher1; 2 - Affine cipher; 3- Vigenere's cipher):")
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

def create_cipher_caesar():
    key = str(read_from_key()).split(" ")[0]
    line = read_from_in()
    cs = CC(key)
    encrypt_line=cs.encrypt(line)
    write_to_crypt(encrypt_line)
    write_to_decrypt(cs.decrypt(encrypt_line))
    return

def create_cipher_affine():
    key = str(read_from_key()).split(" ")
    if(len(key)<2):
        raise Exception("Illegal argument. There is only one argument, but affine cipher needs two.")
    line = read_from_in()
    cs = CA(key[0],key[1])
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

choise=input("Choose cryptosystem (1 - Caesar's cipher1; 2 - Affine cipher; 3- Vigenere's cipher):")
choose_cipher(choise)
