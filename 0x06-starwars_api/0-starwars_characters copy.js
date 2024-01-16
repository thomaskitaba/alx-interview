#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';

request(endPoint + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    //
    const artists = JSON.parse(body).characters;
    artists.map((artist) => printCharacter(artist));
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});

function printCharacter (actor) {
  // console.log(actors);
  request(actor, function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      console.log(JSON.parse(body).name);
    } else {
      console.log('problem occured' + response.statusCode);
    }
  });
}
