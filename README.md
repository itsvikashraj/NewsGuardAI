## About NewsGuardAI 🛡️🔍

**NewsGuardAI** is an AI-driven web application I built to tackle the growing problem of misinformation in our digital world. My goal? To empower users to quickly check if a news article is real or fake, boosting everyone's media literacy in the process.

https://youtu.be/ZfFggAQS1SY

### Why This Project Matters

We're drowning in information, and it's getting harder by the day to tell what's true and what's not. Fake news spreads incredibly fast and can have serious real-world consequences. NewsGuardAI steps in as a practical tool to help cut through the noise, offering an objective way to verify news and foster more critical thinking.

### Under the Hood: How I Built It

This wasn't just about building an AI model; it was a full-stack project from start to finish:

1.  **Gathering the Data (The Foundation):**
    * Getting the right data was crucial. I started by writing custom **web scrapers** to pull news article content directly from various websites. This way, the AI learns from real, constantly evolving information.
    * To bulk up the training data and make it truly robust, I then combined this scraped content with several **publicly available datasets** of labeled real and fake news articles.

2.  **Making Sense of Text with TF-IDF:**
    * All that raw text needed to be converted into something a machine learning model could understand. I used **TF-IDF (Term Frequency-Inverse Document Frequency)** for this. It's a clever technique that turns words into numerical vectors, highlighting how important a word is in a specific article compared to the entire collection. This really helped the AI pick up on the subtle linguistic clues that differentiate genuine content from misleading ones.

3.  **Finding the Best AI Brain for the Job:**
    * I experimented with a few different machine learning models to see which one would perform best for news classification:
        * `Logistic Regression`
        * `Decision Tree Classifier`
        * `Gradient Boosting Classifier`
        * `Random Forest Classifier`
    * After some rigorous testing and fine-tuning, **Logistic Regression emerged as the clear winner, hitting an impressive accuracy of about 94%!** Its combination of high accuracy and efficient performance made it the ideal choice for integration.

4.  **The Flask Backend (Connecting the Dots):**
    * The smarts of the operation—my trained `Logistic Regression` model—is managed by a **Flask backend**. When you submit an article URL, Flask springs into action: it kicks off the web scraping, processes the text with `TF-IDF`, feeds that cleaned data to the AI model, and then sends the prediction (along with a confidence score) back to the front end.

5.  **The User-Friendly Frontend (Your Experience):**
    * I built the user interface with standard web tech: **HTML** for structure, **CSS** for styling, and **JavaScript** to make things interactive. My goal was to make it super intuitive and responsive, so anyone can just paste a URL and get an instant, clear authenticity check.

### What NewsGuardAI Does Best

* **Instant Article Verification:** Get a quick authenticity check for any news article URL.
* **High Accuracy:** Relies on a `Logistic Regression` model that reached 94% accuracy during testing.
* **Simple to Use:** Designed with the user in mind, no tech expertise required.
* **Boosts Media Savvy:** It's not just a tool; it's a way to learn how to spot red flags in news content.

### My Tech Stack

* **Python:** My primary language for all the heavy lifting.
* **Scrapy / BeautifulSoup:** For smart web scraping.
* **scikit-learn:** For all things machine learning, especially `TF-IDF` and model training.
* **Numpy / Pandas:** Essential for data handling and analysis.
* **Flask:** The web framework tying the backend together.
* **HTML, CSS, JavaScript:** Bringing the user interface to life.

### What's Next for NewsGuardAI

I'm always thinking about how to make it better! Future plans include:

* Exploring integration with existing fact-checking APIs to add another layer of verification.
* Developing more sophisticated analysis of source credibility.
* Expanding the training data to cover a broader range of topics and potentially other languages.
* Adding user feedback loops to continuously improve the model over time.

---
