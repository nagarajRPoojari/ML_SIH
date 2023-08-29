from pydantic import BaseModel


class DataItem(BaseModel):
    id : str
    Location : dict
    Severity : list
    Capacity : list
    Services: list
    Availability: list
    Specialization: list
    Medical_Facility: list
    Supply_and_Resource: list
    calamities: list
    
class Data(BaseModel):
    user : DataItem
    all_data : list