import UCMActions
import Constants
import BasicActions


class UnitTestGenerator:
    def __init__(self):
        self.ua = UCMActions.UCMActions()
        self.ba = BasicActions.BasicActions()
        return

    def UT_ApplicationBootstrap(self, bootStrapName):
        self.ua.importDependency(Constants.TEST_ApplicationBootstrap_Path, bootStrapName)
        expectValue = """\t\texpect(createStub).to.be.calledWith(ApplicationBootstrapConstants.{0});\n""".format(
            bootStrapName)
        self.ba.insertCode(Constants.TEST_ApplicationBootstrap_Path, expectValue,
                           """expect(createStub).to.be.calledWith(ApplicationBootstrapConstants.FeaturePilotReadOnlyBootstrap);""")
        expectValue2 = """\t\texpect(castStub.calledWith({0})).to.be.true();\n""".format(bootStrapName)

        self.ba.insertCode(Constants.TEST_ApplicationBootstrap_Path, expectValue2,
                           """expect(castStub.calledWith(FeaturePilotReadOnlyBootstrap)).to.be.true();""")

    def UT_BasicBootScript(self, bootStrapFilePath):
        return

    def UT_Basic(self, testFolderRoot, relatedClassFilePath, testType=Constants.TEST_TYPE_BASIC_UT_TEMPLATE):
        workSpace = Constants.UCM_A_PROJECT
        feataureName = self.ba.getDependencyNameFromPath(relatedClassFilePath)
        filePath = testFolderRoot + "/{0}-Test.ts".format(feataureName)
        templatePath = Constants.TEST_TEMPLATES_PATHS[testType]
        self.ua.createFileByTemplate(templatePath, filePath, feataureName)
        self.ua.registerCsproj(workSpace, Constants.FILE_TYPE_Typescript, filePath)
        return
