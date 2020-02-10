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
import numpy as np

pp = pprint.PrettyPrinter(indent=4)

bonus_properties_list = ['angle','inside','alignment','above']
standard_properties_list = ['shape','fill','size']

class makeFigure:
    def __init__(self, figure, name, properties):
        self.figure = figure
        self.name = name
        self.properties = properties
        self.properties_list = sorted(list(properties.keys()))
        self.properties_list_bonus =  sorted([key for key in properties.keys() if(key in bonus_properties_list)])
        self.properties_list_standard = sorted(standard_properties_list)
        self.meta_obj_name = name
        self.meta_fig_name = figure


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


# REFORMATTING CODE!!!
def how_many_object_in_figure(fig):
    return len(fig)
    # print(fig)

def compare_objects(obj1, obj2):

    object_identical = True
    same_properties = True
    exclusive_properties = False

    difference_object={}

    list_of_differences_for_same_properties=[]

    obj_1_exclusive_properties = []
    obj_2_exclusive_properties = []



    # Check if keys, when sorted, are the same
    if(sorted(obj1['properties_list']) == sorted(obj2['properties_list'])):

        # If keys are the same, check differences in values
        for key in obj1['properties_list']:
            # If values are the same for each key, maintain default value of "these two objects are the same"
            if(obj1['properties'][key]==obj2['properties'][key]):
                continue

            # If values differ for a key, list the differences between these objects
            else:
                object_identical = False

                property_dif = {}
                property_dif['property']=key
                property_dif['obj_1_value']= obj1['properties'][key]
                property_dif['obj_2_value'] = obj2['properties'][key]
                list_of_differences_for_same_properties.append(property_dif)
                del property_dif


    # # If keys are different in some way:
    else:
        same_properties = False
        object_identical = False

        # Check which key is present in object 1 that's not present in object 2
        for key in obj1['properties_list']:
            if(key in obj2['properties_list']):
                continue
            else:
                obj1_exclusive_property = {}
                obj1_exclusive_property['property'] = key
                obj1_exclusive_property['value'] = obj1['properties'][key]


                obj_1_exclusive_properties.append(obj1_exclusive_property)

                del obj1_exclusive_property

        # Check which key is present in object 2 that's not present in object 1

        for key in obj2['properties_list']:
            if (key in obj1['properties_list']):
                continue
            else:
                obj2_exclusive_property = {}
                obj2_exclusive_property['property'] = key
                obj2_exclusive_property['value'] = obj2['properties'][key]

                obj_2_exclusive_properties.append(obj2_exclusive_property)

                del obj2_exclusive_property

    difference_object['object_identical']=object_identical
    difference_object['same_properties'] = same_properties
    difference_object['same_property_differences']=list_of_differences_for_same_properties
    difference_object['num_same_property_differences'] = len(list_of_differences_for_same_properties)
    difference_object['obj_1_exclusive_properties']=obj_1_exclusive_properties
    difference_object['obj_2_exclusive_properties'] = obj_2_exclusive_properties

    return difference_object


def getAngleDifference(ang):
    if (ang < -180):
        # print(ang + 360)
        ang + 360
    else:
        # print(ang)
        return ang

