# __PyPong__

Rarely use Python, first time using pygame. Nice warm up.

## __Env setting__

Most of things is just for my info.  
Check if pygame lib is instal: `pip show pygame`  
Using pygame lib: ```pip install pygame```  

---

## __Below are some notes for my self__

### __Local Network Deployment__

In this project I will be using UDP. The types of network protocol TCP(Transmission Control Protocol) or UDP(User Datagram Protocol). Where the first one provide more stable and ordered commication. The UDP offers a faster transmit of data but might drop pocket.

### __Server-Client Architecture__

Server:

- Handle game's core logic, including ball movement, collision detection, scoring and game state mangement.
- Syncing the game state to the clinet. Make sure connected clinet have consistent gameplay.
- Handling clinet input, clinet will send input in this case the only thing is the paddle movement to the server.  
- When a client connects to the server, the server should send the initial game state, including paddle positions, ball position, and game settings.
- Player should have a way to identify themselves to the server, allowing the server to differentiate between players and assign them to the correct paddles.
- The server needs to handle cases where a client disconnects unexpectedly, such as reassigning the disconnected player's paddle to an AI or notifying other players about the disconnection.

Clinet:

- Rendering the game graphic. This apply to all the clinet who is connecting the game.
- Sending input to the server.  

Scalability and Performance:

- Not going to handle scalabilty since this is local network. Only two player connect max.
- There will be optim when the depoly of local connection is successfully.  

