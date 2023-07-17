# FakeNews Detector Web App

This is a web application called FakeNews, which is designed to detect and classify fake news articles. The app is built using Flask, a Python web framework, and utilizes a machine learning model trained on four different algorithms to achieve an accuracy of approximately 94%. The model uses four features to classify news articles as either real or fake.

## Installation

To run the FakeNews web app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd FakeNews
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask development server:
   ```bash
   flask run
   ```

5. Open your web browser and access the app at `http://localhost:5000`.

## Project Structure

The project has the following structure:

- `static/`: This directory contains static files such as CSS stylesheets and client-side JavaScript files.
- `templates/`: This directory contains the HTML templates used by the Flask app for rendering the web pages.
- `DtModel.pkl`: A machine learning model file trained on the Decision Tree algorithm.
- `GBModel.pkl`: A machine learning model file trained on the Gradient Boosting algorithm.
- `LrModel.pkl`: A machine learning model file trained on the Logistic Regression algorithm.
- `vectorizer.pkl`: A pickle file containing the trained TF-IDF vectorizer used for text preprocessing.
- `Fake_new_detection.ipynb`: Jupyter Notebook file containing the code for training the machine learning models and performing analysis.
- `LICENSE`: The license file for the project.
- `README.md`: This file, providing information about the FakeNews web app.

## Usage

The FakeNews web app offers the following functionalities:

- **Check Latest News**: View the latest news articles and their classification as real or fake.
- **Check Fake News**: Enter a news article URL or text to check if it is real or fake.
- **Check Recent Fake News**: View the most recently detected fake news articles.
- **Report Fake News**: Report any suspicious news articles that you believe are fake.

## Contributing

Contributions to the FakeNews web app are welcome. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute the code for personal or commercial purposes.

## Acknowledgments

The FakeNews web app and machine learning models were developed by Hare Krishna.
