const WebSocket = require('ws');
const port = 4000;
const server = new WebSocket.Server({ port });

server.on('connection', (socket) => {
  console.log('New client connected');
  socket.on('message', (message) => {
    console.log('Received:', message);
    // Echo back the message
    socket.send(message);
  });
  socket.on('close', () => console.log('Client disconnected'));
});

console.log(\`Realtime server is running on ws://localhost:\${port}\`);
