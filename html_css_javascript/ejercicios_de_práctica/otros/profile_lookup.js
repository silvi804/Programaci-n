// Setup
const contacts = [
  {
    firstName: "Akira",
    lastName: "Laine",
    number: "0543236543",
    likes: ["Pizza", "Coding", "Brownie Points"],
  },
  {
    firstName: "Harry",
    lastName: "Potter",
    number: "0994372684",
    likes: ["Hogwarts", "Magic", "Hagrid"],
  },
  {
    firstName: "Sherlock",
    lastName: "Holmes",
    number: "0487345643",
    likes: ["Intriguing Cases", "Violin"],
  },
  {
    firstName: "Kristian",
    lastName: "Vos",
    number: "unknown",
    likes: ["JavaScript", "Gaming", "Foxes"],
  },
];

function lookUpProfile(name, prop) {
  // Only change code below this line

  for (let i = 0; i < contacts.length; i++) {
    if (contacts[i]["firstName"] == name) {
      var exisProp = contacts[i].hasOwnProperty(prop);
      var existe = true;
      var numero = i;
      break;
    } else {
      var existe = false;
    }
  }

  if (existe == false) {
    var answer = "No such contact";
  } else if (exisProp == false) {
    var answer = "No such property";
    // Only change code above this line
  } else {
    var answer = contacts[numero][prop];
  }
  return answer;
}

// lookUpProfile("Akira", "likes");

console.log(lookUpProfile("Akira", "address"));
