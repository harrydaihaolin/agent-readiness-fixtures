const api = require("./src/index.js");
if (api() !== "api") { process.exit(1); }
console.log("api ok");
