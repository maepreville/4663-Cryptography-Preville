## A08 - Public Key Encryption
### Mae-Jeanne Preville 
### Description:

This project will use an existing python library called cryptography (appropriately named) to use public key encryption to encrypt and decrypt messages sent between two entities. We need a method to allow two scripts to "talk" or communicate over a network. This means NOT on the same computer. Using a library called Flask, we can do that. A Flask server runs and "listens" or monitors a "port" on a computer. When requests are directed to that port either from an internal request or an external request, they are handled by the process monitoring the port, or in our case Flask.

A request can either ask for information (GET) or send information (POST). There are variations of requests that imply different actions, but we will get by with GET and POST for our project. Below you see a general picture of what is happening.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [client.py](./client.py)   | Sends and receives requests from server.py   |
|   2   | [server.py](./server.py)   | Handles requests from client.py as well as other clients  |


### Instructions

- Python was used for this project.

### Sources

