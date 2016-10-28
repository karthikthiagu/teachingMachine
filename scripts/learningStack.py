import time

# Class to handle the learning stack
class LearningStack:

    # Initialize the learning stack for a family of ideas
    def __init__(self, family):
        self.stack = []
        self.family = family
        print 'LearningStack for the family of ideas ---%s--- created' % family

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
    def cycleIdea(self):
        self.stack_ = self.stack[1:] + [self.stack[0]]
        self.stack = self.stack_
        print 'cycling the LearningStack, renew engagement with the idea ---%s---' % self.stack[-1]['name']

    # Print the family of ideas
    def printFamily(self):
        for idea in reversed(self.stack):
            print idea['name'], idea['familiarity']

if __name__ == '__main__':
    print 'LearningStack - unit-tests'
    
    dsLS = LearningStack('Data Structures and Algorithms')

    idea = dsLS.createIdea('Growth of Functions')
    idea = dsLS.updateIdea(idea, 'STRANGER')
    dsLS.pushIdea(idea)

    idea = dsLS.createIdea('Binary Search Tree')
    idea = dsLS.updateIdea(idea, 'STRANGER')
    dsLS.pushIdea(idea)   
    dsLS.printFamily()
    
    dsLS.cycleIdea()
    dsLS.printFamily()

