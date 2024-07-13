class SingleLinkedNode :
    def __init__(self, Data: int) :
        self.Data: int = Data
        self.NextNode: SingleLinkedNode | None = None

    # >>>>>>>>>>>>>>> CRUD Operations  <<<<<<<<<<<<<<<<

    # create operation....
    def InsertDataToEnd(self, NewData) -> None:
        if self.NextNode is None :
            self.NextNode = SingleLinkedNode(NewData)
        else :
            self.NextNode.InsertDataToEnd(NewData)
        
    # Create Operation.....
    def InsertDataToAfterNode(self, OldData, NewData) :
        NextNode: SingleLinkedNode | None = self.GetNextNode()
        
        if self.Data == OldData :
            NewNode: SingleLinkedNode = SingleLinkedNode(NewData)
            NewNode.UpdateNextNode(self.GetNextNode())
            self.UpdateNextNode(NewNode)
        
        if not (NextNode is None) :
            NextNode.InsertDataToAfterNode(OldData, NewData)

    # Read Operation....
    def DisplayData(self) -> None :
        print(self.Data)

    # Read Operation....
    def DisplayAllData(self) -> None :
        self.DisplayData()
        if self.NextNode is not None :
            self.NextNode.DisplayAllData()
    
    # Read Operation....
    def GetData(self) -> int:
        return self.Data
    
    # Read Operation...
    def GetAllData(self) -> list :
        result = [self.GetData()]
        if self.NextNode is None :
            return result
        result.extend(self.NextNode.GetAllData())
        return result
    
    # Read Operation....
    def GetNextNode(self):
        return self.NextNode
    
    # Read Operation....
    def GetLength(self) :
        if self.NextNode is None :
            return 1
        return 1 + self.NextNode.GetLength()
    
    # Read Operation.....
    def GetDataByIndex(self, Index: int, CurrentIndex: int = 0) :
        if Index == CurrentIndex :
            return self.GetData()
        if self.NextNode is not None :
            return self.NextNode.GetDataByIndex(Index, CurrentIndex + 1)

    # Read Operation....  
    def GetIndexByData(self, Data: int, CurrentIndex: int = 0) :
        if self.Data == Data :
            return CurrentIndex
        if self.NextNode is not None :
            return self.NextNode.GetIndexByData(Data, CurrentIndex + 1)
 
    # Update Operation.....
    def UpdateData(self, NewData: int) -> None:
        self.Data = NewData        


    # Update Operation......
    def UpdateNextNode(self, NewNextNode) -> None :
        self.NextNode = NewNextNode

    # Update Operation....
    def UpdateAllData(self, OldData: int, NewData: int) -> None :
        if self.Data == OldData :
            self.UpdateData(NewData)
        if self.NextNode is not None :
            self.NextNode.UpdateAllData(OldData, NewData)

    # Update Operation....
    def UpdateDataByIndex(self, NewData: int, Index: int, CurrentIndex: int = 0) -> None :
        if Index == CurrentIndex :
            self.UpdateData(NewData)
            return
        if self.NextNode is not None :
            self.NextNode.UpdateDataByIndex(NewData, Index, CurrentIndex + 1)