class Generator:
    def __init__(self, name):
        self.name = name
        self.path = ""
        print('Generator ' + name)

    def generateViewTemplate(self):
        fh = open('TestTemplate.txt')
        template = fh.read()

        fo = open(self.name+".ts", "w")
        ViewTemplate = """{0}
            {0}"""\
            .format("hahahahah")
        fo.write(template.format("test"))

        print ("generateViewTemplate" + self.name)

    def generateViewModelTemplate(self):
        print ("generateViewModelTemplate")

    def generateViewAndViewModelTemplates(self):
        print("generateViewAndViewModelTemplates")


if __name__ == '__main__':
    generator = Generator("test")
    generator.generateViewTemplate()