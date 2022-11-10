#Write a Python program to print the following string in a specific format (see the output). Go to the editor
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like 
# a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

#Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How I wonder what you are



a="Twinkle, twinkle, little star,\n"
b="        How I wonder what you are!\n"
c="                Up above the world so high,\n"
d="                Like a diamond in the sky.\n"
e="Twinkle, twinkle, little star,\n"
f="        How I wonder what you are"
print(a+b+c+d+e+f)