#Cameron Labrie
#CSC 110 / Lisa Dipippo
#Programming Project - TV Shows Data
#12/13/2022



#Program reads streaming service tv shows from a data file and displays certain information thats requested by the user 


    #checks if the file name entered by the user exists 
def fileValid():

    Valid = False
    while Valid == False:
        fileName = input("Enter the name of the data file: ")
        try:
            File = open(fileName, "r")
            Valid = True

        except IOError:
            print("Invalid file name - try again")

    return File



    #reads data from the selected file and appends the different cate
def getData():
    Filein = fileValid()
    titleList = []
    ratingList = []
    yearList = []
    scoreList = []
    fline = Filein.readline()
    for fline in Filein:
        fline.strip()
        title, rating, year, score = fline.split(',')
        titleList.append(title)
        ratingList.append(rating)
        yearList.append(int(year))
        scoreList.append(int(score))
    Filein.close()



    return titleList, ratingList, yearList, scoreList



# checks to see if the rating entered by the user exists in the data
def ratingCheck(ratingList):

    Rating = False
    while Rating == False:
            userRating = input("Enter rating:")
            if userRating in ratingList:
                Rating = True
            else:
                print("Invalid entry - try again")

    return userRating

#checks to see if the year selected by the user exists in the data
def yearGet (yearList, string):

    yearGood = False
    while yearGood == False:
        try:
            year = int(input(string))
            if year in yearList:
                yearGood = True
            else:
                print("Invalid year - try again")

        except ValueError:
            print("Invalid entry - try again")


    return year

# checks to see if the user entered a valid range of years relative to the data
def getYear(yearList):
    Year = False
    print(" ")
    print("Enter year range to search (oldest year first)")
    while Year == False:
        try:
            oneYear = yearGet(yearList, "Year1: ")
            twoYear = yearGet(yearList, "Year2: ")



            if oneYear < twoYear:
                Year = True
            
            else:
                print("Second year should be after first year - try again")

        except ValueError:
            print("Invalid year - try again")

    return oneYear, twoYear

            


# checks to see if the title selected by the user exists in the data        
def titleCheck(titleList):
    userTitle = input("Enter show title: ")
            
               

    return userTitle


#checks to see if the title selected by the user is valid for function5 
def titleCheck2(titleList):
    #print(" ")
    Title2 = False
    while Title2 == False:
        userTitle2 = input("Enter title:")
        if userTitle2 in titleList:
            Title2 = True
        else:
            print("Invalid entry - try again")



    return userTitle2
        
            



def Function1 (ratingList, titleList, yearList, scoreList):

    #initializes the users selected rating and output lists

    userRating = ratingCheck(ratingList)
    newTitleList = []
    newYearList = []
    newRatingList = []
    newScoreList = []

    #loops through the ratingList to find shows that match the users selected rating

    for i in range(len(ratingList)):
        if userRating == ratingList[i]:
            newTitleList.append(i)
            newYearList.append(i)
            newRatingList.append(i)
            newScoreList.append(i)

    #the information of the matched shows is appended to the output lists
            
    
    
    #for userRating in ratingList:
        #newTitleList.append(i)
        #newYearList.append(i)
        #newRatingList.append(i)
        #newScoreList.append(i)

    return newTitleList,newYearList, newRatingList, newScoreList



def Function2(ratingList, titleList, yearList, scoreList):
    
    #initializes the users selected range of years and output lists

    oneYear, twoYear = getYear(yearList)
    newTitleList = []
    newRatingList = []
    newYearList = []
    newScoreList = []

            
    highScore = 0
    highScoreIndex = 0

    #loops through the yearList to find the single highest score in the users selected range of years

    for i in range(len(yearList)):
        if yearList[i] >= oneYear and yearList[i]<= twoYear:
            if scoreList[i] > highScore:
                highScore = scoreList[i]
                highScoreIndex = i

     #the index of the high score is appended to the output lists in order to match the score with its corresponding show       


    newTitleList.append(highScoreIndex)
    newScoreList.append(highScoreIndex)
    newYearList.append(highScoreIndex)
    newRatingList.append(highScoreIndex)

    return newTitleList, newScoreList, newYearList, newRatingList



