# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment and any with  ''' is also a docstring.
# Please read all the comments in this example file and all others.

# Remember to install en_core_web_md by typing python -m spacy download en_core_web_md into your command line

import spacy  # importing spacy
nlp = spacy.load('en_core_web_sm') # specifying the model we want to use. 

# Now we are going to look into longer texts and compare them. 
# Below we  have two lists: one containing complaints submitted to a company, and another of recipes found online.
# We want to establish how spaCy's model can identify similarities or dissimilarities between complaint and recipes. 

# Make sure to run this example file and read through the explanations.

# Below is a list of six complaints.
complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]

# We will now compare the similarity of the complaints to ascertain if spaCy's similarity
# model is able to distinguish between these long pieces of text.

print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))

# Below is a list of six recipe instructions.

recipes= [ 'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]

# We will now compare the similarity of the recipes. to ascertain how well spaCy's similarity
# model is able to distinguish between them.

print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in recipes:
        token_ = nlp(token_)
        print(token.similarity(token_))

# Now we want to obtain the extent of similarity between the complaints and the recipes.
# we will loop through every recipe instruction and compare it with a complaint.

print("-------------Recipes similarity---------------")

for token in recipes:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))

# What do you observe? Note that the similarity index has reduced from what we observed in the short-text example discussed in the content PDF.


# There are several ways to make your model more accurate with the similarity
# or even prediction such as feeding it with some training data. This could include
# more vocabulary about food and recipes if you are building a models concerning food.
# You can also head over to spaCy documentation here: https://spacy.io/usage/linguistic-features#vectors-similarity
# and check out other cool stuff!


'''
en_core_web_md:
-------------Complaints similarity---------------
1.0
0.8350770380943701
0.9246800668484182
0.8959758607031337
0.8395325188842946
0.8622109066850939
0.8350770380943701
1.0
0.8906699062993373
0.8145959567773281
0.9506982511773873
0.7946509303034253
0.9246800668484182
0.8906699062993373
1.0
0.8905289515151633
0.8818462415576602
0.869256307461911
0.8959758607031337
0.8145959567773281
0.8905289515151633
1.0
0.8115092735139192
0.8775633198697652
0.8395325188842946
0.9506982511773873
0.8818462415576602
0.8115092735139192
1.0
0.759590996735251
0.8622109066850939
0.7946509303034253
0.869256307461911
0.8775633198697652
0.759590996735251
1.0
-------------Recipes similarity---------------
1.0
0.9058969879808717
0.8761883563680793
0.8921915020817676
0.9362320788371851
0.9077991339554589
0.9058969879808717
1.0
0.8960302632860658
0.8683352787585712
0.9251986105731227
0.909277512798149
0.8761883563680793
0.8960302632860658
1.0
0.8206931822271948
0.923499834067875
0.9066167896089331
0.8921915020817676
0.8683352787585712
0.8206931822271948
1.0
0.843615344994607
0.8890459855149918
0.9362320788371851
0.9251986105731227
0.923499834067875
0.843615344994607
1.0
0.8970581769256016
0.9077991339554589
0.909277512798149
0.9066167896089331
0.8890459855149918
0.8970581769256016
1.0
-------------Recipes similarity---------------
0.7908975726272921
0.6548518295341987
0.7398681679268514
0.7337804972179451
0.6703983067394562
0.7674086724411375
0.7580808759364783
0.5323925552042279
0.7114560945673947
0.7008472217256502
0.5443126469769464
0.7254376103761647
0.7884092498717231
0.5253234387230952
0.7214799557383781
0.6939840662542774
0.5243623425430298
0.7301758500107655
0.6633546838990971
0.4596805000526375
0.5643795549917598
0.6354896259101941
0.4868229640175464
0.6469780435027565
0.8458759758734137
0.6612351139999046
0.7954997963311431
0.7757728611773715
0.6793218010601022
0.7921867919801224
0.7706409888372543
0.5407034497147122
0.6932683919739884
0.7135981756961652
0.549146532488016
0.7118486371023985
'''


'''
en_core_web_sm:
-------------Complaints similarity---------------
1.0
/Users/piotr/Library/CloudStorage/OneDrive-AerisCommunications/Programming/hyperiondev/Data Science/T21/example.py:35: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.5181293843480566
0.7174057874383772
0.769836073707098
0.6591949418542005
0.6330322363273272
0.5181293843480566
1.0
0.6737944468473719
0.4451901146396827
0.6772692915046274
0.5799084443531823
0.7174057874383772
0.6737944468473719
1.0
0.6654231571699263
0.6732006259359494
0.6399289231304313
0.769836073707098
0.4451901146396827
0.6654231571699263
1.0
0.5691884077073325
0.6025169357594007
0.6591949418542005
0.6772692915046274
0.6732006259359494
0.5691884077073325
1.0
0.46995671191305083
0.6330322363273272
0.5799084443531823
0.6399289231304313
0.6025169357594007
0.46995671191305083
1.0
-------------Recipes similarity---------------
1.0
/Users/piotr/Library/CloudStorage/OneDrive-AerisCommunications/Programming/hyperiondev/Data Science/T21/example.py:55: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.6941871200523895
0.5810681163824285
0.7831206815337135
0.7158292356769015
0.6553960081080757
0.6941871200523895
1.0
0.7292983572876688
0.6922875031264577
0.6848675820749035
0.6753270423635954
0.5810681163824285
0.7292983572876688
1.0
0.6040474537796157
0.6870432838107841
0.7279226740146795
0.7831206815337135
0.6922875031264577
0.6040474537796157
1.0
0.7286111421305181
0.686102278923058
0.7158292356769015
0.6848675820749035
0.6870432838107841
0.7286111421305181
1.0
0.7674537948348564
0.6553960081080757
0.6753270423635954
0.7279226740146795
0.686102278923058
0.7674537948348564
1.0
-------------Recipes similarity---------------
/Users/piotr/Library/CloudStorage/OneDrive-AerisCommunications/Programming/hyperiondev/Data Science/T21/example.py:66: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token.similarity(token_))
0.5513361188468437
0.3351174428639124
0.4168960720409892
0.6338378452285116
0.3672420486236193
0.6037977885236739
0.4209768301914277
0.1434038584633699
0.40360279354900436
0.5562152669602153
0.18598147337374735
0.5272081093405103
0.5599700762505844
0.2591301333405263
0.490976444001561
0.6101887591269736
0.2803351674719279
0.552595165458264
0.4601953267891984
0.2205403260828522
0.36536239633271705
0.5815827222351897
0.34659800184757245
0.5066580677835565
0.6887837156630946
0.42132082734334125
0.6347594184125857
0.7833611968862726
0.5892172211703519
0.5925174462939254
0.6184740737716764
0.13972162613045463
0.4273963130488689
0.7195851718384655
0.36855291905173254
0.3837304420348635
'''

'''
UserWarning: [W007] The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger, 
parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, 
which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available.
'''