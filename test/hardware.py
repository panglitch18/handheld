import pygame
import sys

class Hardware:
    def __init__(self, width = 128, height = 64, scale = 4):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        pygame.display.set_caption("Handheld Game")

        self.window = pygame.display.set_mode((width * scale, height * scale))
        self.canvas = pygame.Surface((width, height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("couriernew,consolas", 10)

        self.key_map = {
            "UP": pygame.K_UP,
            "DOWN": pygame.K_DOWN,
            "RIGHT": pygame.K_RIGHT,
            "LEFT": pygame.K_LEFT,
            "A": pygame.K_z,
            "B": pygame.K_x
        }

        self.running = True
        self.held = {btn: False for btn in self.key_map}
        self.prev_held = {btn: False for btn in self.key_map}
    
    def update_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.prev_held = self.held.copy() # I think this is wrong
        self.keys = pygame.key.get_pressed()

        for btn, key in self.key_map.items():
            self.held[btn] = bool(self.keys[key])
    
    def is_held(self, btn):
        return self.held.get(btn, False)

    def just_pressed(self, btn):
        return self.held.get(btn, False) and not self.prev_held.get(btn, False)

    def clear(self, color = (0,0,0)):
        self.canvas.fill(color)

    def draw_rect(self, x, y, w, h, color = (255,255,255)):
        pygame.draw.rect(self.canvas, color, (int(x), int(y), int(w), int(h)))

    def draw_text(self, text, x, y, color = (255,255,255)):
        img = self.font.render(str(text), False, color)
        self.canvas.blit(img, (int(x), int(y)))

    def render(self):
        new = pygame.transform.scale(self.canvas, (self.width * self.scale, self.height * self.scale))
        self.window.blit(new, (0, 0))
        pygame.display.flip()
        self.clock.tick(30)

    def quit(self):
        pygame.quit()
        sys.exit()