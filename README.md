# DesignObject
A design object is an object used to represent a collection of shapes in a 2D coordinate system. A shape is a rectangle object and includes information about where they lie within the parent design object with respect to the 0,0 (origin). In addition to shapes, a design can have other designs embedded within it. These are modeled through Instance objects. For example, a design object d1 can contain an instance i1 which has two pieces of information – a reference to another design object d2 and where d2’s origin is situated within the 2D coordinates of d1. 

 The objective of the programming assignment is to implement the following  

    a. The first task is to model the above (design, shape, instance) using appropriate classes/functions 

    b. Given a design object, write a function that returns a list of shapes in that design object such that they are sorted descending by their area. You can ignore instances within the given design as we are concerned only with the shapes in top level of the hierarchy in this function. 

    c. Given a design object, write a function to return all the shapes within 1 level of hierarchy such that the locations of the shapes are described with respect to the 0,0 of the top-level design. Consider the following example. Design d1 contains shape r1 and instance i1. i1 refers to design d2. d2 contains shape r2 and instance i2. Your function should return the location of shapes r1 and r2 with respect to 0,0 of the design d1. You do not need to consider any shapes or instances within design referenced by i2 as it is at level 2 in the hierarchy. We are concerned only till level 1 of hierarchy in this function.     

We are looking for the following as part of your submission: 
- Well structured, readable, and tested code 
- Documentation including descriptions of your assumptions, corner cases, and what you might do differently if given more time 
- Submit your code via GitHub or other online RCS, preferably with several commits in the history 
