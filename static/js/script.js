
function SendForWard() {
    fetch('/ForWard')
}

function SendBackWard() {
    fetch('/BackWard')
}

function SendRight() {
    fetch('/Right')
}

function SendLeft() {
    fetch('/Left')
}
function SendStop() {
    fetch('/Stop')
}

function forwardLed() {
    fetch('/forwardLed')
}

function backwardLed() {
    fetch('/backwardLed')
}

function power() {
    fetch('/power')
}

function buzzer() {
    fetch('/buzzer')
}

function music() {
    fetch('/music')
}

function V_motor() {
    fetch('/V_motor')
}

// ************************************************************************************************************
function SendValue() {
    var sliderValue = document.getElementById("speed").value;
    var speedNum = document.getElementById("speed-num");
    var speedCar = document.getElementById("speed-car");


    fetch('/get_value', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({value: sliderValue})
    });
    speedNum.innerHTML = `${sliderValue} `
    if( +sliderValue < 50){
        speedCar.style.backgroundColor = "green"
    }
    else if(+sliderValue>50 && +sliderValue < 80){
        speedCar.style.backgroundColor = "blue"
    }
    else{
        speedCar.style.backgroundColor = "red"
    }

}


// start
let isMouseDown = false;
var btnActive = ''
let btn = document.querySelectorAll('.btn')
console.log(btn)

btn.forEach( item => {
        
        item.addEventListener('mousedown', () => {
        isMouseDown = true;
        btnActive = item.innerHTML;

        });

        item.addEventListener('mouseup', () => {
            isMouseDown = false;
        });

        item.addEventListener('mouseleave', () => {
            isMouseDown = false;
        });

    })

setInterval(() => {
    if (isMouseDown) {
        console.log(btnActive);
        
        if(btnActive == 'ForWard')
        {
            SendForWard()
        }else if(btnActive == 'BackWard'){
            SendBackWard()
        }else if(btnActive == 'Left'){
            SendLeft()
        }else if(btnActive == 'Right'){
            SendRight()
        }else if( btnActive == 'Stop'){
            SendStop()
        }
        else{
            V_motor()
        }
        
        
    }
}, 100);



// end 