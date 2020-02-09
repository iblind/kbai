# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.

import inspect
import pprint
from PIL import Image
import numpy

pp = pprint.PrettyPrinter(indent=4)




class makeFigure:
    def __init__(self, figure, name, properties):
        self.figure = figure
        self.name = name
        self.properties = properties


def check_num_figures(a,b):
    if(len(a)==len(b)):
        return 1
    else:
      return 0

def get_object_properties(problem,obj):

    object_figure_keys = list(problem.figures[obj].objects.keys())

    # print('Figure : '+str(obj)+'\nNum objects: '+str(len(object_figure_keys)))

    list_of_figures_in_object=[]

    for figure in object_figure_keys:
        fig_name = problem.figures[obj].objects[figure].name
        fig_properties = problem.figures[obj].objects[figure].attributes
        current_figure = makeFigure(obj,fig_name,fig_properties).__dict__ #assign as a dictionary
        list_of_figures_in_object.append(current_figure)

        del fig_name
        del fig_properties
        del current_figure

    # pp.pprint(list_of_figures_in_object)
    return list_of_figures_in_object


def check_number_of_figures(fig_list_1, fig_list_2):
    if (len(fig_list_1) == len(fig_list_2)):
        return 1
    else:
        return 0


def check_if_objects_are_same(fig_A,fig_B):
    if (fig_A['properties'] == fig_B['properties']):
        return True
    else:
        return False

def select_relevant_transformation(differences):
    relevant_differences = []

    for attribute in differences.keys():
        if(differences[attribute]['same_properties']==1):
            continue
        else:
            # print(differences)
            differences[attribute]['differences']['attribute']=attribute
            relevant_differences.append(differences[attribute])
    return relevant_differences

def compare_object_properties(fig_A, fig_B):
    same_properties = 1;
    differences = {}
    # Check that we have the same number of properties
    # if yes, proceed to check whether they're the same
    # #TODO if no, see which object has more properties and deal with that

    if(len(fig_B['properties'])==len(fig_A['properties'])):
        for key in fig_A['properties']:
            if fig_A['properties'][key] == fig_B['properties'][key]:
                same_properties = 1
                differences[key] = {'same_properties': same_properties, 'differences':''}
            else:
                same_properties = 0
                differences[key] = {'same_properties':same_properties,'differences':{'A': fig_A['properties'][key], 'B': fig_B['properties'][key]}}

    # print(differences)
    return differences

    # print(differences)
    # transformations = []
    # for attribute in list(differences.keys()):
    #     if(differences[attribute]['same_properties']==1):
    #         continue
    #     else:
    #         transformations.append(differences[attribute])


# B05
def check_if_object_inside_another(figure):

    inside_present = False;
    for obj in figure:
        if 'inside' in obj['properties'].keys():
            inside_present =  True
        else:
            continue

        return inside_present;

def get_inside_object_two_obj_total(figure):
    for obj in figure:
        if 'inside' in obj['properties'].keys():
            return obj
        else:
            continue

def get_outside_object_two_obj_total(figure):
    for obj in figure:
        if 'inside' in obj['properties'].keys():
            continue
        else:
            return obj

