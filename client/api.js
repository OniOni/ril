class RilClient {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
        this.ajax = new Ajax();
    }

    add(formData, callback) {
        console.log('add');
        this.ajax.queuableRequest('POST', `${this.baseUrl}/save`, formData, callback);
    }

    all(callback) {
        this.ajax.request('GET', `${this.baseUrl}/all`, null, callback);
    }

    del(id, callback) {
        let path = `${BASEURL}/${id}`;
        console.log(`Del ${id} -> ${path}`);
        this.ajax.request('DELETE', path, null, callback);
    }
}
