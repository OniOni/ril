class Ajax {
    constructor() {
        this.queue = [];
        // this.worker = new Worker('worker.js')

        var self = this;
        window.addEventListener('online', () => {
            console.log('Processing queue');
            for (let o of self.queue) {
                self.request(o.type, o.url, o.payload, o.callback);
            }
        });
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


    queueRequest(obj) {
        console.log('Queing request.')
        this.queue.push(obj);
    }

    queuableRequest(type, url, payload, callback) {
        if (!navigator.onLine) {
            console.log('No connection.');
            this.queueRequest({
                type: type,
                url: url,
                payload: payload,
                callback: callback
            })
        } else {
            this.request(type, url, payload, callback);
        }
    };
}
