document.addEventListener("DOMContentLoaded", function () {
    // Get the buttons
    const diseaseButton = document.querySelector('.button:nth-child(1)');
    const medicineButton = document.querySelector('.button:nth-child(2)');
    const chatbotButton = document.querySelector('.button:nth-child(3)');

    // Add click event listeners to the buttons
    diseaseButton.addEventListener('click', function () {
        window.location.href = 'http://127.0.0.1:8000/'; // Navigate to know_disease.html
    });

    medicineButton.addEventListener('click', function () {
        window.location.href = 'http://127.0.0.1:5000/'; // Navigate to choose_medicine.html
    });

    chatbotButton.addEventListener('click', function () {
        window.location.href = 'AI-Chatbot/index.html'; // Navigate to ai_chatbot.html
    });
});

// $(document).ready(function () {
//     $("#MedicineButton").click(function () {
//         $.ajax({
//             type: "GET",
//             url: "http://127.0.0.1:5000/",

//             // url: "Medicine_recommendation/medicine_recommend_model.py", // URL of the server-side script that starts the server
//             success: function (response) {
//                 console.log("Server started successfully:", response);
//             },
//             error: function (xhr, status, error) {
//                 console.error("Error starting server:", error);
//             }
//         });
//     });
// });

function diseaseRecognition() {
    fetch('http://127.0.0.1:8000/', {
        method: 'POST'
    })
        .then(response => {
            if (response.ok) {
                console.log('Script executed successfully');
            } else {
                console.error('Failed to execute script');
            }
        })
        .catch(error => console.error('Error:', error));
}

function MedicineRecommendation() {
    fetch('http://127.0.0.1:5000/', {
        method: 'POST'
    })
        .then(response => {
            if (response.ok) {
                console.log('Script executed successfully');
            } else {
                console.error('Failed to execute script');
            }
        })
        .catch(error => console.error('Error:', error));
}
