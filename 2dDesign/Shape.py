class Shape:
    SubDesignCount = 0
    SubDesigns=[]

    def __init__(self, _LocationX, _LocationY, _Height, _Width) -> None:
        self.LocationX = _LocationX
        self.LocationY = _LocationY
        self.Height = _Height
        self.Width = _Width

    def PrintValues(self):
        print("LocX:%d LocY:%d Hi:%d Wid:%d SubDesignsCount:%d" % (self.LocationX, self.LocationY, self.Height, self.Width, self.SubDesignCount))
        if self.SubDesignCount > 0:
            for SubDesign in self.SubDesigns:
                SubDesign.PrintValues()
        
    def AddSubDesign(self, SubDesign):
        assert type(SubDesign) == Shape
        self.SubDesignCount += 1
        self.SubDesigns.append(SubDesign)
        if self.Height < SubDesign.Height + SubDesign.LocationY:
            self.Height = SubDesign.Height + SubDesign.LocationY
        if self.Width < SubDesign.Width + SubDesign.LocationX:
            self.Height = SubDesign.Width + SubDesign.LocationX


