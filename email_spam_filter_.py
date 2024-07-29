# -*- coding: utf-8 -*-
"""Email Spam Filter .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D0INoTAhaW5AHSu4DWnvepFoy1blC18c
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("/content/spam.csv")

data.head()

data['Category'].value_counts()

"""# Plotting the distribution between Ham and Spam"""

sns.countplot(data = data, x ='Category')

"""## "1" for Spam and "0" for Ham Mails"""

data['Spam'] = data['Category'].apply(lambda x: 1 if x == 'spam' else 0)

data.head()

#'x' is the content of the mail
#'y' is the label of the mail

x_train, x_test, y_train, y_test = train_test_split(data['Message'], data['Spam'], test_size = 0.25)

cv = CountVectorizer()
x_train_count = cv.fit_transform(x_train.values)

x_train_count.shape

x_train_count.toarray()

"""## Training the Model:"""

model = MultinomialNB()
model.fit(x_train_count, y_train)

"""## Testing the model:"""

ham = ["Let's go for hiking this Sunday"]

ham_count = cv.transform(ham)
model.predict(ham_count)

spam = ["Free Rewards, Click to open"]

spam_count = cv.transform(spam)
model.predict(spam_count)

# where 1 is printed if spam is detected and 0 for ham mails

"""## Accuracy of the Model:"""

x_test_count = cv.transform(x_test)

model.score(x_test_count, y_test)*100