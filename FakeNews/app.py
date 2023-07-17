import requests
from flask import Flask, request, render_template
from flask_mail import Mail, Message
import pickle
import re
import string
import pandas as pd

# Loading the models and vectorizer
LrModel = pickle.load(open('LrModel.pkl', 'rb'))
DtModel = pickle.load(open('DtModel.pkl', 'rb'))
RFModel = pickle.load(open('RFModel.pkl', 'rb'))
GBModel = pickle.load(open('GBModel.pkl', 'rb'))
vector = pickle.load(open('vectorizer.pkl', 'rb'))

# Text Cleaning Function
def textCleaner(text):
    text = str(text)
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction page
@app.route('/home')
def home():
    return render_template('home.html')

# Prediction route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        news = request.form['article']
        print(news)
        testing_news = {"text": [news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test['text'] = new_def_test['text'].apply(textCleaner)
        new_xv_test = new_def_test['text']
        new_xv_test = vector.transform(new_xv_test)
        fake = 0
        true = 0

        # Logistic Regression Model
        if LrModel.predict(new_xv_test) == 1:
            true = true+1
        else:
            fake = fake+1

        # Decision Trees Model
        if DtModel.predict(new_xv_test) == 1:
            true = true+1
        else:
            fake = fake+1

        # Gradient Boosting Model
        if GBModel.predict(new_xv_test) == 1:
            true = true+1
        else:
            fake = fake+1

        # Random Forest Model
        if RFModel.predict(new_xv_test) == 1:
            true = true+1
        else:
            fake = fake+1

        print("True Values: ", true)
        print("False Values: ", fake)

        if true>fake:
            return render_template('true.html')
        elif true > 0:
            return render_template('unreliable.html')
        else: 
            return render_template('fake.html')
    
    return 'Invalid Request Method'

# Authentic News page
@app.route('/news')
def news():
    response = requests.get("https://newsdata.io/api/1/news?apikey=pub_25325f37af89bd7d4d9cbed5370e44260af86&q=pegasus&language=en")
    data = response.json()
    articles = data["results"]
    print(len(articles))
    return render_template('authenticNews.html', articles=articles)

# Report page
#mail set up
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sachinu760@gmail.com'
app.config['MAIL_PASSWORD'] = 'dqlbhfpzefdhncgx'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    source = request.form['source']
    date = request.form['date']
    description = request.form['description']
    proof = request.form['proof']
    msg = Message('Report', sender ='defencestudycapsule@gmail.com', recipients = ['sachinu760@gmail.com'])
    msg.body = f"Title: {title}\nSource: {source}\nDate: {date}\nDescription: {description}\nProof: {proof}"
    mail.send(msg)
    # Save the data or perform any other necessary operations
    return render_template('mailResponse.html')

@app.route('/report')
def report():
    return render_template('report.html')

#Recent Fake
@app.route('/recentFake')
def recentFake():
    return render_template('recentFake.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
