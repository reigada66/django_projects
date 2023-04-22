

$(document).ready(function() {
    var fileToRead = document.getElementById("upimagem");
    var imagem = document.getElementById("imagem");

    fileToRead.addEventListener("change", function(event) {
//        var files = fileToRead.files;
        imagem.src = URL.createObjectURL(fileToRead.files[0]);


    }, false);


});
