from .DoubleLinkedListNode import DoubleLinkedNode

class DoubleLinkedNodeConnector :
    def __init__(self, Data: int) :
        self.RootNode: DoubleLinkedNode = DoubleLinkedNode(Data)

    def InsertDataToEnd(self, Data: int )-> None:
        self.RootNode.InsertNodeToEnd(Data)

    # Create Operation.........
    def InsertDataToBegin(self, NewData: int) -> None :
        NewNode: DoubleLinkedNode = DoubleLinkedNode(NewData)
        NewNode.NextNode = self.RootNode

        self.RootNode.PrevNode = NewNode
        
        self.RootNode = NewNode

    def InsertDataToPrevNode(self, OldData: int, NewData: int, Node: DoubleLinkedNode | None) :
        if Node is None :
            return
        
        if Node.Data == OldData :
            NewNode: DoubleLinkedNode = DoubleLinkedNode(NewData)

            if Node.PrevNode is None :
                # it must be the starter node ....
                NewNode.NextNode = Node
                Node.PrevNode = NewNode

                self.RootNode = NewNode
            else :
                NewNode.NextNode = Node
                NewNode.PrevNode = Node.PrevNode

                Node.PrevNode = NewNode
                NewNode.PrevNode.NextNode = NewNode
        self.InsertDataToPrevNode(OldData, NewData, Node.NextNode)

    def InsertDataToNextNode(self, OldData: int , NewData: int) :
        self.RootNode.InsertDataAfterNode(OldData, NewData)

    def DisplayAllData(self) :
        self.RootNode.DisplayAllData()

    # Read Operation....
    def GetAllData(self) :
        return self.RootNode.GetAllData()
    
    # Read Operation....
    def GetLength(self) -> int:
        return self.RootNode.GetLength()
    
    # Read Operation....
    def GetDataByIndex(self, Index: int) :
        return self.RootNode.GetDataByIndex(Index)

    # Read Operation....
    def GetIndexByData(self, Data: int) :
        return self.RootNode.GetIndexByData(Data)

    # Update Operation.....
    def UpdateAllData(self, OldData: int, NewData: int) -> None :
        self.RootNode.UpdateAllData(OldData, NewData)

    # Update Operation....
    def UpdateDataByIndex(self, NewData, Index) -> None:
        self.RootNode.UpdateDataByIndex(NewData, Index)

    # Delete Operation.....
    def DeleteNode(self, Data: int  , Node: DoubleLinkedNode | None) :
        if Node is None :
            return
        
        if Node.Data == Data :
            if Node.PrevNode is None :
                # Node must be starter....
                self.RootNode = self.RootNode.NextNode
                if self.RootNode is not None :
                    self.RootNode.PrevNode = None
            else :
                Node.PrevNode.NextNode = Node.NextNode
                if Node.NextNode is not None :
                    Node.NextNode.PrevNode = Node.PrevNode
        self.DeleteNode(Data, Node.NextNode)

    # Delete Operation...
    def DeleteNodeByIndex(self, Index, Node: DoubleLinkedNode | None, CurrentIndex: int = 0) :
        if Node is None :
            return
        
        if Index == CurrentIndex :
            if Node.PrevNode is None :
                # Node must be starter....
                self.RootNode = self.RootNode.NextNode
                if self.RootNode is not None :
                    self.RootNode.PrevNode = None
                return
            Node.PrevNode.NextNode = Node.NextNode
            if Node.NextNode is not None :
                Node.NextNode.PrevNode = Node.PrevNode
            return
        
        self.DeleteNodeByIndex(Index, Node.NextNode, CurrentIndex + 1)
