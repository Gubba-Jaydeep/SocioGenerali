 var name=document.getElementById("uname").innerHTML;
 localStorage.setItem('name',JSON.stringify(name));
     console.log(name);

     // $('#harsha').click(function () {
     //     console.log("working");
     //     let email = $("#email").html();
     //    window.open("https://mail.google.com/mail/?view=cm&fs=1&to="+email+"&su=SUBJECT&body=BODY&bcc=someone.else@example.com");
     // });