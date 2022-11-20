import json
import os 
import requests

def nested_aimed(parent, structure, original ):
    if type(structure) is list:
        return [nested_aimed(structure, item, original) for item in structure]

    if type(structure) is dict:
        return {key : nested_aimed(structure ,value, original)
                     for key, value in structure.items() }

    if str(structure).find(original) != -1:
        if type(parent) is dict:
            filename = parent["FileName"] + ".mp3"
            if not os.path.exists(filename):
                print(parent["FileName"] + ":")
                print(structure)
                r = requests.get(structure)
                with open(filename, "wb") as codefile:
                    codefile.write(r.content)
                return structure
            else:
                # print("filename duplicated" + filename)
                return
        return                
    else:
        return

g = os.walk("../")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        #print(os.path.join(path, file_name) )
        if file_name.endswith('.aspx'):
            x = os.path.join(path, file_name)
            # print("file xx:" + x)
            with open(x, 'r', encoding='utf-8') as fcc_file:
                string = fcc_file.read()
                # print("file is :" + str(fcc_file))
                # print("string:" + string)
                fcc_data = json.loads(string)
                # print(fcc_data)
                # items = fcc_data.items()
                # for key, value in items:
                #     print(str(key) + '=' + str(value))
                nested_aimed("",fcc_data, ".mp3")
                # nested_replace(items, ".mp3")
                # if type(fcc_data) == list:
                #     print("good")

            
        
