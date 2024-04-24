function formatAnswer(answer) {
    // Bold text between ** and **
    answer = answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // New sentence on new line
    answer = answer.replace(/\n/g, '<br>');
    // Convert bullet points to list items
    answer = answer.replace(/\* (.*?)\n/g, '<li>$1</li>');
    // Wrap each section in appropriate tags
    answer = `<p class="p-3">${answer}</p>`;
    return answer;
}

document.addEventListener("DOMContentLoaded", function () {
    const questionForm = document.getElementById("questionForm");
    const questionInput = document.getElementById("questionInput");
    const answerContainer = document.getElementById("answerContainer");

    questionForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const question = questionInput.value.trim();
        if (!question) return;

        answerContainer.innerHTML = "Loading your answer... <br> It might take up to 10 seconds";

        //  API request 
        fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyASERzONPr1XSoTh7AMf_k7ZwohtGUHCX4`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                contents: [{ parts: [{ text: question }] }],
            }),
        })
            .then((response) => response.json())
            .then((data) => {

                const answer = data.candidates[0].content.parts[0].text;
                const formattedAnswer = formatAnswer(answer); // Apply formatting to the answer text
                answerContainer.innerHTML = `<div class="formatted-answer">${formattedAnswer}</div>`;
              
            })
            .catch((error) => {
                console.error(error);
                answerContainer.innerHTML = "Sorry - Something went wrong. Please try again!";
            });
    });
});
