import streamlit as st

actor = st.radio(
  "what's your favourite movie Celebrities",["***Leminho**","***Nay Toe***","***Justic Biber***"],
  captions=["He is a korean acotor","He is a burmese actor.","He is a famours singer"],
)
if actor=="***Leminho**":
  st.write("Same with me")
elif actor=="***Nay Toe***":
  st.write("Why you prefer him")
else:
  st.write("he has a wife")
