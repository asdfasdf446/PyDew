from settings import *
from support import *
from debug import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('PyDew')
        self.clock = pygame.time.Clock()
        self.running = True
        self._initialize_game()

    def _initialize_game(self):
        """Initialize game assets and create the level."""
        self._load_assets()
        self.level = Level(self.tmx_maps, self.character_frames, self.level_frames, self.overlay_frames, self.font)

    def _load_assets(self):
        """Load all the game assets needed."""
        self.tmx_maps = tmx_importer('data', 'maps')
        self.character_frames = character_importer('images', 'characters')

        # Combine similar functions to avoid repetition
        self.level_frames = {

            'animations': animation_importer('images', 'animations'),
            'soil':       import_folder_dict('images', 'soil'),
            'soil water': import_folder_dict('images', 'soil water'),
            'plants': {
                'tomato': import_folder('images', 'plants', 'tomato'),
                'corn':   import_folder('images', 'plants', 'corn')
            },
            'rain drops': import_folder('images', 'rain', 'drops'),
            'rain floor': import_folder('images', 'rain', 'floor'),
            'objects':    import_folder_dict('images', 'objects')

        }

        self.overlay_frames = import_folder_dict('images', 'overlay')
        self.font = import_font(30, 'font', 'LycheeSoda.ttf')

    def _handle_events(self):
        """Handle all the game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            self._handle_events()
            self.screen.fill('gray')
            self.level.update(dt)
            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()

