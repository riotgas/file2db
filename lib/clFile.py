import codecs
# for working with files
class File:
    # default constructor
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.encoding = ""
        self.error = False
        self.errorMessage = ""
        
    # alternate constructor with ENCODING
    def File(self, name, mode, encoding):
        self.__init__(name, mode)
        self.encoding = encoding
        
    # gets probability ENCODING
    def getEncoding(self, encodings):
        result = ""
        for encoding in encodings:
            try:
                file1 = codecs.open(self.name, self.mode, encoding)
                file1.readline()
                self.error = False
                self.errorMessage = ""
                result = encoding
            except UnicodeDecodeError as e:
                self.error = True
                self.errorMessage = e
            except Exception as e:
                self.error = True
                self.errorMessage = e
                break
            finally:
                file1.close()
                if self.error == False:
                    self.encoding = result
                    return result

    # get first line for checking
    def getFirstLine(self):
        result = ""
        if len(self.encoding) == 0:
            return result
        try:
            file1 = codecs.open(self.name, self.mode, self.encoding)
            result = file1.readline()
            self.error = False
            self.errorMessage = ""
        except UnicodeDecodeError as e:
            self.error = True
            self.errorMessage = e
        except Exception as e:
            self.error = True
            self.errorMessage = e
        finally:
            file1.close()
            if self.error == False:
                return result
        