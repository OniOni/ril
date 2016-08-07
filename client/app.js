let createTag = function(tag) {
    let template = document.querySelector('#tagrow');
    let el = template.content.querySelector('.tag');
    el.innerHTML = tag;

    return document.importNode(template.content, true);
}
let createRow = function(url, tags) {
    let template = document.querySelector('#urlrow');
    let a = template.content.querySelector('.url');
    a.innerHTML = url;
    a.setAttribute('href', url);

    let tagEl = template.content.querySelector('.tags');
    tagEl.innerHTML = '';
    for (t of tags) {
        let tag = createTag(t);
        tagEl.append(tag);
    }

    return document.importNode(template.content, true);
};

let load = function() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8000/all', true);

    xhr.onload = function (e) {
        if (this.status == 200) {
            let target = document.querySelector('#content');
            for (doc of JSON.parse(this.response)['document']) {
                let row = createRow(doc['url'], doc['tags'])
                target.append(row);
            }
        }
    }
    xhr.send();
};

load();
