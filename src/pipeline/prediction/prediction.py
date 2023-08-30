import os
import numpy as np
from scipy.spatial.distance import euclidean
from pipeline.preprocessing.data_preprocessing import DataPreprocesser
from pipeline.component import Data , DataItem
from operator import itemgetter
class Prediction():
    def __init__(self,weight=[0.9,0.9,0.9,0.6,0.4,0.2,0.3,0.7])->None:
        
        self.classes={
            "Severity" : ["high", "low", "medium"],
            "Capacity" : ["large", "medium", "small"],
            "Services" : ["counseling", "food and water", "language assistance", "medical care", "transportation"],
            "Availability" : [ "almost full","available", "full", "temporarily unavailable"],
            "Specialization" : ["fire response","medical", "mental health support","search and rescue","water rescue"],
            "Medical_Facility" : ["basic first aid", "intensive care units", "pediatric care","surgical facilities","trauma care" ],
            "Supply_and_Resource" : [ "limited supplies", "medical equipment available", "pharmaceuticals available","well-stocked"],
            "calamities" : ["earthquake", "fire", "flood",  "hurricane",  "pandemic","tsunami"]
        } 
        self.preprocesser=DataPreprocesser(self.classes)
        self.weight=weight
        
    
    
    
    def similarity(self,user,rescue):
        distances=[]
        proximity=self.proximity(user['Location'],rescue['Location'])
        proximity/=10
        distances.append(proximity)
        
        for feature , _ in self.classes.items():
            if feature != 'Availability':
                dist = euclidean(user[feature],rescue[feature])
                distances.append(dist)
            
        distances = np.array(distances)
        distances = np.array(self.weight, dtype='object') * distances
        return np.sum(distances) 
    
    
    def similarity_search(self,user,data,k=3):
        user_data=self.preprocesser.preprocess(user)
        scores={}
        for rescue in data:
            if self.is_available(rescue):
                rescue_team=self.preprocesser.preprocess(rescue)
                score=self.similarity(user_data,rescue_team)
                print()
                scores[rescue['id']]=score
          
        print(scores)  
        sorted_dict =  dict(sorted(scores.items(), key=itemgetter(1)))
        print(sorted_dict)
        return sorted_dict
    
    def proximity(self,userLocation,rescueLocation):
        point1=np.array([userLocation['lat'],userLocation['long']])
        point2=np.array([rescueLocation['lat'],rescueLocation['long']])
        return euclidean(point1,point2)
    
    
    def is_available(self,rescue_team):
        if rescue_team['Availability'][0]=='available':
            return True
        else : 
            return False 

        
        
        


    
    
