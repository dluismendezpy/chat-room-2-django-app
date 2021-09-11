console.log('Probando')

document.querySelector('#room-name-input').focus();

document.querySelector('#room-name-submit').onclick = function (e) {
    let room = document.querySelector('#room-name-input').value;
    let user = document.querySelector('#username-input').value;
    let obj1 = urlID(8);
    let obj2 = urlID(12);
    window.location.replace(`${room} / ${obj1} /?username= ${user} ${obj2}`)
};

function urlID (length) {
    let result = '';
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let charactersLength = characters.length;

    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result;
}