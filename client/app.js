let load = function() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8000/all', true);

    xhr.onload = function (e) {
        if (this.status == 200) {
            // Target
            let target = document.querySelector('#content');
            for (doc of JSON.parse(this.response)['document']) {
                // Setup element
                let t = document.querySelector('#urlrow');
                let a = t.content.querySelector('.url');
                a.innerHTML = doc['url'];
                a.setAttribute('href', doc['url']);

                // Insert
                var clone = document.importNode(t.content, true);
                target.append(clone);
            }
        }
    }
    xhr.send();
}

load();
