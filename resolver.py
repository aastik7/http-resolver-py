import socket #Provides access to BSD socket interface

def resolve_http(url):
    
    parts = url.split('/')#Remove '/' from the url
    
    host = parts[2] #Finding host in the parts list
    
    path = "/" + "/".join(parts[3:]) #Added the rest of the path

    

