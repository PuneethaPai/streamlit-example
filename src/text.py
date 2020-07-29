import streamlit as st
import streamlit.components.v1 as components

import spacy
from spacy import displacy

def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

# @st.cache
def load_model(path: str):
    return spacy.load(path)

_max_width_()

st.title("NER Service Demo")

text = st.text_area(label="Enter Your Text Here", value="Sample Text: Oxford University has found cure for COVID-19", height=200)
model = load_model("en_core_web_sm")

text

"## NER Highlight"
components.html(displacy.render(model(text), style="ent"), width = 2000, height=300, scrolling=True)

"## Dependency Tree"
components.html(displacy.render(model(text)), width = 2000, height=500, scrolling=True)


