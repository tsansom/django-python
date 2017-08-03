var firstname = prompt('Enter first name');
var lastname = prompt('Enter last name');
var age = prompt('Enter age');
var height = prompt('Enter height in centimeters');
var petname = prompt('Enter the name of your pet');

if (firstname[0] == lastname[0]){
  if (age > 20 && age < 30){
    if (height >= 170){
      if (petname[petname.length - 1] == 'y'){
        console.log('Hello spy! Nice to see you')
      }
    }
  }
}
