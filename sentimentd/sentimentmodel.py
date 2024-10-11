# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from sklearn.pipeline import Pipeline
# import pickle

# def model_making():
    # data = pd.read_csv('sentiment_tweets3.csv')

    # # Preprocessing the data
    # data.dropna(inplace=True)
    # data = data.rename(columns = {'label (depression result)' : 'label'})

    # # Features and target variable
    # X = data['message to examine']
    # y = data['label']
    
#     # Split the dataset into training and testing sets
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     # Create a pipeline with TfidfVectorizer and LogisticRegression
#     pipeline = Pipeline([
#         ('tfidf', TfidfVectorizer()),
#         ('lr', LogisticRegression())
#     ])

#     # Train the model
#     pipeline.fit(X_train, y_train)

#     # Saving the model
#     with open('sentiment_model.pkl', 'wb') as model_file:
#         pickle.dump(pipeline, model_file)

#     # loading the model
#     with open('sentiment_model.pkl', 'rb') as mod:
#         model = pickle.load(mod)
#     return model

# sentiment_model.py
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

# Train the model (this is a sample, adjust it based on your dataset)
def model_making():
    # Example training data
    # X_train = ["I love this!", "I hate this!", "This is amazing", "This is terrible"]
    # y_train = [1, 0, 1, 0]  # 1: Positive, 0: Negative
    data = pd.read_csv('sentiment_tweets3.csv')

    # # Preprocessing the data
    data.dropna(inplace=True)
    data = data.rename(columns = {'label (depression result)' : 'label'})

    # Features and target variable
    X = data['message to examine']
    y = data['label']

    tfidf = TfidfVectorizer()

    # Vectorize the text data
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    # sampling
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_tfidf, y_train)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)

    # Save the model to a file
    with open('sentiment_model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    # Load the pre-trained model
    with open('sentiment_model.pkl', 'rb') as f:
        model = pickle.load(f)
        return model
