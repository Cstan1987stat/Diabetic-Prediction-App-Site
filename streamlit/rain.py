import streamlit as st

import streamlit as st

def embed_tableau_dashboard(url, height=800):
    """
    Embeds a Tableau Public dashboard from a profile URL
    """
    # Convert app URL to embedded URL format
    if "/app/profile/" in url:
        # Extract the viz name from the URL
        viz_name = url.split("/")[-1]
        # Extract the profile name
        profile_name = url.split("/profile/")[1].split("/")[0]
        # Construct the proper embed URL
        embed_url = f"https://public.tableau.com/views/{viz_name}/{viz_name}?:showVizHome=no&:embed=true"
    else:
        embed_url = url

    html = f"""
        <div class='tableauPlaceholder' style='width: 100%; height: {height}px; margin: 0 auto;'>
            <object class='tableauViz' width='100%' height='100%' style='display:block;'>
                <param name='host_url' value='https://public.tableau.com/' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='{embed_url}' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='showAppBanner' value='false' />
            </object>
        </div>
        <script type='text/javascript' src='https://public.tableau.com/javascripts/api/viz_v1.js'></script>
    """
    
    st.components.v1.html(html, height=height)

# Example usage
st.title("Logistic Regression Diabetic Prediction Model Dashboard")

# Your actual Tableau Public dashboard URL
tableau_url = "https://public.tableau.com/app/profile/connor.stanley8849/viz/LogisticRegressionDiabeticPredictionModelDashboard/ModelPerformanceMetricsDashboard"

try:
    embed_tableau_dashboard(tableau_url)
except Exception as e:
    st.error(f"Error loading dashboard: {str(e)}")
