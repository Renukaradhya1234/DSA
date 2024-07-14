from .SingleLinkedList import SingleLinkedNode


class SingleLinkedListConnector :
    def __init__(self, Data) -> None:
        self.RootNode = SingleLinkedNode(Data)

    # >>>>>>>>>>>>>>>> CRUD Operations <<<<<<<<<<<<<<<<<<<<
    
    # Create Operation.........
    def InsertDataToEnd(self, NewData: int) -> None :
        if self.RootNode is not None :
            self.RootNode.InsertDataToEnd(NewData)

    # Create Operation.........
    def InsertDataToBegin(self, NewData: int) -> None :
        NewNode: SingleLinkedNode = SingleLinkedNode(NewData)
        NewNode.UpdateNextNode(self.RootNode)

        self.RootNode = NewNode
    
    # Create Operation......
    def InsertDataToPrevNode(self, OldData: int, NewData: int, Node: SingleLinkedNode | None, PrevNode: SingleLinkedNode | None = None) :
        # first call will be newdata, rootnode, prevnode = none
        if Node is None :
            return 
        if Node.GetData() == OldData :
            NewNode: SingleLinkedNode = SingleLinkedNode(NewData)
            if  PrevNode is None:
                # prevnode is none means, current node must be root node.....
                NewNode.UpdateNextNode(Node)
                self.RootNode = NewNode
            else :
                # prevnode -> nextnode
                # prevnode -> newnode -> nextnode
                NewNode.UpdateNextNode(PrevNode.GetNextNode())
                PrevNode.UpdateNextNode(NewNode)
        self.InsertDataToPrevNode(OldData, NewData, Node.GetNextNode(), Node)

    # Create Operation....
    def InsertDataToNextNode(self, OldData: int, NewData: int) :
        if self.RootNode is not None :
            self.RootNode.InsertDataToAfterNode(OldData, NewData)

    # Read Operation.......
    def DisplayAllData(self) -> None:
        if self.RootNode is not None :
            self.RootNode.DisplayAllData()

    # Read Operation....
    def GetAllData(self) :
        if self.RootNode is not None :
            return self.RootNode.GetAllData()
    
    # Read Operation....
    def GetLength(self) -> int:
        if self.RootNode is not None :
            return self.RootNode.GetLength()
    
    # Read Operation....
    def GetDataByIndex(self, Index: int) :
        if self.RootNode is not None :
            return self.RootNode.GetDataByIndex(Index)
    
    # Read Operation....
    def GetIndexByData(self, Data: int) :
        if self.RootNode is not None :
            return self.RootNode.GetIndexByData(Data) 
    
    # Update Operation.....
    def UpdateAllData(self, OldData: int, NewData: int) -> None :
        if self.RootNode is not None :
            self.RootNode.UpdateAllData(OldData, NewData)

    # Update Operation....
    def UpdateDataByIndex(self, NewData, Index) -> None:
        if self.RootNode is not None :
            self.RootNode.UpdateDataByIndex(NewData, Index)
    
    # Delete Operation....
    def DeleteNode(self, Value, Node: SingleLinkedNode | None, PrevNode: SingleLinkedNode | None = None) -> None :
        if Node is None :
            return
        if Node.Data == Value :
            if PrevNode is None :
                # if prev node is none it must be root node, or starter....
                self.RootNode = self.RootNode.GetNextNode()
                return
            PrevNode.UpdateNextNode(Node.GetNextNode())
        self.DeleteNode(Value, Node.GetNextNode(), Node)

    # Delete Operation.....
    def DeleteNodeByIndex(self, Index, Node: SingleLinkedNode | None, PrevNode: SingleLinkedNode | None = None, CurrentIndex: int = 0) :
        if Node is None :
            return
        if Index == CurrentIndex :
            if PrevNode is None :
                # if prev node is none it must be root node, or starter....
                self.RootNode = self.RootNode.GetNextNode()
                return
            PrevNode.UpdateNextNode(Node.GetNextNode())
            return
        self.DeleteNodeByIndex(Index, Node.GetNextNode(), Node, CurrentIndex + 1)

    # Delete Operation....
    def DeleteFirstNode(self) :
        if self.RootNode is not None :
            self.RootNode = self.RootNode.NextNode

    def DeleteLastNode(self) :
        if self.RootNode is not None :
            if self.RootNode.NextNode is None :
                self.RootNode = None
            else :
                self.RootNode.DeleteLastNode()
        