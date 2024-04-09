import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DeathZerker")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


GRID_SIZE = 50
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x, self.y, GRID_SIZE, GRID_SIZE))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


def main_menu():
    while True:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 36)

        
        title_text = font.render("DeathZerker", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//4))
        screen.blit(title_text, title_rect)

        
        menu_options = ["Start Game", "Quit"]
        for i, option in enumerate(menu_options):
            option_text = font.render(option, True, BLACK)
            option_rect = option_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i * 50))
            screen.blit(option_text, option_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, _ in enumerate(menu_options):
                    option_rect = pygame.Rect((SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + i * 50 - 20), (200, 40))
                    if option_rect.collidepoint(mouse_pos):
                        if i == 0:  
                            return True
                        elif i == 1:  
                            pygame.quit()
                            sys.exit()
    return False


class CharacterCreation:
    def __init__(self):
        self.name = ""
        self.classes = ["Warrior", "Mage", "Rogue"]
        self.class_index = 0

    def draw(self, surface):
        font = pygame.font.SysFont(None, 36)

        
        title_text = font.render("Character Creation", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//4))
        surface.blit(title_text, title_rect)

        
        name_text = font.render("Name:", True, BLACK)
        surface.blit(name_text, (SCREEN_WIDTH//4, SCREEN_HEIGHT//2))
        pygame.draw.rect(surface, BLACK, (SCREEN_WIDTH//4 + 100, SCREEN_HEIGHT//2 - 5, 200, 30), 2)
        name_input = font.render(self.name, True, BLACK)
        surface.blit(name_input, (SCREEN_WIDTH//4 + 105, SCREEN_HEIGHT//2 + 5))

        
        class_text = font.render("Class:", True, BLACK)
        surface.blit(class_text, (SCREEN_WIDTH//4, SCREEN_HEIGHT//2 + 50))
        class_option = font.render(self.classes[self.class_index], True, BLACK)
        surface.blit(class_option, (SCREEN_WIDTH//4 + 100, SCREEN_HEIGHT//2 + 55))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            elif event.key == pygame.K_RETURN:
                pass  
            else:
                self.name += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if SCREEN_WIDTH//4 + 100 <= mouse_pos[0] <= SCREEN_WIDTH//4 + 300 and SCREEN_HEIGHT//2 - 5 <= mouse_pos[1] <= SCREEN_HEIGHT//2 + 25:
                pass  
            elif SCREEN_WIDTH//4 + 100 <= mouse_pos[0] <= SCREEN_WIDTH//4 + 300 and SCREEN_HEIGHT//2 + 50 <= mouse_pos[1] <= SCREEN_HEIGHT//2 + 80:
                self.class_index = (self.class_index + 1) % len(self.classes)


def main():
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        player.draw(screen)

        pygame.display.update()
        clock.tick(30)


def introductory_story():
    story = [
        "Long ago, in the land of Midgard,",
        "a great evil threatened to engulf the world.",
        "The only hope lay with the legendary DeathZerker,",
        "a warrior of unmatched power and skill.",
        "But to save the world, the DeathZerker needs",
        "a brave hero to wield its mighty sword..."
    ]

    font = pygame.font.SysFont(None, 24)
    line_height = 30
    y = SCREEN_HEIGHT // 2 - len(story) * line_height // 2

    for line in story:
        text = font.render(line, True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
        screen.blit(text, text_rect)
        y += line_height

    pygame.display.update()

    pygame.time.wait(3000)  


def main():
    if main_menu():
        character_creation = CharacterCreation()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                character_creation.handle_event(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    main()
            screen.fill(WHITE)
            character_creation.draw(screen)
            pygame.display.update()

if __name__ == "__main__":
    introductory_story()
    main()