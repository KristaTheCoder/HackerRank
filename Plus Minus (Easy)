# Enter your code here. Read input from STDIN. Print output to STDOUT
data <- read.table(file = "stdin", fill = T, header = F, sep = " ")

pos = 0
neg = 0
zer = 0

#counting in the dataframe
for (i in 1:ncol(data)){
    if(data[2, i] > 0){
        pos = pos + 1;
    }
    else if(data[2, i] == 0){
        zer = zer + 1;
    }
    else{
        neg = neg + 1;
    }
  };

    #output
    cat(pos/data[1,1])
    cat("\n")
   cat(neg/data[1,1])
    cat("\n")
    
   cat(zer/data[1,1])
      
