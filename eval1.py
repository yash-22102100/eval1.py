students= {
    "student1" :{"name": "yash", "class": "12","height": "180","weight": "72", "sport": "cricket"},
    "student2" :{"name": "vishal", "class": "10","height": "160","weight": "55", "sport": "football"},
    "student3" :{"name": "mridul", "class": "19","height": "170","weight": "69", "sport": "hockey"}
    }
def diet(weight):
    if weight < 70:
        return "high protien diet"
    elif weight < 60:
        return "balanced diet"
    else:
        return "low carb diet"
def sport(height,weight):
    agility = height / weight
    if agility>2.0:
        return "cricket"
  

        
        
for key, details in students.item():
    height = details["height"] 
    weight = details["weight"]
    diet = generate_diet(weight)
    sport= sport(height,weight)
    students[key]["diet"]=diet
    students[key]["sport"]=sport
            
            
            
for student, details in student.items():
    print(f"Student: {details['name']}")
    print(f"Class: {details['class']}")
    print(f"Height: {details['height']} cm")
    print(f"Weight: {details['weight']} kg")
    print(f"Sport: {details['sport']}")
    print(f"Diet plan: {details['diet']}")
    print(f"Recommended sport: {details['sport']}")
    print()
    
