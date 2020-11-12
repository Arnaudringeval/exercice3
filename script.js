var slide = new Array("images/IMG_20200719_010106.jpg", "images/IMG_20200719_163655.jpg", "images/IMG_20200719_163808.jpg", "images/IMG_20200719_172913.jpg");
var numero = 0;

function ChangeSlide(sens) {
    numero = numero + sens;
    if (numero < 0)
        numero = slide.length - 1;
    if (numero > slide.length - 1)
        numero = 0;
    document.getElementById("slide").src = slide[numero];
}

if (window.innerHeight > document.body.clientHeight)
    {document.getElementById('footer').style.position = 'fixed';}
 else {document.getElementById('footer').style.position = 'absolute';}