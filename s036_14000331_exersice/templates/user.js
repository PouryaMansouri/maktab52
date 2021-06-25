function user_info(id) {
    for (var i of users) {
        if (i.id === id) break;
        document.getElementById("fname").innerText = i.firstname;
        document.getElementById("lname").innerText = i.lastname;
        document.getElementById("username").innerText = i.username;
        document.getElementById("phone").innerText = i.phone;
        document.getElementById("email").innerText = i.email;
        document.getElementById("code").innerText = i.ncode;
    }
}
