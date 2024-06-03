function applyFilter() {
    var qualificationId = document.getElementById("qualificationSelect").value;
    var skillId = document.getElementById("skillSelect").value;
    var startDate = document.getElementById("startDate").value;
    var endDate = document.getElementById("endDate").value;

    var url = '/client/students/?';

    if (qualificationId) {
        url += 'qualification=' + encodeURIComponent(qualificationId) + '&';
    }
    if (skillId) {
        url += 'skill=' + encodeURIComponent(skillId) + '&';
    }
    if (startDate) {
        url += 'start_date=' + encodeURIComponent(startDate) + '&';
    }
    if (endDate) {
        url += 'end_date=' + encodeURIComponent(endDate) + '&';
    }

    if (url.endsWith('&')) {
        url = url.slice(0, -1);
    }

    window.location.href = url;
}

document.getElementById("filterButton").addEventListener("click", applyFilter);

function toggleDiv() {
    var content = document.getElementById("content");
    content.classList.toggle("hidden");
  }