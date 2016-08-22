const BASEURL = "http://chateau208.mynetgear.com/ril-server";

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
        tagEl.appendChild(tag);
    }

    return document.importNode(template.content, true);
};

let load = function(tags=null) {
    let c = new RilClient(BASEURL);
    c.all(e => {
        if (e.target.status == 200) {
            let res = JSON.parse(e.target.response);
            let target = document.querySelector('#content');
            let tagcloud = document.querySelector('#tagcloud');
            target.innerHTML = '';
            tagcloud.innerHTML = '';
            for (doc of res['document']) {
                if (!tags || doc['tags'].indexOf(tags) != -1) {
                    let row = createRow(doc['id'], doc['url'], doc['tags'])
                    target.appendChild(row);
                }
            }

            for (t of res['tags']) {
                let tag = createTag(t)
                tagcloud.appendChild(tag);
            }
        }
    });
};

let add = function() {
    let formData = new FormData(document.querySelector("#addForm"));
    let c = new RilClient(BASEURL);

    c.add(formData, e => {
        if (e.target.status == 200) {
            load();
            console.log('Great success.');
        }
    });
};

let del = function(id) {
    let c = new RilClient(BASEURL);
    c.del(id, e => {
        console.log('done');
        if (e.target.status == 200) {
            load();
            console.log('Great success.');
        } else {
            console.log(`Not so great ${e.target.status}`);
        };
    });
};

load();
