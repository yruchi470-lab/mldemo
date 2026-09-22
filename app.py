import pickle

with open("iris_model.pkl" , "rb") as file:
    model = pickle.load(file)
#s_w = float(input("Enter Sepal Width:"))
#s_l = float(input("Enter Sepal Length:"))
#p_w = float(input("Enter Petal Width:"))
#p_l = float(input("Enter Petal Length:"))

Samples = [[1.5 , 2.6 , 4.4 , 2.8]]
prediction = model.predict([[s_w , s_l , p_w , p_l]])
print(prediction)