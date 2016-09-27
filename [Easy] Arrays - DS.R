# Enter your code here. Read input from STDIN. Print output to STDOUT
array <- read.table(file = "stdin", header = F, fill = T, sep = " ")
revArray <- rev(array[2,]) #reverse values
write.table(revArray, row.names = F, col.names = F) #remove overhead variable and row names for printing
