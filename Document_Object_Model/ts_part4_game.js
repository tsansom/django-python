var opts = [' ', 'X', 'O']

var boxes = document.querySelectorAll('td')

for (i=0; i<boxes.length; i++) {
  boxes[i].textContent = opts[0]
  boxes[i].addEventListener('click', function(){
    var ind = opts.indexOf(this.textContent)
    if (ind != 2){
      this.textContent = opts[ind+1]
    } else {
      this.textContent = opts[0]
    }
  })
}

var restart = document.querySelector('#b')

restart.addEventListener('click', function(){
  for (i=0; i<boxes.length; i++){
    boxes[i].textContent = opts[0]
  }
})
