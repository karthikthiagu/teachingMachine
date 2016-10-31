#!/usr/bin/env python
import os
import argparse

from learningStack import LearningStack

families = 'families'

def addFamily(name):
    ls = LearningStack(name)
    jsonfile = os.path.join(families, '_'.join(name.split(' ')) + '.json')
    ls.writeToJSON(jsonfile)

def addIdea(family, name, relationship):
    ls = LearningStack(family)
    jsonfile = os.path.join(families, '_'.join(family.split(' ')) + '.json')
    ls.readFromJSON(jsonfile)
    idea = ls.createIdea(name)
    idea = ls.updateIdea(idea, relationship)
    ls.pushIdea(idea)
    ls.writeToJSON(jsonfile)   

def viewFamily(family):
    ls = LearningStack(family)
    jsonfile = os.path.join(families, '_'.join(family.split(' ')) + '.json')
    ls.readFromJSON(jsonfile)
    print '---------------'
    ls.printFamily()
    print '---------------'

def cycleFamily(family, relationship):
    ls = LearningStack(family)
    jsonfile = os.path.join(families, '_'.join(family.split(' ')) + '.json')
    ls.readFromJSON(jsonfile)   
    ls.cycleIdea(relationship)
    ls.writeToJSON(jsonfile)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', help = 'add a family or an idea')
    parser.add_argument('-n', '--name', help = 'name of family or idea')
    parser.add_argument('-f', '--family', help = 'name of family if you are entering an idea')
    parser.add_argument('-r', '--relationship', help = 'relationship with the idea, if you are entering an idea')
    parser.add_argument('-v', '--view', help = 'view the learning stack', default = 'NULL')
    parser.add_argument('-c', '--cycle', help = 'cycle the learning stack', default = 'NULL')
    args = vars(parser.parse_args())

    if args['add'] == 'family':
        addFamily(args['name'])
        exit()
    if args['add'] == 'idea':
        addIdea(args['family'], args['name'], args['relationship'])
        exit()
    if args['view'] != 'NULL':
        viewFamily(args['view'])
        exit()
    if args['cycle'] != 'NULL':
        cycleFamily(args['cycle'], args['relationship'])
        exit()

