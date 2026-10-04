from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from training_data import x, y

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)


def predict_risk(difficulty, confidence, hours, progress):
    new_topic = [[difficulty, confidence, hours, progress]]
    prediction = model.predict(new_topic)
    return prediction[0]
