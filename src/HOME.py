import streamlit as st

st.set_page_config(
    page_title="CPF/CNPJ Validator",
    page_icon="🧾",
    layout="centered",
)

st.title("🧾 Validador e Gerador de CPF/CNPJ")

st.markdown("""
Bem-vindo ao **CPF/CNPJ Validator**.

Esta aplicação permite validar e gerar documentos brasileiros de forma rápida,
segura e gratuita, incluindo suporte ao novo padrão de **CNPJ Alfanumérico**.
""")

st.divider()

with st.container(border=True):

    _, col1, col2, _ = st.columns([1, 2, 2, 1])

    with col1:
        st.page_link("pages/1_VALIDADOR_CPF.py", label="🪪 Validador CPF")

    with col2:
        st.page_link("pages/2_VALIDADOR_CNPJ.py", label="🏢 Validador CNPJ")

    _, col3, col4, col5, _ = st.columns([1, 2, 2, 2, 1])

    with col3:
        st.page_link("pages/3_GERADOR_CPF.py", label="Gerador CPF")

    with col4:
        st.page_link("pages/4_GERADOR_CNPJ.py", label="Gerador CNPJ")

    with col5:
        st.page_link("pages/5_GERADOR_CNPJ_ALFANUM.py", label="CNPJ Alfanumérico")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("""
#### ✅ Validadores

- CPF
- CNPJ
- CNPJ Alfanumérico

Verifique instantaneamente se um documento possui
dígitos verificadores válidos.
""")

with col2:
    st.success("""
#### ⚡ Geradores

- CPF válido
- CNPJ válido
- CNPJ Alfanumérico válido

Ideal para testes, desenvolvimento e homologação.
""")

st.divider()