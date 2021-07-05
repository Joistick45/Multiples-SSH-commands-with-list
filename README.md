# Multiples-SSH-commands-with-list

I created this script to send multiple commands to routerboards with ssh, 
the usage is simple, just need to install paramiko and put a list of hosts in a TXT named "clientlist.txt" in same folder.
All the hosts need to have the be same user, password, and ssh port.

the variable


and the list have to be a txt with line wrap like this:
...
10.0.1.1
172.31.0.1
192.168.7.1
...

you can get this txt with some cURL
