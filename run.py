from visualizer import draw_cube
from movements import U, U_prime, F, F_prime, L, L_prime, R, R_prime, B, B_prime, D, D_prime
import rc_face_detector
import pygame
import format_converter
import kociemba

kociemba_solution = []

default_cube = {"white_center_face": [
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


def main(default_cube, kociemba_solution):
    sienna_brown = (160, 82, 45)
    # white = (200, 200, 200)
    window_height = 720
    window_width = 1280
    # offset = block_size = 50

    # global screen, clock

    pygame.init()
    pygame.display.set_caption("Rubik's Cube Visualizer & Solver")
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    font = pygame.font.Font("./Rubik_Doodle_Shadow/RubikDoodleShadow-Regular.ttf", 36)
    running = True
    while running:
        screen.fill(sienna_brown)
        draw_cube(screen, default_cube)
        draw_controller(screen, font)
        draw_capture(screen, font)
        draw_display(screen, font)
        draw_solve(screen, font)
        draw_solution(screen, font, kociemba_solution)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coordinates = pygame.mouse.get_pos()
                if 10 <= mouse_coordinates[0] <= 110 and 10 <= mouse_coordinates[1] <= 110:
                    U(default_cube)
                elif 115 <= mouse_coordinates[0] <= 215 and 10 <= mouse_coordinates[1] <= 110:
                    U_prime(default_cube)
                elif 10 <= mouse_coordinates[0] <= 110 and 115 <= mouse_coordinates[1] <= 215:
                    F(default_cube)
                elif 115 <= mouse_coordinates[0] <= 215 and 115 <= mouse_coordinates[1] <= 215:
                    F_prime(default_cube)
                elif 10 <= mouse_coordinates[0] <= 110 and 220 <= mouse_coordinates[1] <= 320:
                    L(default_cube)
                elif 115 <= mouse_coordinates[0] <= 215 and 220 <= mouse_coordinates[1] <= 320:
                    L_prime(default_cube)
                elif 10 <= mouse_coordinates[0] <= 110 and 325 <= mouse_coordinates[1] <= 425:
                    R(default_cube)
                elif 115 <= mouse_coordinates[0] <= 215 and 325 <= mouse_coordinates[1] <= 425:
                    R_prime(default_cube)
                elif 10 <= mouse_coordinates[0] <= 110 and 430 <= mouse_coordinates[1] <= 530:
                    B(default_cube)
                elif 115 <= mouse_coordinates[0] <= 215 and 430 <= mouse_coordinates[1] <= 530:
                    B_prime(default_cube)
                elif 10 <= mouse_coordinates[0] <= 110 and 535 <= mouse_coordinates[1] <= 635:
                    D(default_cube)
                elif 115 <= mouse_coordinates[0] <= 215 and 535 <= mouse_coordinates[1] <= 635:
                    D_prime(default_cube)
                elif 1050 <= mouse_coordinates[0] <= 1250 and 10 <= mouse_coordinates[1] <= 110:
                    # print("Cap")
                    rc_face_detector.main()
                    # print(default_cube)
                elif 1050 <= mouse_coordinates[0] <= 1250 and 120 <= mouse_coordinates[1] <= 220:
                    default_cube = format_converter.text_to_display()
                elif 1050 <= mouse_coordinates[0] <= 1250 and 230 <= mouse_coordinates[1] <= 330:
                    inp = format_converter.display_to_kociemba(default_cube)
                    # print(inp)

                    kociemba_solution = kociemba.solve(inp).split(" ")
                    # print(kociemba_solution)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def draw_controller(screen, font):
    button_text = ["U", "U'", "F", "F'", "L", "L'", "R", "R'", "B", "B'", "D", "D'"]
    k = 0
    button_size = 100
    x = y = 10
    for i in range(6):
        for j in range(2):
            draw_button(screen, font, x+button_size*j+5*j, y+button_size*i+5*i, button_size, button_text[k])
            k += 1


def draw_capture(screen, font):
    draw_button(screen, font, 1050, 10, 200, "Capture", 0.5)


def draw_display(screen, font):
    draw_button(screen, font, 1050, 120, 200, "Display", 0.5)


def draw_solve(screen, font):
    draw_button(screen, font, 1050, 230, 200, "Solve", 0.5)


def draw_button(screen, font, x, y, button_size_x, button_text, button_size_y_scaler=1.0):
    button = pygame.Rect(x, y, button_size_x, button_size_x*button_size_y_scaler)
    button_border = pygame.Rect(x, y, button_size_x, button_size_x*button_size_y_scaler)
    pygame.draw.rect(screen, (66, 135, 245), button, border_radius=10)
    pygame.draw.rect(screen, (20, 20, 20), button_border, border_radius=10, width=5)

    text_surface = font.render(button_text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)


def draw_solution(screen, font, kociemba_solution):
    text_surface = font.render('Solution : ', True, (0, 0, 0))
    screen.blit(text_surface, (10, 650))
    text_surface = font.render("  ".join(kociemba_solution), True, (0, 0, 0))
    screen.blit(text_surface, (200, 650))
    # print(kociemba_solution)


if __name__ == "__main__":
    F(default_cube)
    F(default_cube)
    B(default_cube)
    B(default_cube)
    U(default_cube)
    U(default_cube)
    D(default_cube)
    D(default_cube)
    L(default_cube)
    L(default_cube)
    R(default_cube)
    R(default_cube)
    main(default_cube, kociemba_solution)
