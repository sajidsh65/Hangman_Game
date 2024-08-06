from django.contrib import admin
from .models import HangmanGame

@admin.register(HangmanGame)
class HangmanGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'wrong_guesses', 'is_game_over', 'is_won', 'created_at')
