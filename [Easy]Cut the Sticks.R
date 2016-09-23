# Enter your code here. Read input from STDIN. Print output to STDOUT
sticks <- read.table(file = "stdin", header = F, fill = T, sep = " ")
sticks <- as.vector(sticks[2,], mode = "numeric") #setting the mode for vectors is helpful. Normally would default to string
removeVal <- c(0) 
while (length(sticks) >0){
    cat(length(sticks))
    cat(" \n")
    sticks <- sticks - min(sticks) #subtracts length of smallest stick 
    sticks <- sticks[!sticks %in% removeVal] #Takes all 0 values in sticks out  
}
