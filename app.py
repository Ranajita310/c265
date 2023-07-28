# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import numpy as n
import cv2

app = Flask(__name__)
@app.route("/")
# Write load_form function below to Open and redirect to default upload webpage
def load_form():
    return render_template("upload.html")

@app.route("/gray",methods=['POST'])
# Write upload_image Function to upload image and redirect to new webpage
def upload_image():
    store=request.files["the_filename"]
    filename=secure_filename(store.filename)
    converted_image=grayscale(store.read())
    with open(os.path.join("static/",filename), "wb") as f: 
        f.write(converted_image)
    #store.save(os.path.join('static/',filename))
    display_message="Image successfully uploaded and displayed belowww!"
    return render_template("upload.html",filename=filename,message=display_message)


@app.route("/display/<filename>")
# Write display_image Function to display the uploaded image
def display_image(filename):
    return redirect(url_for("static",filename=filename))

def grayscale(input_image):
    picture_array=n.fromstring(input_image,dtype="uint8")
    print("Picture array: ",picture_array)
    decoded_array=cv2.imdecode(picture_array,cv2.IMREAD_UNCHANGED)
    print("Decoded array: ",decoded_array)
    gray_image=cv2.cvtColor(decoded_array,cv2.COLOR_RGB2GRAY)
    status,output_image=cv2.imencode(".PNG",gray_image)
    print("status; ",status)
    return output_image


if __name__ == "__main__":
    app.run()