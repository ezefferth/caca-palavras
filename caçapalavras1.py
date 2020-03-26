#Ezefferth Fernandes RGA 201521901022
#Leonardo Sampaio    RGA 201521901028
#Caça Palavras
#UFMT - VG
#python

#cria matriz / para cada elemento em i(linha) insere uma qnt de colunas
#onde a matriz tem seu determinado tamanho 
def matriz(x):
    matriz=['']*x
    for i in range(x): 
        l=raw_input() 
        matriz[i]=l 
    return matriz

#recebe a matriz e a palavra desejada

def imprimematriz(x,y):
    n=len(x)
    w=len(y)
    for i in range(len(x)):
        for j in range(len(x)):
#procura da esquerda para direita OK
            k=0
            while k < w and x[i][(j+k)%n]==y[k]: 
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%(i,(j+(w-1))%n)
                
 #procura direita para esquerda OK
            k=0
            while k < w and x[i][(j-k)%n]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%(i,(j-(w-1))%n)
                
#procura de cima para baixo OK
            k=0
            while k < w and x[(i+k)%n][j]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%((i+(w-1))%n,j)
                
#procura e baixo para cima OK
            k=0
            while k < w and x[(i-k)%n][j]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%((i-(w-1))%n,j)
                
#procura na diagonal esquerda para direita e para cima OK
            k=0
            while k < w and x[(i-k)%n][(j+k)%n]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%((i-(w-1))%n,(j+(w-1))%n)
                
#procura de digonal direita para esquerda para baixo OK
            k=0
            while k < w and x[(i+k)%n][(j-k)%n]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%((i+(w-1))%n,(j-(w-1))%n)
                
#procura diagonal esquerda para direita para cima OK
            k=0
            while k < w and x[(i-k)%n][(j-k)%n]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%((i-(w-1))%n,(j-(w-1))%n)
#procura diagonal direita para esquerda baixo OK

            k=0
            while k < w and x[(i+k)%n][(j+k)%n]==y[k]:
                k+=1
            if k == w:
                print '(%d,%d)'%(i,j),
                print '(%d,%d)'%((i+(w-1))%n,(j+(w-1))%n)
# y recebe o tamanho da matriz / z recebe a palavra a ser buscada
y=input()
w=matriz(y)
z=raw_input()
imprimematriz(w,z)

