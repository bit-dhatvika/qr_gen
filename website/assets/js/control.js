button = document.getElementById('button2');
button.addEventListener("click", clicked);
function clicked(){
    email = document.getElementById('FormInput').value;
    console.log(email);
    window.location.replace("test/v1/?email="+email);
};
