# Autor: Jonathan Hernández
# Fecha: 7 Noviembre 2024
# Descripción: Código game-dino.
# GitHub: https://github.com/Jona163
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")

game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)
