#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Define a recursive function to fetch character data
const fetchCharacters = (characterUrls, index) => {
  // Base case: stop recursion when all characters are fetched
  if (index === characterUrls.length) return;

  // Make a request to fetch character data
  request(characterUrls[index], (err, response, body) => {
    if (err) {
      // Handle error if request fails
      throw err;
    } else {
      // Parse the response body as JSON
      const characterData = JSON.parse(body);
      // Output the name of the character
      console.log(characterData.name);
      // Recursively call the function to fetch the next character
      fetchCharacters(characterUrls, index + 1);
    }
  });
};

// Make a request to fetch movie data
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) {
    // Handle error if request fails
    throw err;
  } else {
    // Parse the response body as JSON
    const movieData = JSON.parse(body);
    // Extract character URLs from movie data
    const characterUrls = movieData.characters;
    // Start fetching characters by calling the fetchCharacters function
    fetchCharacters(characterUrls, 0);
  }
});
