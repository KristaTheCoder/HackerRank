# Enter your code here. Read input from STDIN. Print output to STDOUT
pairs <- read.table(file = "stdin", sep = " ", header = F, fill = T)

number = 0
i = 1
for(i in 1:pairs[1,1]){
    numVal = pairs[1,1]
    while(numVal > i){
        tempSum = pairs[2,i] + pairs[2, numVal]
        if(tempSum%%pairs[1,2] == 0){
            number = number + 1;
        } 
        numVal = numVal - 1;
    }
}
cat(number)
