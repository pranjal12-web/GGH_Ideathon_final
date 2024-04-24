import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix, classification_report, precision_score, roc_curve
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
import pickle
from sklearn.model_selection import train_test_split

df = pd.read_csv('dataset.csv')

cols = df.columns
data = df[cols].values.flatten()

s = pd.Series(data)
s = s.str.strip()
s = s.values.reshape(df.shape)

df = pd.DataFrame(s, columns=df.columns)

#fill NaN values with 0
df = df.fillna(0)

df1 = pd.read_csv('Symptom-severity.csv')
x=df1['Symptom']

data=pd.DataFrame()
data["Disease"]=df["Disease"]
y=0
data[x]=0
for index, row in df.iterrows():
    for symptom in df.columns[1:]:
        if row[symptom] != 0:
            data.loc[index, row[symptom]] = 1
data = data.fillna(0)
data[data.columns[1:]]=data[data.columns[1:]].astype('int')

columns_to_drop =['foul_smell_ofurine', 'dischromic_patches', 'spotting_urination']
data.drop(columns=columns_to_drop, inplace=True)

unique_diseases = pd.DataFrame(data=df['Disease'].unique(), columns=['Unique Diseases'])

X = data.drop('Disease', axis=1)
y = data['Disease']
le = LabelEncoder()
le.fit(y)
Y = le.transform(y)
    
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=20)

# selecting svc
svc = SVC(kernel='linear',probability=True)
svc.fit(X_train,y_train)
ypred = svc.predict(X_test)

# save svc
pickle.dump(svc,open('svc.pkl','wb'))


