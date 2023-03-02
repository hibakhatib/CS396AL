### CS396AL 

for assignment 8, I evolved my random 3D creature from A7. Limbs and sensors are randomly removed based on randomly generated values. Weights are also randomly changed. All joints contain motors and every pair of neurons contains synapses. 

There is a motor for every joint but sensors are added randomly with a 50/50 chance for each link upon creation. I basically 'flipped' a coin to decide the body's fate. The blue indicates that the link does not contain sensors while the green indicates that the link does contain a sensor. 

After cloning this repo, run the command "python search.py" in your terminal. The evolution runs and at the end of it, the computer waits for user to hit the enter key in order to show the first robot and then the evolved robot. 

At the joints which connected the limb to the torso, the joint axis was both in the x direction and z direction. By having joints that are up/down and left/right, we are able to emulate hinge joints, like elbows or knees, and allows the body to move in a smoother way. 


A brief video of the expected behavior can be found here: 

5 fitness curves: 


The diagram below (attempts to) explain how brains and bodies are generated in this morphospace, with basic recursion as demonstrated in lecture: 

![IMG_0431](https://user-images.githubusercontent.com/98929421/220260494-29c6a12c-3b37-45d5-a190-75a0d08d7.jpg)


Diagram of some of my planning/ideation:

![IMG_0430](https://user-images.githubusercontent.com/98929421/220260521-d31af8a6-e19c-41f1-848d-6cf28b2b6d97.jpg)



a morphospace describes the range of variation of the morphology of bodies and their structures. In this morphospace, the body will always have a torso and a randomly generated number of legs only on the left and right side of the torso. The legs are always 



TO find out more about this project: 

   This material builds on the MOOC found at this link: https://www.reddit.com/r/ludobots/
   find pyrosim physics engine here: https://github.com/jbongard/pyrosim 
  
   This specific project is not found on the ludobots subreddit but is course material from CS396 Artificial Life taught at Northwestern University by Professor Sam Kriegman. This class aims to contribute to the field of evolutionary robotics. 
