import matplotlib.pyplot as plt
import numpy as np
import json as js


#Creating Australian user variables
class AustralianUser:

    def __init__(self,age,gender,height,weight,meat,dairy,grain,veg,fruits):
        self._age = age
        self._gender = gender
        self._height = height
        self._weight = weight
        self._meat = meat
        self._dairy = dairy 
        self._grain = grain 
        self._veg = veg 
        self._fruits = fruits

    def __userBmi(self):
        userBmi = (self._weight / (self._height / 100)**2 )
        return round(userBmi, 2)
    
    @property
    def get_userBmi(self):
        return self.__userBmi()

    
#Seperating User food intake and inheriting the input from the user 
class AustralianFoodBase(AustralianUser):
    #Creating the class variable 
    __baseMeat = 3    
    __baseDairy = 2.5 
    __baseGrain = 6 
    __baseVeg = 6 
    __baseFruit = 2


    #Creating user food intake 
    def __init__(self,age,gender,height,weight,meat,dairy,grain,veg,fruits):
        super().__init__(age,gender,height,weight,meat,dairy,grain,veg,fruits)

    #Create a class method to encapsulate the array 
    @classmethod
    def __basePlot(cls):
        foodBase = [cls.__baseMeat,cls.__baseDairy,cls.__baseGrain,cls.__baseVeg,cls.__baseFruit]
        return foodBase
    
    def __userPlot(self):
        userBase = [self._meat,self._dairy,self._grain,self._veg,self._fruits]
        return userBase
    
    def __foodType(self):
        foodLabels = ['Meat','Dairy','Grain', 'Vegetable','Fruit']
        return foodLabels
    

    #Plotting the graph itself 
    def plotFoodIntakeLine(self):
        
        #Calls the private functions to enable the arrays 
        base_data = self.__basePlot()
        user_data = self.__userPlot()
        foodLabels = self.__foodType()

        #Plotting based on the data 
        result, figure = plt.subplots()
        figure.plot(foodLabels, base_data, label="Australian Food Base", marker='o')
        figure.plot(foodLabels, user_data, label="User Intake", marker='o')

        min_val = min(min(base_data),min(user_data))
        max_val = max(max(base_data),max(user_data))

        padding = (max_val - min_val) * 0.1 
        figure.set_ylim(min_val - padding, max_val + padding)



        figure.set_ylabel("Daily Servings")
        figure.set_title("Australian Food Intake Comparison")
        figure.legend()

        plt.suptitle("Daily Intake")


        return result
    
    #Plotting the graph itself 
    def plotFoodIntakeBar(self):
        base_data = self.__basePlot()
        user_data = self.__userPlot()
        foodLabels = self.__foodType()
        barWidth = 0.4

        #Creating the bar widths
        br1 = np.arange(len(base_data))
        br2 = [x + barWidth for x in br1]
        
        #Labeling the other graphs
        result,figure = plt.subplots()
        figure.bar(br1, base_data, width=barWidth, label="Australian Food Base")
        figure.bar(br2, user_data, width=barWidth, label="User intake")
        #Sets the ticks into the centre so they can line up in the graph
        figure.set_xticks([r + barWidth/2 for r in br1])
        figure.set_xticklabels(foodLabels)
        #Label and titles
        figure.set_ylabel("Daily Servings")
        figure.set_title("Australian Food Intake Comparison")
        figure.legend()

        plt.suptitle("Daily intake")

        return result 
    
    def plotFoodIntakePie(self):
        base_data = self.__basePlot()
        user_data = self.__userPlot()
        foodLabels = self.__foodType()

        result, figure = plt.subplots(1, 2)  # Create a figure with 1 row, 2 columns of subplots

        figure[0].pie(base_data, labels=foodLabels, autopct='%1.1f%%')
        figure[0].set_title("Recommended intake")

        figure[1].pie(user_data, labels=foodLabels, autopct='%1.1f%%')
        figure[1].set_title("User intake")

        plt.suptitle("Daily intake")

        return result  # Return the figure if needed
    
    def plotFoodIntakeScatter(self):
        #Calls private functions 
        base_data = self.__basePlot()
        user_data = self.__userPlot()
        foodLabels = self.__foodType()


        #Creating the arrays 
        scat1 = np.array((base_data))
        scat2 = np.array((user_data))

        result,figure = plt.subplots()
        figure.scatter(foodLabels,scat1, label="Recommended intake", facecolors="lightblue")
        figure.scatter(foodLabels,scat2, label="User Intake", edgecolors="orange", facecolors='none')
        figure.set_ylabel("Daily Servings")
        figure.legend()

        plt.suptitle("Daily Intake")

        return result
    
    def plotFoodIntakeBMI(self):
        #Calling private functions
        #Creating weighting variable
        ybase_data = np.array([-1,0,1,2,3,4,5,6])
        xbase_data = np.array([0,5,10,15,20,25,30,35])
        user_data = self.get_userBmi
        
        #Creating bmi ranges
        bmi_start = np.array([0,20,25,30])
        bmi_end = np.array([18.5,25,30,35])
        width = bmi_end - bmi_start
        y_positions = np.array([1,2,3,4])
        bmi_labels = ["Under-Weight","Healthy Weight","Over-weight","Obese"]
        #Plotting the data points
        result,figure = plt.subplots()
        line = figure.plot(xbase_data, ybase_data, label='BMI curve')
        #Creating axis labels
        figure.set_ylabel("Weight class")
        figure.set_xlabel("BMI")
        figure.invert_yaxis()

        #Making the line hidden
        line[0].set_visible(False)

        #Showing bmi ranges
        bars = figure.barh(y_positions, width, left=bmi_start,height=0.1,alpha=0.3)
        figure.bar_label(bars, labels=bmi_labels, label_type="center", padding=3,fontsize=9, color="black")

        #Creating users 
        figure.axvline(x=user_data, label=f"Your bmi {user_data}")
        figure.legend()
        #Creating bmi title 
        plt.suptitle("BMI Chart For Adults")

        return result
    
