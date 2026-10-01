/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function (functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let completed = 0;

        if (!functions.length) {
            resolve(results);
        }

        functions.forEach((asyncFunc, index) => {
            asyncFunc()
                .then(result => {
                    results[index] = result;
                    completed++;
                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch(reject);
        });
    });
};