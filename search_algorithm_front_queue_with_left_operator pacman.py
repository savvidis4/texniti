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
import os

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
    return not state[len(state)-1][0]=='p'

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
                    while (k < len(state)):

                        # Άμα το κελί περιέχει φρούτο (f) ή το Pacman,
                        if (state[k][1] == 'f' or state[k][1] == 'd') or state[k][0] == 'p':

                            # Αποθήκευσε την θέση του κελιού στην λίστα θέσεων οντοτήτων.
                            fruits_list.append(k)
                        k += 1

                    # Έλεγχος θέσεως τυχαίου φρούτου για να μην τοποθετηθεί σε κελί με κάποια υπάρχουσα οντότητα.
                    while (random_index in fruits_list):

                        # Αναπαραγωγή τυχαίου αριθμού από το 0 έως το 5 που θα συμβολίζει την θέση ενός κελιού της κατάστασης.
                        random_index = random.randint(0,len(state)-1)

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
        # Σε αυτήν την περίπτωση θα πρέπει ο τελεστής eat να μπεί τελευταίος στην λίστα απογόνων αφού θέλουμε να εκτελεστεί πρώτος (Last In First Out).

        # Τοποθετούμε λοιπόν τους απογόνους στην λίστα.
        if not child_left==None:
            children.append(child_left) 

        if not child_right==None:
            children.append(child_right) 
        
        if not child_eat==None:
            children.append(child_eat)
    
    elif method == 'BFS':

        # Άμα η μέθοδος αναζήτησης είναι η Πρώτα Σε Πλάτος (Breadth First Search) τότε καταλαβαίνουμε ότι η υλοποίηση της πραγματοποιείται με ουρά.
        # Σε αυτήν την περίπτωση θα πρέπει ο τελεστής eat να μπεί πρώτος στην λίστα απογόνων αφού θέλουμε να εκτελεστεί πρώτος (First In First Out).

        # Τοποθετούμε λοιπόν τους απογόνους στην λίστα.
        if not child_eat==None:
            children.append(child_eat) 

        if not child_right==None:
            children.append(child_right) 

        if not child_left==None:
            children.append(child_left)
    
    elif method == 'HCS':

        # Άμα η μέθοδος αναζήτησης είναι η Αναρρίχηση Λόφων (Hill Climbing Search) τότε καταλαβαίνουμε ότι η υλοποίηση της πραγματοποιείται με στοίβα.
        # Σε αυτήν την περίπτωση θα πρέπει ο τελεστής eat να μπεί τελευταίος στην λίστα απογόνων αφού θέλουμε να εκτελεστεί πρώτος (Last In First Out).

        #["['o']_['o']"]

        # Στον συγκεκριμένο ευριστικό αλγόριθμο το κριτήριο ταξινόμησης είναι το πλησιέστερο, στο pacman, φρούτο.
        
        # Αρχικοποίηση λιστών και του δείκτη του pacman
        fruit_indexes = []
        fruit_distances = []
        abs_fruit_distances = []
        pacman_index = 0

        # Επαναληπτική αναζήτηση του pacman στην εκάστοτε κατάσταση
        for i in range(len(state)):

            # Άμα στο κελί βρίσκεται το pacman,
            if state[i][0] == 'p':

                pacman_index = i

        # Επαναληπτική αναζήτηση των φρούτων στην εκάστοτε κατάσταση
        for i in range(len(state)):

            # Άμα στο κελί βρίσκεται φρούτο (δεν είναι κενό καθώς δεν διαφοροποιούμε τα φρούτα μεταξύ τους),
            if state[i][1] != '':

                # Προσθέτουμε στην λίστα δεικτών, τον δείκτη που βρίσκεται το φρούτο
                fruit_indexes.append(i)

                # Προσθέτουμε στην λίστα αποστάσεων, την διαφορά της θέσης του pacman με αυτήν του φρούτου
                fruit_distances.append(pacman_index - i)
        
        # Για καθεμία από τις αποστάσεις που βρήκαμε,
        for i in range(len(fruit_distances)):

            # Περνάμε το απόλυτό τους στην λίστα απόλυτων τιμών αποστάσεων
            abs_fruit_distances.append(abs(fruit_distances[i]))
            
        # Αν η λίστα απόλυτων αποστάσεων δεν είναι κενή (υπάρχουν φρούτα στην τρέχουσα κατάσταση),
        if abs_fruit_distances:

            # Βρίσκουμε την μικρότερη και κρατάμε τον δείκτη της
            min_index  = abs_fruit_distances.index(min(abs_fruit_distances))

            # Καθώς οι λίστες αποστάσεων είναι παράλληλες, χρησιμοποιούμε τον προαναφερόμενο δείκτη για να βρούμε την πραγματική μικρότερη απόσταση. 
            # Αφού η κύρια λίστα αποστάσεων μπορεί να περιέχει και αρνητικούς ακεραίους δεν θα μας επιστρέψει την μικρότερη απόσταση ως προς το σημείο 0 (το pacman).
            
            # Ο διαχωρισμός μεταξύ των τελεστών μετάβασης (για να ξέρουμε πιο μονοπάτι να αποκλείσουμε) γίνεται από το πρόσημο της τιμής της απόστασης του φρούτου.
             
            # Άμα το πρόσημο είναι αρνητικό, τότε το πλησιέστερο στο pacman φρούτο βρίσκεται στα αριστερά. Επομένως προς τα εκεί θα κινηθεί. 
            if (fruit_distances[min_index] < 0):

                # Τοποθετούμε τον απόγονο στην λίστα.
                if not child_right==None:
                    children.append(child_right) 

            # Άμα το πρόσημο είναι θετικό, τότε το πλησιέστερο στο pacman φρούτο βρίσκεται στα δεξιά. Επομένως προς τα εκεί θα κινηθεί. 
            elif (fruit_distances[min_index] > 0):
                
                # Τοποθετούμε τον απόγονο στην λίστα.
                if not child_left==None:
                    children.append(child_left)

        # Αν η λίστα απόλυτων αποστάσεων είναι κενή (δεν υπάρχουν φρούτα στην τρέχουσα κατάσταση) και πρόκειται για τελική κατάσταση, 
        else:

            # Θα πρέπει να φορτώσουμε τους τελευταίους τελεστές μετάβασης (απογόνους) στην λίστα.
            if not child_right==None:
                children.append(child_right) 

            if not child_left==None:
                children.append(child_left)
        
        # Καθώς πρόκειται για στοίβα ο τελεστής eat μπαίνει τελευταίος για να υλοποιηθεί πρώτος.
        if not child_eat==None:
            children.append(child_eat)

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

    # Άμα η front δεν είναι κενή:     
    if front:

        print("Front:")
        print(front)

        # Αφαιρούμε το πρώτο στοιχείο του μετώπου,
        node=front.pop(0)

        # Βάζουμε στην στοίβα με την σειρά τους τελεστές
        for child in find_children(node,method):

            # Αν η μέθοδος είναι η DFS τότε πρέπει οι τελεστές να τοποθετηθούν στην αρχή του μετώπου καθώς πρόκειται στην πραγματικότητα για στοίβα
            if method == 'DFS':
                front.insert(0,child)

            # Αν η μέθοδος είναι η ΒFS τότε πρέπει οι τελεστές να τοποθετηθούν στο τέλος του μετώπου καθώς πρόκειται στην πραγματικότητα για ουρά
            elif method == 'BFS':
                front.append(child)
            
            # Αν η μέθοδος είναι η HCS τότε πρέπει οι τελεστές να τοποθετηθούν στην αρχή του μετώπου καθώς πρόκειται στην πραγματικότητα για στοίβα
            elif method == 'HCS':
                front.insert(0,child)     
    
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

    print("Queue:")
    print(queue)

    # Διαγράφουμε το πρώτο στοιχείο της ουράς
    node=queue.pop(0)
    queue_copy=copy.deepcopy(queue)
    children=find_children(node[-1],method)

    # Βάζουμε με της σειά τους τελεστές μετάβασης
    for child in children:
        path=copy.deepcopy(node)
        path.append(child)

        # Αν η μέθοδος είναι η DFS τότε πρέπει οι τελεστές να τοποθετηθούν στην αρχή της ουράς καθώς πρόκειται στην πραγματικότητα για στοίβα
        if method == 'DFS':
            queue_copy.insert(0,path)

        # Αν η μέθοδος είναι η ΒFS τότε πρέπει οι τελεστές να τοποθετηθούν στο τέλος της ουράς καθώς πρόκειται στην πραγματικότητα για ουρά
        elif method == 'BFS':
            queue_copy.append(path)
        
        # Αν η μέθοδος είναι η HCS τότε πρέπει οι τελεστές να τοποθετηθούν στην αρχή της ουράς καθώς πρόκειται στην πραγματικότητα για στοίβα
        elif method == 'HCS':
            queue_copy.insert(0,path)

    return queue_copy
            
