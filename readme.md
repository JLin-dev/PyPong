# __PyPong__

Hi everyone, this is my first time using pyton for a looooonng time. Last time I learned python was in a data science course which is years ago. And this is my first indivual big projct with python. I will be using pygame to develope pong game this is also why is called PyPong. I am aimming to learn more about python in this project and in addation muti-player networking, and perhaps AI traning as well. In this open source repo you will see my ~~spaghetti~~ some what organize code.

## __Env setting__

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

---

## __server.py__

Test code area: really interesting way to stop a server by using keyboard package. `keyboard.onpress()` can capture python events which means this is running on a seperate thread and does not block the main program. Inside the parameter we can put in function (without calling the function but the function when we are going to invoke when the events happen). Which we dont include () when we call the handling function. In the provided code demo when we are going to put in a function that contains two variable in the params we can call it by creating an anonymous function which accpet both event and server_socket. By doing this we can pass in two var without invoking the function in the first place. The event right after lambda is automatically pass in by the key press event.