def Function3(ratingList, titleList, yearList, scoreList):

    #initializes the users selected show title and output lists

    userTitle = titleCheck(titleList)

    newTitleList = []
    newRatingList = []
    newYearList = []
    newScoreList = []

    
    #loops through the titleList to find the user show title's corresponding information

    for i in range(len(titleList)):
        if userTitle.upper() == titleList[i].upper():
            newTitleList.append(i)
            newRatingList.append(i)
            newYearList.append(i)
            newScoreList.append(i)





    #lets the user know that there are no shows that match, results are not printed

    if len(newTitleList) == 0 and len(newRatingList) == 0 and len(newYearList) == 0 and len(newScoreList) == 0:
        print(" ")
        print("No shows meet your criteria")
        Choice()
            

    
    #matching information is appended to output lists





    return newTitleList, newRatingList, newYearList, newScoreList




def Function4(ratingList, titleList, yearList, scoreList):

    #initializes the score list used to find the average score and the users selected rating 

    newScoreList = []

    userRating = ratingCheck(ratingList)

    score = 0

    #loops through the ratingList to find all of the scores that correspond with the users selected rating

    for i in range (len(ratingList)):
        if userRating == ratingList[i]:
            newScoreList.append(scoreList[i])


#uses the list of scores to find the total score in the List

    for i in range (len(newScoreList)):
        score = score + newScoreList[i]


#uses the total score to find the average score

    score = score/len(newScoreList)

    


    return score, userRating




def Function5(ratingList, titleList, yearList, scoreList):

    #initializes the output lists and the title selected by the user (with error messages specified for the 5th function)


    userTitle2 = titleCheck2(titleList)
    #for userTitle in titleList:
        #score = i
    score = 0
    newTitleList = []
    newRatingList = []
    newYearList = []
    newScoreList = []

    #loops through the titleList to find the corresponding score for the users selected show title

    for i in range(len(titleList)):
        if userTitle2 == titleList[i]:
            score = scoreList[i]

            

    #loops through the scoreList to find all of the scores that are higher than the score of the users selected show

    for i in range(len(scoreList)):
        if scoreList[i] > score:
            newTitleList.append(i)
            newRatingList.append(i)
            newYearList.append(i)
            newScoreList.append(i)


    #appends the corresponding information of the higher scores to the output lists



    if len(newTitleList) == 0 and len(newRatingList) == 0 and len(newYearList) == 0 and len(newScoreList) == 0:
        print(" ")
        print("No shows meet your criteria")
        Choice()


    #lets the user know that there is no show with a higher average, results are not printed

        


    return newTitleList, newRatingList, newYearList, newScoreList





def Function6part1(ratingList, titleList, yearList, scoreList):

    #initializes the output lists of the sorted data

    
    sort = []
    sort2 = []
    sort3 = []
    sort4 = []

    #loops through the ratingList to prepare the lists for sorting

    for i in range(1, len(ratingList)):
        sort = ratingList[i]
        sort2 = titleList[i]
        sort3 = yearList[i]
        sort4 = scoreList[i]
        
        j = i

        #uses the yearList to sort each list through dual sort

        while j > 0 and yearList[j-1] > sort3:
            ratingList[j] = ratingList[j-1]
            titleList[j] = titleList[j-1]
            yearList[j] = yearList[j-1]
            scoreList[j] = scoreList[j-1]
            


            j = j - 1

        #adds the sorted data to the corresponding output lists

        ratingList[j] = sort
        titleList[j] = sort2
        yearList[j] = sort3
        scoreList[j] = sort4




    return sort, sort2, sort3, sort4







def Function6part2(sort, sort2, sort3, sort4):

    #creates the name of the new file and prepares the file for editing

    fileName = "year-sorted-shows.csv"

    fileIn =  open(fileName, "w")


    i = 0
    
    #writes the header of each data category into the file
    
    fileIn.write(str("Title") + "," + str("Rating") + "," + str("Year") + "," + str("Score") + "\n")

    # loops through the sorted titleList to write the data of each sorted list under its corresponding header in the file

    while i < len(sort2):
        fileIn.write(str(sort2[i]) + "," + str(sort[i]) + "," + str(sort3[i]) + "," + str(sort4[i]) + "\n")


        i = i + 1

    fileIn.close()

    #lets the user know that the file was created

    print("Data sorted by years written to file", fileName)



    return fileName




