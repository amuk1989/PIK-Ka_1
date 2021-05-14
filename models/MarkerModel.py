class marker_model(object):
    #region private variables
    __marker_index: int
    #endregion

    #region properties
    def get_marker_index(self):
        return self.__marker_index

    def set_marker_index(self, value):
        self.__marker_index = value

    marker_index = property(get_marker_index,set_marker_index, doc='marker index')
    #endregion

    #region Methods
    def __init__(self):
        self.__marker_index = None
    #endregion