$(document).ready(function(){

    $(".camera_icon").on('click',function(){
        console.log("ggg");
        $("#ggg").click();
    });

    $("#ggg").on('change', function() {
        $("#profile_button").click();
    });
//          $(".topnav").hide();
//    $(".glyphicon").on("click", function () {
//        var txt = $(".content").is(':visible') ? 'Read More' : 'Read Less';
//        $(".show_hide").text(txt);
//        $(this).next('.content').slideToggle(200);
//        if ($(".topnav").is(":visible")) {
//            $(".topnav").css("display", "none");
//        }
//    });
//        $(".user_photo").on('click',function(){
//            $(".img-responsive-big").attr("src", $(this).data('url'));
//            $(".modal-one").text($(this).data('like'));
//        });

    $( document ).ajaxStop(function() {
        console.log('hello');
        $(".user_photo").on('click',function(){
            $(".img-responsive-big").attr("src", $(this).data('url'));
            $(".modal-one").text($(this).data('like'));
        });
        $(".user_photo").on('click',function(){
            $(".img-responsive-big").attr("src", $(this).data('url'));
            $(".modal-one").text($(this).data('like'));
        });
    })
});