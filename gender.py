
from sklearn import tree

clf =tree.DecisionTreeClassifier()
number_of_elements= int(3)
ask_data = list(map(int,input("\nEnter the your height in cm ,weigth in kg and shoe size  : ").strip().split()))[:number_of_elements] 

data = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

gender= ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(data, gender)
prediction = clf.predict([ask_data])

print(prediction)



