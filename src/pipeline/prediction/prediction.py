import os
import numpy as np
from scipy.spatial.distance import euclidean
from pipeline.preprocessing.data_preprocessing import DataPreprocesser

class Prediction():
    def __init__(self):
        
        self.classes={
            "Severity" : ["high", "low", "medium"],
            "Capacity" : ["large", "medium", "small"],
            "Services" : ["counseling", "food and water", "language assistance", "medical care", "transportation"],
            "Availability" : [ "almost full","available", "full", "temporarily unavailable"],
            "Specialization" : [  "fire response","medical", "mental health support","search and rescue","water rescue"],
            "Medical Facility" : ["basic first aid", "intensive care units", "pediatric care","surgical facilities","trauma care" ],
            "Supply and Resource" : [ "limited supplies", "medical equipment available", "pharmaceuticals available","well-stocked"],
            "calamities" : ["earthquake", "fire", "flood",  "hurricane",  "pandemic","tsunami"]
        } 
        self.preprocesser=DataPreprocesser(self.classes)
        
        
        
    
    
    def similarity(self,user,rescue):
        point1=np.array([user['Location']['lat'],user['Location']['long']])
        point2=np.array([rescue['Location']['lat'],rescue['Location']['long']])
        dist=np.linalg.norm(point1 - point2)
        cos_dist=euclidean(user['Location']['lat'],rescue['Location']['lat'])
        cos_dist+=euclidean(user['Location']['long'],rescue['Location']['long'])
        sev=euclidean(user['Severity'],rescue['Severity'])
        cap=euclidean(user['Capacity'],rescue['Capacity'])
        serv=euclidean(user['Services'],rescue['Services'])
        spec=euclidean(user['Specialization'],rescue['Specialization'])
        med=euclidean(user['Medical Facility'],rescue['Medical Facility'])
        suppy_and_rescource=euclidean(user['Supply and Resource'],rescue['Supply and Resource'])
        cal=euclidean(user['calamities'],rescue['calamities'])

        dist=dist/100

        similarities = np.array([dist,sev,cap,serv,spec,med,suppy_and_rescource, cal])
        return dist ,similarities 
    
    
    def similarity_search(self,user,data,k=3):
        user_data=self.preprocesser.preprocess(user)
        scores=[]
        for rescue in data:
            rescue_data=self.preprocesser.preprocess(rescue)
            score=self.similarity(user_data,rescue_data)
            scores.append((rescue['id'],score))
            
        scores=np.array(scores)
        scores_idx=np.argsort(scores[:,-1])
        
        scores=scores[scores_idx[:k]]
        
        return scores
        
        


    
    
