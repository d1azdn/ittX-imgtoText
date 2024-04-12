import cv2
import easyocr
import webbrowser
import os
import imgSharpen
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

def imageOCR(self,image,method):
    match method:
        case "morphEx" :
            img = imgSharpen.sharpening()
            img = img.morphEx(image)
        case "unsharpMask" :
            img = imgSharpen.sharpening()
            img = img.unsharpMask(image)
        case "gaussThresh" : 
            img = imgSharpen.sharpening()
            img = img.gaussThresh(image)
        case None : 
            img = image
    
    reader = easyocr.Reader(['en'], gpu=True)
    readText = reader.readtext(img)
    text = ""
    for t in text:
        text = text + t[1] + " "
    
    st.session_state.text = text
    st.session_state.enhanced = "imageEnhanced.png"


fileCheck = [f for f in os.listdir("./examples") if f.endswith(".png") 
             or f.endswith(".jpg") or f.endswith(".jpeg")]

grayBg = "https://www.solidbackgrounds.com/images/1280x720/1280x720-light-gray-solid-color-background.jpg"

if "menu" not in st.session_state:
    st.session_state.text = "Your text will show here."
    st.session_state.enhanced = grayBg


##########
st.set_page_config(page_title="imagetoText - ittX", layout='wide')

class streamlitContainer :
    def container(self,input):
        with st.container():
            match input:
                case 1:
                    pass

                case 2:
                    self.left, self.right = st.columns(2)

                case 3:
                    self.left, self.middle, self.right = st.columns(3)

                case _: return

    def iconMid(self,input):
        a,b,c = st.columns(3)
        with b :
            st.image(input, width=250)

    def setContent(self,input):
        st.image(input['image'])
        st.subheader(input['title'])
        st.text(input['view'])
        st.write(input['author'])

header = streamlitContainer()
header.container(2)
with header.left:
    header.iconMid("https://cdn-icons-png.flaticon.com/512/25/25231.png")

with header.right: 
    st.title("ittX - Image to Text")
    st.write("Convert your **image** into **text**, with just a few clicks!")
    if st.button("Start now!"):
        pass

st.markdown("#")
st.write("---")#####
st.markdown("#")

main = streamlitContainer()
main.container(2)
with main.left : 
    file = st.selectbox('Select your image. (png/jpg/jpeg)', fileCheck)
    st.image("./examples/"+file)
    if st.checkbox("Include sharpening image"):
        choice = st.radio("--- Choose method ---",["morphEx", "unsharpMask", "gaussThresh"],
                          captions=['','','Just make it b&w'])
    if st.button("Generate"):
        imageOCR("./examples/"+file)

with main.right:
    st.write("Your text will show here.")
    st.code(st.session_state.text)
    st.write("---")
    st.write("Sharpened image : ")
    st.image(st.session_state.enhanced)
