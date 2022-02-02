#!/usr/bin/node

const fs = require('fs');
const Filefirt = process.argv[2];
const Filesecond = process.argv[3];

fs.writeFile(Filefirt, Filesecond, function (err) {
  if (err) {
    console.log(err);
  }
});
