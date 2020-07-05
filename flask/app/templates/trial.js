var socket;
var timeout = null;

$(document).ready(function(){
    socket = io.connect('http://' + document.domain + ':' + location.port + '/trial');
    socket.on('connect', function() {
        socket.emit('joined', {});
    });
    
    socket.on('status', function(data) {
        $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    
    socket.on('message', function(data) {
        $('#chat').val($('#chat').val() + data.msg + '\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    
    socket.on('trial_new', function(data) {
        // TODO
        // clear ready flag of participants
    });
    
    socket.on('trial_ready', function(data) {
        // TODO
        // set ready flag of participants
    });
    
    socket.on('trial_start', function(data) {
        // TODO
        // start timer
        // set "trial in progress" indicator
    });
    
    socket.on('trial_end', function(data) {
        // TODO
        // stop timer
        // set "idle" indicator
    });
    
    socket.on('packet_receive', function(data) {
        // TODO
    });
    
    socket.on('packet_send', function(data) {
        // TODO
    });
    
    $('#text').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code == 13) {
            text = $('#text').val();
            $('#text').val('');
            socket.emit('text', {msg: text});
        }
    });
});

function trial_ready() {
    socket.emit('trial_ready', {msg: 'ready'});
}

function packet_send(frame) {
    // generate frame if needed
    if (need_frame) {
        current_frame = generate_frame(config);
    }
    
    // delay: value of random timer that just expired
    // frame: string of letters sent
    socket.emit('packet_send', {frame: current_frame, delay: delay});
    // display to user
}

function packet_ack(b) {
    if (b) {
        need_frame = true;
    } else {
        need_frame = false;
    }
    socket.emit('packet_ack', {ack: b});
}

function frame2words(frame) {
    // TODO
    // convert N-characters to N-phonetic alphabet words
    return s;
}

function leave_room() {
    socket.emit('left', {}, function() {
        socket.disconnect();

        // go back to the login page
        window.location.href = "{{ url_for('main.index') }}";
    });
}



/*
 * start_trial()
 *
 * called by Receiver to begin a trial
 *
 * sends "trial_start" event to all Transmitters
 */
function start_trial() {
    socket.emit('trial_start', trial_config);
}

/*
 * rand_exp(mean)
 *
 * Sample an exponential random variable.
 *
 * Input: mean - mean value
 *
 * Return: sample value
 *
 * https://en.wikipedia.org/wiki/Exponential_distribution#Generating_exponential_variates
 * z = -ln(U) / lambda
 * lambda = 1/mean
 */
function rand_exp(mean) {
    return -1 * mean * Math.log(Math.random());
}

function setTimer(sec) {
    timeout = setTimeout(packet_send, sec * 1000);
}
