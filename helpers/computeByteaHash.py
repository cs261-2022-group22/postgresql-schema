import bcrypt
import argparse

#should have one command line argument which is the plaintext password whose 
#hash should be produced and outputted in bytea (postgres) input format
parser = argparse.ArgumentParser(description="""Produces the bytea input form 
of the hash of the given plaintext password.""")
parser.add_argument('password', nargs=1,
                    help='the password to hash')
args = parser.parse_args()

passwordPlainStr = args.password[0]
passwordPlainBytes = passwordPlainStr.encode("utf-8")
passwordHashBytes = bcrypt.hashpw(passwordPlainBytes, bcrypt.gensalt())
byteaHash = "E'" + "\\\\x" + (passwordHashBytes.hex()) + "'"
print(byteaHash)