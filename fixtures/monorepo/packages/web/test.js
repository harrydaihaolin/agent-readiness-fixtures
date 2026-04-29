const web = require("./src/index.js");
if (web() !== "web") { process.exit(1); }
console.log("web ok");
