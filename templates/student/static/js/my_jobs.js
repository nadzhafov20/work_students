const infoUserBlock = document.querySelectorAll('.info-user__block');

infoUserBlock.forEach(function (UserBlock) {
    UserBlock.addEventListener('click', function () {
        const isActive = UserBlock.classList.contains('active');

        infoUserBlock.forEach(function (UserBlockRemove) {
            UserBlockRemove.classList.remove('active');
        });

        if (!isActive) {
            UserBlock.classList.add('active');
        }
    });
});