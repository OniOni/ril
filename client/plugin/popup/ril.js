let add = function(cb) {
    let formData = new FormData(document.querySelector("#addForm"));
    let xhr = new XMLHttpRequest();
    xhr.open('POST', "http://localhost:8000/save", true);

    xhr.onload = function (e) {
        if (this.status == 200) {
            console.log('Great success.');
        } else {
            console.log('Much disapointements...');
        }
        cb(e);
    }
    xhr.send(formData);
};

window.onload = function(e) {
    browser.tabs.query({active: true, currentWindow: true}, function(tabs) {
        if (tabs[0]) {
            let url = tabs[0].url;
            let input = document.querySelector('input[name=url]');
            input.setAttribute('value', url);

            console.log(url);
            console.log(input);
        }
    });
};

document.querySelector('input[type=submit]').onclick = function() {
    console.log('Yo');
    add(function(e) {
        window.close();
    });
}
