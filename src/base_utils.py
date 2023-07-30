class StringConversion:
    
    @staticmethod
    def camel_to_snake(string: str) -> str:
    
        return "".join(["_" + i.lower() if i.isupper() else i for i in string]).lstrip(
            "_"
        )

    @staticmethod
    def snake_to_camel(string: str) -> str:
        temp = string.split('_')
 
        return temp[0] + ''.join(ele.title() for ele in temp[1:])
    