""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""

def walle():

    # Ένα γλυκούλικο ρομπότ καλωσορίσματος
    print('\n')
    print("======GREETINGS TRAVELER======")
    print('  __      _____ ____')
    print(' /---__  ( (O)|/(O) )')
    print('\\ \\ \\ \\/  \\___U\\___/')
    print('    L\\       ||')
    print('     \\\\ ____|||_____')
    print('      \\\\|==|[]__/=|\\--|')
    print('       \\|* ||||\\==|/--|')
    print('    ____| *|[][-- |__')
    print('   ||EEE|__EEEE_[ ]_|EE\\')
    print('   ||EEE|=O      O|=|EEE|')
    print('   \\ LEEE|         \\|EEE|_))')
    print('                          ```')
    print('\n')

def input_method():

    walle()

    # Έλεγχος εγγυρότητας για την επιλογή του χρήστη.
    while True:

        method= input("Which method would you like to implement?\n1) Depth First Search (DFS)\n2) Breadth First Search (BFS)\n3) Hill Climb Search (HCS)\nYour choice (1, 2, 3): ")

        print('\n')

        if method == "1" or method == "2" or method == "3":

            if method == "1":
                method = "DFS"
            elif method == "2":
                method = "BFS"
            elif method == "3":
                method = "HCS"
            
            break
    
    return method

