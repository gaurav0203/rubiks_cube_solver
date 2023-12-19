def text_to_display():
    with open('colors.txt','r') as f:
        faces_list = f.readlines()
        faces_color_list = []
        for face in faces_list:
            faces_color_list.append(face[:-1].lower().split(','))

        cube = {}

        for face in faces_color_list:
            current = ""
            if face[4] == "white":
                current = "white_center_face"
            elif face[4] == "red":
                current = "red_center_face"
            elif face[4] == "orange":
                current = "orange_center_face"
            elif face[4] == "green":
                current = "green_center_face"
            elif face[4] == "blue":
                current = "blue_center_face"
            elif face[4] == "yellow":
                current = "yellow_center_face"

            cube[current] = [[face[0],face[1],face[2]],[face[3],face[4],face[5]],[face[6],face[7],face[8]]]

        return cube


def display_to_kociemba(cube):
    kociemba_input_string = ""
    kociemba_input_string += get_face_string(cube["white_center_face"])
    kociemba_input_string += get_face_string(cube["blue_center_face"])
    kociemba_input_string += get_face_string(cube["red_center_face"])
    kociemba_input_string += get_face_string(cube["yellow_center_face"])
    kociemba_input_string += get_face_string(cube["green_center_face"])
    kociemba_input_string += get_face_string(cube["orange_center_face"])

    return kociemba_input_string


def get_face_string(face):
    face_string = ""

    for i in range(3):
        face_string += get_row_string(face[i])

    return face_string

def get_row_string(row):
    row_string = ""
    for cubie in row:
        if cubie == "white":
            row_string += 'U'
        elif cubie == "red":
            row_string += 'F'
        elif cubie == "orange":
            row_string += 'B'
        elif cubie == "green":
            row_string += 'L'
        elif cubie == "blue":
            row_string += 'R'
        elif cubie == "yellow":
            row_string += 'D'

    return row_string
def text_to_kociemba():
    cube = text_to_display()
    kociemba_input_string = display_to_kociemba(cube)
    return kociemba_input_string
