class Utils:
    
    @staticmethod
    def get_filename():
        filename = "SampleData2017.txt"
        return filename
    #end def
    
    @staticmethod
    def split_line(line):
        try:
            stripped_line = line.strip()
            split_line = stripped_line.split(",")
            return split_line
        except:
            return None        
    #end def
    
    @staticmethod
    def append_to_file(filename, to_append):
        file = open(filename, "a")
        file.writelines(to_append)
    #end def