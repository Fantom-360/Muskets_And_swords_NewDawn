import os

def call_img(season:str, land_type:str):
    """
    Parameters:
    season (str): "1"- spring "2"-Winter,
    land_type (str): "1"-plains "2"-forest "3"-hill

    """
    image_folder = image_folder = os.path.join(os.getcwd(), 'hex_props', 'hex_items', 'images')
    terrain = { 
        "1" : {
            "1": os.path.join(image_folder, r'plains_spr.png'),
            "2": os.path.join(image_folder, r'forest_spr.png'),
            "3": os.path.join(image_folder, r'hill_spring.png')
        },
        "2" : {
            "1": os.path.join(image_folder, r"plains_winter.png"),
            "2": os.path.join(image_folder, r"plains_winter.png"),
            "3": os.path.join(image_folder, r"plains_winter.png"),
        }
    }
    
    return terrain[season][land_type]


