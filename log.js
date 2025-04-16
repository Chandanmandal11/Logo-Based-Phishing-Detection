$(document).ready(function () {
    $(".display").css("display", "none");
    $(".result").css("display", "none");

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('.image').css('background-image', 'url(' + e.target.result + ')');
                $('.image').hide();
                $('.image').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.display').show();
        $('.detect').show();
        $('.result').text('');
        $('.result').hide();
        readURL(this);
    });

    $('.detect').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
    });

    $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('.result').fadeIn(600);
                $('.result').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });

});