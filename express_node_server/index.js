var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var path = require('path');

// Serve index.html
app.get('/', function(req, res){
  res.sendFile(path.join(__dirname, '../client', 'index.html'));
});

// Handle all socket.io connections and messages
io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  socket.on('chat message', function(msg){
    console.log("[new_message] " + msg);
    io.emit('chat message', msg);
  });
});

//
http.listen(3000, function(){
  console.log('listening on *:3000');
});
