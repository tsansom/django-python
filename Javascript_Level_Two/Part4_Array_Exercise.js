// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function add(){
  var name = prompt('Enter a name to add to roster');
  if (roster.indexOf(name) == -1){
    roster.push(name);
  } else {
    console.log(name + ' already in roster, cannot add')
  }

}

// REMOVE STUDENT


// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript

function remove(){
  var name = prompt('Enter a name to remove from roster');
  if (roster.indexOf(name) != -1) {
    roster.splice(roster.indexOf(name), 1)
  } else {
    console.log(name + ' not in roster, cannot remove')
  }
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.

function display(){
  console.log(roster)
}

// Start by asking if they want to use the web app
var request = ''
var start = prompt('Would you like to use the roster app? (y or n)');
if (start === 'y') {
  while (request != 'quit') {
    request = prompt('Please select an action: add, remove, display, or quit.')
    if (request == 'add') {
      add();
    }
    if (request == 'remove') {
      remove();
    }
    if (request == 'display') {
      display();
    }
  }
}

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
