import streamlit as st
import requests

Api_url = "http://127.0.0.1:8000/predict"

st.title("Insurance Premium category Predictior")

st.markdown("Enter your details below :")

age = st.number_input("Age",min_value=1,max_value=119,value=30)
weight = st.number_input("weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Heigt (mtrs)", min_value=0.5,max_value=2.5, value=1.7)
income_lpa=st.number_input("Annual income (LPA)",min_value = 0.1,value = 10.0)
smoker=st.selectbox("Are you a smoker",options=[True,False])
city=st.text_input("City",value="Mumbai")
occupation=st.selectbox("Occupation",options=['retired','freelancer','student','goverment_job','bussiness_owner','unemployed','private_job'])

if st.button("Predict Insurance Premium Category"):
    input_data={'age':age,'weight':weight,'height':height,'income_lpa':income_lpa,'smoker':smoker,'city':city,'occupation':occupation}
    try:
        response = request.post(Api_url,json=input_data)result = response.json()
        
        if response.status_code == 200:
            prediction=result["response"]
            st.success(f"Predicted Insurance Premium Category : **{prediction['predicted_cateogory']}")
            st.write("Confidence:",prediction["confidence"])
            st.write("Class Probabilities:")
            st.json(prediction["class_probabilities"])
        else:
            st.error(f"Api Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastApi Server. Make sure it's running")