document.querySelector('#room-name-input').focus();

document.querySelector('#room-name-submit').onclick = function (e) {
    var roomName = document.querySelector('#room-name-input').value;
    var userName = document.querySelector('#username-input').value;

    window.location.replace(roomName + '/?username=' + userName);
};