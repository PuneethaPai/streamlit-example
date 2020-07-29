# Streamlit
So far on my experience streamlit is a powerful tool for data visualisation, quick dashboarding. The api design is very intuitive and very easy to get started. I say powerful because in few lines of code you can have dashboard with great interaction.


## What is it for:
- Really great for quick Dashboard prototyping and interaction.
- Has a wide range of tools integration.
- Easy to convert output any tool you are familiar, to an interactive dashboard using streamlit
- Pretty lighweight both as library and to use !! :winking face
- Design decisions like caching, dynamic content rendering has made streamlit standout from others.

## What is it **NOT** for:
- It is not for full fledged web app developement.
- Security, authentication, authorisation, scaling is out of scope for streamlit.
- These can be handled separately, if you still want to use steramlit.


# Dash VS Streamlit:
These are my experience of using both tools. For more detailed comparision you can refer [here](https://plotly.com/comparing-dash-shiny-streamlit/) which I think is little biased towards _Dash enterprise_


| Dimension        | Dash                         | Streamlit                      |
| ---------------- | ---------------------------- | ------------------------------ |
| Use case         | Dash-board + Web app         | Dashboard                      |
| Maturity         | 2017                         | 2019                           |
| Popularity       | High                         | ~ High and Catching up         |
| Learning Curve   | Moderate - High              | **ZERO**                       |
| Features         | Both are Comparable          |
| Speed            | Decreases with data size     | Better (because of Caching)    |
| Consistency      | Can be inconsistent at times | Highly accurate and consistent |
| Customisability  | High                         | Low - Moderate                 |
| Tool integration | Plotly, Flask                | ~ Everything                   |
| Backend          | Flask                        | Tornado                        |


# Demo:
Activate your python virtual env. Then
```bash
pip install requirements.txt

streamlit run src/numeric.py
```

# Useful Links:
[Dash VS R-Shiny VS Streamlit Comparison](https://plotly.com/comparing-dash-shiny-streamlit/)

[Streamlit Compatible Tools](https://www.streamlit.io/)

[Streamlit Gallery](https://www.streamlit.io/gallery)

[Dash Gallery](https://dash-gallery.plotly.host/Portal/)
