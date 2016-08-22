class Ajax {
    constructor() {
        this.worker = new Worker('worker.js')
    }

    mkCallbackWrapper(callback) {
        return e => {
            callback(e);
        };
    }

    request(type, url, payload, callback) {
        let xhr = new XMLHttpRequest();
        xhr.open(type, url, true);
        xhr.onload = this.mkCallbackWrapper(callback);

        xhr.send(payload);
    }
}
