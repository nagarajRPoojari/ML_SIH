import pinecone
import os
import numpy as np


class DataPreprocesser():
    def __init__(self,classes):
        self.classes=classes
        self.features=7
    
    def preprocess(self,data):
        user_={
            'Location':user['Location'],
            'Severity': encoder(user['Severity'],self.classes['severity']),
            'Capacity': encoder(user['Capacity'],self.classes['capacity']),
            'Service':encoder(user['Service'],self.classes['Service']),
            'Specialization': encoder(user['Specialization'], self.classes['specialization']),
            'Medical Facility':encoder(user['Medical Facility'],self.classes['Medical Facility']),
            'Supply and Resource':encoder(user['Supply and Resource'], self.classes['Supply and Resource']),
            'calamities':encoder(user['calamities'] , self.classes['calamities'])
        }   
    
    return user_
    
    def encoder(self,values,labels):
        l=np.zeros(len(labels))
        for i in range(len(labels)):
            if labels[i]  in values:
                l[i]=1
        return l
    
    
        
        
        
