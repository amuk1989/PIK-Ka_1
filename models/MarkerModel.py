class marker_model(object):
    #region private variables
    __x: float
    __y: float
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
    #endregion

    #region Methods
    def __init__(self):
        self.__x = None
        self.__y = None
    #endregion