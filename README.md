Our healthcare recommendation system is designed to streamline the healthcare journey for individuals, offering them convenience, accuracy, and peace of mind in managing their health needs. Whether someone is seeking a specialist, a diagnosis, or medication advice, our platform aims to be their trusted companion in navigating the complexities of the healthcare landscape.
My  project aims to revolutionize healthcare recommendations by integrating cutting-edge technology with comprehensive databases of patient symptoms data, diet plans , disease description ,workout plans, medicines and their uses , medicine ratings and user feedback. Through my web application, users can interact with an AI chatbot named DOCQUEST powered by the Google Gemini API, accessing a vast repository of doctor information curated from the entirety of the internet. Leveraging this extensive database, DOCQUEST intelligently recommends specialists with matching expertise and favorable ratings, ensuring users receive tailored care from top-tier professionals conveniently located nearby.
Furthermore, my  system employs advanced machine learning techniques, including Support Vector Classifier (SVC), to accurately predict potential diseases based on user-input symptoms. By analyzing a multitude of algorithms and selecting SVC for its superior performance, we ensure precise disease identification and personalized treatment suggestions. Additionally, our medication recommendation model utilizes Natural Language Processing (NLP) techniques through the NLTK library to analyze symptom descriptions and provide tailored medication suggestions. To further enhance user safety, our model considers medication ratings from reputable sources, guaranteeing the reliability and efficacy of the recommended treatments.
In summary, our healthcare recommendation system offers a seamless and comprehensive solution that integrates AI-driven doctor recommendations, accurate disease prediction, and personalized medication suggestions


## Running Locally

To run the project locally, follow these steps:

1. Clone the git repository.

2. Open a terminal or command prompt and navigate to the directory where you have cloned the git repository.

3. Start a local HTTP server by running the following command:
python -m http.server
This will start a server on your localhost, typically on port 8000.

4. Open your web browser and access the main page of the project by navigating to:
localhost:8000/mainpage.html

5. Navigate to the `Disease_Recognition` folder in the project directory and run the Python script `model.py`.

6. Next, navigate to the `Medicine_Recommendation` folder in the project directory and run the Python script `medicine_recommend_model.py`.

7. You are now ready to use all three components of the project from `localhost:8000/mainpage.html`.