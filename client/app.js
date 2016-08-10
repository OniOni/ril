let createTag = function(tag) {
    let template = document.querySelector('#tagrow');
    let el = template.content.querySelector('.tag');
    el.innerHTML = tag;
    el.setAttribute('onclick', `load('${tag}')`);

    return document.importNode(template.content, true);
}
let createRow = function(id, url, tags) {
    let template = document.querySelector('#urlrow');
    let a = template.content.querySelector('.url');
    a.innerHTML = url;
    a.setAttribute('href', url);

    let a2 = template.content.querySelector('.delete');
    a2.setAttribute('onclick', `del(${id})`);

    let tagEl = template.content.querySelector('.tags');
    tagEl.innerHTML = '';
    for (t of tags) {
        let tag = createTag(t);
        tagEl.append(tag);
    }

    return document.importNode(template.content, true);
};

let load = function(tags=null) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', "http://localhost:8000/all", true);

    xhr.onload = function (e) {
        if (this.status == 200) {
            let res = JSON.parse(this.response);
            let target = document.querySelector('#content');
            let tagcloud = document.querySelector('#tagcloud');
            target.innerHTML = '';
            tagcloud.innerHTML = '';
            for (doc of res['document']) {
                if (!tags || doc['tags'].indexOf(tags) != -1) {
                    let row = createRow(doc['id'], doc['url'], doc['tags'])
                    target.append(row);
                }
            }

            for (t of res['tags']) {
                let tag = createTag(t)
                tagcloud.append(tag);
            }
        }
    }
    xhr.send();
};

let add = function() {
    let formData = new FormData(document.querySelector("#addForm"));
    let xhr = new XMLHttpRequest();
    xhr.open('POST', "http://localhost:8000/save", true);

    xhr.onload = function (e) {
        if (this.status == 200) {
            load();
            console.log('Great success.');
        }
    }
    xhr.send(formData);
};

let del = function(id) {
    let url = `http://localhost:8000/${id}`;
    console.log(`Del ${id} -> ${url}`);

    let xhr = new XMLHttpRequest();
    xhr.open('DELETE', url, true);

    xhr.onload = function (e) {
        console.log('done');
        if (this.status == 200) {
            load();
            console.log('Great success.');
        } else {
            console.log(`Not so great ${this.status}`);
        };
    }
    xhr.send();
};

load();
