from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail
from dotenv import load_dotenv
import pickle
import numpy as np
import os
import smtplib


popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))



app = Flask(__name__)
app.secret_key = os.urandom(24)
mail = Mail(app)

# Load environment variables from .env file
load_dotenv()

# Email Configuration (Using Environment Variables)
SENDER_EMAIL = os.getenv("MAIL_USERNAME")
APP_PASSWORD = os.getenv("MAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("MAIL_RECEIVER")

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:11]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("All fields are required!", "danger")
            return redirect(url_for("contact"))

        # Sending email manually using SMTP
        try:
            smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_object.starttls()
            smtp_object.login(SENDER_EMAIL, APP_PASSWORD)

            subject = f"New Contact Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg = f"Subject:{subject}\n\n{body}".encode("utf-8")

            smtp_object.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg)
            smtp_object.quit()
            
            flash("Thank you! Your message has been sent.", "success")
        except Exception as e:
            flash("Error sending email. Please try again later.", "danger")
            print(f"Email error: {e}")

        return redirect(url_for("contact"))


if __name__ == '__main__':
    app.run(debug=True)