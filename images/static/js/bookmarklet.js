(function(){

      var hellp = document.getElementById("hellp")
      var hellpSuper = document.getElementById("hellpSuper")

    if (hellp) {
      function updateSubmitButton1() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();
          if ((hours === 8 && minutes === 29 && seconds > 15 && milliseconds>0 || hours === 8 && minutes === 30 && seconds < 30 && milliseconds>0)) {
            var currentTime = new Date();
            var milliseconds = currentTime.getMilliseconds();
            console.log('hhhh22', milliseconds);
            document.getElementById("hellp").click()
          }

       }
    }
    else if (hellpSuper){

      function updateSubmitButton() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((hours === 8 && minutes === 29 && seconds > 28 && milliseconds>0 || hours === 8 && minutes === 30 && seconds < 15 && milliseconds>0)) {

                for (i = 0; i < 8000; i++) {
                     var currentTime = new Date();
                     var milliseconds = currentTime.getMilliseconds();
                     document.getElementById("hellpSuper").click();
                     console.log(milliseconds)
                }
                clearInterval(yyy);
              }
          }
        }

    var yyy=setInterval(updateSubmitButton1, 300);
})()