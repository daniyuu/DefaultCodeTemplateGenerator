import Constants
import os


class Generator:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.dir = os.path.dirname(__file__)
        if not os.path.exists(self.name):
            os.mkdir(self.name)

    def execute(self):
        if self.type == Constants.TypeFeatureAll:
            self.generateAll()
        if self.type == Constants.TypeApplicationInterface:
            self.generate(Constants.TypeInterface, Constants.TemplateApplicationInterface, Constants.SuffixTS)
        if self.type == Constants.TypeBuilder:
            self.generateBuilder()

    def generateAll(self):
        print('Generator all files about {0}'.format(self.name))
        # class part
        # constants
        self.generate(Constants.TypeConstants, Constants.TemplatePathConstant, Constants.SuffixTS)
        # bootstrap
        self.generate(Constants.TypeBootstrap, Constants.TemplatePathBootstrap, Constants.SuffixTS)
        # view
        self.generate(Constants.TypeView, Constants.TemplatePathView, Constants.SuffixTS)
        # viewModel
        self.generate(Constants.TypeViewModel, Constants.TemplatePathViewModel, Constants.SuffixTS)
        # template
        self.generate(Constants.TypeTemplate, Constants.TemplatePathTemplate, Constants.SuffixHTM)
        # bootstrapConstants
        self.generate(Constants.TypeBootstrapConstants, Constants.TemplatePathBootstrapConstants, Constants.SuffixTS)

        # mock part
        # view Mock
        self.generate(Constants.TypeViewMock, Constants.TemplatePathViewMock, Constants.SuffixTS)
        # viewModel Mock
        self.generate(Constants.TypeViewModelMock, Constants.TemplatePathViewModelMock, Constants.SuffixTS)

        # interface part
        # view interface
        self.generate(Constants.TypeViewInterface, Constants.TemplatePathViewInterface, Constants.SuffixDTS)
        # viewModel interface
        self.generate(Constants.TypeViewModelInterface, Constants.TemplatePathViewModelInterface, Constants.SuffixDTS)

        # test part
        # view test
        self.generate(Constants.TypeViewTest, Constants.TemplatePathViewTest, Constants.SuffixTS)
        # view Model test
        self.generate(Constants.TypeViewModelTest, Constants.TemplatePathViewModelTest, Constants.SuffixTS)
        # bootstrap test
        self.generate(Constants.TypeBootstrapTest, Constants.TemplatePathBootstrapTest, Constants.SuffixTS)

        # plus
        # application bootstrap
        self.generate(Constants.TypePlusApplicationBootstrap, Constants.TemplatePathApplicationBootstrapPlus,
                      Constants.SuffixTS)
        self.generate(Constants.TypePlusTestHtmlMain, Constants.TemplatePathTestHtmlMainPlus, Constants.SuffixJS)

    def generateBuilder(self):
        # class part
        # class
        self.generate(Constants.TypeBuilder, Constants.TemplatePathBuilder, Constants.SuffixTS)
        # constants
        self.generate(Constants.TypeBuilderConstants, Constants.TemplatePathBuilderConstants, Constants.SuffixTS)

        # Mork part
        self.generate(Constants.TypeBuilderMock, Constants.TemplatePathBuilderMock, Constants.SuffixTS)

        # Test part


        # interface part


    def generate(self, type, templatePath, suffix):
        fh = open(templatePath)
        template = fh.read()
        fh.close()

        outputPath = "./" + self.name

        if Constants.Mock in type:
            if not os.path.exists(self.name + "/" + Constants.Mock):
                os.mkdir(self.name + "/" + Constants.Mock)
            outputPath = outputPath + "/" + Constants.Mock

        if Constants.Interface in type:
            if not os.path.exists(self.name + "/" + Constants.Interface):
                os.mkdir(self.name + "/" + Constants.Interface)
            outputPath = outputPath + "/" + Constants.Interface

        if Constants.Test in type:
            if not os.path.exists(self.name + "/" + Constants.Test):
                os.mkdir(self.name + "/" + Constants.Test)
            outputPath = outputPath + "/" + Constants.Test

        if Constants.Plus in type:
            if not os.path.exists(self.name + "/" + Constants.Plus):
                os.mkdir(self.name + "/" + Constants.Plus)
            outputPath = outputPath + "/" + Constants.Plus

        fo = open(outputPath + "/" + self.name + type + suffix, "w")
        fo.write(template.format(self.name, Constants.LeftBracket, Constants.RightBracket,
                                 self.name[0].lower() + self.name[1:]))
        fo.close()

        print ("[Finish] {0} of {1}".format(type, self.name))

    def generateViewTemplate(self):
        fh = open('TestTemplate.txt')
        template = fh.read()

        fo = open(self.name + ".ts", "w")
        ViewTemplate = """{0}
            {0}""" \
            .format("hahahahah")
        fo.write(template.format("test"))

        print ("generateViewTemplate" + self.name)

    def generateViewModelTemplate(self):
        print ("generateViewModelTemplate")

    def generateViewAndViewModelTemplates(self):
        print("generateViewAndViewModelTemplates")


if __name__ == '__main__':
    generator = Generator(Constants.TypeBuilder, "Cyy")
    generator.execute()
