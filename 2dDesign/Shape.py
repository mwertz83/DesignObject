class Shape:

    def __init__(self, _LocationX, _LocationY, _Height, _Width, _Name) -> None:
        self.LocationX = _LocationX
        self.LocationY = _LocationY
        self.Height = _Height
        self.Width = _Width
        self.Name = _Name
        self.SubDesignCount = 0
        self.SubDesigns = []
        self.Name = _Name
        self.Area = self.Width * self.Height

    def PrintValues(self):
        print("Name:%s LocX:%d LocY:%d Hi:%d Wid:%d SubDesignsCount:%d" % (self.Name, self.LocationX, self.LocationY, self.Height, self.Width, self.SubDesignCount))
        if self.SubDesignCount > 0:
            for SubDesign in self.SubDesigns:
                SubDesign.PrintSubDesign("")
        print()

    def PrintSubDesign(self, _offset):
        offset = "-" + _offset
        print(offset + "Name:%s LocX:%d LocY:%d Hi:%d Wid:%d SubDesignsCount:%d" % (self.Name, self.LocationX, self.LocationY, self.Height, self.Width, self.SubDesignCount))
        if self.SubDesignCount > 0:
            for SubDesign in self.SubDesigns:
                SubDesign.PrintSubDesign(offset)
        
    def AddSubDesign(self, SubDesign):
        assert type(SubDesign) == Shape
        self.SubDesignCount += 1
        self.SubDesigns.append(SubDesign)
        if self.Height < SubDesign.Height + SubDesign.LocationX:
            self.Height = SubDesign.Height + SubDesign.LocationX
        if self.Width < SubDesign.Width + SubDesign.LocationY:
            self.Width = SubDesign.Width + SubDesign.LocationY
        self.Area = self.Width * self.Height

    def SortArea(self):
        self.SubDesigns.sort(key=lambda Shape: Shape.Area)