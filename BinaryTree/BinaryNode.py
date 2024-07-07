class BinaryNode :
    def __init__(self, Data: int) -> None :
        self.Left: BinaryNode | None = None
        self.Right: BinaryNode | None = None
        self.Data: int = Data

    # >>>>>>>>>>>>>>>>>>>> CRUD operations starts<<<<<<<<<<<<<<<<<<<<
    # CREATE operation.......
    def InsertData(self, NewData: int) -> None :
        if self.Data > NewData :  # store to left if given data is smaller the present data
            if self.Left is None :
                self.Left = BinaryNode(NewData)
            else :
                self.Left.InsertData(NewData)
        else :
            if self.Right is None :
                self.Right = BinaryNode(NewData)
            else :
                self.Right.InsertData(NewData)

    # READ operation.........
    def DisplayData(self) -> None :
        print(self.Data)
    
    # UPDATE operation.........
    def UpdateData(self, NewData: int) -> None :
        self.Data = NewData


    # DELETE operation..........
    def DeleteData(self, NewData: int) -> None :
        pass

    # >>>>>>>>>>>>>>>>>>>> CRUD operations ends<<<<<<<<<<<<<<<<<<<<
    
    # to get the data... 
    def GetData(self) -> int :
        return self.Data
    
    # @RETURN BinaryNode | None
    def GetLeftNode(self) :
        return self.Left
    
    # @RETURN BinaryNode | None
    def GetRightNode(self) :
        return self.Right