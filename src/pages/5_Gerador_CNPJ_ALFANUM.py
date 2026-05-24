import streamlit as st
from utils.cnpj import generate_cnpj_alfanum, format_cnpj_alfanum


st.set_page_config(
    page_title="Gerador de CNPJ Alfanumérico",
    page_icon="🏢",
    layout="centered",
)

st.title("Gerador de CNPJ Alfanumérico")
st.caption(
    "Gere números de CNPJ com o novo padrão de CNPJ Alfanumérico da Receita Federal."
)

if "cnpj_alfanum_gerado" not in st.session_state:
    st.session_state.cnpj_alfanum_gerado = ""

with st.container(border=True):

    aplicar_mascara = st.toggle("Aplicar Máscara")

    if st.session_state.cnpj_alfanum_gerado:
        cnpj_exibido = (
            format_cnpj_alfanum(
                st.session_state.cnpj_alfanum_gerado
            )
            if aplicar_mascara
            else st.session_state.cnpj_alfanum_gerado
        )

        st.markdown("##### CNPJ Alfanumérico Gerado")

        st.code(
            cnpj_exibido,
            language=None,
        )

    if st.button(
        "Gerar",
        use_container_width=True,
    ):
        st.session_state.cnpj_alfanum_gerado = generate_cnpj_alfanum()
        st.rerun()