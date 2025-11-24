<script>
// Ask for username
let username = prompt("What is your username?");

// Student login
if (username === "student") {
    alert("Thank you.");
    setTimeout(() => {
        let password1 = prompt("Please input your password:");
        if (password1 === "123456") {
            alert("You are logged in as a student.");
        } else {
            alert("Incorrect password.\nRefresh page and try again.");
        }
    }, 1000);

// Teacher login
} else if (username === "teacher") {
    alert("Thank you.");
    setTimeout(() => {
        let password1 = prompt("Please input your password:");
        if (password1 === "qwerty") {
            alert("You are logged in as a teacher.");
        } else {
            alert("Incorrect password.\nRefresh page and try again.");
        }
    }, 1000);

// Everything else
} else {
    alert("Incorrect username. Please refresh page and try again.");
}
</script>
