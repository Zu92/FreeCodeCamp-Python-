class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.name="Rectangle"  
    def set_width(self,width):
        self.width=width
        return self.width
    def set_height(self,height):
        self.height=height
        return self.height
    def get_area(self):
        self.area=self.height*self.width
        return(self.area)
    def get_perimeter(self):
        self.perimeter=2*self.height+ 2*self.width
        return self.perimeter
    def get_diagonal(self):
        self.diagonal=(self.height**2+ self.width**2)**0.5
        return self.diagonal
    def get_picture(self):
        if self.width>50 or self.height>50:
            return ("Too big for picture.")
        else:
            firstline="*"*self.width+"\n"
            line=""
            for i in range(0,self.height-2):
                line+="*"*(self.width)+"\n"
            
            return(firstline+line+firstline)
    def get_amount_inside(self,figure):
        import math
        vertical=math.trunc(self.width/figure.width)
        horizontal=math.trunc(self.height/figure.height)
        
        return vertical*horizontal


            
    def __repr__(self):
        return (self.name+"(width="+str(self.width)+", height="+str(self.height)+")")

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.name="Square"
        
    def set_side(self,side):
        self.width=side
        self.height=side
        return self.width
    def __repr__(self):
        return (self.name+"(side="+str(self.width)+")")

