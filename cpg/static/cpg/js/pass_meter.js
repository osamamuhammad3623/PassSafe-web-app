var strength = {
    0: "Real bad!",
    1: "Bad!",
    2: "Still bad!",
    3: "Could be better!",
    4: "Strong!"
  }
  
  var password = document.getElementById('password');
  var meter = document.getElementById('password-strength-meter');
  var text = document.getElementById('password-strength-text');
  
  password.addEventListener('input', function()
  {
    var val = password.value;
    var result = zxcvbn(val);
  
    // Update the password strength meter
    meter.value = result.score;
   
    // Update the text indicator
    if(val !== "") {
        text.innerHTML = "<strong>" + strength[result.score] + "</strong>"; 
    }
    else {
        text.innerHTML = "";
    }
  });

  function show() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }