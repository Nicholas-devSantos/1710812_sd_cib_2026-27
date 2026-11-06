x=input("Indique o ficheiro txt, <path>/<nome_file.txt>:")
f = open("./"+x, "r",encoding='utf8')
print(f.read())