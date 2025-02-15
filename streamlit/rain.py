import streamlit as st

import streamlit as st

def embed_tableau_dashboard(url, height=700):
    """
    Embeds a Tableau Public dashboard in a Streamlit app
    
    Parameters:
    url (str): The URL of your Tableau Public dashboard
    height (int): Height of the dashboard in pixels
    """
    # Get the base URL without any parameters
    base_url = url.split('?')[0]
    
    # Construct the embed URL
    tableau_embed = f'{base_url}?:embed=yes&:toolbar=no'
    
    # Use HTML components to embed the dashboard
    html = f"""
        <div style='height: {height}px;'>
            <iframe src='{tableau_embed}'
                    width='100%'
                    height='100%'
                    frameborder='0'
                    scrolling='no'
                    allowfullscreen
            ></iframe>
        </div>
    """
    
    # Render the HTML using Streamlit
    st.components.v1.html(html, height=height)

# Example usage
if __name__ == "__main__":
    st.title("My Dashboard")
    
    # Replace this URL with your Tableau Public dashboard URL
    tableau_url = "https://public.tableau.com/app/profile/connor.stanley8849/viz/LogisticRegressionDiabeticPredictionModelDashboard/ModelPerformanceMetricsDashboard"
    
    embed_tableau_dashboard(tableau_url)




