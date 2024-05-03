from Interface import print_board
from GameMode import play_player_vs_player, play_player_vs_ai, play_ai_vs_ai, play_ai_vs_ai_stats
from UtilsAiMoves import get_valid_difficulty

# ------------------------------------------------------------
# Main function 
# ------------------------------------------------------------
def play_connect_four():
    """
    Main function to play Connect Four.
    """
    fin = True  # Boolean flag to control the game loop

    # Initialize game parameters
    rows = 6
    cols = 7
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    player = 'R'

    print("Bienvenue dans Puissance 4 !")  # Print welcome message
    while fin:  # Main game loop
        try:
            while True:
                try:
                    # Prompt the user to choose the game mode
                    game_mode = int(input(
                        "\nChoisissez le mode de jeu\n1: Joueur vs Joueur\n2: Joueur vs IA\n3: IA vs IA\n4: Stats\n5: Quittez\n"))
                    break
                except ValueError:
                    print("Veuillez entrer un nombre valide.")  # Handle invalid input

            if game_mode == 1:
                # Player vs Player mode
                print_board(grid)  # Display the initial game board
                play_player_vs_player(grid, player, cols)  # Call function to play PvP
                grid = [[' ' for _ in range(cols)] for _ in range(rows)]  # Reset the game grid
            elif game_mode == 2:
                # Player vs AI mode
                print_board(grid)  # Display the initial game board
                difficulty = get_valid_difficulty(
                    "Choisissez le niveau de difficulté pour l'IA (easy, medium, hard) : ")
                play_player_vs_ai(grid, player, difficulty, cols)  # Call function to play PvAI
                grid = [[' ' for _ in range(cols)] for _ in range(rows)]  # Reset the game grid
            elif game_mode == 3:
                # AI vs AI mode
                difficulty_r = get_valid_difficulty(
                    "Choisissez le niveau de difficulté pour l'IA du joueur Rouge (easy, medium, hard) : ")
                difficulty_j = get_valid_difficulty(
                    "Choisissez le niveau de difficulté pour l'IA du joueur Jaune (easy, medium, hard) : ")
                play_ai_vs_ai(grid, player, difficulty_r, difficulty_j, cols)  # Call function to play AiVAi
                grid = [[' ' for _ in range(cols)] for _ in range(rows)]  # Reset the game grid
            elif game_mode == 4:
                # Stats mode
                difficulty1 = get_valid_difficulty(
                    "Choisissez le niveau de difficulté pour le premier IA (easy, medium, hard) : ")
                difficulty2 = get_valid_difficulty(
                    "Choisissez le niveau de difficulté pour le deuxième IA (easy, medium, hard) : ")
                while True:
                    try:
                        iterations = int(input("Entrez le nombre d'itérations à exécuter : "))
                        break  # Exit loop if input is valid
                    except ValueError:
                        print("Veuillez entrer un nombre valide pour les itérations.")
                play_ai_vs_ai_stats(difficulty1, difficulty2, iterations)
            elif game_mode == 5:
                # Exit the game
                fin = False  # Set the flag to exit the game loop
            else:
                print("Mode de jeu invalide.")  # Handle invalid game mode

        except Exception as e:
            print(f"Une erreur inattendue est survenue : {e}")

    print("Fin du jeu.")  # Print end of game message

if __name__ == "__main__":
    play_connect_four()