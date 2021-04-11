var timeout = null;
var flashing = false;
var green = false;
var mobile = false;
var restartWait = Date.now();
var sound = new Audio();
sound.volume = 0;
sound.muted = true;
sound.src = "/utilities/randomtimer/alarm.mp3";

function load() {
	if (localStorage.getItem("RandomTimer-range") !== null) {
		try {
			var values = JSON.parse(localStorage.getItem("RandomTimer-range"));
			document.getElementById("min").value = values.min;
			document.getElementById("max").value = values.max;
		} catch (e) {
			localStorage.removeItem("RandomTimer-range");
		}
	}
}

load();

document.getElementById("start").onclick = function (e) {
	if (sound.muted) {
		sound.play();
		setTimeout(function () {
			sound.volume = 1;
			sound.muted = false;
		}, 1000);
	}
	if (Date.now() - restartWait < 500) {
		return;
	}
	var min = parseInt(document.getElementById("min").value, 10);
	var max = parseInt(document.getElementById("max").value, 10);
	var reload = false;
	if (min < 1) {
		min = 1;
		reload = true;
	}
	if (max < 2) {
		max = min + 1;
		reload = true;
	}
	if (min > max) {
		var temp = max;
		max = min;
		min = temp;
		reload = true;
	}
	localStorage.setItem("RandomTimer-range", JSON.stringify({
		min: min,
		max: max
	}));
	if (reload) {
		load();
	}
	var sec = getRandom(min, max);
	document.getElementById("settings").hidden = true;
	document.getElementById("countdown").hidden = false;
	flashing = false;
	document.body.style.backgroundColor = "#000000";
	if (timeout) {
		clearTimeout(timeout);
	}
	timeout = setTimeout(function () {
		green = true;
		flashing = true;
		timeout = null;
		sound.play();
		document.getElementById("countdown").hidden = true;
		document.getElementById("done").hidden = false;
	}, sec * 1000);
}

window.onclick = function () {
	if (flashing) {
		reset();
		restartWait = Date.now();
	}
}

document.getElementById("cancel").onclick = function (e) {
	if (timeout) {
		clearTimeout(timeout);
	}
	reset();
}

window.ontouchstart = function () {
	if (flashing) {
		reset();
		restartWait = Date.now();
	}
	if (!mobile) {
		var elements = document.getElementsByClassName("clickWord");
		for (var i = 0; i < elements.length; i++) {
			elements[i].innerText = "Touch";
		}
		mobile = true;
	}
}

function reset() {
	flashing = false;
	document.getElementById("countdown").hidden = true;
	document.body.style.backgroundColor = "#FFFFFF";
	document.getElementById("done").hidden = true;
	document.getElementById("settings").hidden = false;
}

setInterval(function () {
	if (flashing) {
		if (green) {
			document.body.style.backgroundColor = "#00FF00";
		} else {
			document.body.style.backgroundColor = "#FF0000";
		}
		green = !green;
	}
}, 200);

sound.addEventListener("ended", function () {
	if (flashing) {
		this.currentTime = 0;
		this.play();
	}
}, false);

function getRandom(min, max) {
	min = parseInt(min, 10);
	max = parseInt(max, 10);
	if (max < min) {
		var temp = max;
		max = min;
		min = temp;
	}
	return Math.floor(Math.random() * (max - min + 1)) + min;
}