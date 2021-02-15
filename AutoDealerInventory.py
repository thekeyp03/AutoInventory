#Clinton Corbin - Module 8, Portfolio Project, Option 1: Create automobile program for use by dealership to track inventory
import os
import copy

class InvalidIdxError(Exception):
    def __init__(self, value):
        self.value = value

#class automobile represents the auto object found in the vendor's inventory
class Automobile:
    #default constructor
    def __init__(self):
        self._make = ''
        self._model = ''
        self._color = ''
        self._year = ''
        self._mileage = ''
    
    #constructor
    def __init__(self, make, model, color, year, mileage):
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._mileage = mileage

    def update_make(self, make):
        self._make = make

    def update_model(self, model):
        self._model = model

    def update_color(self, color):
        self._color = color

    def update_year(self, year):
        self._year = year

    def update_mileage(self, mileage):
        self._mileage = mileage

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    def get_year(self):
        return self._year

    def get_mileage(self):
        return self._mileage

    #output the Automobile instance
    def __str__(self):
        return ('MAKE: %s, MODEL: %s, COLOR: %s, YEAR: %d, MILEAGE: %d' %
                (self._make, self._model, self._color, self._year, self._mileage))

#print_menu is the main interface which allows the user to direct the program of what to do
def print_menu():
    continuePrompt = True
    validOptions = [0, 1, 2, 3, 4, 5] #used to validate user input against
    try:
        #find out what the user wants to do.  Continue execution until user enters 0 to quit
        while continuePrompt:
            print('**** Menu ****')
            print('  1. Add Automobile')                #user wants to add an auto to inventory
            print('  2. Print Inventory')               #user wants to see what is in inventory
            print('  3. Output Inventory to File')      #user wants to output inventory to a text file
            print('  4. Delete Auto from Inventory')    #user wants to delete an auto from inventory
            print('  5. Update Auto already in Inventory')  #user wants to change an existing auto
            print('  0. Quit')                          #user wants to exit the program
            userInput = int(input('Enter number of option to perform: '))
            if userInput in validOptions:
                continuePrompt = False
            else:
                print('Invalid option entered')

    except Exception as ex:
        print('Exception: %s' % ex)
    return userInput

#addAutomobile prompts the user for auto attributes and adds the auto to inventory
def addAutomobile(inventory):
    getValue = True
    print('Please enter:')
    make = input('  Make: ')
    model = input('  Model: ')
    color = input('  Color: ')

    while getValue:
        try:
            year = int(input('  Year: '))
            getValue = False
        except ValueError:
            print('Invalid year, please try again')

    getValue = True
    while getValue:
        try:
            mileage = int(input('  Mileage: '))
            getValue = False
        except ValueError:
            print('Invalid mileage, please try again')

    #create the auto...        
    auto = Automobile(make, model, color, year, mileage)

    #add the instance to inventory
    inventory.append(auto)

#printToFile allows the user to save inventory to a file
def printToFile(inventory):
    continuePrompt = True
    if len(inventory) > 0:
        try:
            currentDirectory = os.getcwd()
            #get
            while continuePrompt:
                fileName = input('Name of file to output to (excluding file name extension): ')
                if fileName.strip() == '':
                    print('Invalid file name, please try again')
                else:
                    fileName = fileName.strip() + '.txt'
                    continuePrompt = False
            #let the user know a default directory has been chosen and the name of the file to be used
            print('  Inventory will be output to %s\\%s' % (currentDirectory, fileName))
            
            file = open(fileName, "w")

            #output inventory to the file
            for automobile in inventory:
                file.write(str(automobile) + '\n')
            file.close()

            #let the user know success
            print('Print to file success!')
        except Exception as ex:
            print('Exception: %s' % ex)
        finally:
            file.close()
    else:
        print('Nothing in inventory to save to file!')

