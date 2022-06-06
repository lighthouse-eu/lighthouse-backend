from PIL import Image
import face_recognition

# Encoding information of images
list_known_face_encodings = []


def lost_person_image(image_path):
    lost_image = face_recognition.load_image_file(image_path)
    lost_image_encodings = face_recognition.face_encodings(lost_image)[0]
    # print(lost_image_encodings)
    list_known_face_encodings.append(lost_image_encodings)


def found_person_image(image_path):
    found_image = face_recognition.load_image_file(image_path)
    lost_image_encodings = face_recognition.face_encodings(found_image)[0]
    return lost_image_encodings


def image_match(found_person_encodings, known_face_encodings):
    for i, known_image in enumerate(known_face_encodings):
        match_results = face_recognition.compare_faces([known_image], found_person_encodings)

        if match_results[0]:
            print("Matched:", i)
        else:
            print("Not a Match")


# sample images
list_lost = ['./known/diana.jpg', './known/boris.jpg', './known/obama.jpg', './known/donald.jpg', './known/hilary.jpg']

# Retrieve Encodings of known images
for lost_img in list_lost:
    lost_person_image(lost_img)


# Found person image /test image
test_image = './unknown/donaldtest.jpg'
found_person = found_person_image(test_image)

# Run a match between lost and list of found images
image_match(found_person, list_known_face_encodings)
