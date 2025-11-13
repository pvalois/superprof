#!/usr/bin/env python3 

import pandas as pd
import random
from faker import Faker

fake = Faker()

# Fonction pour générer un faux fichier de compta analytique
def generate_fake_compta():
    data = []
    for _ in range(50):  # 50 lignes par fichier
        row = {
            'Date': fake.date_between(start_date='-1y', end_date='today'),
            'Compte': random.randint(6000, 7099),
            'Libellé': fake.sentence(nb_words=5),
            'Débit': round(random.uniform(100, 5000), 2),
            'Crédit': round(random.uniform(100, 5000), 2),
            'Centre de coût': random.choice(['Marketing', 'Production', 'R&D', 'Ventes', 'RH'])
        }
        data.append(row)
    return pd.DataFrame(data)

# Générer 5 fichiers
for i in range(1, 6):
    df = generate_fake_compta()
    df.to_excel(f'fake_compta_{i}.xlsx', index=False)

