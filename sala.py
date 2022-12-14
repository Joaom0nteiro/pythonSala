
cad=['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
mat = []
linhas = int(input("Quantas fileiras? "))
colunas = int(input("Quantas cadeiras por fila? "))
for i in range(linhas):
    lin=[]
    for j in range(colunas):
        letra=cad[i]+str(j)
        lin.append((letra))
    mat.append(lin)
for i in mat:
    print(i)#quebra de linha.
p = 1
lista=[]
lin=[]

while p != 0:  
    ass_lin=str(input("Digite a fileira que deseja: "))
    lista.append(ass_lin)
#ass_col=str(input("Digite a cadeira que deseja: "))
    
       
    for i in range(linhas):
        for j in range(colunas):
            letra=cad[i]+str(j)
            if ass_lin==letra:
                lin.append(("--"))
            else:
                letra=cad[i]+str(j)
                lin.append((letra))
                
        mat.append(lin)
    for i in mat:
        print(i)#quebra de linha.

    
    p = int(input("Digite: "))
print("Poltronas selecionados: ",lista)

