
# Predicting Crime in San Francisco using NaiveBayes (2.54591)

library(e1071)

# Load files
train = read.csv ("/home/chandini/Desktop/SEM5/Analy/FinalProj/SFransCrimeClassfn/train.csv",stringsAsFactors=F) #1:878049
test = read.csv ("/home/chandini/Desktop/SEM5/Analy/FinalProj/SFransCrimeClassfn/test.csv",stringsAsFactors=F) #1:884262

# View Structure
#str(train_raw)
#str(test_raw)

# Labels
test_Id = test$Id
train_Category = train$Category

# Remove not used in the model
test$Id = NULL
test$Address = NULL
train$Category = NULL
train$Descript = NULL
train$Resolution = NULL
train$Address = NULL

# Create a total dataset to create a proper Test and Training set
# for the Naive Bayes model. (This helped me avoid error with factors features)
total=rbind(train,test)
str(total)
# Extract Date feature and create Year, Month, Hour features
total$Dates = as.character(total$Dates)
date = strptime(total$Dates,"%Y-%m-%d %H:%M:%S")
total$Year = format(date,"%Y")
total$Month = format(date,"%m")
total$Hour = format(date,"%H")
# Concatenate location X and Y
total$Loc = as.factor(paste(round(total$X,2), round(total$Y,2), sep= " "))

# Remove unsed variables
total$X = NULL
total$Y = NULL
total$Dates = NULL

# Convert to factors
total$DayOfWeek = as.factor(total$DayOfWeek)
total$PdDistrict = as.factor(total$PdDistrict)
total$Year = as.factor(total$Year)
total$Month = as.factor(total$Month)
total$Hour = as.factor(total$Hour)

# Create Training and Testing Sets
train = total[1:878049,]
test = total[878050:1762311,]

rm(total)

# Create submission dataset
submission = data.frame(Id=test_Id)
response = data.frame(Cat=train_Category)
crime = as.character(unique(train_Category))
crime = sort(crime)

# loop through every crime category to predict the probability of happening
# store result in submission
for (i in crime){
    response[i]= 0
    response[i][response$Cat==i,] = 1
    classifier = naiveBayes(response[,i]~.,data=train, laplace=1)
    pred = predict(classifier,test,type = "raw")
    submission[i] = pred[,2]
    print(paste0(ncol(submission)/length(crime)*100,'% completed'))
}

# Export CSV with submission file
write.csv(submission,file='/home/chandini/Desktop/SEM5/Analy/FinalProj/SFransCrimeClassfn/submission.csv',row.names=FALSE)

