import pygame
from settings import *
from debug import *

class Menu:
    def __init__(self, player, toggle_menu, font):

        # general setup
        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = font
        self.index = 0
        self.menu_is_active = False  # Add a flag to track whether the menu is active

        # options
        self.width = 400
        self.space = 10
        self.padding = 8

        # entries
        self.options = list(self.player.inventory.keys())
        self.setup()

    def display_money(self):
        """Display the player's current money on the screen."""
        text_surf = self.font.render(f'${self.player.money}', False, 'Black')
        text_rect = text_surf.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20))

        pygame.draw.rect(self.display_surface, 'White', text_rect.inflate(10, 10), 0, 4)
        self.display_surface.blit(text_surf, text_rect)

    def setup(self):
        """Setup the menu options and calculate dimensions."""
        # create the text surfaces
        self.text_surfs = []
        self.total_height = 0

        for item in self.options:
            text_surf = self.font.render(item, False, 'Black')
            self.text_surfs.append(text_surf)
            self.total_height += text_surf.get_height() + (self.padding * 2)

        self.total_height += (len(self.text_surfs) - 1) * self.space
        self.menu_top = SCREEN_HEIGHT / 2 - self.total_height / 2
        self.main_rect = pygame.Rect(SCREEN_WIDTH / 2 - self.width / 2, self.menu_top, self.width, self.total_height)

        # buy / sell text surface
        self.buy_text = self.font.render('buy', False, 'Black')
        self.sell_text = self.font.render('sell', False, 'Black')

    def _menu_input(self):
        """Handle player input for navigating and interacting with the menu."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.index = (self.index + 1) % len(self.options)
        elif keys[pygame.K_UP]:
            self.index = (self.index - 1) % len(self.options)
        
        if keys[pygame.K_ESCAPE]:
            logging.debug("ESCAPE key pressed, toggling menu")
            self.toggle_menu()

        if keys[pygame.K_SPACE]:
            self.handle_transaction()

    def handle_transaction(self):
        """Handle buying or selling items based on the selected menu option."""
        current_item = self.options[self.index]
        if self.is_seed(current_item):
            seed_price = PURCHASE_PRICES[current_item]
            if self.player.money >= seed_price:
                self.player.inventory[current_item] += 1
                self.player.money -= seed_price
        else:
            if self.player.inventory[current_item] > 0:
                self.player.inventory[current_item] -= 1
                self.player.money += SALE_PRICES[current_item]

    def is_seed(self, item):
        """Determine if the given item is a seed."""
        return 'seed' in item

    def show_entry(self, text_surf, amount, top, index, text_index):
        """Display a single menu entry, including its background, text, and amount."""
        # background
        bg_rect = pygame.Rect(self.main_rect.left, top, self.width, text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, 'White', bg_rect, 0, 4)

        # text
        text_rect = text_surf.get_rect(midleft=(self.main_rect.left + 20, bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)

        # amount
        amount_surf = self.font.render(str(amount), False, 'Black')
        amount_rect = amount_surf.get_rect(midright=(self.main_rect.right - 20, bg_rect.centery))
        self.display_surface.blit(amount_surf, amount_rect)

        # selected
        if index == text_index:
            pygame.draw.rect(self.display_surface, 'black', bg_rect, 4, 4)
            pos_rect = self.buy_text.get_rect(midleft=(self.main_rect.left + 250, bg_rect.centery))
            surf = self.sell_text if self.is_seed(self.options[index]) else self.buy_text
            self.display_surface.blit(surf, pos_rect)

    def update(self):
        """Update the menu, handle input, and display all entries."""
        if self.menu_is_active:
            logging.debug("menu: active")
            self._menu_input()
            self.display_money()

            for text_index, text_surf in enumerate(self.text_surfs):
                top = self.main_rect.top + text_index * (text_surf.get_height() + (self.padding * 2) + self.space)
                amount_list = list(self.player.inventory.values())
                amount = amount_list[text_index]
                self.show_entry(text_surf, amount, top, self.index, text_index)

    def toggle_menu(self):
        """Toggle the game menu visibility."""
        self.menu_is_active = not self.menu_is_active

