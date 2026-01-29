import pandas as pd
import random

class Bag:
    def __init__(self, bag_id, data):
        self.id = bag_id
        self.items = []
        for _, row in data[data['Bag_ID'] == bag_id].iterrows():
            self.items.append({
                'name': row['Object_Name'],
                'metal': 1 if row['Metal_Presence'] == 'Yes' else 0,
                'duration': random.randint(1, 10),
                'angle': random.randint(1, 10),
                'density': random.randint(1, 10),
                'sharp': row['Sharp_Object'] == 'Yes'
            })

class MetalDetector:
    def scan(self, bag):
        score = 0
        for item in bag.items:
            score += item['metal'] * 10
            score += min(item['duration'] * 2, 20)  
            score += min(item['angle'] * 2, 20)     
            score += min(item['density'] * 2, 20)   
            if item['sharp']:
                score += 30
        
        avg = score / len(bag.items) if bag.items else 0
        return "HIGH" if avg > 25 else "MEDIUM" if avg > 15 else "LOW"

data = pd.read_csv('Students_bag_dataset.csv')
bag = Bag('BAG_002', data)
detector = MetalDetector()
print(f"Threat: {detector.scan(bag)}")