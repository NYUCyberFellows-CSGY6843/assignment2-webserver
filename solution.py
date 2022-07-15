# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start

  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = #Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]
      
      #fill in start - open your hellworld.html file. Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      
      #fill in end
      
      outputdata = #Fill in start -This variable can store your headers you want to send for any valid or invalid request. #Fill in end

      #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok? 
      #Fill in start

      #Fill in end

      #Send the content of the requested file to the client
      for i in f:
        #Fill in start - send your html file contents #Fill in end 
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      #Fill in start

      #Fill in end


      #Close client socket
      #Fill in start

      #Fill in end

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
