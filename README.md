# ChatApp
Demo Chat App to learn things, specifically sockets.io

The core of this was innitially created from: http://socket.io/get-started/chat/

### Running the node.js express server
`node` needs to be installed on your maching

1. `cd express_node_server`
2. `npm install`
3. `node index.js`

This will serve the client on `localhost:3000`.

### Running the python Flask server

1. `cd flask_server`
2. Optional but recommended: create a python virtualenv that packages will be installed to.
3. Optional activate created virtualenv
4. `pip install .`
5. `FLASK_APP=flask_server.flask_server flask run`

This will serve the client on `localhost:5000`.

### Client App
Run the server then open multiple tabs on `localhost:3000` or `localhost:5000`.  All tabs will see chat messages.


