class Theme:
    textarea_bg: str
    textarea_fg: str
    menubar_bg: str
    menubar_fg: str

    def get_background(self):
        raise self.textarea_bg

    def get_color(self):
        raise self.textarea_fg