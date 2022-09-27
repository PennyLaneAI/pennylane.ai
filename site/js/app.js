
const plLogo = `
 ////////,,,,,,,    /////////////////////////////*                                                       
///////###,,,,,,,,,#///////////////////////////////                                                      
////////###(,,,,,,,,####//////////////////////////                                                       
  ////////###,,,,,,,,,#####(/////////////////////                                                        
   ///////////*,,,,,,,,,,,,,,,,     ////////////                                                         
     /////////// ,,,,,,,,,,,,,,,,  ///////////                                                           
      ///////////    ,,,,,,,,,,,,////////////                                                            
       ,///////////    ,,,,,,,,,#//////////                                                              
         ///////////   ,,,,,,,,##/////////                                                               
          ////////////  ,,,,,,###///////                                                                 
            /////////// ,,,,,,,##//////                                                                  
             ///////////(,,,,,,,,,                                                                       
               /////////##,,,,,,,,                                                                       
                ////////###,,,,,,,                                                                       
                  ///////####,,,,                                                                        
                   ///////////                                                                           
                    ./////////                                                                           
                      ///////                                                                            
--------------------------------------------------------
Contribute at: https://github.com/PennyLaneAI/pennylane  
--------------------------------------------------------
`;

// a key map of allowed keys
const allowedKeys = {
  37: 'left',
  38: 'up',
  39: 'right',
  40: 'down',
  65: 'a',
  66: 'b'
};

// the 'official' Konami Code sequence
const konamiCode = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a'];

// a variable to remember the 'position' the user has reached so far.
var konamiCodePosition = 0;

function konamiListener(e) {
  // get the value of the key code from the key map
  var key = allowedKeys[e.keyCode];
  // get the value of the required key from the konami code
  var requiredKey = konamiCode[konamiCodePosition];
  // compare the key with the required key
  if (key == requiredKey) {

    // move to the next key in the konami code sequence
    konamiCodePosition++;

    // if the last key is reached, activate cheats
    if (konamiCodePosition == konamiCode.length) {
      konamiPower();
      konamiCodePosition = 0;
    }
  } else {
    konamiCodePosition = 0;
  }
}

function konamiPower() {
  new cursoreffects.ghostCursor();
}

function onDocumentLoad() {
  console.log(plLogo)
}

document.addEventListener('keydown', konamiListener);
document.addEventListener("DOMContentLoaded", onDocumentLoad);
