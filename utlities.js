function print() {
    console.log(...arguments)
}
function error() {
    console.error(...arguments)
}

module.exports = {
    error, print
}
