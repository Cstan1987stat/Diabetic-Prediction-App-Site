import streamlit as st
import streamlit.components.v1 as components
import joblib
import pandas as pd

# Load models
model = joblib.load("/mount/src/test/streamlit/model/lg.joblib.diab")
column_transformer = joblib.load("/mount/src/test/streamlit/preprocessing/column_transformer.joblib.diab")

# Streamlit App Title
st.title("Diabetes Classification Prediction")
st.write("Answer the following questions to receive a prediction.")

# Define categorical mappings
yes_no_dict = {"Yes": 1.0, "No": 0.0}
health_dict = {
    "Excellent": 1.0, "Very Good": 2.0, "Good": 3.0, 
    "Fair": 4.0, "Poor": 5.0
}
activity_dict = {"150+ minutes": 1.0, "1-149 minutes": 2.0, "0 minutes": 3.0}
education_dict = {
    "Didn't graduate High School": 1.0, "Graduated High School": 2.0, 
    "Attended College or Technical School": 3.0, 
    "Graduated from College or Technical School": 4.0
}
income_dict = {
    "Less than $15,000": 1.0, "$15,000 - $25,000": 2.0, "$25,000 - $35,000": 3.0,
    "$35,000 - $50,000": 4.0, "$50,000 - $100,000": 5.0, 
    "$100,000 - $200,000": 6.0, "More than $200,000": 7.0
}
smoking_dict = {
    "Everyday smoker": 1.0, "Smokes some days": 2.0, 
    "Former smoker": 3.0, "Never smoked": 4.0
}

# Create input form
with st.form("diabetes_form"):
    st.subheader("General Health & Lifestyle")
    general_health = st.selectbox("How would you rate your general health?", list(health_dict.keys()))
    physical_health_days = st.number_input("Days in the past 30 where physical health was poor:", 0, 30)
    mental_health_days = st.number_input("Days in the past 30 where mental health was poor:", 0, 30)
    
    st.subheader("Medical & Lifestyle Information")
    has_insurance = st.selectbox("Do you have health insurance?", list(yes_no_dict.keys()))
    physical_activity = st.selectbox("Did you engage in physical activity outside of work?", list(yes_no_dict.keys()))
    activity_minutes = st.selectbox("How many minutes of physical activity per week?", list(activity_dict.keys()))
    muscle_strengthening = st.selectbox("Do you meet muscle-strengthening recommendations?", list(yes_no_dict.keys()))
    
    st.subheader("Health Conditions")
    high_bp = st.selectbox("Have you been diagnosed with high blood pressure?", list(yes_no_dict.keys()))
    high_cholesterol = st.selectbox("Have you been diagnosed with high cholesterol?", list(yes_no_dict.keys()))
    heart_disease = st.selectbox("Have you had a heart attack or coronary heart disease?", list(yes_no_dict.keys()))
    asthma = st.selectbox("Have you been diagnosed with asthma?", list(yes_no_dict.keys()))
    arthritis = st.selectbox("Have you been diagnosed with arthritis?", list(yes_no_dict.keys()))
    
    st.subheader("Demographics & Lifestyle")
    sex = st.selectbox("Sex at birth:", ["Male", "Female"])
    age = st.number_input("Age (18-99):", 18, 99)
    height_inches = st.number_input("Height (in inches, 36-95):", 36, 95)
    bmi = st.number_input("Body Mass Index (BMI):")
    education = st.selectbox("Highest level of education:", list(education_dict.keys()))
    income = st.selectbox("Yearly income range:", list(income_dict.keys()))
    smoking_status = st.selectbox("Smoking status:", list(smoking_dict.keys()))
    alcohol = st.selectbox("Have you had alcohol in the past 30 days?", list(yes_no_dict.keys()))
    binge_drinking = st.selectbox("Are you a binge drinker?", list(yes_no_dict.keys()))
    heavy_drinking = st.selectbox("Are you a heavy drinker?", list(yes_no_dict.keys()))
    difficulty_walking = st.selectbox("Do you have difficulty walking or climbing stairs?", list(yes_no_dict.keys()))
    
    submitted = st.form_submit_button("Get Prediction")

# Process input and make prediction
if submitted:
    user_input = [
        health_dict[general_health], physical_health_days, mental_health_days, 
        yes_no_dict[has_insurance], yes_no_dict[physical_activity], 
        activity_dict[activity_minutes], yes_no_dict[muscle_strengthening], 
        yes_no_dict[high_bp], yes_no_dict[high_cholesterol], yes_no_dict[heart_disease], 
        yes_no_dict[asthma], yes_no_dict[arthritis], 1.0 if sex == "Male" else 0.0, 
        age, height_inches, bmi, education_dict[education], income_dict[income], 
        smoking_dict[smoking_status], yes_no_dict[alcohol], 
        yes_no_dict[binge_drinking], yes_no_dict[heavy_drinking], 
        yes_no_dict[difficulty_walking]
    ]
    
    cols = [
        "general_health", "physical_health_days", "mental_health_days",
        "has_health_plan", "meets_aerobic_guidelines", "physical_activity_150min", 
        "muscle_strengthening", "high_blood_pressure", "high_cholesterol", "heart_disease",
        "lifetime_asthma", "arthritis", "sex", "age", "height_inches", "bmi",
        "education_level", "income_group", "smoking_status", "alcohol_consumption",
        "binge_drinking", "heavy_drinking", "difficulty_walking"
    ]
    
    df = pd.DataFrame([user_input], columns=cols)
    transformed_input = column_transformer.transform(df)
    
    # Make prediction
    prediction = model.predict(transformed_input)[0]
    probability = model.predict_proba(transformed_input)[0]
    
    st.subheader("Prediction Results")
    if prediction == 1:
        st.error(f"⚠️ The model predicts that you may have diabetes. (Confidence: {probability[1]:.2%})")
    else:
        st.success(f"✅ The model predicts that you are not diabetic. (Confidence: {probability[0]:.2%})")
    
    st.info("Note: This tool is for screening purposes only. Consult a medical professional for proper diagnosis.")

st.subheader('Tableau Model Performance Dashboard')
import streamlit as st
import streamlit.components.v1 as components

def embed_tableau_dashboard():
    # Updated Tableau embedding method
    viz_url = "https://public.tableau.com/views/LogisticRegressionDiabeticModelDashboard/ConfusionMatrixDashboard"
    
    # More robust embedding approach
    tableau_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
        <script type="text/javascript">
            function initViz() {{
                var containerDiv = document.getElementById("tableauViz");
                var url = "{viz_url}";
                var options = {{
                    width: "100%",
                    height: "800px",
                    hideTabs: true,
                    hideToolbar: false
                }};
                var viz = new tableau.Visualization(containerDiv, url, options);
            }}
            
            window.onload = initViz;
        </script>
    </head>
    <body style="margin: 0;">
        <div id="tableauViz" style="width:100%; height:800px;"></div>
    </body>
    </html>
    '''
    
    # Use components.html with updated parameters
    components.html(tableau_html, height=850, width=1200, scrolling=True)

# Call the function
embed_tableau_dashboard()
