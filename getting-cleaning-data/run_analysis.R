library(data.table)
library(dplyr)
library(plyr)

##Read feature names and activity labels
namesFeature <- read.table("./UCI HAR Dataset/features.txt", header = FALSE)
labelsActivity <- read.table("./UCI HAR Dataset/activity_labels.txt", header = FALSE)

##Read train data
trainFeatures <- read.table("./UCI HAR Dataset/train/X_train.txt", header = FALSE)
trainActivities <- read.table("./UCI HAR Dataset/train/y_train.txt", header = FALSE)
trainSubjects <- read.table("./UCI HAR Dataset/train/subject_train.txt", header = FALSE)

##Read test data
testFeatures <- read.table("./UCI HAR Dataset/test/X_test.txt", header = FALSE)
testActivities <- read.table("./UCI HAR Dataset/test/y_test.txt", header = FALSE)
testSubjects <- read.table("./UCI HAR Dataset/test/subject_test.txt", header = FALSE)

##Merges the training and the test sets to create one data set
Features <- rbind(trainFeatures, testFeatures)
Activities <- rbind(trainActivities, testActivities)
Subjects <- rbind(trainSubjects, testSubjects)

####Name columns
colnames(Features) <- namesFeature[,2]
colnames(Activities) <- "Activity"
colnames(Subjects) <- "Subject"
colnames(labelsActivity) <- c("id","Activity")

####Merge the data
fullData <- cbind(Features, Activities, Subjects)

##Extracts only the measurements on the mean and standard deviation for 
##each measurement
colsMeanStd <- grep(".*mean.*|.*std.*", names(fullData), ignore.case = TRUE)
extractData <- fullData[,c(colsMeanStd,562,563)]

##Uses descriptive activity names to name the activities in the data set
extractData$Activity <- labelsActivity[extractData$Activity,2]

##Appropriately labels the data set with descriptive variable names
names(extractData)<-gsub("Acc", "Accelerometer", names(extractData))
names(extractData)<-gsub("Gyro", "Gyroscope", names(extractData))
names(extractData)<-gsub("^t", "time", names(extractData))
names(extractData)<-gsub("^f", "frequency", names(extractData))
names(extractData)<-gsub("tBody", "timeBody", names(extractData))
names(extractData)<-gsub("BodyBody", "Body", names(extractData))
names(extractData)<-gsub("Mag", "Magnitude", names(extractData))

##creates a second, independent tidy data set with the average of each variable
##for each activity and each subject
extractData$Subject <- as.factor(extractData$Subject)
tidyData <- aggregate(.~Subject+Activity, extractData, mean)
write.table(tidyData, "tidyData.txt", row.names = FALSE)
