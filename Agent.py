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


        if('Basic Problem B-01' in problem.name): #TODO generalize to more problems

            object_a = {}
            object_b = {}
            object_c = {}
            object_d = {}

            print('\n\n\n')
            print(problem.name)
            print(problem.problemType)
            print(problem.problemSetName)




            choices = ['1','2','3','4','5','6']
            original_objects = ['A','B']
            new_object= 'C'


            # for choice in choices:
            #     print(choice+':')
            #     pp.pprint(problem.figures[choice].objects.keys())
            #     print('\n')

            pp.pprint(problem.figures['B'].objects['b'].name)
            pp.pprint(problem.figures['B'].objects['b'].attributes)

            pp.pprint(problem.figures['A'].objects['a'].name)
            pp.pprint(problem.figures['A'].objects['a'].attributes)

            a_attributes


            # for fig in problem.figures.keys():
            #     print(fig)

            # print(problem.figures['A'].keys())
            # print(problem.figures['A'].name)
            # print(problem.figures['A'].objects)
            # print(problem.figures['A'].visualFilename)
            #
            # relevant_key = problem.figures['A'].objects.keys()
            #
            # print(problem.figures['A'].objects['a'].attributes)
            #
            # all_figures = list(problem.figures.keys())
            #
            # for fig in all_figures:
            #     problem.figures





            # pp.pprint(inspect.getmembers(problem, lambda a: not (inspect.isroutine(a))))
            # for key in problem.figures:
            #     print(key.keys())



            return -1

        else:
            return -1



