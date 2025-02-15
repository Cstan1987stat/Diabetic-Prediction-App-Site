import streamlit as st

def embed_tableau_dashboard(url, height=800):
    """
    Embeds a Tableau Public dashboard with simplified URL handling
    """
    # Extract the viz name from the URL
    viz_name = "LogisticRegressionDiabeticPredictionModelDashboard"
    dashboard_name = "ModelPerformanceMetricsDashboard"
    
    html = f"""
        <div class='tableauPlaceholder' style='width: 100%; height: {height}px;'>
            <iframe src='https://public.tableau.com/views/{viz_name}/{dashboard_name}?:embed=yes&:showVizHome=no'
                    width='100%'
                    height='100%'
                    frameborder='0'
                    scrolling='yes'>
            </iframe>
        </div>
    """
    
    st.components.v1.html(html, height=height)

# Example usage
st.title("Logistic Regression Diabetic Prediction Model Dashboard")

try:
    embed_tableau_dashboard(None)  # URL is hardcoded in the function for now
except Exception as e:
    st.error(f"Error loading dashboard: {str(e)}")
