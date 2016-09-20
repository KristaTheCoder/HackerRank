# Enter your code here. Read input from STDIN. Print output to STDOUT
time <- read.table(file = "stdin", header = F) 
t <-as.POSIXct(time[1,1], format = "%I:%M:%S%p") #The different ways of representing data stored behind the %
cat(format(t, format = "%H:%M:%S"))
