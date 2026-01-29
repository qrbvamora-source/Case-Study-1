import pandas as pd
import random

data = pd.read_csv('C:\Users\tipqc\Documents\Case-Study-1\SchoolDocx\Case_study_1(Group1)\Students_bag_dataset.csv')  

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
            score += item['duration']
            score += item['angle']
            score += item['density']
            if item['sharp']:
                score += 30
        
        avg = score / len(bag.items) if bag.items else 0
        return "HIGH" if avg > 25 else "MEDIUM" if avg > 15 else "LOW"

all_bag_ids = data['Bag_ID'].unique()

detector = MetalDetector()

print("BAG SECURITY SCAN RESULTS")
print("=" * 40)

for bag_id in all_bag_ids:
    bag = Bag(bag_id, data)

    threat_level = detector.scan(bag)

    dangerous_count = sum(1 for item in bag.items if item['sharp'])

    print(f"{bag_id}: {threat_level} threat", end="")
    if dangerous_count > 0:
        print(f" ({dangerous_count} sharp objects!!)")
    else:
        print()

print("=" * 40)
print(f"Total bags scanned: {len(all_bag_ids)}")