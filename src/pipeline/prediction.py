import os
import numpy as np
from scipy.spatial.distance import cosine
from data_preprocessing import DataPreprocesser

class Prediction():
    def __init__(self):
        self.classes={
            "severity" : ["low", "medium", "high"],
            "capacity" : ["small", "medium", "large"],
            "services" : ["medical care", "food and water", "transportation", "language assistance", "counseling"],
            "availability" : ["available", "almost full", "full", "temporarily unavailable"],
            "specialization" : ["medical", "water rescue", "search and rescue", "fire response", "mental health support"],
            "medical_facility" : ["basic first aid", "trauma care", "surgical facilities", "intensive care units", "pediatric care"],
            "supply_and_resource" : ["well-stocked", "limited supplies", "medical equipment available", "pharmaceuticals available"],
            "calamities" : ["earthquake", "flood", "fire", "hurricane", "tsunami", "pandemic"]
        } 
        preprocesser=DataPreprocesser(self.classes)
        
    
    
    def similarity(self,user,rescue):
        point1=np.array([user['Location']['lat'],user['Location']['long']])
        point2=np.array([rescue['Location']['lat'],rescue['Location']['long']])
        dist=np.linalg.norm(point1 - point2)
        cos_dist=cosine(user['Location']['lat'],rescue['Location']['lat'])
        cos_dist+=cosine(user['Location']['long'],rescue['Location']['long'])
        sev=cosine(user['Severity'],rescue['Severity'])
        cap=cosine(user['Capacity'],rescue['Capacity'])
        serv=cosine(user['Service'],rescue['Services'])
        spec=cosine(user['Specialization'],rescue['Specialization'])
        med=cosine(user['Medical Facility'],rescue['Medical Facility'])
        suppy_and_rescource=cosine(user['Supply and Resource'],rescue['Supply and Resource'])
        cal=cosine(user['calamities'],rescue['calamities'])

        dist=dist/100

        similarities = np.array([0.9*dist,0.8*sev,0.5*cap,0.3*serv,0.5*spec,0.2*med,0.2*suppy_and_rescource, 0.4*cal])
        return dist ,similarities 
    
    
    def similarity_search(self,user,data,k=3):
        user_data=self.preprocesser.preprocess(user)
        scores=[]
        for rescue in data:
            rescue_data=self.preprocesser.preprocess(rescue_data)
            score=similarity(user_data,rescue_data)
            scores.append((rescue['id'],score))
            
        scores=np.array(scores)
        scores_idx=np.argsort(scores[:,-1])
        
        scores=scores[scores_idx[:k]]
        
        return scores
        
        


    
    
