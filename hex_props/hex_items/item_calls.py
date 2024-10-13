import os

def call_img(season:str, land_type:str):
    """
    Parameters:
    season (str): "1"- spring "2"-Winter,
    land_type (str): "1"-plains "2"-forest "3"-hill

    """
    image_folder = r'C:\Users\Majitel\Documents\programing\Muskets_And_swords_NewDawn\hex_props\hex_items\images'
    terrain = { 
        "1" : {
            "1": os.path.join(image_folder, 'plains_spr.png'),
            "2": os.path.join(image_folder, 'forest_spring.png'),
            "3": os.path.join(image_folder, 'hill_spring.png')
        },
        "2" : {
            "1": os.path.join(image_folder, "plains_winter.png"),
            "2": os.path.join(image_folder, "plains_winter.png"),
            "3": os.path.join(image_folder, "plains_winter.png"),
        }
    }
    return terrain[season][land_type]
