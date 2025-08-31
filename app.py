import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
import streamlit as st
st.title("To find The Cover Type Of the Forest")
Elevation=st.number_input("Enter The Elevation in m",step=1)
Aspect=st.number_input("Enter The Aspect in Degrees",min_value=0,max_value=360,step=1)
Slope=st.number_input("Enter The Slope in Degrees",step=1)
Horizontal_Distance_To_Hydrology=st.number_input("Enter The Horizontal Distance To Hydrology in m",step=1)
Vertical_Distance_To_Hydrology=st.number_input("Enter The Vertical Distance To Hydrology in m",step=1)
Horizontal_Distance_To_Roadways=st.number_input("Enter The Horizontal Distance To Roadways in m",step=1)
Hillshade_9am=st.number_input("Enter The Hillshade 9am,in m",step=1)
Hillshade_Noon=st.number_input("Enter The Hillshade Noon in m",step=1)
Hillshade_3pm=st.number_input("Enter The Hillshade 3pm in m",step=1)
Horizontal_Distance_To_Fire_Points=st.number_input("Enter The Horizontal Distance To Fire Points in m",step=1)
soil=st.number_input("Enter the Soil Type in Numerical Form",min_value=1,max_value=40,step=1)
wildarea=st.number_input("Enter the Wilderness Area in Numerical Form",min_value=1,max_value=4,step=1)
arr=[0]*54
arr[0]=Elevation
arr[1]=Aspect
arr[2]=Slope
arr[3]=Horizontal_Distance_To_Hydrology
arr[4]=Vertical_Distance_To_Hydrology
arr[5]=Horizontal_Distance_To_Roadways
arr[6]=Hillshade_9am
arr[7]=Hillshade_Noon
arr[8]=Hillshade_3pm
arr[9]=Horizontal_Distance_To_Fire_Points
arr[9 + wildarea]=1
arr[13+soil]=1
if st.button("Predict Cover Type"):
    prediction=model.predict(np.array([arr]))
    st.success(f"Predicted Forest Cover Type:{prediction[0]}")


