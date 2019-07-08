
    
def translets(formatted):
    error_list=[
    {
        "from": "unexpected indent",
        "to": "Aapke code ki formatting theek nahi hai. Aapko apne code ki indentation (yaani spacing) theek karo, jisse ki python aapke code ko samajh jayein."
    },
    {
        "from": "NameError",
        "to": "NaamNahiHaiError: ye naam undefined hai ye defined nahi kiya hai aapne"
    },
    {
        "from": "SyntaxError",
        "to": "aapne jo Styntax use kiya hai wo galat hai python isko support nahi karta hai"
    },
    {
        "from": "IndexxError",
        "to": "aapne loop ki jo range li hai vo sima ke bahar hai"

    },
    {
        "from": "FileNotFoundError",
        "to": "FileNotFoundError: file nahi mil rahi hai"

    },
    {
        "from": "TabError",
        "to": "aapne TabKey or spaceKey ka use galat kiya hai usko sahi karo"

    },
    {
        "from": "UnsupportedOperation",
        "to": "ye operation support nahi karta hai isko pad nahi sakte"

    },
    {
        "from": "Missing parentheses",
        "to": "aapne parentheses ka use nahi kiya hai python 3 parentheses ke bina print nahi karta hai"
    },
    {
        "from": "KeyError",
        "to": "aapki key sahi nahi hai"

    },
    {
        "from": "AttributeError",
        "to": "AttributeError: ye oject nahi hai"

    },
    {
        "from": "UnboundLocalError:",
        "to": "UnboundLocalError: aapne defined karne se phele variable ka use kiya hai"

    },
    {
        "from": "EOL",
        "to": "SyntaxSahiNahiError: line ke last mai Styntax sahi nahi hai"
    },
        {
        "from": "TypeError: unsupported operand type(s) for /: 'str' and 'int'",
        "to": "TypeSahiNahihai: aapka type sahi nahi hai intger or string isko support nahi karte hai"
        }]
    
    
    # for i in range(len(list1)):
    #     print list1[i]
    for i in error_list:
        
        english_error=i["from"]
        hindi_error=i["to"]
        

        if english_error in formatted:
            formatted+=hindi_error
            return formatted    

          

