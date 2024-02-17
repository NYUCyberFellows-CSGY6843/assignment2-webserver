# import socket module
from socket import *
# In order to terminate the program

import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  # I put 1 as the number of requests, since in the assignment it says to only accept 1 at a time
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode()#Fill in start -a client is sending you a message   #Fill in end
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      if filename == "/helloworld.html":
        f = open(filename[1:], "r")
        outputdata = f.read()

      #fill in start #fill in end)


      #fill in end
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
        connectionSocket.send("HTTP/1,1 200 OK\r\n".encode())

      #Content-Type is an example on how to send a header as bytes. There are more!
      #outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      #Fill in start
        connectionSocket.send("Content-Type: text/html; charset=UTF-8\r\n".encode())

      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
        connectionSocket.send("\r\n\r\n".encode())
      #Fill in end
               
        for i in range(0, len(outputdata)): #for line in file
      #Fill in start - append your html file contents #Fill in end 
          connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        f.close()
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      else:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      connectionSocket.send("HTTP/1.1 404 Not Found\r\n").encode()
      connectionSocket.send("\r\n".encode())
      connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()

      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)