def compare_same_property_object(obj1, obj2):
    differences ={}
    # print(obj1)
    # print(obj2)
    for key in obj1['properties']:
        try:
            if obj1['properties'][key] == obj2['properties'][key]:
                same_properties = 1
                differences[key] = {'same_properties': same_properties, 'differences':''}
            else:
                same_properties = 0
                differences[key] = {'same_properties':same_properties,'differences':{'A': obj1['properties'][key], 'B': obj2['properties'][key]}}
        except:
            differences = False

    return differences
    # print(differences)
    # return differences

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass



    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):

        solvethings=1
        # solvethings
    # 'Basic Problem B-04' in problem.name
        if(solvethings): #TODO add other problems

            def handle_goal(x,differences):

                if (x == 'single_object_no_change'):

                    returned_answer = -1
                    for answer in potential_answers:
                        if(check_if_objects_are_same(figures_C[0],answer[0])):
                            returned_answer = int((answer[0]['figure']))

                    return returned_answer
                elif(x=='single_object_change_single'):

                    differences_A_B = differences

                    attribute_A_B = differences_A_B[0]['differences']['attribute']

                    if(attribute_A_B=='angle'):
                        difference_attribute_A_B = int(differences_A_B[0]['differences']['B'])-int(differences_A_B[0]['differences']['A'])

                    print('-')
                    print(differences_A_B)
                    print('-')

                    for answer in potential_answers:

                        differences_C_and_choice = compare_object_properties(figures_C[0], answer[0])
                        # Reduce differences to only relevant ones
                        relevant_differences_C_and_choice = select_relevant_transformation(differences_C_and_choice)

                        if(len(relevant_differences_C_and_choice)==0):
                            continue
                        attribute_C_choice = relevant_differences_C_and_choice[0]['differences']['attribute']

                        print(relevant_differences_C_and_choice)
                        if(attribute_C_choice=='angle'):
                            difference_attribute_C_choice = int(relevant_differences_C_and_choice[0]['differences']['B']) - int(relevant_differences_C_and_choice[0]['differences']['A'])
                            print(difference_attribute_C_choice)
                            if ((attribute_A_B==attribute_C_choice) and(difference_attribute_A_B==difference_attribute_C_choice)):
                                returned_answer = int((answer[0]['figure']))
                                return returned_answer

                        if(differences_A_B==relevant_differences_C_and_choice):
                            returned_answer = int((answer[0]['figure']))
                            return returned_answer

                    return -1
                elif(x=='two_objects_both_identical'):
                    inside_object_C = get_inside_object_two_obj_total(figures_C)
                    outside_object_C = get_outside_object_two_obj_total(figures_C)

                    print(inside_object_C)
                    print(outside_object_C)

                    answercnt=0
                    for answer in potential_answers:
                        answercnt+=1
                        print(answercnt)
                        choices_inside_object_answer = get_inside_object_two_obj_total(answer)
                        choices_outside_object_answer = get_outside_object_two_obj_total(answer)

                        choices_inside_obj_differences = compare_same_property_object(inside_object_C, choices_inside_object_answer)
                        choices_outside_obj_differences = compare_same_property_object(outside_object_C, choices_outside_object_answer)

                        if(choices_inside_obj_differences==False):
                            continue
                        choices_relevant_inside_obj_differences = select_relevant_transformation(choices_inside_obj_differences)
                        choices_relevant_outside_obj_differences = select_relevant_transformation(choices_outside_obj_differences)

                        print(choices_relevant_inside_obj_differences)
                        print(choices_relevant_outside_obj_differences)

                        if ((len(choices_relevant_outside_obj_differences) == 0) and len(choices_relevant_inside_obj_differences) == 1):
                            print('')
                            attribute_dif = relevant_inside_obj_differences[0]['differences']['attribute']
                            # print(relevant_inside_obj_differences)
                            print(attribute_dif)
                            if (attribute_dif == 'inside'):
                                returned_answer = int((answer[0]['figure']))
                                return returned_answer

                        # try:
                        #     get_inside_object_two_obj_total(answer)

                    return -1
                elif(x=='skip'):
                    returned_answer = -1
                    return returned_answer
                else:
                    return -1


            figures_A = get_object_properties(problem, 'A')
            figures_B = get_object_properties(problem, 'B')
            figures_C = get_object_properties(problem, 'C')
            figures_1 = get_object_properties(problem, '1')
            figures_2 = get_object_properties(problem, '2')
            figures_3 = get_object_properties(problem, '3')
            figures_4 = get_object_properties(problem, '4')
            figures_5 = get_object_properties(problem, '5')
            figures_6 = get_object_properties(problem, '6')

            potential_answers= [figures_1,figures_2,figures_3,figures_4,figures_5,figures_6]

            match_goal = ' '
            differences = {}


            # Check if number of figures are the same
            #     if yes, check if number of properties are the same
            #             if yes, check if values of properties are the same


            # Check number of properties in A; check number of properties in B; if they are equal, transition is  "no change"


            # Compare figures A and B
            # 1. Same number of figures?
            #         if yes: same_num_figures = True
            #         a. only one figure?
            #                 if yes:

            #         b. many figures?
            #                 if yes:
            #                     check_differences_between_figures()
            #                 if no:
            #                     set_objective(find_figure_identical_to_C)

            # 2. Dif number of figures?
            #         same_num_figures = False
            #         i. which figure is missing?
            # 2.
            #


            same_num_figures_A_B = len(figures_A)==len(figures_B)

            # Same number of figures AND 1 figure each
            if((same_num_figures_A_B) and (len(figures_A)==1)):
                # Check if values for any properties are different.
                object_A_and_B_same = check_if_objects_are_same(figures_A[0],figures_B[0])
                if(object_A_and_B_same==True): #If same num of objects, and only 1 object, and those objects are the same
                    match_goal = 'single_object_no_change'
                elif(object_A_and_B_same==False):
                    differences = compare_object_properties(figures_A[0],figures_B[0])
                    differences = select_relevant_transformation(differences)
                    if(len(differences)>1):
                        match_goal = 'single_object_change_multiple'
                    elif(len(differences)==1):
                        match_goal = 'single_object_change_single'
            elif ((same_num_figures_A_B) and (len(figures_A) == 2)):
                num_of_objects = len(figures_A)
                # remember that this implementation is brittle if the order of the objects isn't the same but the objects themselves are!

                one_object_inside_another_A = check_if_object_inside_another(figures_A)
                one_object_inside_another_B = check_if_object_inside_another(figures_B)

                # if both figures have one object inside of another
                if(one_object_inside_another_A and one_object_inside_another_B):

                    inside_object_A = get_inside_object_two_obj_total(figures_A)
                    outside_object_A = get_outside_object_two_obj_total(figures_A)
                    #
                    inside_object_B = get_inside_object_two_obj_total(figures_B)
                    outside_object_B = get_outside_object_two_obj_total(figures_B)

                    #     Check which differences exist between
                    inside_obj_differences = compare_same_property_object(inside_object_A,inside_object_B)
                    outside_obj_differences = compare_same_property_object(outside_object_A, outside_object_B)

                    relevant_inside_obj_differences = select_relevant_transformation(inside_obj_differences)
                    relevant_outside_obj_differences = select_relevant_transformation(outside_obj_differences)

                    if( (len(relevant_outside_obj_differences) ==0) and len(relevant_inside_obj_differences)==1 ):
                        attribute_dif = relevant_inside_obj_differences[0]['differences']['attribute']

                        # print(type(attribute_dif))
                        if(attribute_dif=='inside'):
                            # print('hell yes')
                            match_goal = 'two_objects_both_identical'
                            differences = relevant_inside_obj_differences
                            print(differences)


                    # if(a['properties'])


            print('match goal: '+match_goal)

            selected_choice = handle_goal(match_goal, differences)
            print(selected_choice)
            return selected_choice


        else:
            return -1




