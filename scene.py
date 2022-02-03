import pygame

class Scene():
    """Abstract class"""
    def __init__(self):
        pass

    def update(self):
        "Called from the main loop and defined on the subclass."
 
        raise NotImplementedError("update abstract method must be defined in subclass.")
 
    def trigger_event(self, event):
        "Called when a specific event is detected in the loop."
 
        raise NotImplementedError("trigger_event abstract method must be defined in subclass.")
 
    def render(self, screen):
        "Called when something needs to be drawn within the scene"
 
        raise NotImplementedError("render abstract method must be defined in subclass.")