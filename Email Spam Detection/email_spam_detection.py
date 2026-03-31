import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully")
    print(df.shape)
    return df

# Preprocessing
def preprocess_data(df):

    # Features (remove Email No and Prediction)
    X = df.drop(["Email No.", "Prediction"], axis=1)

    # Target
    Y = df["Prediction"]

    return X, Y

# Split Dataset
def split_data(X, Y):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42
    )

    return X_train, X_test, Y_train, Y_test

# Train Model
def train_model(X_train, Y_train):

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    print("Model Training Completed")

    return model

# Evaluate The Model
def evaluate_model(model, X_test, Y_test):

    predictions = model.predict(X_test)

    acc = accuracy_score(Y_test, predictions)

    print("\nModel Accuracy:", acc)

    print("\nClassification Report:")
    print(classification_report(Y_test, predictions))
    
# Predict New Email
def predict_email(model, email_features):

    prediction = model.predict([email_features])

    if prediction[0] == 1:
        print("SPAM EMAIL")
    else:
        print("NOT SPAM EMAIL")

# Main Function
def email_detection():

    # Load data
    df = load_dataset("emails.csv")

    # Preprocess
    X, Y = preprocess_data(df)

    # Split
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    # Train
    model = train_model(X_train, Y_train)

    # Evaluate
    evaluate_model(model, X_test, Y_test)

    return model, X


if __name__ == "__main__":

    model, X = email_detection()

    print("\nTesting With New Email Data")

    # Example new email (random sample from dataset)
    # Spam-1 & Not Spam-0
    new_email = X.iloc[10].values

    predict_email(model, new_email)