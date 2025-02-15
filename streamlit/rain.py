import streamlit as st

# Make the layout wide
st.set_page_config(layout="wide")

def embed_tableau_dashboard(height=800):
    """
    Embeds a Tableau Public dashboard with full width display
    """
    # Add custom CSS to ensure full width
    st.markdown(
        """
        <style>
        .element-container iframe {
            width: 100%;
        }
        .stApp {
            max-width: 100%;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    viz_name = "LogisticRegressionDiabeticPredictionModelDashboard"
    dashboard_name = "ModelPerformanceMetricsDashboard"
    
    html = f"""
        <div class='tableauPlaceholder' style='width: 100vw; height: {height}px; margin: -4rem -4rem;'>
            <iframe src='https://public.tableau.com/views/{viz_name}/{dashboard_name}?:embed=yes&:showVizHome=no&:display_count=yes&:display_static_image=yes'
                    width='100%'
                    height='100%'
                    frameborder='0'
                    scrolling='no'>
            </iframe>
        </div>
    """
    
    st.components.v1.html(html, height=height, width=None)

# Example usage
try:
    embed_tableau_dashboard()
except Exception as e:
    st.error(f"Error loading dashboard: {str(e)}")
