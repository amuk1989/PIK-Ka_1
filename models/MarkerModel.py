colors = [
    'b',#blue
    'g',#green
    'r',#red
    'c',#light blue
    'm',#purple
    'y',#yellow
    'k',#black
    'w',#white
]
class marker_model(object):
    #region private variables

    __x: float
    __y: float
    __color: str
    #endregion

    #region properties
    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    x = property(get_x,set_x, doc='marker x')

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

    y = property(get_y,set_y, doc='marker y')

    def get_color(self):
        return self.__color

    def set_color(self, value):
        if colors.count(value) > 0:
            self.__color = value

    color = property(get_color,set_color, doc='marker color')

    def get_legend(self):
        return f'Ч:{round(self.x, 2)}\nA:{round(self.y, 2)}'

    def set_legend(self, value):
        self.__legend = value

    legend = property(get_legend,set_legend, doc='marker color')
    #endregion

    #region Methods
    def __init__(self):
        self.__x = None
        self.__y = None
        self.__color = 'b'
        self.__legend = ''
    #endregion