document.addEventListener("DOMContentLoaded", function() {
    const portfolioBtn = document.querySelector(".portfolio-btn");
    let selectedFile = null;

    portfolioBtn.addEventListener("click", function() {
        const fileInput = document.createElement("input");
        fileInput.type = "file";
        fileInput.accept = "image/*";

        fileInput.addEventListener("change", function() {
            selectedFile = fileInput.files[0];
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement("img");
                img.src = e.target.result;
                img.alt = "Uploaded Image";

                const imgBox = document.createElement("div");
                imgBox.classList.add("img-box-a");
                imgBox.appendChild(img);

                const container = document.querySelector(".image-box");
                container.innerHTML = "";
                container.appendChild(imgBox);
            };
            reader.readAsDataURL(selectedFile);
        });

        fileInput.click();
    });

    const continueBtn = document.querySelector(".btn-calendar");

    continueBtn.addEventListener("click", function() {
        if (selectedFile) {
            const title = ""; 
            const description = "";
            const formData = new FormData();
            formData.append("title", title);
            formData.append("description", description);
            formData.append("image", selectedFile);

            const csrftoken = getCookie('csrftoken');

            fetch("/student/portfolio", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken
                },
                body: formData,
            })
            .then(response => {
                if (response.ok) {
                    console.log("Data submitted successfully!");
                    window.location.href = '/student/my/';
                } else {
                    console.error("Error submitting data!");
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        } else {
            console.error("No image uploaded!");
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}