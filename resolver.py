import socket #Provides access to BSD socket interface

def resolve_http(url):
    
    # Parse the URL to get the host and path

    parts = url.split('/')  #Remove '/' from the url
    
    host = parts[2]   #Finding host in the parts list
    
    path = "/" + "/".join(parts[3:])  #Added the rest of the path

    # Create a socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM ) #Arg AF_INET = IPv4 and socket.SOCK_STREAM = TCP
                                                                       #Arg AF_INET6 = IPv6 and socket.SOCK_DGRAM = UDP                                                                               
    # IP's and Port can be defined as such
    # server_ip = "127.0.0.1" 
    # port = 8000

    client_socket.connect((host,80))

    #Send an HTTP GET Request
    # Send an HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client_socket.sendall(request.encode())

    # Recieve and print server response
    response = b""   # Initializing the empty byte string to store recieved data 
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data # Combining chunks to reconstruct full response after the initial 2096 bytes request
    
    print(response.decode("utf-8")) #Converting the recieved bytes to utf-8 string

    client_socket.close()

resolve_http("http://www.google.com")







