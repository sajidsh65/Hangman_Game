from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return redirect('game_status')

# List of words to be used in the Hangman game
WORD_LIST = [
    'ABANDON', 'ACCELERATE', 'BARRIERS', 'BRILLIANT', 'CALENDAR', 'CAPTURE', 
    'CHAMPION', 'COMPUTER', 'DISCOVER', 'DYNAMITE', 'ELEVATOR', 'EXCELLENT', 
    'FANTASTIC', 'FOREST', 'GALLERY', 'HARMONIZE', 'HORIZON', 'INSTANT', 
    'JUNCTION', 'KINGDOM', 'LIBRARY', 'MARATHON', 'MYSTERY', 'NEUTRAL', 
    'OPPORTUNITY', 'PARADISE', 'PEACEFUL', 'PHANTOM', 'PLAYGROUND', 'PRISM', 
    'QUALITY', 'RESEARCH', 'REMOTE', 'SATELLITE', 'SECRETS', 'SUCCESS', 
    'SYMPHONY', 'TELESCOPE', 'TERRIFIC', 'TRANSFORM', 'UNIVERSE', 'VALIANT', 
    'VICTORY', 'VINTAGE', 'WILDLIFE', 'WONDERFUL', 'YELLOW', 'ZEBRA', 
    'ABILITY', 'ACCOUNT', 'ADVENTURE', 'ATHLETE', 'BANANA', 'CREDIBLE', 
    'DEFENSE', 'DIAMOND', 'ENERGY', 'HORIZON'
]


# Helper function to get a new game word
def get_random_word():
    return random.choice(WORD_LIST)

# View to start a new game
def new_game(request):
    # Set up a new game session
    request.session['word'] = get_random_word()
    request.session['guessed_letters'] = []
    request.session['wrong_guesses'] = 0
    request.session['max_attempts'] = 6
    request.session['is_game_over'] = False
    request.session['is_won'] = False

    return redirect('game_status')

# View to process a guessed letter
def guess_letter(request):
    if request.method == 'POST' and not request.session.get('is_game_over', False):
        guessed_letter = request.POST.get('letter', '').upper()
        word = request.session.get('word', '')
        guessed_letters = request.session.get('guessed_letters', [])

        # Ensure word is not None
        if word is None:
            return redirect('new_game')  # or handle the error as needed

        if guessed_letter and guessed_letter not in guessed_letters:
            guessed_letters.append(guessed_letter)

            if guessed_letter not in word:
                request.session['wrong_guesses'] = request.session.get('wrong_guesses', 0) + 1

            request.session['guessed_letters'] = guessed_letters

            # Check if the game is won or lost
            if all(letter in guessed_letters for letter in word):
                request.session['is_game_over'] = True
                request.session['is_won'] = True
            elif request.session['wrong_guesses'] >= request.session.get('max_attempts', 6):
                request.session['is_game_over'] = True
                request.session['is_won'] = False

    return redirect('game_status')

# View to display the current game status
def game_status(request):
    word = request.session.get('word', '')
    guessed_letters = request.session.get('guessed_letters', [])
    wrong_guesses = request.session.get('wrong_guesses', 0)
    max_attempts = request.session.get('max_attempts', 6)
    is_game_over = request.session.get('is_game_over', False)
    is_won = request.session.get('is_won', False)

    # Prepare the word display
    word_display = [letter if letter in guessed_letters else '_' for letter in word]

    context = {
        'word_display': word_display,
        'wrong_guesses': wrong_guesses,
        'max_attempts': max_attempts,
        'is_game_over': is_game_over,
        'game_message': 'You won!' if is_won else f'Game over! The word was: {word}',
    }

    return render(request, 'index.html', context)
