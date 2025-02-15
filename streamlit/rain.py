import streamlit as st

# Make the layout wide
st.set_page_config(layout="wide")

def embed_tableau_dashboard(height=850):
    """
    Embeds a Tableau Public dashboard with proper sizing
    """
    # Add custom CSS to ensure full width and proper padding
    st.markdown(
        """
        <style>
        .element-container iframe {
            width: 100%;
        }
        .stApp {
            max-width: 100%;
        }
        [data-testid="stAppViewContainer"] {
            padding: 1rem;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    viz_name = "LogisticRegressionDiabeticPredictionModelDashboard"
    dashboard_name = "ModelPerformanceMetricsDashboard"
    
    html = f"""
        <div class='tableauPlaceholder' style='width: 100%; height: {height}px; padding: 0; margin: 0;'>
            <iframe src='https://public.tableau.com/views/{viz_name}/{dashboard_name}?:embed=yes&:showVizHome=no&:display_count=yes&:display_static_image=yes'
                    width='100%'
                    height='100%'
                    frameborder='0'
                    scrolling='no'
                    style='display: block; margin: 0 auto;'>
            </iframe>
        </div>
    """
    
    st.components.v1.html(html, height=height, width=None)

# Example usage
try:
    embed_tableau_dashboard()
except Exception as e:
    st.error(f"Error loading dashboard: {str(e)}")
