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
    def GetData(self) -> int:
        return self.Data
    
    # Read Operation....
    def GetNextNode(self):
        return self.NextNode
    
    # Update Operation.....
    def UpdateData(self, NewData: int) -> None:
        self.Data = NewData

    # Update Operation......
    def UpdateNextNode(self, NewNextNode) -> None :
        self.NextNode = NewNextNode