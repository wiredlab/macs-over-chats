from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

import inspect

def myname():
    return(inspect.stack()[1][3])


@socketio.on('trial_new', namespace='/trial')
def trial_new(message):
    """Sent by Receiver to begin a new trial.
    message contains configuration for the particular trial.
    Resets ready status of all clients.
    Config is sent to clients."""
    room = session.get('room')
    name = session.get('name')
    print(myname(), room, name, message)
    emit('trial_new', message, room=room)


@socketio.on('trial_ready', namespace='/trial')
def trial_ready(message):
    """Sent by a Client to indicate they are ready to begin.
    Broadcast name to all clients."""
    room = session.get('room')
    name = session.get('name')
    print(myname(), room, name, message)
    emit('trial_ready', {'name':name}, room=room)


@socketio.on('trial_start', namespace='/trial')
def trial_start(message):
    """Sent by Receiver when starting the trial timer.
    Broadcast the message to all clients."""
    # the event itself is sufficient, so no message content
    room = session.get('room')
    name = session.get('name')
    print(myname(), room, name, message)
    emit('trial_start', {}, room=room, include_self=False)


@socketio.on('trial_end', namespace='/trial')
def trial_end(message):
    """Sent by Receiver to stop a trial.
    Broadcast to clients so they know to stop transmitting."""
    room = session.get('room')
    emit('trial_end', message, room=room)
    print(myname(), room, name, message)


@socketio.on('packet_receive', namespace='/trial')
def packet_receive(message):
    """Sent by Receiver upon receiving an apparently complete packet.
    Broadcast to clients so they can N/ACK."""
    #timestamp
    room = session.get('room')
    emit('packet_receive', message, room=room)
    print(myname(), room, name, message)



@socketio.on('packet_send', namespace='/trial')
def packet_send(message):
    """Sent by Client when the random timer expires and the User
    begins to read the frame contents.

    No broadcast to others, just for logging."""
    room = session.get('room')
    name = session.get('name')
    #log room,name,frame
    print(myname(), room, name, message)


@socketio.on('packet_ack', namespace='/trial')
def packet_ack(message):
    """Sent by client when declaring reception of a packet.
    'ack' is a boolean."""
    room = session.get('room')
    name = session.get('name')
    ack = message['ack']
    #log (room, name, ack)
    print(myname(), room, name, message)









@socketio.on('joined', namespace='/trial')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)
    print(myname(), room, name, message)


@socketio.on('text', namespace='/trial')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)
    print(myname(), room, name, message)


@socketio.on('left', namespace='/trial')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    name = session.get('name')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)
    print(myname(), room, name, message)

