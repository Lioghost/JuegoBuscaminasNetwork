import socket, random, pickle
from buscaminas import build_buscaminas, clic

serverAddress = "localhost"
port = 65432
HEADER = 512

def cont(m,b):
    """Cuenta la cantidad de veces que se repite b en la matriz m"""
    c=0
    for a in range(len(m)):
        c=c+m[a].count(b)

    return(c)

def build_buscaminas(i, j, mines):
    
    campo = matriz(i, j, 0)

    a = 0
    #Este while rellena la matriz de minas "*".
    while cont(campo,"*") < mines:
        campo[random.randint(0,i-1)][random.randint(0,j-1)] = "*"
        a += 1
       
    for x in range(i):
        for y in range(j):
            if campo[x][y] != "*":
                count=0
                for a in [1,0,-1]:
                    for b in [1,0,-1]:
                        try:
                            if campo[x+a][y+b]=="*":
                                if (x+a>-1 and y+b > -1):
                                    count += 1
                        except:
                            pass
                campo[x][y]=count
    #print("Minitas", campo)  #PARA VER LA MATRIZ CON MINAS
    return campo

def clic(campo, i=1, j=1, mina="n"):
    """Función que simula un click"""
    i = int(i) - 1
    j = int(j) - 1

    if mina == "s":
        return 1
    else:
        if campo[i][j] == "*":
            return 0
        elif campo[i][j] != "*":
            return 2

def check_mines(matrix, i, j):
    #Verifica las minas seleccionadas
    count = 0
    i = int(i) - 1
    j = int(j) - 1
    campo = list(matrix)

    #for i in range(len(matrix)):
        #for j in range(len(matrix)):
    if matrix[i][j] == "*":
                #print("+"+client_matrix[i][j]+"+ +"+matrix[i][j]+"+")
        count += 1

    return count

"""
def printmin(campo,i,j):
    #Función que imprime la matriz en un formato agradable para el usuario
    campoprint=list(campo)

    for p in range(len(campoprint)):
        for t in range(len(campoprint[0])):
            if len(str(campoprint[p][t])) == 1:
                campoprint[p][t] = str(campoprint[p][t]) + " "

"""

def matriz(i,j,s):
    #Devuelve una matriz de dimensiones i * j rellena de s
    m = []
    for a in range(i):
        m.append([])
        for b in range(j):
            m[a].append(s)

    return(m)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((serverAddress, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        level = conn.recv(HEADER)
        datos = pickle.loads(level)
        count = 0
        matrix = build_buscaminas(datos[0], datos[1], datos[2])
        while True:
            print(matrix)
            data_len = conn.recv(HEADER)
            
            if not data_len:
                break
            else:
                data = b''
                data += conn.recv(int(data_len))
                data_deserial = pickle.loads(data)
                i, j, mine = data_deserial

            resp = clic(matrix, i, j, mine)
            aux = [0] * 3
            aux.insert(0, resp)

            if resp == 0:
                aux[0] = resp
                aux.insert(1, matrix)

            count += check_mines(matrix,i,j)
            aux.insert(2, count)
            
            data_serial = pickle.dumps(aux)
            data_len = str(len(data_serial))
            data = bytes(f"{data_len:<{HEADER}}", "utf-8") + data_serial
            conn.sendall(data)
        
        print("Cliente Desconectado", addr)