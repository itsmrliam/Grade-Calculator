import wpf

from System.Windows import Application, Window, MessageBox
from System.Windows.Controls import Label, ColumnDefinition, RowDefinition, ComboBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'GradeCalculator.xaml')
        myList = ['Comms and Employment', 'Computer Systems', 'Managing Networks', 'Organisational System Security', 'Event Driven Programming', 'Procedural Programming', 'Human Computer Interaction', 'Controlling Systems using IT', 'Website Production'] #sets modules for year 1
        myList2 = ['Comms and Employment', 'Computer Systems', 'Managing Networks', 'Organisational System Security', 'Event Driven Programming', 'Procedural Programming', 'Human Computer Interaction', 'Controlling Systems using IT', 'Website Production'] #sets modules for year 2
        i = 0 #sets the value for the row
        c = 3 #sets the value for the column
        l = 0 #sets the value for the label
        self.subtotal = 0
        self.feedbackLabel.ToolTip = "Your total points will display here" # sets the tooltip for the feedback label.
        self.cmdCalculate.ToolTip = "Press this button to calculate your UCAS points" # sets the tooltip for the calculate button.
        for n in range(8):
            self.myGrid.ColumnDefinitions.Add(ColumnDefinition()) #defines column

        for guest in myList:
            self.myGrid.RowDefinitions.Add(RowDefinition()) #defines row
            self.makeLabel(guest, i, c, l) #makes a label and positions it
            i=i+1 #sets the row + 1

        i = 0 #resets the value for rows
        c = 7 #resets the value for columns
        l = 4 #resets the value for the label
        for guest in myList2:
            self.makeLabel(guest, i, c, l)
            i=i+1


    def makeLabel(self, guest, i, c, l):
        myLabel = Label() #Creates a label
        myLabel.Content = guest #sets content for label
        self.myGrid.SetRow(myLabel, i) #sets row for label
        self.myGrid.SetColumn(myLabel, l) #sets column for label
        self.myGrid.SetColumnSpan(myLabel, 3) #sets length/span for label
        self.myGrid.Children.Add(myLabel) #adds the label as a child to the grid
        
        combo = ComboBox() #creates combo box
        combo.Items.Add("Pass") #adds pass to combo box
        combo.Items.Add("Merit") #adds merit to combo box
        combo.Items.Add("Distinction") #adds distinction to combo box
        self.myGrid.SetRow(combo, i) #sets the row for the combo box
        self.myGrid.SetColumn(combo, c) #sets the column for the combobox
        self.myGrid.Children.Add(combo) #adds the combo box as a child to the grid
        combo.SelectionChanged += self.combochanged #Sets the position for the combo box
        combo.ToolTip = "Choose your Grade for this unit"  #Sets a tooltip for the combo box

    def combochanged(self, sender, event):
        if sender.SelectedIndex == 0:
            self.subtotal = self.subtotal + 70 #if pass then add 70 to total
                        
        if sender.SelectedIndex == 1:
            self.subtotal = self.subtotal + 80 #if merit then add 80 to total
            
        if sender.SelectedIndex == 2:
            self.subtotal = self.subtotal + 90 #if distinction then add 90 to total
            
        self.feedbackLabel.Content = (str(self.subtotal)) #sets the content of the label
       
        sender.IsEnabled = False #Makes sure combo boxes can only be checked once
        
    
    def cmdCalculate_Click(self, sender, e):
        points = self.subtotal
        if points < 1260:
            value = " BTEC Points \n0 UCAS points."
        if points > 1259 and points < 1300:
            value = " BTEC Points \n120 UCAS points. Overall Grade: PPP"
        if points > 1299 and points < 1340:
            value = " BTEC Points \n160 UCAS points. Overall Grade: MPP"
        if points > 1339 and points < 1380:
            value = " BTEC Points \n200 UCAS points. Overall Grade: MMP"
        if points > 1379 and points < 1420:
            value = " BTEC Points \n240 UCAS points. Overall Grade: MMM"
        if points > 1419 and points < 1460:
            value = " BTEC Points \n280 UCAS points. Overall Grade: DMM"
        if points > 1459 and points < 1500:
            value = " BTEC Points \n320 UCAS points. Overall Grade: DDM"
        if points > 1499 and points < 1530:
            value = " BTEC Points \n360 UCAS points. Overall Grade: DDD"
        if points > 1529 and points < 1560:
            value = " BTEC Points \n380 UCAS points. Overall Grade: D*DD"
        if points > 1559 and points < 1590:
            value = " BTEC Points \n400 UCAS points. Overall Grade: D*D*D"
        if points > 1589:
            value = " BTEC Points \n420 UCAS points. Overall Grade: D*D*D*"
        #Checks if the total points is in between a certain range, then puts a grade to it.
       
        self.feedbackLabel.Content = (str(points) + value) #Changes the feedback label to display the points
        MessageBox.Show(str(points) + value) #Displays message box showing end result.
        
        

if __name__ == '__main__':
    Application().Run(MyWindow())