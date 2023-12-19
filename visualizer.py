import pygame
from movements import face_rotate_clockwise, face_rotate_anticlockwise

sienna_brown = (160, 82, 45)
white = (200, 200, 200)
window_height = 720
window_width = 1280
offset = block_size = 50

temp_cube = {"white_center_face":[
                    ["white", "white", "white"],
                    ["white", "white", "white"],
                    ["white", "white", "white"]
                ],
             "red_center_face":[
                    ["red", "red", "red"],
                    ["red", "red", "red"],
                    ["red", "red", "red"]
                ],
             "green_center_face":[
                    ["green", "green", "green"],
                    ["green", "green", "green"],
                    ["green", "green", "green"]
                ],
             "orange_center_face":[
                    ["orange", "orange", "orange"],
                    ["orange", "orange", "orange"],
                    ["orange", "orange", "orange"]
                ],
             "blue_center_face":[
                    ["blue", "blue", "blue"],
                    ["blue", "blue", "blue"],
                    ["blue", "blue", "blue"]
                ],
             "yellow_center_face":[
                    ["yellow", "yellow", "yellow"],
                    ["yellow", "yellow", "yellow"],
                    ["yellow", "yellow", "yellow"]
                ]}

def main(cube=temp_cube):
    global screen, clock

    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(sienna_brown)
        draw_cube(screen, cube)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def draw_grid(screen, x, y, cubies_face_color):
    # block_size = 50
    # x, y = 110, 110
    cube_face = pygame.Rect(x, y, block_size, block_size)
    border = pygame.Rect(x, y, block_size, block_size)

    pygame.draw.rect(screen, cubies_face_color, cube_face, border_radius=5)
    pygame.draw.rect(screen, white, border, 3, border_radius=5)


def draw_face(screen, x, y, cubies_face_color):
    for i in range(3):
        for j in range(3):
            draw_grid(screen, x + j * offset, y + i * offset, cubies_face_color[i][j])


def draw_cube(screen, cube=temp_cube):
    draw_face(screen, window_width // 2 - 2 * block_size, window_height // 2 - 2 * block_size, cube["red_center_face"])
    draw_face(screen, window_width // 2 - 2 * block_size, window_height // 2 + block_size, cube["yellow_center_face"])

    draw_face(screen, window_width // 2 - 5 * block_size, window_height // 2 - 2 * block_size, cube["green_center_face"])
    draw_face(screen, window_width // 2 - 2 * block_size, window_height // 2 - 5 * block_size, cube["white_center_face"])
    draw_face(screen, window_width // 2 + block_size, window_height // 2 - 2 * block_size, cube["blue_center_face"])
    draw_face(screen, window_width // 2 + 4 * block_size, window_height // 2 - 2 * block_size, cube["orange_center_face"])


if __name__ == "__main__":
    main()
