from flask import Flask, request,render_template
import re
import string
from newspaper import Article
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


app = Flask(__name__)

vectorizer = pickle.load(open(r'model\vectorizer.pkl', 'rb'))
model = pickle.load(open(r'model\model.pkl', 'rb'))


def extract_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        full_text = article.text.strip()
        lines = full_text.split('\n')
        if len(lines)>1:
            body = '\n'.join(lines[1:]).strip()
        else:
            body = full_text.strip()
        
        return body
    except Exception as e:
        return f'error: {str(e)}'

def clean_text(text):
  text = text.lower()
  text = re.sub('\[.*?\]','',text)
  text = re.sub('\\W', " ", text)
  text = re.sub('https?://\S+|www\.\S+', '', text)
  text = re.sub('<.*?>+', '', text)
  text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
  text = re.sub('\n', '',text)
  text = re.sub('\w*\d\w*', '', text)
  return text.strip()

@app.route('/',methods = ['GET','POST'])
def index():
    prediction = None
    confidence = None
    url = ""

    if request.method == 'POST':
        url = request.form['url']
        article_text = extract_article(url)

        if article_text:
            cleaned = clean_text(article_text)
            vect_text = vectorizer.transform([cleaned])
            pred = model.predict(vect_text)[0]
            label = 'Fake News' if pred == 1 else 'Real News'
            conf = round(model.predict_proba(vect_text)[0][pred]*100,2)


            prediction = label
            confidence = conf
        else:
            prediction = 'Error'
            confidence = 0.0
        
    return render_template('index.html', prediction = prediction, confidence = confidence, url = url)
    
if __name__ == '__main__':
    app.run(debug=True)    
