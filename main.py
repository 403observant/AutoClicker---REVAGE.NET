import os
import time
import random
import threading
from pynput import mouse, keyboard
from pystyle import *

# Clear screen and set title
os.system("cls")
os.system("title ")

# Color constants
RED = '\033[1;91m'
WHITE = '\033[0m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
GOLD = '\033[0;33m'

class MinecraftAutoClicker:
    def __init__(self):
        self.left_clicking = False
        self.right_clicking = False
        self.running = True
        self.mouse_controller = mouse.Controller()
        
        # Initialize listeners
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        
        # Start listeners
        self.keyboard_listener.start()
        self.mouse_listener.start()
        
        # Start clicking thread
        self.clicking_thread = threading.Thread(target=self.clicking_loop, daemon=True)
        self.clicking_thread.start()

    def on_key_press(self, key):
        try:
            if key.char == 'r':
                self.left_clicking = not self.left_clicking
                status = f"{GREEN}Enabled{WHITE}" if self.left_clicking else f"{RED}Disabled{WHITE}"
                print(f"{BLUE}[!] {WHITE}Left AutoClicker: {status}")
        except AttributeError:
            pass

    def on_mouse_click(self, x, y, button, pressed):
        if button == mouse.Button.x2:
            self.right_clicking = pressed
            status = f"{GREEN}Enabled{WHITE}" if pressed else f"{RED}Disabled{WHITE}"
            print(f"{BLUE}[!] {WHITE}Right AutoClicker: {status}")

    def random_delay(self, is_right_click=False):
        base_delay = random.uniform(0.1, 0.125) if is_right_click else random.uniform(0.006, 0.008)
        micro_variation = random.uniform(0, 0.001)
        
        if random.random() < 0.03:
            base_delay += random.uniform(0.001, 0.002)
        
        return base_delay + micro_variation

    def click(self, is_right_click=False):
        if random.random() < 0.02:
            return
            
        click_duration = random.uniform(0.001, 0.002)
        button = mouse.Button.right if is_right_click else mouse.Button.left
        
        self.mouse_controller.press(button)
        time.sleep(click_duration)
        self.mouse_controller.release(button)

    def clicking_loop(self):
        while True:
            if self.left_clicking:
                self.click(is_right_click=False)
                time.sleep(self.random_delay(is_right_click=False))
            elif self.right_clicking:
                self.click(is_right_click=True)
                time.sleep(self.random_delay(is_right_click=True))
            else:
                time.sleep(0.1)

def main():
    banner = """
    ███████╗░█████╗░░██████╗██╗░░░██╗░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗
    ██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝
    █████╗░░███████║╚█████╗░░╚████╔╝░██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░
    ██╔══╝░░██╔══██║░╚═══██╗░░╚██╔╝░░██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░
    ███████╗██║░░██║██████╔╝░░░██║░░░╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗
    ╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝
    """
    
    print()
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))
    print()
    print(f"{BLUE}[*]{WHITE} Controls:")
    print(f"{BLUE}[*]{WHITE} R - Toggle Left AutoClicker")
    print(f"{BLUE}[*]{WHITE} M5 (Hold) - Right AutoClicker for Building")
    print("─" * 65)
    
    clicker = MinecraftAutoClicker()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
