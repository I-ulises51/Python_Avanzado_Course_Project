import pytesseract
import pandas as pd
import pickle
#importint the libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from dotenv import dotenv_values,load_dotenv
import os


from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist


from app.utils.utils import Utils
import os
import shutil



class Customer_classify(Utils):

  def __init__(self):
    print("constructor")

  def svm_classifier(self, file_name):
    #Cargar el dataset
    df = pd.read_csv('./app/services/Customer_classify/Datasets/marketing_campaign_copy.csv')
    print("--------------------Data Modifications------------------------")
    #adding Total Spending Amount
    df['Total_Spending'] = df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] + df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
    
    #Changing Strings from Education
    labels = []
    for value in df['Education']:
        if value == 'Graduation':
            labels.append(0)
        elif value == 'Master' or  value =="2n Cycle":
            labels.append(1)
        elif value == 'PhD':
            labels.append(2)
        else:
            labels.append(3)
    df.loc[:, 'Education'] = labels
    df["Education"] = df["Education"].astype("int64")
    #Changing Strings from Marital Status
    labels = []
    for value in df['Marital_Status']:
        if value == 'Married':
            labels.append(5)
        elif value == 'Widow':
            labels.append(4)
        elif value == 'Separated':
            labels.append(3)
        elif value == 'Divorced':
            labels.append(2)
        elif value == 'Single':
            labels.append(1)
        else:
            labels.append(0)
    df.loc[:, 'Marital_Status'] = labels
    df["Marital_Status"] = df["Marital_Status"].astype("int64")
    #Changin Year of Bith to Age 2023
    labels = []
    for value in df['Year_Birth']:
        labels.append(2023 - int(value))
    
    df.loc[:, 'Year_Birth'] = labels
    #Eliminando columna que yo cree 
    #df = df.drop('Total_Spending', axis=1)
    df['Num_Kids']  = df['Kidhome'] + df['Teenhome']
    
    df['TotalAcceptedCmp'] = df['AcceptedCmp1'] + df['AcceptedCmp2'] + df['AcceptedCmp3'] + df['AcceptedCmp4'] + df['AcceptedCmp5'] + df['Response']
    
    #eliminando mayores de 90 
    filter = (df['Year_Birth'] <= 90)
    df = df.loc[filter]
    #eliminando ingresos mayores de 300K 
    filter = (df['Income'] <= 300000)
    df = df.loc[filter]
    
    #eliminando mayores de 90 
    filter = (df['NumWebVisitsMonth'] < 11)
    df = df.loc[filter]
    #eliminando ingresos mayores de 300K 
    filter = (df['NumWebPurchases'] < 20)
    df = df.loc[filter]
    #eliminando ingresos mayores de 300K 
    filter = (df['NumCatalogPurchases'] < 20)
    df = df.loc[filter]
    
    #Not sure how it is related to the Data Set
    df = df.drop('Z_CostContact', axis=1)
    df = df.drop('Z_Revenue', axis=1)
    #Removing only a small per centage of the customers complain
    df = df.drop('Complain', axis=1)
    #ID relevant? 
    df = df.drop('ID', axis=1)
    #Dt_Customer relevant? 
    df = df.drop('Dt_Customer', axis=1)
    
    df["Income"] = df["Income"].astype("int64")
    
    print("--------------------Inside SVM Classifier------------------------")
    path_results_csv = os.path.abspath(
        "./app/services/Customer_classify/Datasets/" + file_name + ".csv")
    
    print("-------------------- Using PCA PKL ------------------------")
    #PCA
    pickle_file_pca = r"./app/services/Customer_classify/pca_model_integrador.plk"

    with open(pickle_file_pca, 'rb') as file:
      pickle_pca = pickle.load(file)
    X_PCA = pickle_pca.transform(df)
    print(len(X_PCA))
    
    print("-------------------- Using SVM PKL ------------------------")
    #SVM
    pickle_file_svm = "./app/services/Customer_classify/svm_model_integrador.plk"
    with open(pickle_file_svm, 'rb') as file:
      pickle_svm = pickle.load(file)
    X_SVM = pickle_svm.predict(X_PCA)
    
    print("-------------------- Adding Labels to DF ------------------------")
    df['labels'] = X_SVM
    classified_file_name = './app/services/Customer_classify/Datasets/' + file_name + 'classified.csv'
    df.to_csv(classified_file_name)
    print("Files Processed: ", classified_file_name)
