type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    let v1 = await promise1
    let v2 = await promise2
    return v1+v2
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */