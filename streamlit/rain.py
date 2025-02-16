import streamlit.components.v1 as components

def embed_tableau_dashboard(url):
    tableau_html = f"""
    <div class='tableauPlaceholder'>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https://public.tableau.com/' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='{url}' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    """
    
    # Use components.html instead of unsafe_allow_html
    components.html(tableau_html, height=800)

# Usage
url = "https://public.tableau.com/views/LogisticRegressionDiabeticPredictionModelDashboard/ModelPerformanceMetricsDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
embed_tableau_dashboard(url)
