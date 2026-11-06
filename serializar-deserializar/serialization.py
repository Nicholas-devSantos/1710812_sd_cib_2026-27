# A test object
import pickle

u=input("Indique o ficheiro txt, <path>/<nome_file.txt>:")
f = open("./"+u, "r",encoding='utf8')
x=f.read()
v=input("nome do file-serializado, file de output:")
# Serialization
with open(v+".pickle", "wb") as outfile:
    pickle.dump(x, outfile)
print("Written object"+x)