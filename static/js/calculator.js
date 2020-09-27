var prev = 0
var curr = 0
var prevop = "plus"
var prevbutton = false
var prevequals = false
var dark = true


function theme() {
    if (dark) {
        document.documentElement.style.backgroundColor = "white";
        document.getElementById('calc-display').style.backgroundColor = "rgb(0, 116, 161)";
        dark = false;
        //console.log(dark)
    } else {
        document.documentElement.style.backgroundColor = "rgb(22, 22, 22)";
        document.getElementById('calc-display').style.backgroundColor = "rgb(0, 25, 49)";
        dark = true; 
        //console.log(dark);
    }
}
function singOp(op) {
    if (prevequals) {
        if (op == 'negate') prev *= -1
        else if (op == 'square') prev *= prev
        else if (op == 'sqrt') prev = Math.sqrt(prev)
        document.getElementById('calc-display').value = prev
    } else {
        if (op == 'negate') curr *= -1
        else if (op == 'square') curr *= curr
        else if (op == 'sqrt') curr = Math.sqrt(curr)
        document.getElementById('calc-display').value = curr
    }
    prevequals = false
    console.log("neg")
}

function operate() {
    switch (prevop) {
        case 'equals':
            break;
        case 'plus':
            prev += curr
            break
        case 'minus':
            prev -= curr
            break
        case 'times':
            prev *= curr
            break
        case 'mod':
            prev %= curr
            break
        case 'divide':
            if (curr == 0) {
                prev = 0
                curr = 0
                alert("Arithmetic Error: Divide by Zero")
            }
            else { prev /= curr }
            break
        default:
            console.log('')
    }
}

function doMath(num, op, type) {
    if (type){
        if(prevequals) prev = 0
        curr *= 10
        curr += num
        prevbutton = false
        document.getElementById('calc-display').value = curr
    } else if (op == 'clear') {
        prevop = "plus"
        prev = 0
        curr = 0
        prevbutton = false
        prevequals = false
        document.getElementById('calc-display').value = prev
    }
    else {
        if(!prevbutton) operate()
        if (op == 'equals') {
            prevop = 'plus'
            curr = 0
            prevequals = true
        } else {
            if(!prevbutton) curr = 0
            prevop = op
            prevequals = false   
        }
        document.getElementById('calc-display').value = prev
        prevbutton = true
        console.log(op)
        
    }
}