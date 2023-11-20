import streamlit as st

headerSelection = st.container()
mainSection = st.container()
LeftNav = st.sidebar

with headerSelection:
    st.title("Streamlit")
    st.markdown("This is a demo of Streamlit - TEST-Repeated5")

with mainSection:
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("Left Column")
        st.markdown("Left Column")
        textValue = st.text_input("Enter text", "")
        st.write(textValue)

    with right_col:
        st.header("Right Column")
        st.markdown("Right Column")


with LeftNav:
    st.button("menu1", on_click=lambda: st.success("Menu1"))
    st.button("menu2", on_click=lambda: st.success("Menu2"))
