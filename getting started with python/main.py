import pygame
import random
import sys

# -----------------------------
# Game Configuration
# -----------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 15

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# -----------------------------
# Snake Game Class
# -----------------------------
class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("🐍 Snake Game with Effects")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 28, bold=True)

        # Create game window
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Initialize game state
        self.reset_game()

    def reset_game(self):
        """Reset snake, food, and score."""
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Snake body segments
        self.direction = "RIGHT"
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        """Generate food at a random grid position."""
        return (
            random.randrange(0, WINDOW_WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, WINDOW_HEIGHT // CELL_SIZE) * CELL_SIZE
        )

    def handle_input(self):
        """Handle keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                    self.direction = "RIGHT"
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()

    def move_snake(self):
        """Move snake in the current direction."""
        head_x, head_y = self.snake[0]
        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Check collisions
        if (
            head_x < 0 or head_x >= WINDOW_WIDTH or
            head_y < 0 or head_y >= WINDOW_HEIGHT or
            new_head in self.snake
        ):
            self.game_over = True
            return

        # Insert new head
        self.snake.insert(0, new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten

    def draw_snake(self):
        """Draw snake with gradient effect."""
        for i, segment in enumerate(self.snake):
            color_intensity = 255 - (i * 5) % 255
            pygame.draw.rect(
                self.screen,
                (0, color_intensity, 0),
                pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE)
            )

    def draw_food(self):
        """Draw food with glowing effect."""
        pygame.draw.rect(
            self.screen,
            RED,
            pygame.Rect(self.food[0], self.food[1], CELL_SIZE, CELL_SIZE)
        )
        # Glow outline
        pygame.draw.rect(
            self.screen,
            YELLOW,
            pygame.Rect(self.food[0] - 2, self.food[1] - 2, CELL_SIZE + 4, CELL_SIZE + 4),
            2
        )

    def draw_score(self):
        """Display score."""
        score_surface = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surface, (10, 10))

    def draw_game_over(self):
        """Display game over message."""
        game_over_surface = self.font.render("GAME OVER! Press R to Restart", True, RED)
        self.screen.blit(
            game_over_surface,
            (WINDOW_WIDTH // 2 - game_over_surface.get_width() // 2,
             WINDOW_HEIGHT // 2 - game_over_surface.get_height() // 2)
        )

    def run(self):
        """Main game loop."""
        while True:
            self.handle_input()

            if not self.game_over:
                self.move_snake()

            # Draw everything
            self.screen.fill(BLACK)
            self.draw_snake()
            self.draw_food()
            self.draw_score()

            if self.game_over:
                self.draw_game_over()

            pygame.display.flip()
            self.clock.tick(FPS)

# -----------------------------
# Run the Game
# -----------------------------
if __name__ == "__main__":
    SnakeGame().run()
