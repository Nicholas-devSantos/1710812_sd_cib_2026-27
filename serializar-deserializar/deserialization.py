# A test object
import pickle
x=input("Indique o ficheiro a deserializar:")
# Deserialization
x_reconstructed=""
with open(x, "rb") as infile:
    x_reconstructed = x_reconstructed+pickle.load(infile)
print("Reconstructed object" + x , x_reconstructed)
