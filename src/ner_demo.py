import streamlit as st
import streamlit.components.v1 as components
import spacy
from spacy import displacy

model = spacy.load("en_core_web_sm")


st.title("NER Service Demo")

text = st.text_area(
    label="Enter Your Text Here",
    value="Sample Text: Oxford University has found cure for COVID-19",
    height=200,
)

text

"## NER Highlight"

components.html(displacy.render(model(text), style="ent"), width = 800, height=300, scrolling=True)


# Latext Support:
st.latex(
    r"""
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     """
)

