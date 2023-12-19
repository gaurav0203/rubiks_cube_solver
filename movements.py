def U(cube):
    face_rotate_clockwise(cube["white_center_face"])
    (cube["red_center_face"][0], cube["green_center_face"][0],
     cube["orange_center_face"][0], cube["blue_center_face"][0]) = sides_row_rotate_clockwise(
                                cube["red_center_face"][0], cube["green_center_face"][0],
                                cube["orange_center_face"][0], cube["blue_center_face"][0])


def U_prime(cube):
    face_rotate_anticlockwise(cube["white_center_face"])
    (cube["red_center_face"][0], cube["green_center_face"][0],
     cube["orange_center_face"][0], cube["blue_center_face"][0]) = sides_row_rotate_anticlockwise(
        cube["red_center_face"][0], cube["green_center_face"][0],
        cube["orange_center_face"][0], cube["blue_center_face"][0])

def F(cube):
    face_rotate_clockwise(cube["red_center_face"])
    (cube["yellow_center_face"][0], [cube["green_center_face"][0][2],cube["green_center_face"][1][2],cube["green_center_face"][2][2]],
     [cube["white_center_face"][2][2],cube["white_center_face"][2][1],cube["white_center_face"][2][0]], [cube["blue_center_face"][2][0],cube["blue_center_face"][1][0],cube["blue_center_face"][0][0]]) = sides_row_rotate_clockwise(
        cube["yellow_center_face"][0],
        [cube["green_center_face"][0][2], cube["green_center_face"][1][2], cube["green_center_face"][2][2]],
        [cube["white_center_face"][2][2],cube["white_center_face"][2][1],cube["white_center_face"][2][0]],
        [cube["blue_center_face"][2][0], cube["blue_center_face"][1][0], cube["blue_center_face"][0][0]])

def F_prime(cube):
    face_rotate_anticlockwise(cube["red_center_face"])
    (cube["yellow_center_face"][0],
     [cube["green_center_face"][0][2], cube["green_center_face"][1][2], cube["green_center_face"][2][2]],
     [cube["white_center_face"][2][2], cube["white_center_face"][2][1], cube["white_center_face"][2][0]], [cube["blue_center_face"][2][0], cube["blue_center_face"][1][0],
                                    cube["blue_center_face"][0][0]]) = sides_row_rotate_anticlockwise(
        cube["yellow_center_face"][0],
        [cube["green_center_face"][0][2], cube["green_center_face"][1][2], cube["green_center_face"][2][2]],
        [cube["white_center_face"][2][2],cube["white_center_face"][2][1],cube["white_center_face"][2][0]],
        [cube["blue_center_face"][2][0], cube["blue_center_face"][1][0], cube["blue_center_face"][0][0]])


def L(cube):
    face_rotate_clockwise(cube["green_center_face"])
    ([cube["white_center_face"][0][0],cube["white_center_face"][1][0],cube["white_center_face"][2][0]],
     [cube["red_center_face"][0][0],cube["red_center_face"][1][0],cube["red_center_face"][2][0]],
     [cube["yellow_center_face"][0][0],cube["yellow_center_face"][1][0],cube["yellow_center_face"][2][0]],
     [cube["orange_center_face"][2][2],cube["orange_center_face"][1][2],cube["orange_center_face"][0][2]]) = (
        sides_row_rotate_clockwise([cube["white_center_face"][0][0],cube["white_center_face"][1][0],cube["white_center_face"][2][0]],
     [cube["red_center_face"][0][0],cube["red_center_face"][1][0],cube["red_center_face"][2][0]],
     [cube["yellow_center_face"][0][0],cube["yellow_center_face"][1][0],cube["yellow_center_face"][2][0]],
     [cube["orange_center_face"][2][2],cube["orange_center_face"][1][2],cube["orange_center_face"][0][2]]))


