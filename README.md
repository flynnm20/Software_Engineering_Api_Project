# Software_Engineering_Api_Project
Goal:
The goal of this project is to see is there a correlation between the amount of programming languages a person knows and the quality of their code (G1). 
A secondary goal is to compare the best language used by various companies to see which language produces the company’s best repositories and how they compare with other companies(G2).
Data Representation:
G1: I decided to use a scatter plot to map this graph. For the x-axis the average amount of stars each person’s repository has received is used. For the y-axis, the amount of languages that were used in all the person’s repositories. The dots will be colour coded depending on the organization that the person was associated with.
G2: I use a bar chart to represent this graph. On the x-axis there is a list of each company and the language that has the most stars in the company’s repositories. On the y axis there is the sum of all the repository stars which that language received.

Code:
API calling:
Using the github api for python, PyGithub, the program can get a list of all members in that organization. It then gets all the repos for the member and calculates the average stars that repository earned and the number of languages used. Then the data is added to a list of average stars and number of languages known so that they can be used for G_1. After all data has been gathered for all members the process then calculates the language with the most stars earned and returns that as the best language for that organization. 

Graphical Representation;
Once all the data has been gathered and parsed G1 and G2 are generated. Using the Plotly Library It is easy to generate these two graphs using the libraries basic functionality.

Result:

