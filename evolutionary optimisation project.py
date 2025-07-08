#!/usr/bin/env python
# coding: utf-8

# # Evolutionary Optimisation project

# # Basic Scenario

# ## 1. Write a function that calculates the distance between two words of equal length.

# In[8]:


import random
import numpy as np
import matplotlib.pyplot as plt

def distances(str1, str2):
    dist = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dist = dist+1
            
    return dist


# The function defined in the above cell is the Hamming distance which counts the number of differences between strings

# In[9]:


distances('1111','0000')


# ## 2. Initialisation

# ### 2.1 Use the first two lines of the Shakespeare sonnet number corresponding to the last two digits of your student number as a ‘master sequence’ 
# 
# The last two digits of my Student Number is '24' therefore, the first 2 lines of Shakespeare's 24th sonnet will be used for initialisation

# In[10]:


master_sequence = "mine eye hath playd the painter and hath stelld, thy beautys form in table of my heart"

def mast_dist(string1):
    dist = 0
    
    for i in range(len(master_sequence)):
        if string1[i] != master_sequence[i]:
            dist = dist+1
            
    return dist


# ### 2.2 Generate N random sequences of length L in the letters of the alphabet (e.g. N=10)

# In[14]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',']
# alphabet accounts for ' ' and ','

rand_sequence_list = []
parent = "mine eye hath playd the painter and hath stelld, thy beautys form in table of my heart"
print(len(parent))
prob = 0.1
N = 10

for i in range(N):
    rand_seq = ''
    for character in parent:
        if random.random()>prob:
            rand_seq = rand_seq + character
        else:
            rand_seq = rand_seq + random.choice(alphabet)
    rand_sequence_list.append(rand_seq)
    print(rand_seq, mast_dist(rand_seq))
    


# ### 2.3 - Select that sequence out of the N sequences that you have just generated, which has the smallest distance to the ‘master sequence’ you picked above

# In[15]:


smallest = min(mast_dist(x) for x in rand_sequence_list)
print(smallest)


for i in rand_sequence_list:
    if mast_dist(i) == smallest:
        initialiser = i

print(initialiser)


# ## 3. Evolution

# ## Make N error-prone copies (‘offspring’) of this sequence: that is, with a probability, each letter in this sequence can randomly change to another letter of the alphabet (mutation) in this copying process
# 
# ## - If any offspring has a smaller distance to the master sequence select the one with the smallest distance and use that to create a new generation of offspring, otherwise use the previous one again.
# 

# In[16]:


parent = initialiser

dist_list = []

gens = 150
prob = 0.1

for gen in range(gens):
    child = ''
    for character in parent:
        if random.random()>prob:
            child = child + character
        else:
            child = child + random.choice(alphabet)
    if mast_dist(parent) < mast_dist(child): # ensures the corruption process only gets worse
        parent = child
    dist_list.append([gen, mast_dist(parent)])
    if mast_dist(parent) == len(parent): # stops the corruption process once maximum corruption reached
        corrupted_string = parent
        print(gen, parent, mast_dist(parent))
        break

point(dist_list)


# We can see that the corruption of the string is very effective at the beginning of the corruption process. This is because early in the corruption process, nearly all characters of the initialising string are susceptible to becoming corrupted. As more characters of the string become corrupted over generations, the ability to corrupt the remaining uncorrupted characters becomes increasingly difficult. This can be seen by the plot becoming shallower in later generations.

# ## 4. Termination - Repeat the process for a number of G generations till you have achieved the master sequence through evolution.

# In[17]:


dist_list = []

parent = corrupted_string

gens = 1000000
prob = 0.1

for gen in range(gens):
    child = ''
    for character in parent:
        if random.random()>prob:
            child = child + character
        else:
            child = child + random.choice(alphabet)
    if mast_dist(parent) > mast_dist(child): # ensures that corrupted string only gets better
        parent = child
    dist_list.append([gen, mast_dist(parent)])
    if mast_dist(parent) == 0: # stops the optimisation process once master string is reached
        print(gen, parent, mast_dist(parent))
        break
        
point(dist_list)


# The above code has now become an optimisation algorithm going in the direction of decreasing hamming distance
# 
# We can see that the optimisation of the corrupted string is very effective at the beginning of the optimisation process. This is because early in the optimisation process, nearly all characters of the corrupted string are susceptible to becoming optimised to the master string. As more characters of the string become optimised over generations, the ability to optimise the remaining corrupted characters becomes increasingly difficult. This can be seen by the plot becoming shallower in later generations.

# In[18]:


print(gen, parent, mast_dist(parent))


# We can see that despite running the optimisation process for 1 million generations, the offspring do not converge to the master sequence. As with the corruption process, optimisation 

# # Advanced Scenario

# ## 1. Investigate how many generations G it typically takes to reach this master sequence

# As seen in the basic scenario, the optimisation solution did not converge to the master string despite running for 1 million generations. Therefore, we will investigate the effect of different parameters such as string length, probability and the alphabet on the number of generations needed to converge to the master sequence.

# ### 1.1 Effect of string length

# In[51]:


master_sequence = "mine eye hath playd"

def mast_dist(string1):
    dist = 0
    
    for i in range(len(master_sequence)):
        if string1[i] != master_sequence[i]:
            dist = dist+1
            
    return dist


# In[52]:


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',']
# alphabet accounts for ' ' and ','

rand_sequence_list = []
parent = "mine eye hath playd"
print(len(parent))
prob = 0.1
N = 10

