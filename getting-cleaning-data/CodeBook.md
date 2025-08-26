# Getting and Cleaning Data Course Project - Code Book

This code book describes the result data in file "tidyData.txt"

## Variables
Each row contains 88 variables.

### Identifiers 
- Subject - An identifier of the subject who carried out the experiment.
- Activity - Activity identifier, string with 6 possible values:
    - WALKING: subject was walking
    -WALKING_UPSTAIRS: subject was walking upstairs
    - WALKING_DOWNSTAIRS: subject was walking downstairs
    - SITTING: subject was sitting
    - STANDING: subject was standing
    - LAYING: subject was laying

### Measurements
- timeBodyAccelerometer-mean()-X 
- timeBodyAccelerometer-mean()-Y 
- timeBodyAccelerometer-mean()-Z 
- timeBodyAccelerometer-std()-X 
- timeBodyAccelerometer-std()-Y 
- timeBodyAccelerometer-std()-Z 
- timeGravityAccelerometer-mean()-X 
- timeGravityAccelerometer-mean()-Y 
- timeGravityAccelerometer-mean()-Z 
- timeGravityAccelerometer-std()-X 
- timeGravityAccelerometer-std()-Y 
- timeGravityAccelerometer-std()-Z 
- timeBodyAccelerometerJerk-mean()-X 
- timeBodyAccelerometerJerk-mean()-Y 
- timeBodyAccelerometerJerk-mean()-Z 
- timeBodyAccelerometerJerk-std()-X 
- timeBodyAccelerometerJerk-std()-Y 
- timeBodyAccelerometerJerk-std()-Z 
- timeBodyGyroscope-mean()-X 
- timeBodyGyroscope-mean()-Y 
- timeBodyGyroscope-mean()-Z 
- timeBodyGyroscope-std()-X 
- timeBodyGyroscope-std()-Y 
- timeBodyGyroscope-std()-Z 
- timeBodyGyroscopeJerk-mean()-X 
- timeBodyGyroscopeJerk-mean()-Y 
- timeBodyGyroscopeJerk-mean()-Z 
- timeBodyGyroscopeJerk-std()-X 
- timeBodyGyroscopeJerk-std()-Y 
- timeBodyGyroscopeJerk-std()-Z 
- timeBodyAccelerometerMagnitude-mean() 
- timeBodyAccelerometerMagnitude-std() 
- timeGravityAccelerometerMagnitude-mean() 
- timeGravityAccelerometerMagnitude-std() 
- timeBodyAccelerometerJerkMagnitude-mean() 
- timeBodyAccelerometerJerkMagnitude-std() 
- timeBodyGyroscopeMagnitude-mean() 
- timeBodyGyroscopeMagnitude-std() 
- timeBodyGyroscopeJerkMagnitude-mean() 
- timeBodyGyroscopeJerkMagnitude-std() 
- frequencyBodyAccelerometer-mean()-X 
- frequencyBodyAccelerometer-mean()-Y 
- frequencyBodyAccelerometer-mean()-Z 
- frequencyBodyAccelerometer-std()-X 
- frequencyBodyAccelerometer-std()-Y 
- frequencyBodyAccelerometer-std()-Z 
- frequencyBodyAccelerometer-meanFreq()-X 
- frequencyBodyAccelerometer-meanFreq()-Y 
- frequencyBodyAccelerometer-meanFreq()-Z 
- frequencyBodyAccelerometerJerk-mean()-X 
- frequencyBodyAccelerometerJerk-mean()-Y 
- frequencyBodyAccelerometerJerk-mean()-Z 
- frequencyBodyAccelerometerJerk-std()-X 
- frequencyBodyAccelerometerJerk-std()-Y 
- frequencyBodyAccelerometerJerk-std()-Z 
- frequencyBodyAccelerometerJerk-meanFreq()-X 
- frequencyBodyAccelerometerJerk-meanFreq()-Y 
- frequencyBodyAccelerometerJerk-meanFreq()-Z 
- frequencyBodyGyroscope-mean()-X 
- frequencyBodyGyroscope-mean()-Y 
- frequencyBodyGyroscope-mean()-Z 
- frequencyBodyGyroscope-std()-X 
- frequencyBodyGyroscope-std()-Y 
- frequencyBodyGyroscope-std()-Z 
- frequencyBodyGyroscope-meanFreq()-X 
- frequencyBodyGyroscope-meanFreq()-Y 
- frequencyBodyGyroscope-meanFreq()-Z 
- frequencyBodyAccelerometerMagnitude-mean() 
- frequencyBodyAccelerometerMagnitude-std() 
- frequencyBodyAccelerometerMagnitude-meanFreq() 
- frequencyBodyAccelerometerJerkMagnitude-mean() 
- frequencyBodyAccelerometerJerkMagnitude-std() 
- frequencyBodyAccelerometerJerkMagnitude-meanFreq() 
- frequencyBodyGyroscopeMagnitude-mean() 
- frequencyBodyGyroscopeMagnitude-std() 
- frequencyBodyGyroscopeMagnitude-meanFreq() 
- frequencyBodyGyroscopeJerkMagnitude-mean() 
- frequencyBodyGyroscopeJerkMagnitude-std() 
- frequencyBodyGyroscopeJerkMagnitude-meanFreq() 
- angle(timeBodyAccelerometerMean,gravity) 
- angle(timeBodyAccelerometerJerkMean),gravityMean) 
- angle(timeBodyGyroscopeMean,gravityMean) 
- angle(timeBodyGyroscopeJerkMean,gravityMean) 
- angle(X,gravityMean) 
- angle(Y,gravityMean) 
- angle(Z,gravityMean) 

## Transformations
The following transformations were applied:
- Merges the training and the test sets to create one data set.
- Extracts only the measurements on the mean and standard deviation for each measurement.
- Uses descriptive activity names to name the activities in the data set
- Appropriately labels the data set with descriptive variable names:
    - the label beginning with "t" replaced with "time" 
    - the label beginning with "f" replaced with "frequency" 
    - "Acc" replaced with "Accelerometer" 
    - "Gyro" replaced with "Gyroscope"
    - "tBody" replaced with "timeBody
    - "BodyBody" replaced with "Body"
    - "Mag" replaced with "Magnitude"
- From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject.

