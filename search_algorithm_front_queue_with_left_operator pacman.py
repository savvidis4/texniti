""" ----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front and extending queue)
******** author:  AI lab
********
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
******** (επέκταση μετώπου και διαχείριση ουράς)
******** Συγγραφέας: Εργαστήριο ΤΝ
"""

import random
import copy

import sys 
sys.setrecursionlimit(10**6) 

""" Helper functions for checking operator's conditions """

# Έλεγχος για το αν μπορεί το Pacman να φάει στο κελί που βρίσκεται.
def can_eat(state):

    # Σειριακή αναζήτηση σε όλη την υπάρχουσα κατάσταση.
    for i in range(len(state)):

        # Άμα στο κελί βρίσκεται το Pacman,
        if state[i][0] == 'p':

            # Αν υπάρχει είτε καλό είτε κακό φρούτο,
            if state[i][1] == 'f' or state[i][1] == 'd':

                # Μπορεί να φάει το εκάστοτε φρούτο.
                return True
    
    # Δεν υπάρχει φρούτο στο κελί που βρίσκεται το Pacman οπότε δεν μπορείς να φάει.
    return False
      
# Έλεγχος για το αν μπορεί το Pacman να κουνηθεί ένα βήμα δεξιά.
def can_move_right(state):

    # Άμα δεν βρίσκεται το Pacman στο τελευταίο κελί της υπάρχουσας κατάστασης τότε μπορεί.
    return not state[5][0]=='p'

# Έλεγχος για το αν μπορεί το Pacman να κουνηθεί ένα βήμα αριστερά.
def can_move_left(state):

    # Άμα δεν βρίσκεται το Pacman στο πρώτο κελί της υπάρχουσας κατάστασης τότε μπορεί.
    return not state[0][0]=='p'


""" Operator function: eat, move right, move left """

# Τελεστής eat.
def eat(state):

    # Αν το Pacman μπορεί να φάει,
    if can_eat(state):

        # Αρχικοποίηση κενής λίστας θέσεως των φρούτων και ενός μετρητή.
        fruits_list = []
        k = 0
        random_index = 0

        # Σειριακή αναζήτηση του κελιού που βρίσκεται το Pacman στην τρέχουσα κατάσταση.
        for i in range(len(state)):

            # Άμα το Pacman βρεθεί,
            if state[i][0] == 'p':

                # Άμα το φρούτο είναι καλό φρούτο,
                if state[i][1] == 'f':

                    # Φάε το φρούτο (εξαφάνισέ το).
                    state[i][1] = ''
                
                # Άμα το φρούτο είναι κακό φρούτο,
                elif state[i][1] == 'd':

                    # Κατάστρεψε το φρούτο (εξαφάνισέ το),
                    state[i][1] = ''

                    # Σειριακή αναζήτηση οντοτήτων στην τρέχουσα κατάσταση.
                    while (k < 6):

                        # Άμα το κελί περιέχει φρούτο (f) ή το Pacman,
                        if (state[k][1] == 'f' or state[k][1] == 'd') or state[k][0] == 'p':

                            # Αποθήκευσε την θέση του κελιού στην λίστα θέσεων οντοτήτων.
                            fruits_list.append(k)
                        k += 1

                    # Έλεγχος θέσεως τυχαίου φρούτου για να μην τοποθετηθεί σε κελί με κάποια υπάρχουσα οντότητα.
                    while (random_index in fruits_list):

                        # Αναπαραγωγή τυχαίου αριθμού από το 0 έως το 5 που θα συμβολίζει την θέση ενός κελιού της κατάστασης.
                        random_index = random.randint(0,5)

                    # Αφού ο τυχαίος "δείκτης" δεν αντιστοιχεί σε κελί με οντότητα, βάλε στο κελί που δείχνει ένα νέο φρούτο.
                    state[random_index][1] = 'f'
        
        # Επιστροφή κατάστασης μετά το φάγωμα ενός φρούτου.
        return state
    
    # Άμα δεν υπάρχει φρούτο και το Pacman δεν μπορεί να φάει επιστρέφουμε Κενό (None).
    return None
    
# Τελεστής move_right. 
def move_right(state):

    # Άμα το Pacman μπορεί να κουνηθεί μία θέση δεξιά,
    if can_move_right(state):

        # Σειριακή αναζήτηση του Pacman στην τρέχουσα κατάσταση.
        for i in range(len(state)):

            # Άμα βρήκαμε το Pacman
            if state[i][0]=='p':

                # Βγάλτο από το κελί του,
                state[i][0]=''

                # και μετέφερε το στο επόμενο στα δεξιά.
                state[i+1][0]='p'

                # Επέστρεψε την τρέχουσα κατάσταση μετά την μετακίνηση του Pacman.
                return state

    # Άμα δεν μπορεί να κουνηθεί δεξιά (π.χ. διότι έχει πετύχει "τοίχο") επιστρέφουμε Κενό (None).
    return None
    

# Τελεστής move_left.
def move_left(state):

    # Άμα το Pacman μπορεί να κουνηθεί μία θέση αριστερά,
    if can_move_left(state):

        # Σειριακή αναζήτηση του Pacman στην τρέχουσα κατάσταση.
        for i in range(len(state)):

            # Άμα βρήκαμε το Pacman
            if state[i][0]=='p':

                # Βγάλτο από το κελί του,
                state[i][0]=''

                # και μετέφερε το στο επόμενο στα αριστερά.
                state[i-1][0]='p'

                # Επέστρεψε την τρέχουσα κατάσταση μετά την μετακίνηση του Pacman.
                return state

    # Άμα δεν μπορεί να κουνηθεί δεξιά (π.χ. διότι έχει πετύχει "τοίχο") επιστρέφουμε Κενό (None). 
    return None


