class SingleLinkedNode {
    NextNode: SingleLinkedNode | null;
    Data: number;
    constructor(Data: number) {
        this.Data = Data;
    }
}


class SingleLinkedNodeConnector {
    private RootNode: SingleLinkedNode | null;

    private InsertDataHelper(Data: number, Node: SingleLinkedNode): void {
        if (!Node.NextNode) {
            Node.NextNode = new SingleLinkedNode(Data);
            return;
        }
        this.InsertDataHelper(Data, Node.NextNode);
    }

    // Create Operation....
    InsertData(Data: number): void {
        if (this.RootNode) {
            this.InsertDataHelper(Data, this.RootNode);
        }
        else {
            this.RootNode = new SingleLinkedNode(Data);
        }
    }

    private ReadAllDataHelper(Output: Array<number>, Node: SingleLinkedNode | null): void {
        if (Node) {
            Output.push(Node.Data);
            this.ReadAllDataHelper(Output, Node.NextNode);
        }
    }
    // Read Operation....
    ReadAllData(): Array<number> {
        var Output: Array<number> = [];

        if (this.RootNode) {
            this.ReadAllDataHelper(Output, this.RootNode);
        }
        return Output;
    }

    private UpdateAllDataHelper(OldData: number, NewData: number, Node: SingleLinkedNode | null): void {
        if (Node) {
            if (Node.Data === OldData) {
                Node.Data = NewData;
            }
            this.UpdateAllDataHelper(OldData, NewData, Node.NextNode);
        }
    }

    // Update Operation.....
    UpdateAllData(OldData: number, NewData: number): void {
        if (this.RootNode) {
            this.UpdateAllDataHelper(OldData, NewData, this.RootNode);
        }
    }

    private GetLengthHelper(Count: number, Node: SingleLinkedNode | null): number {
        if (Node) {
            return this.GetLengthHelper(Count + 1, Node.NextNode);
        }
        return Count + 1;
    }

    GetLength(): number {
        var Count = 0

        if (this.RootNode) {
            Count = this.GetLengthHelper(Count, this.RootNode);
        }

        return Count;
    }

    private DeleteNodeHelper(Data: number, Node: SingleLinkedNode | null): SingleLinkedNode | null {
        if (! Node) {
            return Node;
        }

        if (Node.Data === Data) {
            return Node.NextNode;
        }

        Node.NextNode = this.DeleteNodeHelper(Data, Node.NextNode);
        return Node;
    }

    // Delete Operation...
    DeleteNode(Data: number): void {
        this.RootNode = this.DeleteNodeHelper(Data, this.RootNode);
    }
}

var SingleConnector = new SingleLinkedNodeConnector();
SingleConnector.InsertData(10);
SingleConnector.InsertData(20);
SingleConnector.InsertData(30);
SingleConnector.InsertData(40);
SingleConnector.InsertData(50);

console.log("Data:- ", SingleConnector.ReadAllData());
SingleConnector.UpdateAllData(10, 50);
console.log("Data:- ", SingleConnector.ReadAllData());
SingleConnector.DeleteNode(30);
console.log("Data:- ", SingleConnector.ReadAllData());

