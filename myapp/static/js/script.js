const SignUpForm = document.getElementById('SignUpForm');
const submitButton = document.getElementById('submitButton');

function checkFormFilled() {
    const username = SignUpForm.username.value.trim();
    const emailAddress = SignUpForm.emailAddress.value.trim();
    const password1 = SignUpForm.password1.value.trim();
    const password2 = SignUpForm.password2.value.trim();

    if (username === '' || emailAddress === '' || password1 === '' || password2 === '') {
        submitButton.disabled = true;
    } else {
        submitButton.disabled = false;
    }
}