class GraphSave(AustralianFoodBase):

    def __init__(self, age, gender, height, weight, meat, dairy, grain, veg, fruits):
        super().__init__(age, gender, height, weight, meat, dairy, grain, veg, fruits)

    def savePlot(self):
        graphFigures = [self.plotFoodIntakeBar(),self.plotFoodIntakeBMI(),self.plotFoodIntakeLine(),self.plotFoodIntakePie(),self.plotFoodIntakeScatter()] # assuming this returns a figure
        
        #Enumerate so each graph function can be added with an index so it can be looped through.
        for index,fig in enumerate(graphFigures):
            fig.savefig(f"UserGraphs_{index+1}.jpg", dpi=300) # Save as JPEG with 300 dpi resolution
        return graphFigures
    #Showing each plot of the graph without having it in the graph itself
    def showPlot(self):
        graphFigures = [self.plotFoodIntakeBar(),self.plotFoodIntakeBMI(),self.plotFoodIntakeLine(),self.plotFoodIntakePie(),self.plotFoodIntakeScatter()]
        #Calls all the figures in the graph and demonstrates them 
        for fig in graphFigures:
            plt.show()
        return  graphFigures
            


class UserInformation(js.JSONEncoder):
    def default(self, obj):
        #Serializes the user information into a json format
        if isinstance(obj, AustralianUser):
            return {
                "Age": obj._age,
                "Gender": obj._gender,
                "Height": obj._height,
                "Weight": obj._weight,
                "BMI": obj.get_userBmi,
                "Meat" : f"{obj._meat} Daily servings",
                "Dairy": f"{obj._dairy} Daily servings",
                "Grain": f"{obj._grain} Daily servings",
                "Vegetable": f"{obj._veg} Daily servings",
                "Fruit": f"{obj._fruits} Daily servings",
                }
        return super().default(obj)
    
    #Creates an users output into a text file 
    def useroutput(self, obj , username): #Allows for the user name to be dynamically applied to the file
        filename = f"{username}.txt"
        #Opens the text file
        with open(filename, 'w') as f :
            js.dump(obj,f, cls=UserInformation, indent=4)
        return filename


def main():
    #Applies and store information to prevent boilerplate coding
    keys = ['age','gender','height','weight', 'meat','dairy','grain','veg','fruits']
    user_info = []
    #Loops through the keys and appends them into the empty list so it can be used for a class 
    for key in keys:
        if key in ['meat','dairy','grain','veg','fruits']:
            try:
                value = int(input(f"Enter your {key} daily servings: "))
            except ValueError:
                print("Enter a proper value!")
        elif key in ['height','weight']:
            try:
                value = int(input(f"Enter your {key}: "))
            except ValueError:
                print("Input a proper value!")
        else:
            value = input(f"Enter your {key}: ")
        
        user_info.append(value)
    
    #Allows for multiple values of the list to be processed 
    user_graphs = GraphSave(*user_info)
    #Allows for the graphs to be saved
    user_graphs.showPlot()
    user_save = bool(input("Enter a key to save the information (Leave empty to pass): "))
    #Enters user name and saves the text information 
    if user_save == True:
        user_name = input("Enter your name: ")
        encoder = UserInformation()
        encoder.useroutput(user_graphs, user_name)
        user_graphs.savePlot()
    else:
        print("Good-bye!")


main()
