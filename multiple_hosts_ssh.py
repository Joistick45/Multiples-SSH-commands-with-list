import paramiko

username = 'USERNAME'
password = 'PASSWORD'
port = 'SSHPORT'
command = '/YOURCOMMAND'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def sendCommandToRB(address):
    ssh.connect(hostname=address, port=port, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()

    for line in stdout.readlines():
        print(line.replace('\n', ' '))
    ssh.close()

with open('clientlist.txt', 'r') as file:
    data = file.read().replace('\n', ' ')

lista = data.split()

for i in lista:
    try:
        sendCommandToRB(i)
        print(f'SUCESS to send command to client {i}')
    except:
        print(f"FAILED to send command to client {i}")
        continue



