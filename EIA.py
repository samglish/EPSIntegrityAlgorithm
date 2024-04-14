#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:45:49 2023

@author:  BEIDI DINA SAMUEL 18A1093FS
"""

##########################################################
#                                                        #
# intégrité : Algorithme EIA (EPS Integrity Algorithm)   #
#                                                        #
#                   BEIDI DINA SAMUEL                    #
##########################################################

import hashlib

def calculate_integrity(message):
    # Calculer le hachage SHA-256
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    return sha256_hash

# Exemple d'utilisation
message = "Hello, world!"
integrity = calculate_integrity(message)
print("Message integrity:", integrity)

"""
la fonction `hashlib.sha256()` est utilisée 
pour calculer le hachage SHA-256 du message. 
La méthode `hexdigest()` est utilisée pour obtenir la représentation 
hexadécimale du hachage résultant.

Il est important de noter que cet algorithme d'intégrité ne fournit 
pas d'authentification, mais seulement la capacité de détecter les
changements dans le message.
"""