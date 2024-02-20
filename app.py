from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt

from pexels_api import API

from dotenv import load_dotenv





load_dotenv()





import streamlit as st
from present_ai import get_presentation


def main():
    st.image("aipresenter.png")
    st.image("pptgen.png")
    st.write("Welcome to AI Presenter")
    topic = st.text_input("Enter a topic of PPT")

    # Store the presentation generated flag in Streamlit's session state
    if "presentation_generated" not in st.session_state:
        st.session_state.presentation_generated = False

    # Initialize ppt_bytes outside the if block
    ppt_bytes = None

    if topic:
        if not st.session_state.presentation_generated:
            ppt_bytes = get_presentation(topic)
            st.session_state.presentation_generated = True
            st.success("Presentation generated!")
        else:
            st.success("Presentation already generated!")

    if st.session_state.presentation_generated and ppt_bytes:
        # Provide the generated presentation for download
        st.download_button(
            "Download Presentation",
            ppt_bytes.getvalue(),
            file_name=f"{topic}.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

if __name__ == "__main__":
    main()









