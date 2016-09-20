# Enter your code here. Read input from STDIN. Print output to STDOUT
num <- read.table( file = "stdin", sep = " ", header = F)
x<- as.numeric(num[1,1])
space <- ' '
hashtag <- '#'
upCount = 1
i = 1
while(x >0){ #must use while loop because a for loop will cause there to be an extra space on every line -- very difficult to fix that condition via forloop
    while(i < x){
        #print spaces
        cat(space)
        i = i+1;
    }  
    i = 1;
    for(i in 1:upCount){
        #print hashtags
        cat('#');
    }
    if(x > 1){
    cat('\n');
        }
    x = x -1;
    upCount = upCount + 1;
    i = 1;
}
