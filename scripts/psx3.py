import pygame
import vgamepad as vg

gamepad = vg.VX360Gamepad()
pygame.init()
pygame.joystick.init()


AMARILLO = "\033[93m"
BLANCO = "\033[97m"
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"     

def identificar_joystick():
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print(ROJO + "Nenhum joystick conectado." + RESET)
        return None
    else:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(ROJO + f"Joystick conectado: {joystick.get_name()}" + RESET)
        return joystick
                                   
def title():
    print(VERDE + "Emulador PSX3" + RESET)
    print(VERDE + "-" * 67 + RESET)
    print(ROJO + "Author : Cyber Wanderer" + RESET)
    print(ROJO + "Github : https://github.com/kennedy-0" + RESET)

print(VERDE + "-" * 67 + RESET)
print(VERDE + "-" * 67 + RESET)
print(ROJO + "Controle virtual conectado" + RESET)
print(ROJO + f"Gamepad: {gamepad}" + RESET)
print(VERDE + "-" * 67 + RESET)


def comando():
    eixo_x_esquerdo = 0
    eixo_y_esquerdo = 0
    eixo_x_direito = 0
    eixo_y_direito = 0
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    
                    if event.button == 0:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gamepad.update()
                        
                    elif event.button == 1:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                        gamepad.update()

                    elif event.button == 2:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                        gamepad.update()

                    elif event.button == 3:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                        gamepad.update()

                    elif event.button == 4:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                        gamepad.update()

                    elif event.button == 5:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                        gamepad.update()

                    elif event.button == 6:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                        gamepad.update()

                    elif event.button == 7:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                        gamepad.update()

                    elif event.button == 8:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
                        gamepad.update()

                    elif event.button == 9:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                        gamepad.update()

                    #D-Pad
                    if event.button == 13:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                        gamepad.update()
                    elif event.button == 14:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                        gamepad.update()
                    elif event.button == 15:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                        gamepad.update()
                    elif event.button == 16:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                        gamepad.update()
                    #Joystick
                    if event.type == pygame.JOYAXISMOTION:
                        print("EIXO: ", event.axis, "VALOR: ", round(event.value, 2))
                    
                elif event.type == pygame.JOYBUTTONUP:

                    if event.button == 0:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gamepad.update()

                    elif event.button == 1:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                        gamepad.update()

                    elif event.button == 2:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                        gamepad.update()

                    elif event.button == 3:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                        gamepad.update()

                    elif event.button == 4:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                        gamepad.update()

                    elif event.button == 5:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                        gamepad.update()

                    elif event.button == 6:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
                        gamepad.update()

                    elif event.button == 7:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                        gamepad.update()

                    elif event.button == 8:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
                        gamepad.update()

                    elif event.button == 9:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                        gamepad.update()

                    #D-Pad
                    if event.button == 13:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                        gamepad.update()
                    elif event.button == 14:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                        gamepad.update()
                    elif event.button == 15:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                        gamepad.update()
                    elif event.button == 16:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                        

                elif event.type == pygame.JOYAXISMOTION:
                    valor = event.value

                    if event.axis == 0:
                        eixo_x_esquerdo = int(valor * 32767)

                    elif event.axis == 1:
                        eixo_y_esquerdo = int(valor * 32767)

                    elif event.axis == 2:
                        eixo_x_direito = int(valor * 32767)

                    elif event.axis == 3:
                        eixo_y_direito = int(valor * 32767)

                    gamepad.left_joystick(
                        x_value=eixo_x_esquerdo,
                        y_value=eixo_y_esquerdo
                    )

                    gamepad.right_joystick(
                        x_value=eixo_x_direito,
                        y_value=eixo_y_direito
                    )

                    gamepad.update()
                                                            
    except:         
        print(ROJO + "Erro ao processar os eventos do joystick." + RESET)
        pygame.quit()

if __name__ == "__main__":
    title()
    joystick = identificar_joystick()
    comando()
