import sys
import servidor
import cliente

help = """
[help] 
python3 main.py [servidor/cliente] [tcp/udp] ip porta

    -s = servidor
    -c = cliente
    -t = tcp
    -u = udp

"""

tipo = sys.argv[1]


if tipo == "-s":
    protocolo = sys.argv[2]
    ip = sys.argv[3]
    porta = int(sys.argv[4])

    s = servidor.Servidor
    if protocolo == "-t":
        s.tcp(ip, porta)
    elif protocolo == "-u":
        s.udp(ip, porta)
    else:
        print(help)

elif tipo == "-c":
    protocolo = sys.argv[2]
    ip = sys.argv[3]
    porta = int(sys.argv[4])

    c = cliente.Cliente
    if protocolo == "-t":
        c.clienteTCP(ip, porta)
    elif protocolo == "-u":
        c.clienteUDP(ip, porta)
    else:
        print(help)

else:
    print(help)