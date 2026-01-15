function login() {
    const username = document.getElementById("username").value;

    if (!username) {
        alert("Enter name");
        return;
    }

    localStorage.setItem("isLoggedIn", "true");
    localStorage.setItem("username", username);

    window.location.href = "index.html";
}

const loginBtn = document.getElementById("loginBtn");
const logoutBtn = document.getElementById("logoutBtn");

if (localStorage.getItem("isLoggedIn")) {
    loginBtn.style.display = "none";
    logoutBtn.style.display = "inline-block";
} else {
    loginBtn.style.display = "inline-block";
    logoutBtn.style.display = "none";
}

function logout() {
    localStorage.clear();
    window.location.href = "login.html";
}

document.addEventListener("DOMContentLoaded", () => {
    const authBtn = document.getElementById("authBtn");

    if (!authBtn) return;

    if (localStorage.getItem("isLoggedIn")) {
        authBtn.innerText = "Logout";
    } else {
        authBtn.innerText = "Login";
    }
});

function handleAuth() {
    if (localStorage.getItem("isLoggedIn")) {
        // LOGOUT
        localStorage.clear();
        alert("👋 Logged out successfully");
        window.location.href = "login.html";
    } else {
        // LOGIN
        window.location.href = "login.html";
    }
}
