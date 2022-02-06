import pygame
from scene import Scene

class BattleScene(Scene):
    """"Contains functions that handle the battle logic. Called from main game loop."""
    def __init__(self):
        pass

    def update(self):
        raise NotImplementedError("update abstract method must be defined in subclass.")
 
    def trigger_event(self, event):
        "Called when a specific event is detected in the loop. Tracks only events relevant to this state"
 
        raise NotImplementedError("trigger_event abstract method must be defined in subclass.")
 
    def render(self, screen):
        "Called when something needs to be drawn on the scene"
 
        raise NotImplementedError("render abstract method must be defined in subclass.")