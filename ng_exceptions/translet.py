import json   
def translets(formatted):
    a="ng_exceptions/"+"translet.json"
    with open(a, 'r') as f:
        error_list = json.load(f)

    
    
    
    for i in error_list:
        
        english_error=i["from"]
        hindi_error=i["to"]
        

        if english_error in formatted:
            formatted+=hindi_error
            return formatted    

          