for i in range(N):
    rand_seq = ''
    for character in parent:
        if random.random()>prob:
            rand_seq = rand_seq + character
        else:
            rand_seq = rand_seq + random.choice(alphabet)
    rand_sequence_list.append(rand_seq)
    print(rand_seq, mast_dist(rand_seq))


# In[53]:


smallest = min(mast_dist(x) for x in rand_sequence_list)
print(smallest)


for i in rand_sequence_list:
    if mast_dist(i) == smallest:
        initialiser = i

print(initialiser)


# In[54]:


parent = initialiser

dist_list = []

gens = 150
prob = 0.1

for gen in range(gens):
    child = ''
    for character in parent:
        if random.random()>prob:
            child = child + character
        else:
            child = child + random.choice(alphabet)
    if mast_dist(parent) < mast_dist(child): # ensures the corruption process only gets worse
        parent = child
    dist_list.append([gen, mast_dist(parent)])
    if mast_dist(parent) == len(parent): # stops the corruption process once maximum corruption reached
        corrupted_string = parent
        print(gen, parent, mast_dist(parent))
        break

point(dist_list)


# In[55]:


dist_list = []

parent = corrupted_string

gens = 1000000
prob = 0.1

number_of_runs = 50

generation_list = []

for i in range(number_of_runs):
    parent = corrupted_string
    for gen in range(gens):
        child = ''
        for character in parent:
            if random.random()>prob:
                child = child + character
            else:
                child = child + random.choice(alphabet)
        if mast_dist(parent) > mast_dist(child):
            parent = child
        #dist_list.append([gen, mast_dist(parent)])
        if mast_dist(parent) == 0:
            generation_list.append(gen)
            #print(gen, parent, mast_dist(parent))
            break

print(generation_list)
#point(dist_list)


# In[56]:


plt.hist(generation_list, bins = 5)
plt.show()


# Shortening the length of the string has significantly reduced the number of generations needed to reach the master string. It can be concluded that the shorter the length of the string, the less time needed to converge to the master string.
# 
# With a probbility of 0.1, the vast majority of runs reaching the master sequence approximately between 2000 and 8000 generations

# ### 1.2 Effect of probability

# In[57]:


dist_list = []

parent = corrupted_string

gens = 1000000
prob = 0.05

number_of_runs = 50

generation_list = []

for i in range(number_of_runs):
    parent = corrupted_string
    for gen in range(gens):
        child = ''
        for character in parent:
            if random.random()>prob:
                child = child + character
            else:
                child = child + random.choice(alphabet)
        if mast_dist(parent) > mast_dist(child):
            parent = child
        #dist_list.append([gen, mast_dist(parent)])
        if mast_dist(parent) == 0:
            generation_list.append(gen)
            #print(gen, parent, mast_dist(parent))
            break

print(generation_list)
#point(dist_list)


# In[58]:


plt.hist(generation_list, bins = 5)
plt.show()


# Halving the probability from 0.1 to 0.05 appears to have the effect of causing the number of generations to reach the master sequence to be reached quicker with the vast majority of runs reaching the master sequence approximately between 2000 and 7000 generations

# In[60]:


dist_list = []

parent = corrupted_string

gens = 1000000
prob = 0.2

number_of_runs = 50

generation_list = []

for i in range(number_of_runs):
    parent = corrupted_string
    for gen in range(gens):
        child = ''
        for character in parent:
            if random.random()>prob:
                child = child + character
            else:
                child = child + random.choice(alphabet)
        if mast_dist(parent) > mast_dist(child):
            parent = child
        #dist_list.append([gen, mast_dist(parent)])
        if mast_dist(parent) == 0:
            generation_list.append(gen)
            #print(gen, parent, mast_dist(parent))
            break

print(generation_list)
#point(dist_list)


# In[61]:


plt.hist(generation_list, bins = 5)
plt.show()


# Doubling the probability from 0.1 to 0.2 appears to have the effect of causing the number of generations to reach the master sequence to be reached after more generations with the vast majority of runs reaching the master sequence approximately between 5000 and 17000 generations

# ### 1.3 Effect of alphabet

# In[63]:


alphabet = ['a', 'd', 'e', 'h', 'i', 'l', 'm', 'n', 'p', 't', 'y', ' ']

dist_list = []

parent = corrupted_string

gens = 1000000
prob = 0.1

number_of_runs = 50

generation_list = []

for i in range(number_of_runs):
    parent = corrupted_string
    for gen in range(gens):
        child = ''
        for character in parent:
            if random.random()>prob:
                child = child + character
            else:
                child = child + random.choice(alphabet)
        if mast_dist(parent) > mast_dist(child):
            parent = child
        #dist_list.append([gen, mast_dist(parent)])
        if mast_dist(parent) == 0:
            generation_list.append(gen)
            #print(gen, parent, mast_dist(parent))
            break

print(generation_list)
#point(dist_list)


# In[64]:


plt.hist(generation_list, bins = 5)
plt.show()


# The alphabet now only includes the characters that are part of the master string and the probability has been kept at 0.1. Reducing the characters of the alphabet causes the master sequence to be reached sooner as the vast majority of runs reachi the master sequence approximately between 550 and 1800 generations

# ### 1.4 Application of evolutionary algorithms in the workplace

# - Evaluation of pharmaceutical compunds to create more effective treatments
# - Evovle and optimise deep learning archietcture
# - Biological system modelling
# 
# Cognizant. _Model and prescribe optimal outcomes_. www.cognizant.com. Evolutionary AI | Cognizant. [online] Available at: https://www.cognizant.com/us/en/ai/evolutionary-ai.

# In[ ]:




