# P2P CHAT APPLICATION


## Summary

In this project, we implement peer-to-peer chat using high-level socket programming. And in this project, after connecting to each other, the clients send commands to each other to enter the system of that client and send the answer to that client.

We have two main components which are server and client.

Simply, on the client side, the user sends a registration request to register himself on the server, after registration, the user also sends a login request to the server. After completing the login process, the user will be able to exchange messages with other peers.

The user has the following options for communication:
*   1) Getting a list of active clients
*   2) Connect to one of the clients
*   3) Send the command to the client
*   4) Close the connection with the client
*   5) Activation of the client in the network
*   6) Deactivation of the client on the network
*   7) Show the clients that I am connected to
*   8) Disconnected from the server
*   9) Refresh the page
*   10) My username and IP

The client can get the list of active clients in the network from the server by choosing the first option, and then by choosing the second option and giving the usename of one of the active clients of the server, the client can send the IP of that client to the client that makes the request, and the client sends the request to That client sends, and whenever that client confirms its request, the two clients are connected in a peer-to-peer manner.

By choosing the fifth option, the client is activated inside the server and from now on, other clients can communicate with it.

On the server side, the server assigns an IP to each of the clients and sends it to the client to communicate with the rest of the clients with that IP from now on.

## Solution to Approach

We have to do more than one thing at a time. So we are implementing multi-threaded system.

There is a TCP socket listening on port 12000. We are setting up a thread for each user that wants to connect to the server to listen on a TCP socket and handle requests. These threads work until the user logs out or terminates the program. Receive messages from peers.

On the client side, after the login process, the user establishes a channel between himself and the server. By using this channel, it communicates with the server

Also, the customer has two main issues. The first is to listen to chat requests coming from other peers. The second topic is to receive messages from peers and print these messages on the chat page.


## PROTOCOLS

We have a number of requests between the server and the client (which we put in type, which is a number):

*   1: Request a list of active clients
*   2: Activation or deactivation request
*   3: Getting or receiving IP
*   4: Request to connect to another client
*   8: The answer to the command run in the system
*   9: Sending the command to run into another system
*   10: List of active clients
*   11: Request to connect another client to the server and receive the answer
*   12: Sending and receiving messages

![1](https://github.com/falakian/socket-programming/assets/107622368/ea68e818-cdb4-4018-8cf7-624c3e718a9d)


*  Message package:

    |     packet     | 
    | -------------  |       
    | Type (b)       |
    | Username (15s) |
    | Message (2000s)|
