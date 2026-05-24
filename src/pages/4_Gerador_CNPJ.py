import streamlit as st
from utils.cnpj import generate_cnpj, format_cnpj


st.set_page_config(
    page_title="Gerador de CNPJ",
    page_icon="🏢",
    layout="centered",
)

st.title("Gerador de CNPJ")
st.caption(
    "Gere números de CNPJ válidos com máscara."
)

if "cnpj_gerado" not in st.session_state:
    st.session_state.cnpj_gerado = ""

with st.container(border=True):

    aplicar_mascara = st.toggle("Aplicar Máscara")

    if st.session_state.cnpj_gerado:
        cnpj_exibido = (
            format_cnpj(st.session_state.cnpj_gerado)
            if aplicar_mascara
            else st.session_state.cnpj_gerado
        )

        st.markdown("##### CNPJ Gerado")

        st.code(
            cnpj_exibido,
            language=None,
        )

    if st.button(
        "Gerar",
        use_container_width=True,
    ):
        st.session_state.cnpj_gerado = generate_cnpj()
        st.rerun()