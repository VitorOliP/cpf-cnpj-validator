import streamlit as st
from utils.cnpj import validar_cnpj

st.set_page_config(
    page_title="Validador de CNPJ",
    page_icon="🏢",
    layout="centered",
)

st.title("🏢 Validador de CNPJ")
st.caption("Digite um CNPJ para verificar se ele é válido.")

with st.form("cnpj_form"):
    cnpj = st.text_input(
        "CNPJ",
        placeholder="00.000.000/0000-00 ou 00000000000000",
        max_chars=18,
        help="Aceita CNPJ com ou sem pontuação.",
    )

    submitted = st.form_submit_button(
        "🔍 Validar CNPJ",
        use_container_width=True,
    )

if submitted:

    if not cnpj.strip():
        st.info("ℹ️ Informe um CNPJ.")
        st.stop()

    st.markdown("### CNPJ informado")
    st.code(cnpj, language=None)

    if validar_cnpj(cnpj):
        st.success("✅ CNPJ válido")
    else:
        st.error("❌ CNPJ inválido")