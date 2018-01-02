import BasicActions
import Constants


class UCMActions:
    def __init__(self):
        self.basicActions = BasicActions.BasicActions()
        self.importMapping = {}
        return

    def registerCsproj(self, workSpace, fileType, filePath):
        csprojPath = Constants.UCM_CSPROJ_PATHS[workSpace]
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

    def createNewPage(self, workSpace, pageName):
        _workSpacePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App
        _featureFolderRoot = _workSpacePath + "/{0}".format(pageName)
        _bootstrapFilePath = _featureFolderRoot + "/{0}Bootstrap.ts".format(pageName)
        _constantsFilePath = _featureFolderRoot + "/{0}Constants.ts".format(pageName)
        _columnFactoryFilePath = _featureFolderRoot + "/{0}ColumnFactory.ts".format(pageName)
        _columnsFilePath = _featureFolderRoot + "/{0}Columns.ts".format(pageName)
        _gridMetadataFilePath = _featureFolderRoot + "/{0}Grid.ts".format(pageName)
        _repositoryFilePath = _featureFolderRoot + "/{0}Repository.ts".format(pageName)
        _breadCrumbViewFilePath = _featureFolderRoot + "/{0}BreadCrumbView.ts".format(pageName)
        _breadCrumbTemplateFilePath = _featureFolderRoot + "/{0}BreadCrumbTemplate.htm".format(pageName)
        _breadCrumbViewModelFilePath = _featureFolderRoot + "/{0}BreadCrumbViewModel.ts".format(pageName)
        _gridViewFilePath = _featureFolderRoot + "/{0}View.ts".format(pageName)
        _pageFilePath = _featureFolderRoot + "/{0}Page.ts".format(pageName)

        self.basicActions.createFolder(_featureFolderRoot)

        self.createClass(pageName + "Bootstrap", _bootstrapFilePath, Constants.CLASS_TYPE_BOOTSTRAP)
        self.createClass(pageName + "Constants", _constantsFilePath, Constants.CLASS_TYPE_CONSTANTS)
        self.createClass(pageName + "Columns", _columnsFilePath, Constants.CLASS_TYPE_BASIC)
        self.createClass(pageName + "ColumnFactory", _columnFactoryFilePath, Constants.CLASS_TYPE_COLUMN_FACTORY)
        self.createClass(pageName + "Grid", _gridMetadataFilePath, Constants.CLASS_TYPE_GRID_METADATA)
        self.createClass(pageName + "Repository", _repositoryFilePath, Constants.CLASS_TYPE_REPOSITORY)
        self.createClass(pageName + "View", _gridViewFilePath, Constants.CLASS_TYPE_GRID_VIEW)
        self.createClass(pageName + "BreadCrumbView", _breadCrumbViewFilePath, Constants.CLASS_TYPE_VIEW)
        self.createClass(pageName + "BreadCrumbViewModel", _breadCrumbViewModelFilePath,
                         Constants.CLASS_TYPE_VIEW_MODEL)
        self.createClass(pageName + "BreadCrumbTemplate", _breadCrumbTemplateFilePath, Constants.CLASS_TYPE_TEMPLATE,Constants.FILE_TYPE_Content)
        self.createClass(pageName + "Page", _pageFilePath, Constants.CLASS_TYPE_PAGE)

        return
    #
# filePath = "D:/Repo/UCM/private/UI/UCMWeb/UCMWeb/Scripts/App/NewFeature.ts"
#
# ua = UCMActions()
# # ua.createClass("NewFeature", filePath, Constants.CLASS_TYPE_REPOSITORY)
#
# bootstrapFilePath = "D:/Repo/UCM/private/UI/UCMWeb/UCMWeb/Scripts/App/Common/AgentWorkspaceCommonBootstrap.ts"