""" Function that checks if current state is a goal state """

# Έλεγχος άμα η τρέχουσα κατάσταση είναι τελική.
def is_goal_state(state):

    # Για να είναι μία κατάσταση τελική θα πρέπει να μήν υπάρχει ΚΑΜΙΑ άλλη οντότητα εκτός του Pacman.
    for cell in state:

        # Κοινώς ελέγχουμε όλο τον κόσμο του προβλήματος για το αν υπάρχουν φρούτα (δηλητηριώδη και μη).
        if cell[1] != '':

            # Άμα βρεθεί φρούτο, επιστρέφουμε πως η κατάσταση ΔΕΝ είναι τελική.
            return False
    
    # Άμα δεν βρεθεί φρούτο επιστρέφουμε το Ο.Κ.
    return True

    

""" Function that finds the children of current state """

# Συνάρτηση εύρεσης απογόνων.
def find_children(state, method):

    # Αρικοποίηση λίστας απογόνων
    children=[]
    
    # Δημιουργία αντιγράφων της τρέχουσας κατάστασης. 
    eat_state=copy.deepcopy(state)
    left_state=copy.deepcopy(state)
    right_state=copy.deepcopy(state)

    # Δημιουργία απογόνων με βάση τους τελεστές κατάστασης.
    child_eat=eat(eat_state)
    child_left=move_left(left_state)
    child_right=move_right(right_state)

    # Καθώς ο κόσμος του προβλήματος είναι ο συγκεκριμένος έχουμε κάποιους περιορισμούς για την σειρά προτεραιότητας των απογόνων μέσα στην λίστα.
    # Δηλαδή άμα το Pacman βρεθεί σε ίδιο κελί με φρούτο, πρέπει ΠΡΩΤΑ να το φάει και ύστερα να κουνηθεί.
    # Δεν επιτρέπεται να το προσπεράσει και να επιστρέψει να το φάει αργότερα.

    # Για αυτόν τον λόγο η σειρά με την οποία θα βάλουμε τους απογόνους στην λίστα απογόνων διαφέρει από μέθοδο σε μέθοδο.

    if method == 'DFS':

        # Άμα η μέθοδος αναζήτησης είναι η Πρώτα Σε Βάθος (Depth First Search) τότε καταλαβαίνουμε ότι η υλοποίηση της πραγματοποιείται με στοίβα.
        # Σε αυτήν την περίπτωση θα πρέπει το τελεστής eat να μπεί τελευταίος στην λίστα απογόνων αφού θέλουμε να εκτελεστεί πρώτος (Last In First Out).

        # Τοποθετούμε λοιπόν τους απογόνους στην λίστα.
        if not child_left==None:
            children.append(child_left) 

        if not child_right==None:
            children.append(child_right) 
        
        if not child_eat==None:
            children.append(child_eat)
    
    elif method == 'BFS':

        # Άμα η μέθοδος αναζήτησης είναι η Πρώτα Σε Πλάτος (Breadth First Search) τότε καταλαβαίνουμε ότι η υλοποίηση της πραγματοποιείται με ουρά.
        # Σε αυτήν την περίπτωση θα πρέπει το τελεστής eat να μπεί πρώτος στην λίστα απογόνων αφού θέλουμε να εκτελεστεί πρώτος (First In First Out).

        # Τοποθετούμε λοιπόν τους απογόνους στην λίστα.
        if not child_eat==None:
            children.append(child_eat) 

        if not child_right==None:
            children.append(child_right) 

        if not child_left==None:
            children.append(child_left)

    # Επιστρέφουμε την λίστα απογόνων.
    return children


""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]

""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""

def expand_front(front, method):  

    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node,method):     
                front.insert(0,child)

    
    elif method=='BFS':
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node,method):     
                front.append(child)
    
    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front

""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση ουράς
"""

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""

def make_queue(state):
    return [[state]]

""" ----------------------------------------------------------------------------
**** expanding queue
**** επέκταση ουράς
"""

def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1],method)
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    
    elif method=='BFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1],method)
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)
    #elif method=='BestFS':
    #else: "other methods to be added" 
    
    return queue_copy
            
""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""
def find_solutions(front, queue, closed, method,counter):
    counter+=1
    if not front:
        print('No solution')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solutions(new_front, new_queue, closed, method, counter)
    
    elif is_goal_state(front[0]):
        print('This is the solution in',counter,' steps: ')
        print(queue[0])
    
    else:
        closed.append(front[0])
        with open('6cells_closed.txt','w') as f:
            f.write(str(closed) + '\n')
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solutions(front_children, queue_children, closed_copy, method, counter)



"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""
          
def main():
    
    initial_state=[['','d'],['','f'],['p',''],['',''],['','f'],['','']]
    """ ----------------------------------------------------------------------------
    **** πρέπει να οριστεί η is_goal_state, καθώς δεν είναι μόνο μια η τελική κατάσταση
    """
    counter = 0
    method='DFS'
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    find_solutions(make_front(initial_state), make_queue(initial_state), [], method, counter)

        
if __name__ == "__main__":
    main()
