class DoubleLinkedNode {
    PreviousNode: DoubleLinkedNode | null;
    Data: number;
    NextNode: DoubleLinkedNode | null;

    constructor(Data: number) {
        this.Data = Data;
    }
}

class DoubleLinkedListConnector {
    RootNode: DoubleLinkedNode | null;

    private static InsertDataHelper(NewData: number, Node: DoubleLinkedNode): void {
        if (!Node.NextNode) {
            var NewNode: DoubleLinkedNode = new DoubleLinkedNode(NewData);
            Node.NextNode = NewNode;
            NewNode.PreviousNode = Node;
            return;
        }
        DoubleLinkedListConnector.InsertDataHelper(NewData, Node.NextNode);
    }

    // Create Operation.....
    InsertData(NewData: number): void {
        if (this.RootNode) {
            DoubleLinkedListConnector.InsertDataHelper(NewData, this.RootNode);
        }
        else {
            this.RootNode = new DoubleLinkedNode(NewData);
        }
    }

    private static ReadAllDataHelper(Output: Array<number>, Node: DoubleLinkedNode | null): void {
        if (Node) {
            Output.push(Node.Data);
            DoubleLinkedListConnector.ReadAllDataHelper(Output, Node.NextNode);
        }
    }

    ReadAllData(): Array<number> {
        var Output: Array<number> = [];

        if (this.RootNode) {
            DoubleLinkedListConnector.ReadAllDataHelper(Output, this.RootNode);
        }

        return Output;
    }

    private static UpdateAllDataHelper(OldData: number, NewData: number, Node: DoubleLinkedNode | null): void {
        if (Node) {
            if (Node.Data === OldData) {
                Node.Data = NewData;
            }
            DoubleLinkedListConnector.UpdateAllDataHelper(OldData, NewData, Node.NextNode);
        }
    }

    UpdateAllData(OldData: number, NewData: number): void {
        if (this.RootNode) {
            DoubleLinkedListConnector.UpdateAllDataHelper(OldData, NewData, this.RootNode);
        }
    }

    private static DeleteDataHelper(Data: number, Node: DoubleLinkedNode | null): void {
        if (Node) {
            if (Node.Data === Data) {
                Node.PreviousNode.NextNode = Node.NextNode;
                if (Node.NextNode) {
                    Node.NextNode.PreviousNode = Node.PreviousNode;
                }
            }
            DoubleLinkedListConnector.DeleteDataHelper(Data, Node.NextNode);
        }
    }

    DeleteData(Data: number): void {
        if (this.RootNode) {
            if (this.RootNode.Data === Data) {
                this.RootNode = this.RootNode.NextNode;
            }
            DoubleLinkedListConnector.DeleteDataHelper(Data, this.RootNode);
        }
    }
}

var double = new DoubleLinkedListConnector();

double.InsertData(10);
double.InsertData(20);
double.InsertData(30);
double.InsertData(40);

console.log("Data:- ", double.ReadAllData());

double.UpdateAllData(10, 100);
double.UpdateAllData(40, 400);
double.UpdateAllData(30, 300);
double.UpdateAllData(20, 200);

console.log("Updated Data:- ", double.ReadAllData());

double.DeleteData(200);
console.log("Nodes:- ", double.ReadAllData());