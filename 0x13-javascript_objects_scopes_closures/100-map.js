#!/usr/bin/node
const list = require('./100-data.js').list;
const multiIdx = (value, index) => value * index;
const newlist = list.map(multiIdx);
console.log('Initial List:', list);
console.log('New List:', newlist);
