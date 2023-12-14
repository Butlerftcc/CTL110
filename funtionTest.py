def Main():
    Length = float(input('Enter length: '))
    Width = float(input('Enter width: '))

    def CalcArea(length, width):
        return(length * width)
    
    print(CalcArea(Length, Width))
    
Main()
