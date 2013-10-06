##When running R, please make sure to change Path to whereever you launched the .txt file from, url to github won't work
LE = readLines("~/Dropbox/School/Statistics/Stat 157 Fall 2013/project1/Learning.txt")
LEA = as.numeric(gsub("[^0-9]*", "", LE))
LEA= as.numeric(LEA[!is.na(LEA)])
Learninglast = (length(LEA)-4)/4
Visual = LEA[c(1,1+4*(1:Learninglast))]
Aural = LEA[c(2,2+4*(1:Learninglast))]
Read_Write = LEA[c(3,3+4*(1:Learninglast))]
Kinesthetic = LEA[c(4,4+4*(1:Learninglast))]
Learning = data.frame(Visual, Aural, Read_Write, Kinesthetic)
##When running R, please make sure to change Path to whereever you launched the .txt file from, url to github won't work
PE = readLines("~/Dropbox/School/Statistics/Stat 157 Fall 2013/project1/personal.txt")
Personal = gsub("/", " ", PE)
