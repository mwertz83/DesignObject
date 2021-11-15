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

    def PrintValues(self, depth):
        print("Depth:%d Name:%s LocX:%d LocY:%d Hi:%d Wid:%d Area:%s SubDesignsCount:%d" % (depth, self.Name, self.LocationX, self.LocationY, self.Height, self.Width, self.Area, self.SubDesignCount))
        if self.SubDesignCount and depth != 0:
            for SubDesign in self.SubDesigns:
                SubDesign.PrintSubDesign("", depth if depth < 0 else depth-1)
        print()

    def PrintSubDesign(self, _offset, depth):
        offset = "-" + _offset
        print(offset + "Depth:%s Name:%s LocX:%d LocY:%d Hi:%d Wid:%d Area:%d SubDesignsCount:%d" % (depth, self.Name, self.LocationX, self.LocationY, self.Height, self.Width, self.Area, self.SubDesignCount))
        if self.SubDesignCount and depth != 0:
            for SubDesign in self.SubDesigns:
                SubDesign.PrintSubDesign(offset, depth if depth < 0 else depth-1)
        
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

    def ReturnOneLevel(self):
        self.PrintValues(1)