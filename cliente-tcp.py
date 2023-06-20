import socket

HOST = '192.168.124.34'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

filename = input("Digite o caminho do arquivo: ")

with open(filename, 'rb') as file:
    file_content = file.read()

# Concatenar o nome do arquivo com os dados do arquivo usando o separador '|||'
message = filename.encode() + b'|||' + file_content

tcp.sendall(message)

tcp.close()
