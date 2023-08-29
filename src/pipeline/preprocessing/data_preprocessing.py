import os
import numpy as np


class DataPreprocesser():
    def __init__(self,classes):
        self.classes=classes
        self.features=7
    
    def preprocess(self,data):
        data_={
            'Location':data['Location'],
            'Severity': self.encoder(data['Severity'],self.classes['Severity']),
            'Capacity': self.encoder(data['Capacity'],self.classes['Capacity']),
            'Services':self.encoder(data['Services'],self.classes['Services']),
            'Specialization': self.encoder(data['Specialization'], self.classes['Specialization']),
            'Medical_Facility':self.encoder(data['Medical_Facility'],self.classes['Medical_Facility']),
            'Supply_and_Resource':self.encoder(data['Supply_and_Resource'], self.classes['Supply_and_Resource']),
            'calamities':self.encoder(data['calamities'] , self.classes['calamities'])
        }   
    
        return data_
    
    def encoder(self,values,labels):
        l=np.zeros(len(labels))
        for i in range(len(labels)):
            if labels[i]  in values:
                l[i]=1
        return l
    
    
        
        
        
