#1. Write a Python program to calculate the length of a string.

str = "Write a Python program to calculate the length of a string."
print("Total length of this string is =", len(str))

stri1 = "But at the time he had no doubt; what had taken him over was the will to live, unadulterated, irresistible, pure, and the first thing it did was to inform him that it wanted nothing to do with his pathetic personality, that half-reconstructed affair of mimicry and voices, it intended to bypass all that, and he found himself surrendering to it, yes, go on, as if he were a bystander in his own mind, in his own body, because it began in the very centre of his body and spread outwards, turning his blood to iron, changing his flesh to steel, except that it also felt like a fist that enveloped him from outside, holding him in a way that was both unbearably tight and intolerably gentle; until finally it had conquered him totally and could work his mouth, his fingers, whatever it chose, and once it was sure of its dominion it spread outward from his body and grabbed Gibreel Farishta by the balls."
print("The lenght of this string is = ", len(stri1))
print(len(stri1))



# 2.Write a Python program to count the number of characters (character frequency) in a string.
str2 = "Write a Python program to count the number of characters (character frequency) in a string."
count = str2.count("i")
print("The count of i =", count)

str3 = "That night he dreamt of horses on a high plain where the spring rains had brought up the grass and the wildflowers out of the ground and the flowers ran all blue and yellow far as the eye could see and in the dream he was among the horses running and in the dream he himself could run with the horses and they coursed the young mares and fillies over the plain where their rich bay and their chestnut colors shone in the sun and the young colts ran with their dams and trampled down the flowers in a haze of pollen that hung in the sun like powdered gold and they ran he and the horses out along the high mesas where the ground resounded under their running hooves and they flowed and changed and ran and their manes and tails blew off them like spume and there was nothing else at all in that high world and they moved all of them in a resonance that was like a music among them and they were none of them afraid horse nor colt nor mare and they ran in that resonance which is the world itself and which cannot be spoken but only praised."
count = str3.count("e")
print("The total count is =",count)



# 3. 3. Write a Python program to count the occurrences of the word "python" in a given sentence below:
# "We are learning how to program in python. I find python programming fun"
str4 = "We are learning how to program in python. I find python programming fun"
count = str4.count("python")
print("The total number of the word Python is =",count)

str5 = "Python is a very simple yet very powerful object oriented programming language. The syntax of Python is very simple so a beginner can learn Python with ease. I have covered Python language in several separate python tutorials, this is the main Python tutorial page that has links to all the tutorials I have shared on Python. This tutorial is for both beginners and advanced Python learners."
count = str5.count("Python")
print("The total count of the word Python is = ",count)


# 4. Write a Python function to reverses the word below:
str6 = "reven"
x = str6[:: -1]
print(x)

str7 = "Reverse each word in a sentence"
y = str7[:: -1]
print(y)