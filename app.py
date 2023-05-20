from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt
from text_gen import get_response
from image import get_image
import streamlit as st
from present_ai import get_presentation



def main():
    st.image("aipresenter.png")
    st.image("pptgen.png")
    topic = st.text_input("Enter a topic of PPT")

    if topic:
        get_presentation(topic)
        st.success("Presentation generated!")

        # Provide the generated presentation for download
        with open("output.pptx", "rb") as f:
            st.download_button("Download Presentation", f.read(), file_name="output.pptx")


# Run the Streamlit web application
if __name__ == "__main__":
    main()