def L_prime(cube):
    face_rotate_anticlockwise(cube["green_center_face"])
    ([cube["white_center_face"][0][0], cube["white_center_face"][1][0], cube["white_center_face"][2][0]],
     [cube["red_center_face"][0][0], cube["red_center_face"][1][0], cube["red_center_face"][2][0]],
     [cube["yellow_center_face"][0][0], cube["yellow_center_face"][1][0], cube["yellow_center_face"][2][0]],
     [cube["orange_center_face"][2][2], cube["orange_center_face"][1][2], cube["orange_center_face"][0][2]]) = (
        sides_row_rotate_anticlockwise(
            [cube["white_center_face"][0][0], cube["white_center_face"][1][0], cube["white_center_face"][2][0]],
            [cube["red_center_face"][0][0], cube["red_center_face"][1][0], cube["red_center_face"][2][0]],
            [cube["yellow_center_face"][0][0], cube["yellow_center_face"][1][0], cube["yellow_center_face"][2][0]],
            [cube["orange_center_face"][2][2], cube["orange_center_face"][1][2], cube["orange_center_face"][0][2]]))

def R(cube):
    face_rotate_clockwise(cube["blue_center_face"])
    ([cube["white_center_face"][0][2], cube["white_center_face"][1][2], cube["white_center_face"][2][2]],
     [cube["orange_center_face"][2][0], cube["orange_center_face"][1][0], cube["orange_center_face"][0][0]],
     [cube["yellow_center_face"][0][2], cube["yellow_center_face"][1][2], cube["yellow_center_face"][2][2]],
     [cube["red_center_face"][0][2], cube["red_center_face"][1][2], cube["red_center_face"][2][2]]) = (
        sides_row_rotate_clockwise([cube["white_center_face"][0][2], cube["white_center_face"][1][2], cube["white_center_face"][2][2]],
     [cube["orange_center_face"][2][0], cube["orange_center_face"][1][0], cube["orange_center_face"][0][0]],
     [cube["yellow_center_face"][0][2], cube["yellow_center_face"][1][2], cube["yellow_center_face"][2][2]],
     [cube["red_center_face"][0][2], cube["red_center_face"][1][2], cube["red_center_face"][2][2]]))

def R_prime(cube):
    face_rotate_anticlockwise(cube["blue_center_face"])
    ([cube["white_center_face"][0][2], cube["white_center_face"][1][2], cube["white_center_face"][2][2]],
     [cube["orange_center_face"][2][0], cube["orange_center_face"][1][0], cube["orange_center_face"][0][0]],
     [cube["yellow_center_face"][0][2], cube["yellow_center_face"][1][2], cube["yellow_center_face"][2][2]],
     [cube["red_center_face"][0][2], cube["red_center_face"][1][2], cube["red_center_face"][2][2]]) = (
        sides_row_rotate_anticlockwise(
            [cube["white_center_face"][0][2], cube["white_center_face"][1][2], cube["white_center_face"][2][2]],
            [cube["orange_center_face"][2][0], cube["orange_center_face"][1][0], cube["orange_center_face"][0][0]],
            [cube["yellow_center_face"][0][2], cube["yellow_center_face"][1][2], cube["yellow_center_face"][2][2]],
            [cube["red_center_face"][0][2], cube["red_center_face"][1][2], cube["red_center_face"][2][2]]))

def B(cube):
    face_rotate_clockwise(cube["orange_center_face"])
    (cube["white_center_face"][0],[cube["green_center_face"][2][0],cube["green_center_face"][1][0],cube["green_center_face"][0][0]],
     [cube["yellow_center_face"][2][2], cube["yellow_center_face"][2][1], cube["yellow_center_face"][2][0]],[cube["blue_center_face"][0][2],cube["blue_center_face"][1][2],cube["blue_center_face"][2][2]]) = (
        sides_row_rotate_clockwise(cube["white_center_face"][0],[cube["green_center_face"][2][0],cube["green_center_face"][1][0],cube["green_center_face"][0][0]],
     [cube["yellow_center_face"][2][2], cube["yellow_center_face"][2][1], cube["yellow_center_face"][2][0]],[cube["blue_center_face"][0][2],cube["blue_center_face"][1][2],cube["blue_center_face"][2][2]]))

