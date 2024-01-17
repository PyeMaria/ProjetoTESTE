import streamlit as st

#abrindo a estilização do CSS no app.py:
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) #pega o codigo de html e joga pra o streamlit. unsafe porque não é seguro
#podemos descobrir os componentes que estão na nossa pagina fazer alterações dando F12 no site

usuarios = {}

col1, col2, col3 = st.columns([1,2,3])

with col2:
    with st.form("login"):
        st.markdown("#### Painel de Login") #pode programar html dentro dele
        emlog = st.text_input("Email",placeholder="Digite aqui seu email") #o segundo texto aparece dentro do input abaixo onde você digita
        senhalog = st.text_input("Senha",placeholder="Digite aqui sua senha",type="password") #esconde a senha sendo digitada, dando também a opção de esconde-las
        botãologin = st.form_submit_button("Login")


if botãologin:
    if emlog and senhalog in usuarios.items():
        st.text("Usuario logado")
    if emlog and senhalog not in usuarios.items():
        st.text("Email ou senha incorretos")
        
#usando tag de style do css:
st.markdown("<style></style>", unsafe_allow_html=True)