#prints the results of each of the 6 functions except function 4 which computes an average
def printResults(newTitleList, newRatingList, newYearList, newScoreList, titleList, ratingList, yearList, scoreList ):
    print(" ")
    print("The TV shows that meet your criteria are:")
    print(" ")


    #formats each of the out headings and their corresponding output

    
    print("TITLE".ljust(40),"RATING".ljust(8),"YEAR".ljust(5), "SCORE".ljust(4))
    for i in range(len(newTitleList)):
        print(titleList[newTitleList[i]].ljust(40), ratingList[newRatingList[i]].ljust(8), str(yearList[newYearList[i]]).ljust(5),str(scoreList[newScoreList[i]]).ljust(4))
        #print(newTitleList[i], " ", " ", " ", " ", " ", newRatingList[i], " ", " ", " ", newYearList[i], " ", newScoreList[i])





    return




    # prints the average calculated from function 4 and rounds it 2 decimal places
def resultFunction4(score, userRating ):
    print("The average score for shows with a", userRating, "rating is ", "{:,.2f}".format(score))



    return


        
        












    

    




#Gives the user a choice of what they want the program to do
def Choice():
    choice = 0

    print("")
    print("Please choose one of the following options:")
    print("1 -- Find all shows with a certain rating")
    print("2 -- Find the show with the highest score released in a specified range of years")
    print("3 -- Search for a show by title")
    print("4 -- Find the average score for films with a specific rating")
    print("5 -- Find all shows with a score higher than the score for a given show")
    print("6 -- Sort all lists by year and write results to a new file")
    print("7 -- Quit")

    #checks to see if the choice selected by the user is valid
    
    choiceError = False
    while choiceError == False:
        try:
            choice = int(input("Choice ==> "))
            if choice >= 1 and choice <= 7:
                choiceError = True

            else:
                print("Invalid entry - try again")

        except ValueError:
            print("Invalid entry - try again")


    print(" ")

    return choice




def main():
    choice = 0

    titleList, ratingList, yearList, scoreList = getData()
    choice = Choice()
    while choice != 7:

        if choice == 1:

            #calls the function to find all shows with a specified rating
            
            newTitleList,newYearList, newRatingList, newScoreList = Function1(ratingList, titleList, yearList, scoreList)

            printResults(newTitleList,newYearList, newRatingList, newScoreList, titleList, ratingList, yearList, scoreList)

            choice = Choice()

            


        elif choice == 2:

            #calls the function to find highest score within specific year range
            
            newTitleList,newYearList, newRatingList, newScoreList = Function2(ratingList, titleList, yearList, scoreList)

            printResults(newTitleList,newYearList, newRatingList, newScoreList, titleList, ratingList, yearList, scoreList)

            choice = Choice()


            


        elif choice == 3:

            #calls the function to search for a show by title
            
            newTitleList, newYearList, newRatingList, newScoreList = Function3(ratingList, titleList, yearList, scoreList)

            if len(newTitleList) > 0 and len(newRatingList) > 0 and len(newYearList) > 0 and len(newScoreList) > 0:
                printResults(newTitleList,newYearList, newRatingList, newScoreList, titleList, ratingList, yearList, scoreList)
                choice = Choice()



        elif choice == 4:

            #calls the function to find average of shows with specific rating
            
            score, userRating = Function4(ratingList, titleList, yearList, scoreList)

            resultFunction4(score, userRating)

            choice = Choice()


            
            


        elif choice == 5:

            #calls the function that returns a viewer score higher than the given show score
            
            newTitleList,newYearList, newRatingList, newScoreList = Function5(ratingList, titleList, yearList, scoreList)

            if len(newTitleList) > 0 and len(newRatingList) > 0 and len(newYearList) > 0 and len(newScoreList) > 0:
                printResults(newTitleList,newYearList, newRatingList, newScoreList, titleList, ratingList, yearList, scoreList)
                choice = Choice()

          


            

            #choice = Choice()

            


        elif choice == 6:

            #calls the function that sorts all lists by year
            
            sort, sort2, sort3, sort4 = Function6part1(ratingList, titleList, yearList, scoreList)

            fileName = Function6part2(ratingList, titleList, yearList, scoreList)

            choice = Choice()

            


       

            

    print(" ")
    print("Good-bye")