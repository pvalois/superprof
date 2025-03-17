#!/usr/bin/env python3 

import random
import os

# Function to generate a random DNA sequence
def generate_dna_sequence(length=38):
  return ''.join(random.choices("ATCG", k=length))

# Functions to randomize with probabilities eyes hairs and sex and cancer
def eyes_color():
  classifier=random.uniform(1,2)

  if (classifier<=1.3): return("Blue")
  if (classifier<=1.7): return("Green")
  if (classifier<=1.8): return("Gray")
  if (classifier<=1.95): return("Brown")
  return("Hazel")

def hair_color():
  classifier=random.uniform(1,2)

  if (classifier<=1.2): return("Gray")
  if (classifier<=1.5): return("Blond")
  if (classifier<=1.7): return("Black")
  return("Red")

def sex():
  classifier=random.uniform(1,2)

  if (classifier<=1.55): return("Male");
  return ("Female")

def cancerous():
  classifier=random.uniform(1,2)

  if (classifier<=1.2): return("Yes");
  return ("No")

num_files = 10
num_entries_per_file = 1000

adn_hair={'Black':'ATG', 'Blond':'GAC', 'Red':'CCA', 'Gray':'ACT'}
adn_eyes={'Blue':'GAC', 'Green':'TTG', 'Gray':'AAA', 'Brown':'ACG', 'Hazel':'GTA'}
adn_sex={'Male':'AA', 'Female':'AT'}

# Generate files and sequences
for i in range(1, num_files + 1):
  file_path = f"dna_data_{i:02}.csv"
  data = []
    
  for _ in range(num_entries_per_file):
    dna_seq = generate_dna_sequence()

    alpha=dna_seq[0:6]
    beta=dna_seq[7:9]
    gamma=dna_seq[10:16]
    delta=dna_seq[17:24]
    omega=dna_seq[25:]

    eyes = eyes_color()
    hairs = hair_color()
    gender = sex()
    cancer = cancerous()
    if (cancer=="Yes"): delta="GATTACA"

    dna_seq=alpha+adn_eyes[eyes]+beta+adn_hair[hairs]+gamma+delta+omega
    data.append([dna_seq, eyes, hairs, gender, cancer])

  with open(file_path, 'w') as file:
      for entry in data:
          file.write(",".join(entry) + "\n")
