
# Export functions

class Exporter():
    def __init__(self, file_name, question):
        self.file_name = file_name
        self.question = str(question)

    def report_return(self, return_data):
        file_ = open(self.file_name, "a+")
        string = "- " + str(self.question)
        string += "\n" + str(return_data) + "\n\n"
        file_.write(str(string))
        file_.close()
