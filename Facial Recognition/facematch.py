from PIL import Image
import face_recognition

# Array for appending it to the list of known images
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


# Inserting multiple image path to the list
list_lost = ['./known/diana.jpg', './known/boris.jpg', './known/obama.jpg', './known/donald.jpg', './known/hilary.jpg']

# Calling function lost_person_image

for lost_img in list_lost:
    lost_person_image(lost_img)

'''  
print(list_known_face_encodings)
for i in list_known_face_encodings:
    print(f"Face Encodings {i}") '''

# Found person image
test_image = './unknown/donaldtest.jpg'
found_person = found_person_image(test_image)

# Running a match lost and found image
image_match(found_person, list_known_face_encodings)
