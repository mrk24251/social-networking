(function(){

    function updateSubmitButton() {
      var currentTime = new Date();
      var milliseconds = currentTime.getMilliseconds();
      var hours = currentTime.getHours();
      var minutes = currentTime.getMinutes();
      var seconds = currentTime.getSeconds();
      var hellp = document.getElementById("hellp")
      var hellp2 = document.getElementById("hellp2")
      var lengthh= 3500;
      if (hellp2 === null) {
          if ((hours === 13 && minutes === 39 && seconds === 29 && milliseconds>0 )) {
            for (i = 0; i < lengthh; i++) {
                var currentTime = new Date();
                var milliseconds = currentTime.getMilliseconds();
                console.log('hhhh22', milliseconds);
                document.getElementById("hellp").click()
            }
          }
      }
        var lengthh= 3500;
      if (hellp === null) {
          if ((hours === 13 && minutes === 39 && seconds === 29 && milliseconds>14 )) {
            for (i = 0; i < lengthh; i++) {
                var currentTime = new Date();
                var milliseconds = currentTime.getMilliseconds();
                console.log('hhhh22', milliseconds);
                document.getElementById("hellp2").click()
            }
          }
      }
      }
    setInterval(updateSubmitButton, 10);
})()