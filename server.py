#!/usr/bin/python3
import socket
import sys
import docker
def run_container(target):
    client = docker.from_env()
    container = client.containers.run(target,'/bin/sh',detach=True)
    backoff='ID:'+str(container.id)+' |Stats:'+str(container.stats)
    return backoff

def stop_container(target):
    #This code will stop all containers, do not use
    client = docker.from_env()
    for container in client.containers.list():
        container.stop()

def list_container():
    client = docker.from_env()
    lista=''
    for image in client.images.list():
        lista+=''.join(str(image))
    return lista

def pull_image(name):
    client = docker.from_env()
    image = client.images.pull(name)
    print(str(image.id))

def restart_container(target):
    client = docker.from_env()
    container = client.containers.restart(target)
    return container.stats

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', int(sys.argv[1]))
print('[+] Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    print('[-] StandBy')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(16)
            if data:
                request,arg=data.decode().split()
                print(request)
                print(arg)
                if request == 'run':
                    print(run_container(arg))
                if request == 'stop':
                    stop_container(arg)
                # Feature de listar está aqui para propositos experimentais apenas.
                if request == 'list': 
                    connection.sendall(list_container().encode())
                if request == 'restart':
                    connection.sendall(restart_container(arg).encode())
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()
