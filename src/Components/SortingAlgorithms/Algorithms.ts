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

    InserationSort(InputArray: Array<number>): void {
        /*
            Take the value, and compare with backwards, if it is small place it correct place...
            We will starts with Second Index by considering first Index is already sorted....
        */
        
        for(var Index: number = 1; Index < InputArray.length; Index ++) {
            for(var SubIndex: number = Index - 1; SubIndex >= 0; SubIndex --) {
                if (InputArray[Index] >= InputArray[SubIndex] ) {
                    break;
                }
                [InputArray[Index], InputArray[SubIndex]] = [InputArray[SubIndex], InputArray[Index]];
            }
        }
    }

    private MergeArray(LeftInputArray: Array<number>, RightInputArray: Array<number>): Array<number> {
        let Result: Array<number> = [];
        let LeftIndex: number = 0;
        let RightIndex: number = 0;

        /*
            Merget by comparing the left and right array.
            if left array value is lessthan right array value then add value of left then increment only left index
            else add right value to array then increment only right index...
        */
        while (LeftIndex < LeftInputArray.length && RightIndex < RightInputArray.length) {
            if (LeftInputArray[LeftIndex] < RightInputArray[RightIndex]) {
                Result.push(LeftInputArray[LeftIndex]);
                LeftIndex ++;
            }
            else {
                Result.push(RightInputArray[RightIndex]);
                RightIndex ++;
            }
        }

        /*
            if any value is present in left and right array add them 
            first left array then right array....
        */
       while(LeftIndex < LeftInputArray.length) {
            Result.push(LeftInputArray[LeftIndex]);
            LeftIndex ++;
       }

       while (RightIndex < RightInputArray.length) {
            Result.push(RightInputArray[RightIndex]);
            RightIndex ++;
       }

        return Result;
    }

    private DivideTheArray(InputArray: Array<number>): Array<number> {
        /*
            Divide the Array into two Parts then give to merge function to solve the sorting...
        */
        
        if (InputArray.length == 1) {
            return InputArray
        }

        let MiddleIndex: number = Math.floor(InputArray.length / 2);
        let LeftArray: Array<number> = InputArray.slice(0, MiddleIndex);
        let RightArray: Array<number> = InputArray.slice(MiddleIndex);

        return this.MergeArray(this.DivideTheArray(LeftArray), this.DivideTheArray(RightArray))
    }

    MergeSort(InputArray: Array<number>): void {
        console.log("After Sorting:- ", this.DivideTheArray(InputArray));
    }
}

var sorting = new SortingAlgorithms();
var Input = [7, 12, 9, 11, 3]
console.log("before Sorting:- ", Input);
// bubble.InserationSort(Input);
sorting.MergeSort(Input);
// console.log("After Sorting:- ", Input);