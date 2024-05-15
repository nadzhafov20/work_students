const checkboxes = document.querySelectorAll('.def-checkbox');

checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('click', function () {
        checkboxes.forEach(function (otherCheckbox) {
            if (otherCheckbox !== checkbox) {
                otherCheckbox.checked = false;
            }
        });
    });
});

// pass-btn

const btnPass = document.querySelector('.pass-btn');
const passContent = document.querySelector('.pass-content input');

let isPasswordVisible = false;

btnPass.addEventListener('click', function () {
    if (isPasswordVisible) {
        passContent.type = 'password';
        isPasswordVisible = false;
    } else {
        passContent.type = 'text';
        isPasswordVisible = true;
    }
});

