function check() {
    var bt = document.getElementById('btSubmit');
    const passValue = document.getElementById("pass").value.trim(); 
    if (document.getElementById("pass").value == document.getElementById("cpass").value )
    {
      if(passValue.length >=4){
        bt.disabled=false
        bt.value="SIGN UP"
        bt.style.cssText='cursor: pointer';
        document.getElementById("message").style.cssText='color:green; position:relative;top:13px;font-weight:bold;';
        document.getElementById("message").innerHTML = " password matching";
      }
      else{
        bt.disabled=true
        bt.value=""
        bt.style.cssText='background:#e33629;'
        document.getElementById("message").style.cssText='color:red; position:relative;top:13px;font-weight:bold;';
        document.getElementById("message").innerHTML = "Enter min. 4 digit password";
       }  
    } 
    else {
      bt.disabled=true
      bt.value=""
      bt.style.cssText='background:#e33629;'
      document.getElementById("message").style.cssText='color:red; position:relative;top:13px;font-weight:bold;';
      document.getElementById("message").innerHTML = "password not matching";
    }
  }



function closeAlert() {
    var customAlert = document.getElementById("customAlert");
    customAlert.style.opacity = "0";
    setTimeout(function() {
        customAlert.style.display = "none";
    }, 300);
}


window.onload = function() {
  var showAlert = {% if show_alert %}true{% else %}false{% endif %};
  if (showAlert) {
      // Set a timeout to close the alert after 3 seconds
      setTimeout(function() {
          closeAlert();
      }, 2500);
  }
};