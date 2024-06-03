function setCookie(name, value, seconds) {
    const date = new Date();
    date.setTime(date.getTime() + (seconds * 1000));
    const expires = "; expires=" + date.toUTCString();
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
function checkAdDisplay(adId) {
    const adClosed = getCookie("adClosed_" + adId);
    const adElement = document.getElementById(adId);
    if (!adClosed) {
        adElement.style.display = 'block';
    }
}
function closeAd(adElement, adId, timer) {
    adElement.style.display = 'none';
    setCookie("adClosed_" + adId, "true", timer * 60);
}

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.ad-container').forEach(adElement => {
        const adId = adElement.getAttribute('data-ad-id');
        const timer = adElement.getAttribute('data-timer');
        checkAdDisplay(adId);
    });
});