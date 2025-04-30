import socket

class Servidor:
    
    def tcp(ip, porta):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, porta))
        s.listen(1)
        c_msg, c_end = s.accept()

        while True:
            msg = input("> ")
            msg += "\n"

            if msg == "exit\n":
                break
            else:
                c_msg.send(msg.encode())

                data = c_msg.recv(1024)
                print(f"{c_end} - {data.decode()}")
        s.close()

    def udp(ip, porta):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((ip, porta))

            while True:
                s_msg, s_end = s.recvfrom(1024)
                print(f"{s_end} - {s_msg.decode()}")

                msg = input("> ")
                msg += "\n"

                if msg == "exit\n":
                     break
                else:
                    s.sendto(msg.encode(), s_end)

            s.close()