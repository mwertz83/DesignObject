class Shape:
    SubDesignCount = 0
    SubDesigns=[]

    def __init__(self, _LocationX, _LocationY, _Length, _Width) -> None:
        self.LocationX = _LocationX
        self.LocationY = _LocationY
        self.Length = _Length
        self.Width = _Width

    def PrintValues(self):
        print("LocX:%d LocY:%d Len:%d Wid:%d SubDesignsCount:%d" % (self.LocationX, self.LocationY, self.Length, self.Width, self.SubDesignCount))
        if self.SubDesignCount > 0:
            for SubDesign in self.SubDesigns:
                SubDesign.PrintValues()
        