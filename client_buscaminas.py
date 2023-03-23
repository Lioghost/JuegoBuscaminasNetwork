import socket, pickle, os, time

serverAddress = "localhost"
port = 65432
HEADER = 512

def printmin(campo,i,j):
    #Función que imprime la matriz en un formato agradable para el usuario
    campoprint = list(campo)
    x = "  "
    ascii = 65
    for j in range(0, i):
        x += " " + chr(j + ascii)

    print("".join(x))
    for p in range(len(campoprint)):
        for t in range(len(campoprint[0])):
            if len(str(campoprint[p][t])) == 1:
                campoprint[p][t]=str(campoprint[p][t])+" "

        if (p + 1) < 10:
            print(" " + str(p+1)+ " " + "".join(campoprint[p]))
        else:
            print(str(p+1)+ " " + "".join(campoprint[p]))

def cont(m,b):
    #Cuenta la cantidad de veces que se repite b en la matriz m
    c = 0
    for a in range(len(m)):
        c += m[a].count(b)

    return(c)

def matriz(i,j,s):
    #Devuelve una matriz de dimensiones i * j rellena de s
    m = []
    for a in range(i):
        m.append([])
        for b in range(j):
            m[a].append(s)

    return(m)

def start():
    #Inicia el juego
    print('######--BUSCAMINAS--######')
    print("Selecciona un nivel")
    level = input("(1) PRINCIPIANTE\n(2) EXPERTO\nNivel: ")

    match level:
        case "1":
            return (9, 9, 2)
        case "2":
            return (16, 16, 40)
        
def cronometer():
    for h in range(0, 24):
        for m in range(0, 60):
            for s in range(0, 60):
                os.system('cls')
                return f"{h}:{m}:{s}"
                time.sleep(1)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverAddress, port))
    level = start()
    incio = time.time()
    i, j, mines = level
    start = pickle.dumps(level)
    s.send(start)
    matrix = matriz(i,j,"#")
    while True:

        os.system("cls")
        num_mines = mines - cont(matrix, "* ")

        print(f"MINAS RESTANTES: {num_mines}")
        printmin(matrix,i,j)
        aux = []
        aux.append(int(input("\nFila: ")))
        aux.append(ord(input("Columna: ").upper()) - 64)
        aux.append(input("Colocar mina? (s/n): ").lower())
        i1, j1, mine = aux
        data_serial = pickle.dumps(aux)
        data_len = str(len(data_serial))
        data = bytes(f"{data_len:<{HEADER}}", "utf-8") + data_serial
        s.sendall(data)
        
        data_len = s.recv(HEADER)
            
        if not data_len:
            break
        else:
            data = b''
            data += s.recv(int(data_len))
            data_deserial = pickle.loads(data)
            print("dataserial", data_deserial)
            input()
        
            if data_deserial[2] == mines:
                os.system("cls")
                print("\tGANASTE!!!!")
                break

            match data_deserial[0]:
                case 0:
                    print("\t¡¡¡BOOOOOOOOOM!!!\n")
                    printmin(data_deserial[1], i, j)
                    input("\n\tGAME OVER!...\n\tENTER!")
                    break
                case 1:
                    matrix[i1-1][j1-1] = "*"
                    printmin(matrix,i,j)
                    continue
                case 2:
                    matrix[i1-1][j1-1] = "X"
            
        printmin(matrix,i1,j1)
    final = time.time()
    print(f"Tiempo Transcurrido: {final - incio}")
#print(f"Received {data!r}")