# ChatApplication
A Real-time chat server and client.

The server can handle multiple client connections. Each time any of the users send a message, all the other users recieve it. All the clients are connected centrally to the server and not to each other. Multiple clients can be handled using multithreading or asynchrous framework. 'asyncio', python's async framework has been used in this project.

 Backend pattern WebSocket has been used to implement the problem statement.
A websocket allows bidrectional communication on HTTP.

How to test the project?
- Download the following dependency:
    - pip3 install websocket
- On terminal, run the python files for server and all clients.