#removeAutomobile prompts the user for a record to be deleted
def removeAutomobile(inventory):
    #class InvalidIdxError(Exception):
    #    def __init__(self, value):
    #        self.value = value
            
    continuePrompt = True

    #let the user know what is available to be removed
    for idx, automobile in enumerate(inventory):
        print('  %d: %s' % (idx, automobile))

    #find out which record the user wants to delete and delete it
    while continuePrompt:
        try:
            if len(inventory) > 0:
                #give the user an out to abort (not delete anything) by entering -1
                userInput = int(input('Please enter number of automobile to delete or \'-1\' to abort: '))
                if userInput == -1:
                    continuePrompt = False

                #elseif valid input then delete the record
                elif 0 <= userInput and userInput <= (len(inventory) - 1):
                    del inventory[userInput]
                    print('Record deleted!')
                    continuePrompt = False
                else:
                    raise InvalidIdxError('Invalid')
            else:
                print('No inventory to delete!')
                continuePrompt = False
        except (ValueError, InvalidIdxError):
            print('Invalid entry, please try again')
        except Exception as ex:
            print('Exception: %s' % ex)

#updateAuto is used to allow the user to change an existing auto
def updateAuto(inventory):
    continueAutoPrompt = True
    getValue = True
    
    
    if len(inventory) > 0:
        while continueAutoPrompt:
            try:
                for idx, automobile in enumerate(inventory):
                    print('  %d: %s' % (idx, automobile))
                #give the user an out to abort (not update anything) by entering -1
                userInput = int(input('Enter number of automobile you\'d like to change or \'-1\' to abort: '))
                if userInput == -1:
                    continueAutoPrompt = False
                elif 0 <= userInput and userInput <= (len(inventory) - 1):
                    oldAuto = copy.deepcopy(inventory[userInput])
                    
                    print('Enter new values or leave null to keep the existing value')
                    
                    newValue = input('  Make (%s): ' % inventory[userInput].get_make())
                    if newValue.strip() != '':
                        inventory[userInput].update_make(newValue)
                    
                    newValue = input('  Model (%s): ' % inventory[userInput].get_model())
                    if newValue.strip() != '':
                        inventory[userInput].update_model(newValue)
                    
                    newValue = input('  Color (%s): ' % inventory[userInput].get_color())
                    if newValue.strip() != '':
                        inventory[userInput].update_color(newValue)
                        
                    try:
                        while getValue:
                            newValue = int(input('  Year (%s): ' % inventory[userInput].get_year()))
                            getValue = False
                            if str(newValue).strip() != '':
                                inventory[userInput].update_year(newValue)
                    except ValueError:
                        print('Invalid year, please try again')
                        
                    getValue = True
                    try:
                        while getValue:
                            newValue = int(input('  Mileage (%s): ' % inventory[userInput].get_mileage()))
                            getValue = False
                            if str(newValue).strip() != '':
                                inventory[userInput].update_mileage(newValue)
                    except ValueError:
                        print('Invalid mileage, please try again')
                    print('Old Values: %s' % oldAuto)
                    print('New Values: %s' % inventory[userInput])
                    continueAutoPrompt = False
                else:
                   raise InvalidIdxError('Invalid')
            except (ValueError, InvalidIdxError):
                print('Invalid entry, please try again')
            except Exception as ex:
                print('Exception: %s' % ex)
    else:
        print('There is nothing in inventory to be updated!')

#main is the main method of the program
def main():
    userCommand = 1
    inventory = []
    while userCommand != 0: #if the user enters 0 then quit the program
        userCommand = print_menu() #display the menu to find out what the user wants to do
        
        if userCommand == 1: #user wants to add an auto to inventory
            addAutomobile(inventory)
        elif userCommand == 2: #user wants to see what is in inventory
            print('**** Inventory ****')
            if len(inventory) > 0:
                for idx, automobile in enumerate(inventory):
                    print('  %d: %s' % (idx, automobile))
            else:
                print('Nothing in your inventory!')
            print('\n')
        elif userCommand == 3: #user wants to output inventory to file
            printToFile(inventory)
        elif userCommand == 4: #user wants to delete a record from inventory
            removeAutomobile(inventory)
        elif userCommand == 5: #user wants to edit an existing record
            updateAuto(inventory)

main()
    
