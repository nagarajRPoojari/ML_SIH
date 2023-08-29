from pipeline.preprocessing.data_preprocessing import DataPreprocesser
from pipeline.prediction.prediction import Prediction

class Pipeline():
    def __init__(self):
        self.predictor=Prediction()
        
    def main(self,user,all_data):
        res=self.predictor.similarity_search(user,all_data)
        return res