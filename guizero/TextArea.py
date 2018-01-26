from tkinter import Text, StringVar, END
from .mixins import WidgetMixin
from .tkmixins import ScheduleMixin, DestroyMixin, EnableMixin, FocusMixin, DisplayMixin, ReprMixin
from . import utilities as utils

class TextArea(
    WidgetMixin,
    ScheduleMixin,
    DestroyMixin,
    EnableMixin,
    FocusMixin,
    DisplayMixin,
    ReprMixin):

    def __init__(self, master, text="", width=10, grid=None, align=None, colour=None, bgcolour=None):

        self._master = master
        self._text = text
        self._grid = grid
        self._align = align
        self._visible = True
        self._colour = colour
        self._bgcolour = bgcolour

        # Description of this object (for friendly error messages)
        self.description = "[TextArea] object with text \"" + str(text) + "\""

        # Create a tk Label object within this object
        self.tk = Text(master.tk, width=width, foreground=self._colour, background=self._bgcolour)

        # Add the specified text
        self.tk.insert(END, self._text)

        # Pack or grid depending on parent
        utils.auto_pack(self, master, grid, align)


    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        return self._text

    @value.setter
    def value(self, value):
        self._text = value
        self.tk.delete(1.0, END)
        self.tk.insert(END, self._text)

        self.description = "[TextArea] object with text \"" + str(value) + "\""

    # Colour of the text
    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour
        self.tk.config(foreground=self._colour)

    # Background colour
    @property
    def bgcolour(self):
        return self._bgcolour

    @bgcolour.setter
    def bgcolour(self, bgcolour):
        self._bgcolour = bgcolour
        self.tk.config(background=self._bgcolour)


    # METHODS
    # -------------------------------------------
    # Clear text box
    def clear(self):
        self.tk.delete(0, END)

    # Append text
    def append(self, text):
        self.value = self.value + str(text)
        self.description = "[TextArea] object with text \"" + self.value + "\""


    # DEPRECATED METHODS
    # --------------------------------------------
    # Returns the text
    def get(self):
        return self._text.get()
        utils.deprecated("TextBox get() is deprecated. Please use the value property instead.")

    # Sets the text
    def set(self, text):
        self._text.set( str(text) )
        self.description = "[TextArea] object with text \"" + str(text) + "\""
        utils.deprecated("TextBox set() is deprecated. Please use the value property instead.")
