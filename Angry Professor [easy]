# Enter your code here. Read input from STDIN. Print output to STDOUT
TestsCases <- read.table(file = "stdin", header = F, fill = T, sep = " ")
#TestsCases[1,1] is the number of test cases

nextRow <- 1
for(i in 1:TestsCases[1,1]){
    nextRow <- nextRow + 1;
    testBase <- TestsCases[nextRow,];
    nextRow <- nextRow + 1;
    thisTest <- TestsCases[nextRow,];
    thisTest <- as.vector(thisTest, mode = "numeric");
    numSummary <- summary(thisTest <= 0); #number negative or zero
    #Must be of type numeric or else will not compare properly
    if(as.numeric(numSummary["TRUE"]) >= testBase[1,2]){ #if the number on time is greater than the minimum number required
        cat("NO\n") #don't cancel
    }
    else{ # cancel
        cat("YES\n")
    }
}
