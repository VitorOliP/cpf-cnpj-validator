import streamlit as st
from utils.cpf import validate_cpf

st.set_page_config(
    page_title="Validador de CPF",
    page_icon="🪪",
    layout="centered",
)

st.title("Validador de CPF")
st.caption("Digite um CPF para verificar se ele é válido.")

with st.form("cpf_form"):
    cpf = st.text_input(
        "CPF",
        placeholder="000.000.000-00, 00000000000",
        max_chars=14,
        help="Aceita CPF com ou sem pontuação.",
    )

    submitted = st.form_submit_button(
        "🔍 Validar CPF",
        use_container_width=True,
    )

if submitted:

    if not cpf.strip():
        st.info("ℹ️ Informe um CPF.")
        st.stop()

    st.markdown("### CPF informado")
    st.code(cpf, language=None, )

    if validate_cpf(cpf):
        st.success("✅ CPF válido")
    else:
        st.error("❌ CPF inválido")