def B_prime(cube):
    face_rotate_anticlockwise(cube["orange_center_face"])
    (cube["white_center_face"][0],
     [cube["green_center_face"][2][0], cube["green_center_face"][1][0], cube["green_center_face"][0][0]],
     [cube["yellow_center_face"][2][2], cube["yellow_center_face"][2][1], cube["yellow_center_face"][2][0]],
     [cube["blue_center_face"][0][2], cube["blue_center_face"][1][2], cube["blue_center_face"][2][2]]) = (
        sides_row_rotate_anticlockwise(cube["white_center_face"][0],
                                       [cube["green_center_face"][2][0], cube["green_center_face"][1][0],
                                        cube["green_center_face"][0][0]],
                                       [cube["yellow_center_face"][2][2], cube["yellow_center_face"][2][1], cube["yellow_center_face"][2][0]],
                                       [cube["blue_center_face"][0][2], cube["blue_center_face"][1][2],
                                        cube["blue_center_face"][2][2]]))


def D(cube):
    face_rotate_clockwise(cube["yellow_center_face"])
    (cube["red_center_face"][2], cube["blue_center_face"][2], cube["orange_center_face"][2], cube["green_center_face"][2])=(
        sides_row_rotate_clockwise(cube["red_center_face"][2], cube["blue_center_face"][2], cube["orange_center_face"][2], cube["green_center_face"][2]))

def D_prime(cube):
    face_rotate_anticlockwise(cube["yellow_center_face"])
    (cube["red_center_face"][2], cube["blue_center_face"][2], cube["orange_center_face"][2],
     cube["green_center_face"][2]) = (
        sides_row_rotate_anticlockwise(cube["red_center_face"][2], cube["blue_center_face"][2],
                                   cube["orange_center_face"][2], cube["green_center_face"][2]))


def face_rotate_clockwise(face):
    transpose(face)
    mirror(face)

def face_rotate_anticlockwise(face):
    mirror(face)
    transpose(face)

def sides_row_rotate_anticlockwise(first, second, third, fourth):
    first, second, third, fourth = second, third, fourth, first
    return first, second, third, fourth


def sides_row_rotate_clockwise(first, second, third, fourth):
     first, second, third, fourth = fourth, first, second, third
     return first, second, third, fourth

def transpose(face):
    for i in range(len(face)):
        for j in range(i, len(face[0])):
            temp = face[i][j]
            face[i][j] = face[j][i]
            face[j][i] = temp

def mirror(face):
    for i in range(len(face)):
        face[i].reverse()


if __name__ == "__main__":
    first = [1,2,3]
    second = [4,5,6]
    third = [7,8,9]
    fourth = [10,11,12]
    first, second, third, fourth = sides_row_rotate_clockwise(first,second,third,fourth)
    #print(first)
    temp_cube = {"white_center_face": [
        ["white", "white", "white"],
        ["white", "white", "white"],
        ["white", "white", "white"]
    ],
        "red_center_face": [
            ["red", "red", "red"],
            ["red", "red", "red"],
            ["red", "red", "red"]
        ],
        "green_center_face": [
            ["green", "green", "green"],
            ["green", "green", "green"],
            ["green", "green", "green"]
        ],
        "orange_center_face": [
            ["orange", "orange", "orange"],
            ["orange", "orange", "orange"],
            ["orange", "orange", "orange"]
        ],
        "blue_center_face": [
            ["blue", "blue", "blue"],
            ["blue", "blue", "blue"],
            ["blue", "blue", "blue"]
        ],
        "yellow_center_face": [
            ["yellow", "yellow", "yellow"],
            ["yellow", "yellow", "yellow"],
            ["yellow", "yellow", "yellow"]
        ]}

    U(temp_cube)
    print(temp_cube)