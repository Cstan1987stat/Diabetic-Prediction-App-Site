import streamlit.components.v1 as components

def embed_tableau_dashboard():
    # Get the Tableau visualization URL
    viz_url = "https://public.tableau.com/views/LogisticRegressionDiabeticPredictionModelDashboard/ModelPerformanceMetricsDashboard"
    
    # Construct the embed code using Tableau's JS API
    tableau_html = f"""
        <div class='tableauPlaceholder'>
            <iframe 
                src='{viz_url}?:embed=yes&:showVizHome=no'
                width='100%' 
                height='800' 
                style='border: none;'>
            </iframe>
        </div>
        <script type='text/javascript' src='https://public.tableau.com/javascripts/api/tableau-2.min.js'></script>
    """
    
    # Embed the visualization
    components.html(tableau_html, height=800, width=1000)

# Call the function
embed_tableau_dashboard()
