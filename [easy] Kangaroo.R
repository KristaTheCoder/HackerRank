# Enter your code here. Read input from STDIN. Print output to STDOUT
# y1 = ax + b; y2 = cx + d
#we want y1 to equal y2 so find x such that
#ax - cx = d - b >>> (d-b)/(a-c) = x

kangaroos <- read.table(file = "stdin", header = F, sep = " ", fill = T)
#check structure of kangaroos dataframe for variable names 
#str(kangaroos)
a <- kangaroos$V2
b <- kangaroos$V1
c <- kangaroos$V4
d <- kangaroos$V3
y <- (a - c)
z <- (d - b)

#this code was giving me problems with having nested if statements... i'm not sure if nested if statements work in R
if(y == 0){
    cat("NO")
}else if( (z/y >= 0) && ((z/y)%%1 ==0)){
    cat("YES")
}else{
    cat("NO")
}
