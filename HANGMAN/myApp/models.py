from django.db import models
from django.contrib.auth.models import User

class HangmanGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    word = models.CharField(max_length=100)
    guessed_letters = models.JSONField(default=list)
    wrong_guesses = models.IntegerField(default=0)
    max_attempts = models.IntegerField(default=6)
    is_game_over = models.BooleanField(default=False)
    is_won = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
