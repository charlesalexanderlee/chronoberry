import os
import sys
import json

class Settings:
    SETTINGS_FILE = 'settings.json'

    def __init__(self):
        self.load_settings()

    # Compares the last JSON file modified time with the current JSON file modified time
    # If the last modified time is different, the settings are updated
    def update_settings(self):
        if self.last_update != os.stat(self.SETTINGS_FILE).st_mtime:
            self.load_settings()

    def load_settings(self):
        with open(self.SETTINGS_FILE) as json_settings:
            settings = json.load(json_settings)
            self.last_update = os.fstat(json_settings.fileno()).st_mtime

            # Device
            self.room = settings['device']['room']
            self.teacher = settings['device']['teacher']

            # Window
            self.full_screen = settings['window']['full_screen']
            self.window_title = settings['window']['window_title']
            self.update_ms = settings['window']['update_ms']

            # Background
            self.background_color = settings['background']['color']

            # Time
            self.time_font = settings['time']['font']
            self.time_size = settings['time']['size']
            self.time_weight = settings['time']['weight'] 
            self.time_slant = settings['time']['slant']
            self.time_color = settings['time']['color']    
            self.time_format = settings['time']['format']

            # Date
            self.date_font = settings['date']['font']
            self.date_size = settings['date']['size']
            self.date_weight = settings['date']['weight']
            self.date_slant = settings['date']['slant']
            self.date_color = settings['date']['color']
            self.date_format = settings['date']['format']
