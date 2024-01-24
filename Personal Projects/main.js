const oAuth = "tiperfq6664yoquc1gyk37bdp7sgjo"
const nick = 'Skairry';

const socket = new WebSocket("wss://irc-ws.chat.twitch.tv:443");

socket.addEventListener('open', () => {
    socket.send(`PASS ouath:${oAuth}`);
    socket.send(`NICK ${nick}`);
});

socket.addEventListener('message', event => {
    console.log(event.data);
})