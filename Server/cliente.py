import socket

class Cliente:

        def clienteTCP(ip, porta):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, porta))

                while True:
                        data = s.recv(1024)
                        print(f"{ip} - {data.decode()}")

                        msg = input("> ")
                        msg += "\n"

                        if msg == "exit\n":
                                break
                        else:
                                s.send(msg.encode())


                s.close()

        def clienteUDP(ip, porta):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                servidor = (ip, porta)

                while True:
                        msg = input("> ")
                        msg += "\n"

                        if msg == "exit\n":
                                break
                        else:
                                s.sendto(msg.encode(), servidor)

                                s_msg, s_end = s.recvfrom(1024)
                                print(f"{s_end} - {s_msg.decode()}")