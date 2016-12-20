import time
import json

# Class to handle the learning stack
class LearningStack:

    # Initialize the learning stack for a family of ideas
    def __init__(self, family):
        self.stack = []
        self.family = family

    # Create an idea-template
    def createIdea(self, idea):
        idea = dict({'name' : idea, 'familiarity' : 'STRANGER', 'meetings' : 0, 'meeting_times' : [], 'interactions' : []})
        print 'decided to meet the idea ---%s---' % idea['name']
        return idea
    
    # Update the idea post this meeting
    def updateIdea(self, idea, familiarity):
        idea['familiarity'] = familiarity
        idea['meetings'] += 1
        meeting_time = time.time()
        idea['meeting_times'].append(meeting_time)
        print 'updated relationship with idea ---%s---' % idea['name']
        return idea

    # Push idea on to the stack
    def pushIdea(self, idea):
        self.stack.append(idea)
        print 'meeting with idea ---%s--- ended, preparing for next idea' % idea['name']
    
    # Cycle the stack
    def cycleIdea(self, familiarity):
        self.stack_ = self.stack[1:] + [self.stack[0]]
        self.stack = self.stack_
        self.updateIdea(self.stack[-1], familiarity)
        print 'cycling the LearningStack, renew engagement with the idea ---%s---' % self.stack[-1]['name']

    # Print the family of ideas
    def printFamily(self):
        for idea in reversed(self.stack):
            print idea['name'], idea['familiarity']

    # Store state in JSON
    def writeToJSON(self, jsonfile):
        print 'writing the contents of learning stack to json'
        jsonfile = open(jsonfile, 'w')
        json.dump({self.family : self.stack}, jsonfile)

    # Read from JSON
    def readFromJSON(self, jsonfile):
        print 'reading contents into the learning stack'
        jsonfile = open(jsonfile, 'r')
        family_stack = json.load(jsonfile)
        self.family = family_stack.keys()[0]
        self.stack = family_stack[self.family]

    def makeNULL(self):
        print 'emptying the learning stack'
        self.family = 'NULL'
        self.stack  = []

if __name__ == '__main__':
    print 'LearningStack - unit-tests'
   
    # Create a family of ideas --- DSA in this case
    dsLS = LearningStack('Data Structures and Algorithms')

    # Create a template for an idea
    idea = dsLS.createIdea('Growth of Functions')
    # Update the idea after meeting it
    idea = dsLS.updateIdea(idea, 'STRANGER')
    # Push the idea onto the stack
    dsLS.pushIdea(idea)

    # Push one more idea onto the stack
    idea = dsLS.createIdea('Binary Search Tree')
    idea = dsLS.updateIdea(idea, 'STRANGER')
    dsLS.pushIdea(idea)   

    # Print the learning stack as it currently appears
    dsLS.printFamily()
    
    # Cycle the ideas, the one at the bottom comes to the top
    dsLS.cycleIdea('STRANGER')

    # Print the learning stack to see how it looks
    dsLS.printFamily()

    # Write results to json-file
    dsLS.writeToJSON('test.json')

    # Make stack null
    dsLS.makeNULL()

    # Read results from json-file
    dsLS.readFromJSON('test.json')
    dsLS.printFamily()  

