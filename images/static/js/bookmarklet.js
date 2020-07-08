(function(){

      var hellp = document.getElementById("hellp")
      var hellp1 = document.getElementById("hellp1")
      var hellp2 = document.getElementById("hellp2")
      var hellp3 = document.getElementById("hellp3")
      var hellpSuper = document.getElementById("hellpSuper")

    if (hellp) {
      function updateSubmitButton1() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((minutes<31)) {
                    var currentTime = new Date();
                    var milliseconds = currentTime.getMilliseconds();
                    console.log('hhhh22', milliseconds);
                    document.getElementById("hellp").click()
              }
       }

      function updateSubmitButton() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((hours === 8 && minutes === 29 && seconds > 23 && milliseconds>0 || hours === 8 && minutes === 30 && seconds < 15 && milliseconds>0)) {
                clearInterval(yyy);
                setInterval(updateSubmitButton1, 300);
              }
          }
    }else if (hellp1){
      function updateSubmitButton1() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((minutes<31)) {
                    var currentTime = new Date();
                    var milliseconds = currentTime.getMilliseconds();
                    console.log('hhhh22', milliseconds);
                    document.getElementById("hellp1").click()
              }
       }

      function updateSubmitButton() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((hours === 8 && minutes === 29 && seconds > 23 && milliseconds>75 || hours === 8 && minutes === 30 && seconds < 15 && milliseconds>75)) {
                clearInterval(yyy);
                setInterval(updateSubmitButton1, 300);
              }
          }
        }
        else if (hellp2){
      function updateSubmitButton1() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((minutes<31)) {
                    var currentTime = new Date();
                    var milliseconds = currentTime.getMilliseconds();
                    console.log('hhhh22', milliseconds);
                    document.getElementById("hellp2").click()
              }
       }

      function updateSubmitButton() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((hours === 8 && minutes === 29 && seconds > 23 && milliseconds>150 || hours === 8 && minutes === 30 && seconds < 15 && milliseconds>150)) {
                clearInterval(yyy);
                setInterval(updateSubmitButton1, 300);
              }
          }
        }
        else if (hellp3){
      function updateSubmitButton1() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((minutes<31)) {
                    var currentTime = new Date();
                    var milliseconds = currentTime.getMilliseconds();
                    console.log('hhhh22', milliseconds);
                    document.getElementById("hellp3").click()
              }
       }

      function updateSubmitButton() {
          var currentTime = new Date();
          var milliseconds = currentTime.getMilliseconds();
          var hours = currentTime.getHours();
          var minutes = currentTime.getMinutes();
          var seconds = currentTime.getSeconds();

              if ((hours === 8 && minutes === 29 && seconds > 23 && milliseconds>225 || hours === 8 && minutes === 30 && seconds < 15 && milliseconds>225)) {
                clearInterval(yyy);
                setInterval(updateSubmitButton1, 300);
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

    var yyy=setInterval(updateSubmitButton, 1);
})()