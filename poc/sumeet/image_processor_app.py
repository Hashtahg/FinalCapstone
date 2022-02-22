#------------------------------------------------------
# The program is an evaluation of the opencv library
# in streamlit
#------------------------------------------------------
__author__ = "Sumeet Vaidya"
#------------------------------------------------------


import face_recognition
import imutils
import pickle
import time
import cv2
import os
from PIL import Image,ImageEnhance
import numpy as np 
import streamlit as st

#find path of xml file containing haarcascade file
cascPathface = "./etc/haarcascade_frontalface_alt2.xml"

# load the harcaascade in the cascade classifier
face_cascade = cv2.CascadeClassifier(cascPathface)

# load the known faces and embeddings saved in last file
enc_dir="./data"
enc_file = enc_dir+"/face_enc"
data = pickle.loads(open(enc_file, "rb").read())

#choice = st.selectbox("Select Option",[
#    "Face Detection",
#    "Face Detection 2",
#    "Face Verification"
#])


def compare_face_image(img, faces):
	encodings = face_recognition.face_encodings(img)
	names = []

	# loop over the facial embeddings incase
	# we have multiple embeddings for multiple fcaes
	for encoding in encodings:

		#Compare encodings with encodings in data["encodings"]
		#Matches contain array with boolean values and True for the embeddings it matches closely
		#and False for rest

		matches = face_recognition.compare_faces(data["encodings"], encoding)

		#set name =inknown if no encoding matches
		name = "Unknown"

		# check to see if we have found a match
		if True in matches:
			#Find positions at which we get True and store them
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				#Check the names at respective indexes we stored in matchedIdxs
				name = data["names"][i]
				#increase count for the name we got
				counts[name] = counts.get(name, 0) + 1
				#set name which has highest count
				name = max(counts, key=counts.get)

			# update the list of names
			names.append(name)
			# loop over the recognized faces
			for ((x, y, w, h), name) in zip(faces, names):
				# rescale the face coordinates
				# draw the predicted face name on the image
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
				cv2.putText(img, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
					0.75, (0, 255, 0), 2)


	return names


def detect_faces(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	return img,faces 



def main():
	"""Face Detection App"""

	st.title("Face Detection App")
	st.text("Build with Streamlit and OpenCV")

	activities = ["Detection","About"]
	choice = st.sidebar.selectbox("Select Activty",activities)

	if choice == 'Detection':
		st.subheader("Face Detection")

		image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)
			st.text("Original Image")
			# st.write(type(our_image))
			st.image(our_image)
			

			enhance_type = st.sidebar.radio("Enhance Type",
				["Original","Gray-Scale","Contrast","Brightness","Blurring"])
			if enhance_type == 'Gray-Scale':
				new_img = np.array(our_image.convert('RGB'))
				img = cv2.cvtColor(new_img,1)
				gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
				# st.write(new_img)
				st.image(gray)
			elif enhance_type == 'Contrast':
				c_rate = st.sidebar.slider("Contrast",0.5,3.5)
				enhancer = ImageEnhance.Contrast(our_image)
				img_output = enhancer.enhance(c_rate)
				st.image(img_output)
	
			elif enhance_type == 'Brightness':
				c_rate = st.sidebar.slider("Brightness",0.5,3.5)
				enhancer = ImageEnhance.Brightness(our_image)
				img_output = enhancer.enhance(c_rate)
				st.image(img_output)
	
			elif enhance_type == 'Blurring':
				new_img = np.array(our_image.convert('RGB'))
				blur_rate = st.sidebar.slider("Brightness",0.5,3.5)
				img = cv2.cvtColor(new_img,1)
				blur_img = cv2.GaussianBlur(img,(11,11),blur_rate)
				st.image(blur_img)
	           
			elif enhance_type == 'Original':
				st.image(our_image,width=300)
			else:
				st.image(our_image,width=300)
	
	
	
			# Face Detection
			task = ["Faces","Smiles","Eyes","Cannize","Cartonize"]
			feature_choice = st.sidebar.selectbox("Find Features",task)
			if st.button("Process"):
	
				if feature_choice == 'Faces':
					result_img,result_faces = detect_faces(our_image)
					st.image(result_img)
					st.success("Found {} faces".format(len(result_faces)))
					result_names=compare_face_image(result_img,result_faces)
					st.image(result_img)
					st.success("Found {} matched faces".format(len(result_names)))
	
	#			elif feature_choice == 'Smiles':
	#				result_img = detect_smiles(our_image)
	#				st.image(result_img)
	
	
	#			elif feature_choice == 'Eyes':
	#				result_img = detect_eyes(our_image)
	#				st.image(result_img)
	
	#			elif feature_choice == 'Cartonize':
	#				result_img = cartonize_image(our_image)
	#				st.image(result_img)
	
	#			elif feature_choice == 'Cannize':
	#				result_canny = cannize_image(our_image)
	#				st.image(result_canny)




	elif choice == 'About':
		st.subheader("About Face Detection App")
		st.markdown("Built with Streamlit by [Sumeet,Pat, Bipasha, Hossain]")
		st.text("Sumeet,Pat, Bipasha, Hossain")
		st.success("Sumeet,Pat, Bipasha, Hossain")








if __name__ == "__main__":
    main()
