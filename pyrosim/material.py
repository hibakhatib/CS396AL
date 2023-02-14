from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, colorName):
        

        self.depth  = 3
        
        if colorName == "green":
            self.string1 = '<material name="green">'
            self.string2 = '    <color rgba="0 1 0 1"/>'
        else:
            self.string1 = '<material name="blue">'
            self.string2 = '    <color rgba="0 0 1 1"/>'
            

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
