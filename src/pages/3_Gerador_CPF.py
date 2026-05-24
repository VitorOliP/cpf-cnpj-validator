import streamlit as st
from utils.cpf import generate_cpf


def formatar_cpf(cpf: str) -> str:
    return (
        f"{cpf[:3]}."
        f"{cpf[3:6]}."
        f"{cpf[6:9]}-"
        f"{cpf[9:]}"
    )


st.set_page_config(
    page_title="Gerador de CPF",
    page_icon="🪪",
    layout="centered",
)

st.title("Gerador de CPF")
st.caption(
    "Gere números de CPF válidos com máscara."
)

if "cpf_gerado" not in st.session_state:
    st.session_state.cpf_gerado = ""

with st.container(border=True):

    aplicar_mascara = st.toggle("Aplicar Máscara")

    if st.session_state.cpf_gerado:
        cpf_exibido = (
            formatar_cpf(st.session_state.cpf_gerado)
            if aplicar_mascara
            else st.session_state.cpf_gerado
        )

        st.markdown("##### CPF Gerado")
        st.code(
            cpf_exibido,
            language=None,
        )

    if st.button(
        "Gerar",
        use_container_width=True,
    ):
        st.session_state.cpf_gerado = generate_cpf()
        st.rerun()