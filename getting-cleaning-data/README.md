# Getting and Cleaning Data Course Project - README

In this project, we collect, worked with, and clean a data set. The goal is to prepare tidy data that can be used for later analysis. 

The repository contains the following:

- README.md: explains how all of the scripts work and how they are connected
- CodeBook.md: describes the variables, the data, and any transformations or work
- run_analysis.R: a script for performing the analysis
- tidyData.txt: a tidy data set

## Creating the tidy data set
 
- Download the source data for the project:
[Source data for the project](https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip
) ( [Source data description](http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones) )

- Call "run_analysis.R" to create the tidy data set. This script will do the following:
  1. Merges the training and the test sets to create one data set.
  2. Extracts only the measurements on the mean and standard deviation for each measurement.
  3. Uses descriptive activity names to name the activities in the data set
  4. Appropriately labels the data set with descriptive variable names.
  5. From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject.
  6. Writes the data set in step 5 to the file "tidyData.txt".