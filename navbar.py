import streamlit as st
#                 z-index: 1000;

def create_navbar():
    st.markdown("""
<nav class="navbar navbar-expand-lg navbar-dark bg-dark navbar-custom " style="z-index: 2000 !important;display:flex;justify-content: center;border-bottom: 1px solid #00ff00">
  <span class="navbar-brand" style="font-size: 30px; font-family: Arial; color: #00ffff">🛍️ Análisis de Ventas</span>
</nav>
""", unsafe_allow_html=True)  
    
def create_links():
    st.markdown(
        """
        <div style="background-color: black; padding: 10px; text-align: center; border-radius: 5px;border:solid 1px #00ff00">
            <div style="margin: 10px 0;">
                <a href="https://github.com/JulioLaz" target="_blank" style="margin-right: 20px;">
                    <i class="fab fa-github fa-lg" style="color: #00ff00;font-size: 1.5rem; margin:0 10px"></i>
                </a>
                <a href="https://www.linkedin.com/in/julio-lazarte-developer/" target="_blank" style="margin-right: 20px;">
                    <i class="fab fa-linkedin fa-lg" style="color: #00ff00;font-size: 1.5rem; margin:0 10px"></i>
                </a>
                <a href="https://cv-lazarte-julio.web.app/" target="_blank">
                    <i class="fas fa-globe fa-lg" style="color: #00ff00;font-size: 1.5rem; margin:0 10px"></i>
                </a>
            </div>
            <div>
                <img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=f77136&size=50&center=true&vCenter=true&width=1300&height=60&duration=1200&lines=+++Hi,+I'm+Julio+Lazarte+++">
            </div>
        </div>
        """, unsafe_allow_html=True) 
    


