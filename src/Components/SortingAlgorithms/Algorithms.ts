class SortingAlgorithms {
    BubbleSort(InputArray: Array<number>): void {
        /*
            Compare the value with next value,
            if the value is greater then the next value
            swap the values.
        */

        for (var index: number = 0; index < InputArray.length; index++) {
            for (var subIndex: number = index + 1; subIndex < InputArray.length; subIndex++) {
                if (InputArray[index] > InputArray[subIndex]) {
                    [InputArray[index], InputArray[subIndex]] = [InputArray[subIndex], InputArray[index]];
                }
            }
        }
    }

    SelectionSort(InputArray: Array<number>): void {
        /*
            first select the minimun value index for first position, then second position and so on...
        */

        for(var Index: number = 0; Index < InputArray.length; Index ++) {
            var MinIndex: number = Index;
            for(var SubIndex: number = Index; SubIndex < InputArray.length; SubIndex ++) {
                if (InputArray[Index] > InputArray[SubIndex]) {
                    MinIndex = SubIndex;
                }
            }
            if (Index != SubIndex) {
                [InputArray[Index], InputArray[MinIndex]] = [InputArray[MinIndex], InputArray[Index]]
            }
        }
    }

    
}

var bubble = new SortingAlgorithms();
var Input = [7, 12, 9, 11, 3]
console.log("before Sorting:- ", Input);
bubble.SelectionSort(Input);
console.log("After Sorting:- ", Input);