class DoubleLinkedNode :
    def __init__(self, Data: int) -> None :
        self.PrevNode: DoubleLinkedNode | None = None
        self.Data: int = Data
        self.NextNode: DoubleLinkedNode | None = None
    
    # >>>>>>>>>>>>>>>>>> CRUD Operations <<<<<<<<<<<<<<<<<
    
    # Create Operation
    def InsertNodeToEnd(self, Data: int) :
        # to insert the new node to end of the list...
        NewNode: DoubleLinkedNode = DoubleLinkedNode(Data)
        if self.NextNode is None :
            self.NextNode = NewNode
            NewNode.PrevNode = self
        else :
            self.NextNode.InsertNodeToEnd(Data)

    # Create Operation....
    def InsertDataAfterNode(self, Data: int, NewData: int) :
        # to insert the node after the given data...
        NextNode: DoubleLinkedNode | None = self.NextNode
        if self.Data == Data :
            NewNode: DoubleLinkedNode = DoubleLinkedNode(NewData)
            NewNode.PrevNode = self
            NewNode.NextNode = self.NextNode
            # update the next node...
            if self.NextNode is not None :
                self.NextNode.PrevNode = NewNode
            # update the current node...
            self.NextNode = NewNode
        
        if NextNode is not None :
            NextNode.InsertDataAfterNode(Data, NewData)

    # Read Operation.....
    def DisplayAllData(self) :
        print(self.Data)
        
        if self.NextNode is not None :
            self.NextNode.DisplayAllData()

    # Read Operation....
    def GetAllData(self) -> list:
        result = [self.Data]

        if self.NextNode is None :
            return result
        
        result.extend(self.NextNode.GetAllData())
        return result

    # Read Operation....
    def GetLength(self) :
        if self.NextNode is None :
            return 1
        return 1 + self.NextNode.GetLength()
    
    # Read Operation....
    def GetDataByIndex(self, Index: int, CurrentIndex: int = 0) :
        if Index == CurrentIndex :
            return self.Data
        
        if self.NextNode is not None :
            return self.NextNode.GetDataByIndex(Index, CurrentIndex + 1)
    
    # Read Operation...
    def GetIndexByData(self, Data: int, CurrentIndex: int = 0) :
        if self.Data == Data :
            return CurrentIndex
        if self.NextNode is not None :
            return self.NextNode.GetIndexByData(Data, CurrentIndex + 1)

    # Update Operation.... 
    def UpdateAllData(self, OldData: int, NewData: int) -> None :
        if self.Data == OldData :
            self.Data = NewData
        if self.NextNode is not None :
            self.NextNode.UpdateAllData(OldData, NewData)

    # Update Operation....
    def UpdateDataByIndex(self, NewData: int, Index: int, CurrentIndex: int = 0) -> None :
        if Index == CurrentIndex :
            self.Data = NewData
            return
        if self.NextNode is not None :
            self.NextNode.UpdateDataByIndex(NewData, Index, CurrentIndex + 1)