def initial_state_creation():
    
    os.system('clear')
    choice = int("0")

    while int(choice) != 1 and int(choice) != 2:

        choice = input("Would you like a custom initial state or the predefined from the AI Lab one? (1,2): ")
    
    if int(choice) == 2:

        initial_state=[['','d'],['','f'],['p',''],['',''],['','f'],['','']]
        return initial_state

    else:

        cell_number = 0

        while int(cell_number) < 3:
            cell_number = input("State the number of cells you would like the world to be created into (>=3): ")

        fruits = int(cell_number) // 3
        devil_fruit = 1
        pacman = 1

        state = []
        indexes = []

        for i in range (0,int(cell_number)):
            state.append(['',''])

        for i in range (0, fruits + devil_fruit + pacman):

            index = random.randint(0,int(cell_number)-1)

            while index in indexes:
                
                index = random.randint(0,int(cell_number)-1)
            
            indexes.append(index)

        for i in range (0, devil_fruit):

            findex = random.choice(indexes)

            state[findex][1] = 'd'

            indexes.remove(findex)
            
        for i in range (0, fruits):

            findex = random.choice(indexes)

            state[findex][1] = 'f'

            indexes.remove(findex)

        for i in range (0, pacman):

            findex = random.choice(indexes)

            state[findex][0] = 'p'

            indexes.remove(findex)

        print('The state created: ', state)
        
        return state

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

def find_solutions(front, queue, closed, method):

    # Άμα το μέτωπο είναι κενό και δεν υπάρχει κάποιος κόμβος για εξερεύνηση δεν υπάρχει λύση.
    if not front:
        print('No solution')
    
    # Άμα το πρώτο στοιχείο του μετώπου (ο τελεστής) υπάρχει στο closed (έχει εξερευνηθεί), 
    elif front[0] in closed:

        # Θα φτιάξουμε νέα αντίγραφα χωρίς τον ήδη εξερευνημένο τελεστή
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)

        # Και θα ξανατρέξουμε την εύρεση λύσης αναδρομικά
        find_solutions(new_front, new_queue, closed, method)
    
    # Άμα ο τελεστής στο μέτωπο είναι τελική κατάσταση,
    elif is_goal_state(front[0]):

        # Εκτυπώνουμε το κλαδί (το πρώτο στοιχείο της ουράς) στο οποίο βρέθηκε η λύση
        print('This is the solution: ')
        print(queue[0])
    
    # Άμα δεν ισχύει τίποτα από τα παραπάνω,
    else:

        # Βάζουμε στο closed τον πλέον εξερευνημένο κόμβο (τελεστή)
        closed.append(front[0])
        
        # Δημιουργούμε νέα αντίγραφα στα οποία βάζουμε και νέους τελεστές
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)

        # Ξανατρέχουμε αναδρομικά την συνάρτηση με τα καινούργια δεδομένα
        find_solutions(front_children, queue_children, closed_copy, method)

"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""
          
def main():
    
    # Αρχικοποίηση αρχικής κατάστασης
    # initial_state=[['','d'],['','f'],['p',''],['',''],['','f'],['','']]

    initial_state = initial_state_creation()

    method = input_method()
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """

    find_solutions(make_front(initial_state), make_queue(initial_state), [], method)

        
if __name__ == "__main__":
    main()
