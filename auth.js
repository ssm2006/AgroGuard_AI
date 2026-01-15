const isLoggedIn = localStorage.getItem("isLoggedIn");

if (!isLoggedIn) {
    window.location.href = "login.html";
}
