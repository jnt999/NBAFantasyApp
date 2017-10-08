class Player:
    #Creates a new player with the parameters set to the correct
    #values
    def __init__(self,firstname,lastname,pt,rb,ass):
        self._firstname = firstname #Players first name
        self._lastname = lastname #Players last name
        self._pt = pt #Points per game
        self._rb = rb #Rebounds per game
        self._ass = ass #Assists per game

    #Return the first name
    @property
    def firstname(self):
        return self._firstname

    #Return the last name
    @property
    def lastname(self):
        return self._lastname

    #Return the points per game
    @property
    def pt(self):
        return self._pt

    #Return the rebounds per game
    @property
    def rb(self):
        return self._rb

    #Return the assists
    @property
    def ass(self):
        return self._ass

    #Sets the first name
    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    #Sets the last name
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    #Sets the points per game
    @pt.setter
    def pt(self, pt):
        self._pt = pt

    #Sets the rebounds
    @rb.setter
    def rb(self, rb):
        self._rb = rb

    #Sets the assists
    @ass.setter
    def ass(self, ass):
        self._ass = ass