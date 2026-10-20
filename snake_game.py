import random
import pygame

WIDTH, HEIGHT = 600, 400
SNAKE_BLOCK = 20
# 每秒移动的格数：数字越大，速度越快。
DIFFICULTIES = {"Easy": 5, "Normal": 8, "Hard": 12}
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)


def new_food(snake):
    """只在空格子里生成食物；填满棋盘时返回 None。"""
    empty = [(x, y) for x in range(0, WIDTH, SNAKE_BLOCK)
             for y in range(0, HEIGHT, SNAKE_BLOCK) if (x, y) not in snake]
    return random.choice(empty) if empty else None


def move_snake(snake, direction, food):
    """计算一次移动，返回蛇、食物、是否吃到食物、是否碰撞。"""
    x, y = snake[-1]
    dx, dy = direction
    head = (x + dx, y + dy)
    eating = head == food
    # 没有吃食物时，尾巴同时移走，因此可以走到原来尾巴的位置。
    body = snake if eating else snake[1:]
    if not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT) or head in body:
        return snake, food, False, True
    snake = body + [head]
    if eating:
        food = new_food(snake)
    return snake, food, eating, False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()

    def text(message, y, color=WHITE, large=False):
        image = (title_font if large else font).render(message, True, color)
        screen.blit(image, image.get_rect(center=(WIDTH // 2, y)))

    state = "menu"
    difficulty = "Normal"
    snake = [(300, 200)]
    direction = (SNAKE_BLOCK, 0)
    food = new_food(snake)
    score = 0
    elapsed = 0
    turned = False
    running = True
    keys = {pygame.K_LEFT: (-SNAKE_BLOCK, 0),
            pygame.K_RIGHT: (SNAKE_BLOCK, 0),
            pygame.K_UP: (0, -SNAKE_BLOCK),
            pygame.K_DOWN: (0, SNAKE_BLOCK)}

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    state = "menu"
                elif state == "menu":
                    choices = {pygame.K_1: "Easy", pygame.K_2: "Normal", pygame.K_3: "Hard"}
                    if event.key in choices:
                        difficulty = choices[event.key]
                    elif event.key == pygame.K_RETURN:
                        snake = [(300, 200)]
                        direction = (SNAKE_BLOCK, 0)
                        food = new_food(snake)
                        score = 0
                        elapsed = 0
                        turned = False
                        state = "playing"
                elif state in ("playing", "paused") and event.key == pygame.K_SPACE:
                    state = "paused" if state == "playing" else "playing"
                    elapsed = 0
                elif state == "playing" and event.key in keys and not turned:
                    proposed = keys[event.key]
                    if proposed != (-direction[0], -direction[1]):
                        direction = proposed
                        turned = True
                elif state == "over" and event.key == pygame.K_c:
                    state = "menu"

        if state == "playing" and running:
            elapsed += dt
            if elapsed >= 1000 / DIFFICULTIES[difficulty]:
                elapsed = 0
                snake, food, ate, collided = move_snake(snake, direction, food)
                turned = False
                if ate:
                    score += 1
                if collided or food is None:
                    state = "over"

        screen.fill(BLUE)
        if state == "menu":
            text("Snake Game", 65, YELLOW, large=True)
            text("1: Easy    2: Normal    3: Hard", 140)
            text("Selected: " + difficulty, 185, YELLOW)
            text("Enter: Start", 240)
            text("Arrows: Move    Space: Pause", 290)
            text("Esc: Menu    Q: Quit", 335)
        else:
            if food is not None:
                pygame.draw.circle(screen, RED, (food[0] + 10, food[1] + 10), 10)
            for i, (x, y) in enumerate(snake):
                pygame.draw.rect(screen, DARK_GREEN if i == len(snake) - 1 else GREEN,
                                 (x, y, SNAKE_BLOCK, SNAKE_BLOCK))
            image = font.render(f"Score: {score}   {difficulty}", True, YELLOW)
            screen.blit(image, (10, 10))
            if state == "paused":
                text("Paused - Space to continue", 190, YELLOW)
            elif state == "over":
                text("You Win!" if food is None else "Game Over", 175, YELLOW, large=True)
                text("C: Menu / Play again    Q: Quit", 225)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
