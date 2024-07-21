import streamlit as st

def create_navbar():
    st.markdown("""
<nav class="navbar navbar-expand-lg navbar-dark bg-dark navbar-custom">
  <a class="navbar-brand" href="#" style="font-size: 40px; font-family: Arial; color: #00ffff; margin-left: 2.5rem">🛍️ Análisis de Ventas</a>
  <div class="collapse navbar-collapse" id="navbarNav" >
    <ul class="navbar-nav margenes">
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/JulioLaz" target="_blank">
          <i class="fab fa-github me-2 fa-lg"></i></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/julio-lazarte-developer/" target="_blank">
          <i class="fab fa-linkedin me-2 fa-lg"></i></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://cv-lazarte-julio.web.app/" target="_blank">
          <i class="fas fa-globe me-2 fa-lg"></i></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)  