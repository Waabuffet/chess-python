var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);


var ipAddress = 'localhost';
var portNumber = 3000;

io.on('connection', function(socket) {
    console.log('a user connected');


    socket.on('piece_move', function(data) {
        console.log('piece moved');
        console.log(data);
    });


    socket.on('disconnect', function() {
        console.log('user disconnected');
    });
});

http.listen(portNumber, ipAddress, function() {
    console.log('listening on ' + ipAddress + ':' + portNumber);
});