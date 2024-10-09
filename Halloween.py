#SECRET DON'T LOOK
secret = 0
def secret_ending():
    print('The rock breaks down the door. You and your friends escape and call')
    print('the police. A few weeks later, the place gets torn down.')
#Name
name = input("Enter your name: ")
print()
#Intro
print("Greetings " + name + ". So... you and a couple of friends")
print('decide to head to the haunted mansion down the road.')

#First choice of endings
start = input("Are you sure you are ready? (yes or no) ")
#Effect
if start == 'yes':    
    print('')
    print('Alright if you say so.')
    print('')
elif start == 'no':
    print('You run out of there leaving your friends to explore')
    print('the mansion by themselves.')
    exit()
else:
    print('Invalid answer')
#What happens when you go in
print('You and your friends enter the mansion. As soon as you do, the doors shut')
print('behind you. You see a rock on the floor. ')

next_choice = input('Do you throw the rock or explore the mansion? (Rock or Explore)')
#Choose something else
while next_choice == 'Rock':
    print('You threw the rock. Nothing happened')
    next_choice = input('Do you throw the rock or explore the mansion? (Rock or Explore)')
    secret = secret + 1
    if secret == 10:
        secret_ending()
        exit()
#One option
if next_choice == 'Explore':
    print('')
    print('Ok')
    print('')
print('You and you friends go in and look around. Suddenly, you hear erie')
print('noises in the house. You come across two exits. One is small enough')
print('for you but not your friends another exit is big enough for all of')
print('you. Your friends dont see the exits. Which do you take?')
final_decision = input('Which do you take? (Small or Friends)')
#Betryal or friendship?
if final_decision == 'Small':
    print('As you exit, leaving your friends behind, you fall and break your leg.')
    print('You limp home with a feeling of guilt. You never see your friends again')
elif final_decision == 'Friends':
    print('You tell your friends about the exit. You escape together.')
elif final_decision == name:
    #SECRET ENDING!!
    print('You know this is a story, I am impressed. Kudos to you. ')
    narrator = input('Would you like me to end this story?(Yes or No)')
    if narrator == 'No':
        exit()
    elif narrator == 'Yes':
        print('You and your friends were teleported outside, with a handy narrator(me)')
        print('to help them in life.')
    else:
        print('I dont understand.')
        exit()
else:
    print('You have said the wrong thing. You and your friends were trapped in the mansion')
