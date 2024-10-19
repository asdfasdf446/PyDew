import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # imports
        overlay_path = '../graphics/overlay/'
        self.tools_surf = {}
        self.seeds_surf = {}
        try:
            self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
            self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}
        except pygame.error as e:
            print(f'Error loading overlay image: {e}')

    def display(self):
        # tool
        if self.player.selected_tool in self.tools_surf:
            tool_surf = self.tools_surf[self.player.selected_tool]
            tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS['tool'])
            self.display_surface.blit(tool_surf, tool_rect)
        else:
            print(f"Warning: Selected tool '{self.player.selected_tool}' not found in tools_surf.")

        # seeds
        if self.player.selected_seed in self.seeds_surf:
            seed_surf = self.seeds_surf[self.player.selected_seed]
            seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
            self.display_surface.blit(seed_surf, seed_rect)
        else:
            print(f"Warning: Selected seed '{self.player.selected_seed}' not found in seeds_surf.")

