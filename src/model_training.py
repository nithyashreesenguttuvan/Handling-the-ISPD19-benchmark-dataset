import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(features, labels):
    X = np.array([list(f.values()) for f in features])
    y = np.array(labels)
    
    if len(X) <= 1:  # Check if there is more than one sample
        print("Not enough samples to train and test the model. Consider adding more data.")
        return None
    
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return model
