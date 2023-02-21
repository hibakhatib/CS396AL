### CS396AL 

For assignment 7, we created 3D bodies. In accordance to assignment details, all joints contain motors and every pair of neurons contains synpases.

There is a motor for every joint but sensors are added randomly with a 50/50 chance for each link upon creation. I basically 'flipped' a coin to decide the body's fate. The blue indicates that the link does not contain sensors while the green indicates that the link does contain a sensor. 

After cloning this repo, run the command "python search.py" in your terminal to see a new body. 
Run the command everytime you wish to view a new body. All bodies should have a main torso or abdomen with a series of limbs which act as legs. 

At the joints which connected the limb to the torso, the joint axis was both in the x direction and z direction. By having joints that are up/down and left/right, we are able to emulate hinge joints, like elbows or knees, and allows the body to move in a smoother way. 


A brief video of the expected behavior can be found here: https://youtu.be/Qu6ia1WaUcQ

The clip shows the initial generation of random sized boxes at random positions, often overlapping and crowding. Eventually I repurposed old my hexapod to create a cleaner body with a random number of legs at positions which don't overlap. 

The diagram below (attempts to) explain how brains and bodies are generated in this morphospace, with basic recursion as demonstrated in lecture: 

![IMG_0431](https://user-images.githubusercontent.com/98929421/220260494-29c6a12c-3b37-45d5-a190-75a0d08d7.jpg)


Diagram of some of my planning/ideation:

![IMG_0430](https://user-images.githubusercontent.com/98929421/220260521-d31af8a6-e19c-41f1-848d-6cf28b2b6d97.jpg)



a morphospace describes the range of variation of the morphology of bodies and their structures. 

Additionally, here is a gif of the best result from my trials (which honestly were not many 😬)

![a7](https://user-images.githubusercontent.com/98929421/220257729-8bc0220b-6534-4b97-a6be-4038cafe569b.gif)


TO find out more about this project: 

   This material builds on the MOOC found at this link: https://www.reddit.com/r/ludobots/
   find pyrosim here: https://github.com/jbongard/pyrosim 
  
   This specific project is not found on the ludobots subreddit but is course material from CS396 Artificial Life taught at Northwestern University by Professor Sam Kriegman. This class aims to contribute to the field of evolutionary robotics. 