def check_if_all_but_names_are_same(fig1,fig2):
    stripped_figure_1 = []
    stripped_figure_2 = []

    for obj in fig1:
        stripped_obj = {}
        stripped_obj['properties'] = obj['properties']
        stripped_obj['properties_list'] = obj['properties_list']
        stripped_obj['properties_list_bonus'] = obj['properties_list_bonus']
        stripped_obj['properties_list_standard'] = obj['properties_list_standard']

        if ('inside' in stripped_obj['properties_list_bonus']):
            stripped_obj['properties']['inside'] = 'same_object'
        elif ('above' in stripped_obj['properties_list_bonus']):
            stripped_obj['properties']['above'] = 'same_object'

        stripped_figure_1.append(stripped_obj)
        del stripped_obj

    for obj in fig2:
        stripped_obj = {}
        stripped_obj['properties'] = obj['properties']
        stripped_obj['properties_list'] = obj['properties_list']
        stripped_obj['properties_list_bonus'] = obj['properties_list_bonus']
        stripped_obj['properties_list_standard'] = obj['properties_list_standard']

        if('inside' in stripped_obj['properties_list_bonus']):
            stripped_obj['properties']['inside']='same_object'
        elif('above' in stripped_obj['properties_list_bonus']):
            stripped_obj['properties']['above']='same_object'

        stripped_figure_2.append(stripped_obj)
        del stripped_obj



    # print('FIGURE 1')
    # pp.pprint(stripped_figure_1)
    # print('\n')
    #
    # print('FIGURE 2')
    # pp.pprint(stripped_figure_2)
    # print('\n')
    #
    # print('figure 1')
    # pp.pprint(sorted(stripped_figure_1, key = lambda i: i['properties_list']))
    #
    # print('figure 2')
    # pp.pprint(sorted(stripped_figure_2, key=lambda i: i['properties_list']))

    # Compare the lists, but only in order!
    same_figures= sorted(stripped_figure_1, key = lambda i: i['properties_list'])==sorted(stripped_figure_2, key = lambda i: i['properties_list'])
    return same_figures

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
    # 'Basic Problem B-0' in problem.name
        if(solvethings): #TODO add other problems
            print(problem.name)

            def handle_differences_one_object(dif_A_B, dif_A_C):

                pp.pprint(dif_A_B)
                pp.pprint(dif_A_C)
                # If same object in figures A, B, and C (i.e., all objects the same)
                if((dif_A_B['object_identical']==True) and (dif_A_C['object_identical']==True)):
                    for choice in potential_answers:
                        dif_C_choice =  compare_objects(figures_C[0],choice[0])
                        if((dif_C_choice==dif_A_B) and (dif_C_choice==dif_A_C)):
                            answer = choice[0]['meta_fig_name']
                            print('answer is: '+answer )
                            return int(answer)

                # If there's a difference between figures A and B, but not A and C (horizontal difference, vertically the same)
                elif((dif_A_B['object_identical']==False) and (dif_A_C['object_identical']==True) and ( dif_A_B['same_properties']==True)):

                    if(dif_A_B['num_same_property_differences']==1):
                        differing_property = dif_A_B['same_property_differences']

                        for choice in potential_answers:
                            dif_C_1 = compare_objects(figures_C[0], choice[0])
                            if(dif_C_1==dif_A_B):
                                answer = choice[0]['meta_fig_name']
                                print('answer is: ' + answer)
                                return int(answer)

                # # If there's a differences between figures A and C, but not A and B (vertical different, horizontally the same), and if difference is only in values
                elif((dif_A_B['object_identical']==True) and (dif_A_C['object_identical']==False) and (dif_A_C['same_properties']==True)):
                    if (dif_A_C['num_same_property_differences'] == 1):
                        for choice in potential_answers:
                            dif_B_1 = compare_objects(figures_B[0], choice[0])
                            if(dif_B_1==dif_A_C):
                                answer = choice[0]['meta_fig_name']
                                print('answer is: ' + answer)
                                return int(answer)
                #
                # If there's a difference between both A and B AND A and C (vertical AND horizontal difference), and if difference is only in values
                elif ((dif_A_B['object_identical'] == False) and (dif_A_C['object_identical'] == False) and (dif_A_B['same_properties'] == True) and (dif_A_C['same_properties'] == True)):

                    if (dif_A_B['num_same_property_differences'] == 1 and dif_A_C['num_same_property_differences'] == 1):
                        for choice in potential_answers:

                            dif_B_choice = compare_objects(figures_B[0], choice[0])
                            dif_C_choice = compare_objects(figures_C[0], choice[0])

                            # Since we know there's a difference between BOTHA and B (horizontal ) and A and C (vertical) already,
                            # we can ignore all answer choices that have no differences between B and the choice, or C and the choice.

                            if(len(dif_B_choice['same_property_differences'])==0):
                                continue
                            if (len(dif_C_choice['same_property_differences']) == 0):
                                continue

                            # Vertical
                            relevant_dif_B_choice = dif_B_choice['same_property_differences'][0]['property']

                            # Horizontal
                            relevant_dif_C_choice = dif_C_choice['same_property_differences'][0]['property']
                            # pp.pprint(dif_B_choice)
                            # pp.pprint(dif_C_choice)


                            # print('horizontal: A vs. B')
                            # pp.pprint(dif_A_B)
                            # print('horizontal: C vs. Choice')
                            # pp.pprint(dif_C_choice)
                            #
                            # print('vertical: A vs. C')
                            # pp.pprint(dif_A_C)
                            # print('vertical: B vs. Choice')
                            # pp.pprint(dif_B_choice)

                            if ((dif_C_choice == dif_A_B) and (dif_B_choice==dif_A_C)):
                                answer = choice[0]['meta_fig_name']
                                print('answer is: ' + answer)
                                return int(answer)
                            elif((relevant_dif_B_choice==relevant_dif_C_choice) and (relevant_dif_C_choice=='angle') ):

                                all_obj_2_values=[int(dif_A_B['same_property_differences'][0]['obj_2_value']),
                                                  int(dif_A_B['same_property_differences'][0]['obj_1_value']),
                                                  int(dif_A_C['same_property_differences'][0]['obj_2_value'])
                                                  ]

                                angle_dif_A_B = int(dif_A_B['same_property_differences'][0]['obj_2_value']) - int(dif_A_B['same_property_differences'][0]['obj_1_value'])
                                angle_dif_A_C = int(dif_A_C['same_property_differences'][0]['obj_2_value']) - int(dif_A_C['same_property_differences'][0]['obj_1_value'])
                                angle_dif_C_choice = int(dif_C_choice['same_property_differences'][0]['obj_2_value']) - int(dif_C_choice['same_property_differences'][0]['obj_1_value'])
                                angle_dif_B_choice = int(dif_B_choice['same_property_differences'][0]['obj_2_value']) - int(dif_B_choice['same_property_differences'][0]['obj_1_value'])

                                ag_dif_ab = (angle_dif_A_B + 180) % 360 - 180
                                ag_dif_ac = (angle_dif_A_C + 180) % 360 - 180
                                ag_dif_c_choice = (angle_dif_A_C + 180) % 360 - 180
                                ag_dif_b_choice = (angle_dif_B_choice + 180) % 360 - 180


                                value_not_already_in_figures = False
                                if(int(choice[0]['properties']['angle']) in all_obj_2_values):
                                    continue
                                else:
                                    value_not_already_in_figures = True

                                all_absolute_values_same = np.absolute(ag_dif_ab) == np.absolute(ag_dif_ac) == np.absolute(ag_dif_c_choice) == np.absolute(ag_dif_b_choice)

                                if(all_absolute_values_same and value_not_already_in_figures):
                                    answer = choice[0]['meta_fig_name']
                                    print('answer is: ' + answer)
                                    return int(answer)
                    elif (dif_A_B['num_same_property_differences'] > 1 or dif_A_C['num_same_property_differences'] > 1):
                        for choice in potential_answers:

                            dif_B_choice = compare_objects(figures_B[0], choice[0])
                            dif_C_choice = compare_objects(figures_C[0], choice[0])

                            if((dif_A_B['num_same_property_differences']==dif_C_choice['num_same_property_differences']) and (dif_A_C['num_same_property_differences']==dif_B_choice['num_same_property_differences'])):
                                print('nice')
                                answer = choice[0]['meta_fig_name']
                                print('answer is: ' + answer)
                                return int(answer)

                            # pp.pprint(dif_B_choice)
                            # pp.pprint(dif_C_choice)
                else:
                    return -1

            def handle_differences_two_objects(differences):
                if(differences=='identical_objects'):
                    for choice in potential_answers:
                        same_objects_in_A_choice = check_if_all_but_names_are_same(figures_A, choice)

                        if(same_objects_in_A_choice):
                            answer = choice[0]['meta_fig_name']
                            print('answer is: ' + answer)
                            return int(answer)

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

                    # print('-')
                    # print(differences_A_B)
                    # print('-')

                    for answer in potential_answers:

                        differences_C_and_choice = compare_object_properties(figures_C[0], answer[0])
                        # Reduce differences to only relevant ones
                        relevant_differences_C_and_choice = select_relevant_transformation(differences_C_and_choice)

                        if(len(relevant_differences_C_and_choice)==0):
                            continue
                        attribute_C_choice = relevant_differences_C_and_choice[0]['differences']['attribute']

                        # print(relevant_differences_C_and_choice)
                        if(attribute_C_choice=='angle'):
                            difference_attribute_C_choice = int(relevant_differences_C_and_choice[0]['differences']['B']) - int(relevant_differences_C_and_choice[0]['differences']['A'])
                            # print(difference_attribute_C_choice)
                            if ((attribute_A_B==attribute_C_choice) and(np.absolute(difference_attribute_A_B)==np.absolute(difference_attribute_C_choice))):
                                returned_answer = int((answer[0]['figure']))
                                return returned_answer

                        if(differences_A_B==relevant_differences_C_and_choice):
                            returned_answer = int((answer[0]['figure']))
                            return returned_answer

                    return -1
                elif(x=='two_objects_both_identical'):
                    inside_object_C = get_inside_object_two_obj_total(figures_C)
                    outside_object_C = get_outside_object_two_obj_total(figures_C)

                    # print(inside_object_C)
                    # print(outside_object_C)

                    answercnt=0
                    for answer in potential_answers:
                        answercnt+=1
                        # print(answercnt)
                        choices_inside_object_answer = get_inside_object_two_obj_total(answer)
                        choices_outside_object_answer = get_outside_object_two_obj_total(answer)

                        choices_inside_obj_differences = compare_same_property_object(inside_object_C, choices_inside_object_answer)
                        choices_outside_obj_differences = compare_same_property_object(outside_object_C, choices_outside_object_answer)

                        if(choices_inside_obj_differences==False):
                            continue
                        choices_relevant_inside_obj_differences = select_relevant_transformation(choices_inside_obj_differences)
                        choices_relevant_outside_obj_differences = select_relevant_transformation(choices_outside_obj_differences)

                        # print(choices_relevant_inside_obj_differences)
                        # print(choices_relevant_outside_obj_differences)

                        if ((len(choices_relevant_outside_obj_differences) == 0) and len(choices_relevant_inside_obj_differences) == 1):
                            # print('')
                            attribute_dif = relevant_inside_obj_differences[0]['differences']['attribute']
                            # print(relevant_inside_obj_differences)
                            # print(attribute_dif)
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

            # Lengths of answers
            length_fig_A = how_many_object_in_figure(figures_A)
            length_fig_B = how_many_object_in_figure(figures_B)
            length_fig_C = how_many_object_in_figure(figures_C)
            length_fig_1 = how_many_object_in_figure(figures_1)
            length_fig_2 = how_many_object_in_figure(figures_2)
            length_fig_3 = how_many_object_in_figure(figures_3)
            length_fig_4 = how_many_object_in_figure(figures_4)
            length_fig_5 = how_many_object_in_figure(figures_5)
            length_fig_6 = how_many_object_in_figure(figures_6)

            # Checking if number of figures
            same_num_figures_A_B = length_fig_A == length_fig_B
            same_num_figures_A_C = length_fig_A == length_fig_C

            # If same number of figures in A-B, A-C dyads AND that number is 1
            if((same_num_figures_A_B) and (same_num_figures_A_B) and (length_fig_A==1)):
                # print('\n\n')
                # print('Difference between A and B:')
                difference_A_B = compare_objects(figures_A[0], figures_B[0])
                # pp.pprint(difference_A_B)
                # print('\n')
                # print('Difference between A and C:')
                difference_A_C = compare_objects(figures_A[0], figures_C[0])
                # pp.pprint(difference_A_C)
                # print('\n')

                test_return_val = handle_differences_one_object(difference_A_B, difference_A_C)
                if(test_return_val is None):
                    test_return_val=-1
                return test_return_val

            elif ((same_num_figures_A_B) and (same_num_figures_A_B) and (length_fig_A == 2)):

                same_objects_in_A_B = check_if_all_but_names_are_same(figures_A,figures_B)
                same_objects_in_A_C = check_if_all_but_names_are_same(figures_A, figures_C)

                if(same_objects_in_A_B and same_objects_in_A_C):
                    test_return_val = handle_differences_two_objects('identical_objects')
                    if (test_return_val is None):
                        test_return_val = -1
                    return test_return_val

                # pp.pprint(figures_A)
            # elif((not same_num_figures_A_B) or (not same_num_figures_A_C)):
            #     for fig in figures_A:
            #         print(fig['properties_list_bonus'])
                 # (test_return_val is None):
                 #    test_return_val = -1
                # return test_return_val






            # QA checks
            # check_problem_list = ['B-01', 'B-03', 'B-04', 'B-05', 'B-07', 'B-09']
            #
            # for prob in check_problem_list:
            #     if(prob in problem.name):
            #         compare_objects(figures_A[0],figures_B[0])



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
                            # print(differences)


                    # if(a['properties'])


            # print('match goal: '+match_goal)

            selected_choice = handle_goal(match_goal, differences)
            # print(selected_choice)
            return selected_choice


        else:
            return -1




