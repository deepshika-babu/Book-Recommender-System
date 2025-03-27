# Book-Recommender-System

This is a Flask-based Book Recommendation System that suggests books based on user preferences. The system leverages a pre-trained recommendation model to provide personalized book suggestions.

It features two recommendation models:

- Popularity-Based Recommendation: Displays the top 50 books with the highest average rating, considering only books that have received a minimum of 250 votes.

- Collaborative Filtering: Uses a model-based approach that filters experienced readers (users who have rated more than 200 books) and displays books with at least 50 ratings. This makes the system more intelligent and relevant.

### Tech Stack
- Backend: Flask
- Frontend: HTML, CSS, Bootstrap
- Database: Processed CSV/ Pickle files
- Machine Learning: NumPy, Pandas, Scikit-Learn
- Email Service: Flask-Mail


## Dataset Information
The dataset used for this project is sourced from [Kaggle: Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data).
It contains three main files:

1. Books.csv

This file contains metadata about books:

| Column Name         | Description |
|---------------------|-------------|
| ISBN            | Unique identifier for books |
| Book-Title         | Title of the book |
| Book-Author        | Author of the book |
| Year-Of-Publication | Year the book was published |
| Publisher          | Publisher of the book |
| Image-URL-S        | URL of the small-sized book cover image |
| Image-URL-M            | URL of the medium-sized book cover image |
|Image-URL-L         | URL of the large-sized book cover image |

2. Users.csv

Contains user demographic information:

| Column Name         | Description |
|---------------------|-------------|
| User-ID             | Unique identifier for users |
| Location            | Location of the user (City, State, Country) |
| Age                  |Age of the user (if available) |

3. Ratings.csv

Contains user ratings for books:

| Column Name         | Description |
|---------------------|-------------|
| User-ID             |Unique identifier for users |
| ISBN                | Unique identifier for books|
| Book-Rating         |Rating given by the user (scale of 0-10) |

## Technologies Used

- Python

- Flask (for web application development)

- Pandas & NumPy (for data preprocessing and analysis)

- Scikit-Learn (for collaborative filtering model)

- Flask-Mail (for email integration)

## Features

- Top 50 Books Recommendation (Popularity-Based)

- Personalized Recommendations (Collaborative Filtering)

- Book Metadata Display (Title, Author, Image, etc.)

- Contact Form with Email Notification

## How To Run the Project

1. Clone the Repository
```bash
git clone <repo-link>
cd book-recommendation-system
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Set Up .env File for Email Configuration
Create a .env file and add:
```bash
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_RECEIVER=your-email@gmail.com
```

4. Run the Application
```bash
python app.py
```

5. Open in Browser
Visit ```http://127.0.0.1:5000/``` to access the web app.

## 🎯 Future Improvements

- Implement a content-based recommendation model

- Deploy on a cloud service like Heroku/AWS

