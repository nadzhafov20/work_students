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

function logout() {
    console.log('LOGOUT');
    var button = document.querySelector('.close-acc');
    var closeUrl = button.dataset.closeUrl;
    var csrfToken = button.dataset.csrfToken;
    
    var xhr = new XMLHttpRequest();
    xhr.open('POST', closeUrl, true);
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log('Logged out successfully');
                location.reload();
            } else {
                console.error('Error logging out');
            }
        }
    };
    xhr.send();
}