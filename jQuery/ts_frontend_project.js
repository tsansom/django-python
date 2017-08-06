var p1Name = prompt('Player 1: Enter your name, you will be BLUE');
var p1Color = 'rgb(104, 160, 249)';
var p1ColorName = 'BLUE';

var p2Name = prompt('Player 2: Enter your name, you will be RED');
var p2Color = 'rgb(249, 104, 104)';
var p2ColorName = 'RED';

// working don't touch
function checkBottom(colNum) {
    for (rowNum=5; rowNum>-1; rowNum--) {
        var buttonColor = returnColor(rowNum, colNum)
        if (buttonColor === 'rgb(128, 128, 128)') {
            return rowNum
        }
    }
}

// working don't touch
function returnColor(rowNum, colNum) {
    return $('table').find('tr').eq(rowNum).find('td').eq(colNum).find('button').css('background-color')
}

//working dont' touch
function checkWinner() {
    if (horizWinner() || verticalWinner() || diagonalWinner()) {
        return true
    } else {
        return false
    }
}



//working don't touch
function diagonalWinner() {
    for (row=0; row<6; row++) {
        for (col=0; col<5; col++) {
            if (colorsMatch(returnColor(row, col), returnColor(row+1, col+1), returnColor(row+2, col+2), returnColor(row+3, col+3))) {
                return true
            }
        }
        for (col=5; col>0; col--) {
            if (colorsMatch(returnColor(row, col), returnColor(row+1, col-1), returnColor(row+2, col-2), returnColor(row+3, col-3))) {
                return true
            }
        }
    }
    return false
}

//working don't touch
function verticalWinner() {
    for (col=0; col<6; col++) {
        for (row=5; row>2; row--) {
            if (colorsMatch(returnColor(row, col), returnColor(row-1, col), returnColor(row-2, col), returnColor(row-3, col))) {
                return true
            }
        }
    }
    return false
}

//working don't touch
function horizWinner() {
    for (row=5; row>-1; row--) {
        for (col=0; col<3; col++) {
            if (colorsMatch(returnColor(row, col), returnColor(row, col+1), returnColor(row, col+2), returnColor(row, col+3))) {
                return true
            }
        }
    }
    return false
}

//working don't touch
function colorsMatch(c1, c2, c3, c4) {
    if (c1 !== 'rgb(128, 128, 128)' && c1 === c2 && c2 === c3 && c3 === c4) {
        return true
    } else {
        return false
    }
}

// logic goes here
var game_on = true;
var table = $('table tr');

//start with player 1
var currentPlayer = 1;
var currentName = p1Name;
var currentColor = p1Color;
var currentColorName = p1ColorName;

$('#whosturn').text(currentName + ": it's your turn, please click a column to drop your " + currentColorName + " chip");

$('.board button').on('click', function(){

    var col = $(this).closest('td').index()

    var row = checkBottom(col)

    $('table').find('tr').eq(row).find('td').eq(col).find('button').css('background-color', currentColor)

    if (checkWinner()) {
        alert(currentName + ' is the winner!!! Reload to play again')
        return
    } else {
        currentPlayer *= -1;
        if (currentPlayer === 1) {
            currentName = p1Name;
            currentColor = p1Color;
            currentColorname = p1ColorName;
        } else {
            currentName = p2Name;
            currentColor = p2Color;
            currentColorName = p2ColorName;
        }
        $('#whosturn').text(currentName + ": it's your turn, please click a column to drop your " + currentColorName + " chip");
    }

})
