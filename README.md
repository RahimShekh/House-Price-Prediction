# Pune House Price Prediction

This project is a web application that predicts home prices in Pune based on various features such as size in square feet, number of bedrooms, number of bathrooms, and location. The application uses a machine learning model to make the predictions.
In this project, I Used the predictive power of a model trained on houses price data. It deploys with flask  and using Linear Regression to predict the price value. Deploy Machine Learning Model Using Flask to take a model from python code.

#Installation
 To run the web app on your local computer, install the required libraries, These packages are 
 
  python 
  flask 
  sci-kit learn
  pandas
  numpy
  pickle
  HTML/CSS/Javascript for UI

  #IDE
  Visual Studio Code
  Jupyter Notebook

#Build your house price prediction model

###Step-1
The first step of model prediction is to understand the data. It is more important to all machine learning and deep learning projects. You can find more information about the data, You can get the dataset from kaggle or github in my case ,i used pune dataset the dataset i found from a github repository i used that dataset.

###Step-2
Create a python file in jupyter with extension .ipyb. After installed the required packages, import packages  in your python file.

###Step-3
import thae data from the dataset file punedataset.csv and load the data into the jupyter by using import pandas.

###Step-3
 Remove the unwanted features (Columns), now choose columns are  number of bedrooms, number of bathrooms, Square Foot,Location, and price of the house. In price of the house is the target value. We trained the model in the other four columns to find the price of the house.

###Step-4
Unecessary Outlier Removed,Removing Low Square Footage Outliers,
Rows with square footage smaller than 300 per room (for 1-room listings) are removed

###Step-5
 Feature Encoding and Data Preparation for Modeling
One-Hot Encoding: The categorical columns like site_location, availability, and area_type are converted into dummy variables using get_dummies,
Final Dataset Preparation: The final dataset df6 is prepared by dropping unnecessary columns like area_type, availability, and site_location and leaving only the relevant features.

### Step-6
 We want to create a model, must have split it into training and testing. the model trained by training dataset and then apply the evaluation of model used by test dataset.The features X (inputs) and the label y (output) are separated.

 ### Step-6
 The best model is selected using GridSearchCV, which tests multiple models (Linear Regression, Lasso, DecisionTreeRegressor) and finds the best hyperparameters in this case Linear regression model is selected with highest accuracy,So Linear Regression is selected as the best model based on accuracy.

 ### Step-7
 Now, we use Linear regression model to predict the house price,The LinearRegression model is trained using the training data.

 ### Step-8
 The trained model is saved using pickle so it can be loaded later for predictions.so we download and save the punedataset.pickle file.

 #Backend

##Server.py

for Backend i Created a Server folder in that folder i created a Python file Server.py using Flask, a web framework, to create a simple web API for predicting home prices based on the information
 The API exposes two main routes:

1> /get_location_names: This endpoint returns a list of available locations.
2> /predict_home_price: This endpoint predicts the price of a home based on the parameters passed (like square feet, location, number of BedRooms, number of bathrooms).
3>  If the request is a POST, the function extracts the input values (sqft, location, No of bed rooms, and no of bath) from the request body using request.form[]. These values are converted to appropriate data types (e.g., float for area and int for number of rooms).
If the request is a GET, the values are extracted from the query parameters using request.args.get().
4> After receiving the inputs, the function calls the get_estimated_price() function from the util module. This function likely takes the location, square footage, number of bedrooms (BHK), and number of bathrooms as input and predicts the price of the house using the trained model.
5> Columns.json file contains all the locations that we want to show.

##util.py

This file is designed to load the machine learning model and perform predictions based on the user's input for a house's price. The model is trained on historical data and saved as a pickle file. Here's an explanation of the file and its components.

It loads the list of column names from a columns json file. The columns.json contains the names of all the features used for training the model. The first four columns represent features like No of bath,No of bedroom, and sqft. The remaining columns represent the different locations.

The trained model (house_price_prediction.pickle) is loaded into __model using pickle.load().get_location_names() This function returns the list of location names (__locations). These are the different locations that the model has been trained on and are used to predict house prices based on location.

