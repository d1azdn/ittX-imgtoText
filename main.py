import cv2
import easyocr
import webbrowser
import os
import imgSharpen
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

def imageOCR(image,method):
    match method:
        case "morphEx" :
            img = imgSharpen.sharpening()
            img = img.morphEx(image)
            st.session_state.enhanced = "./imageEnhanced.png"
        case "unsharpMask" :
            img = imgSharpen.sharpening()
            img = img.unsharpMask(image)
            st.session_state.enhanced = "./imageEnhanced.png"
        case "gaussThresh" : 
            img = imgSharpen.sharpening()
            img = img.gaussThresh(image)
            st.session_state.enhanced = "./imageEnhanced.png"
        case None : 
            img = image
    
    reader = easyocr.Reader(['en'], gpu=True)
    readText = reader.readtext(img)
    text = ""
    for t in readText:
        text = text + t[1] + " "
    
    st.session_state.text = text


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
##########


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
    choice = None
    if st.checkbox("Include sharpening image"):
        st.warning("If the generated text isn't right, please turn off Sharpening Image.")
        choice = st.radio("--- Choose method ---",["unsharpMask", "morphEx", "gaussThresh"],
                          captions=['(Recommended)','',''], index=None)
    if st.button("Generate"):
        imageOCR("./examples/"+file, choice)

with main.right:
    st.text_area("Your text will show here.", st.session_state.text)
    st.write("---")
    st.write("Sharpened image : ")
    st.image(st.session_state.enhanced)


st.markdown("#")
st.write("---")#####
st.markdown("#")


bottom = streamlitContainer()
bottom.container(2)
with bottom.left : 
    st.title("What is ittX ?")
    st.write("(ittX - imagetoText) is an application that convert image into text, with help of python package : EasyOCR.")
    st.write("And also there are features to enhance your image too!")

with bottom.right:
    bottom.iconMid("https://icons.iconarchive.com/icons/dtafalonso/android-l/256/Youtube-icon.png")


st.markdown("#")
st.write("---")#####
st.markdown("#")


footer = streamlitContainer()
footer.container(2)
with footer.right : 
    st.title("About this Project")
    st.write("This is my **second** project for python language. I will happy to accept any suggestion you share with me ^^.")
    st.write("My Github page linked down below.")
    if st.button("See more on Github ->") :
        webbrowser.open("https://github.com/d1azdn")

with footer.left:
    footer.iconMid("https://cdn-icons-png.flaticon.com/512/25/25231.png")
