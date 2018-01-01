import BasicActions
import Constants


class UCMActions:
    def __init__(self):
        self.basicActions = BasicActions.BasicActions()
        self.importMapping = {}
        return

    def registerCsproj(self, workSpace, fileType, filePath):
        csprojPath = Constants.UCM_CSPROJ_PATHES[workSpace]
        fileRegisterPath = "Scripts" + filePath.split("Scripts")[1].replace("/", "\\")
        if fileType == Constants.FILE_TYPE_Typescript or fileType == Constants.FILE_TYPE_TypescriptDefinition:
            self.registerTSFile(csprojPath, fileRegisterPath)
        else:
            self.registerContentFile(csprojPath, fileRegisterPath)
        return

    def registerTSFile(self, csprojPath, fileRegisterPath):
        value = """\t<TypeScriptCompile Include="{0}">\n""".format(fileRegisterPath.decode('string_escape'))
        self.basicActions.insertCode(csprojPath, value, "<TypeScriptCompile", "<TypeScriptCompile")
        return

    def registerContentFile(self, csprojPath, fileRegisterPath):
        value = """\t<Content Include="{0}">\n""".format(fileRegisterPath.decode('string_escape'))
        self.basicActions.insertCode(csprojPath, value, "<Content", "<Content")
        return

    def addConstant(self, constantsFilePath, constantName, constantValue, constantType=Constants.TYPE_STRING):
        value = """\tpublic static {0}: {1} = "{2}";\n""".format(constantName, constantType, constantValue)
        self.basicActions.insertCode(constantsFilePath, value, "BEFORE", "}")
        return

    def createClass(self, className, filePath, classType, fileType=Constants.FILE_TYPE_Typescript,
                    workSpace=Constants.UCM_A_PROJECT):
        templatePath = Constants.TEMPLATES_PATHS[classType]
        self.createFileByTemplate(templatePath, filePath, className)
        self.registerCsproj(workSpace, fileType, filePath)
        self.updateImportMapping(className, filePath)
        return

    def createFileByTemplate(self, templatePath, filePath, className):
        variable_name = self.getVariableNameByClassName(className)

        fh = open(templatePath)
        template = fh.read()
        fh.close()

        fo = open(filePath, "w")
        fo.write(
            template.format(Constants.LeftBracket, Constants.RightBracket, className, variable_name))
        fo.close()

        return

    def importDependency(self, filePath, className):
        value = """import {0} = require("{1}");\n""".format(className, self.importMapping[className])
        self.basicActions.insertCodeByIndex(filePath, value, 0)
        return

    def registerDependency(self, bootstrapFilePath, constantsFileName, dependencyName, isSingleton=False):
        self.importDependency(bootstrapFilePath, dependencyName)
        value = """\t\tthis.constructorMapping[{0}.{1}] = this.typeConstructorCasting.Cast({1});\n""".format(
            constantsFileName, dependencyName)
        context = "public SetConstructorMapping()"
        if isSingleton:
            value = """\t\tthis.singletonConstructorMapping[{0}.{1}] = this.typeConstructorCasting.Cast({1});\n""".format(
                constantsFileName, dependencyName)
            context = "public SetSingletonConstructorMapping()"

        self.basicActions.insertCode(bootstrapFilePath, value, context)

    def getVariableNameByClassName(self, className):
        variableName = className[0].lower() + className[1:]
        return variableName

    def getImportMapping(self):
        return self.importMapping

    def updateImportMapping(self, className, filePath):
        importPath = ""
        flag = False
        for item in filePath.split('/'):
            if item == 'Core' or item == 'App':
                flag = True
            if flag:
                if 'Core' in importPath:
                    continue
                importPath += item.split('.')[0] + "/"

        self.importMapping[className] = importPath[:-1]
