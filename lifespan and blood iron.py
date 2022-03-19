# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:08:32 2022

@author: Sulav
"""

# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# vein is the basic package and artery is premium package

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]

# mean lifespans of vein subscribers
vein_mean = np.mean(vein_pack_lifespans)
print(vein_mean)

# testing if vein samplifespans.lifespan[lifespans.pack == "vein"]e mean of 76.16 is significantly different from average life expectancy of 73 years.
#Null: The average lifespan of a Vein Pack subscriber is 73 years.
#Alternative: The average lifespan of a Vein Pack subscriber is NOT 73 years.

tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print(pval)

# since pvalue is less than 0.05 we can conclude that vein pack subscribers lifespan is significantly different than average lifespan of 73 years.

artery_pack_lifespans = lifespans.lifespan[lifespans.pack == "artery"]

artery_pack_mean = np.mean(artery_pack_lifespans)
print(artery_pack_mean)

# hypothesis testing between vein pack and artery pack subscribers
#Null: The average lifespan of a Vein Pack subscriber is equal to the average lifespan of an Artery Pack subscriber.
#Alternative: The average lifespan of a Vein Pack subscriber is NOT equal to the average lifespan of an Artery Pack subscriber.

tstat, pval = ttest_ind(vein_pack_lifespans,artery_pack_lifespans)
print(pval)

# since pval is 0.055 i.e. greater than 0.05 we can conclude there isn't a significant difference between lifespans of vein pack vs artery pack subscribers.
#########################################

# comparing data between low, medium, and high iron count subscribers.

# assoociation between vein and artery pack subscribers and their blood iron count
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)