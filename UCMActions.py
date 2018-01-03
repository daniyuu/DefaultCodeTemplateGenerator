import BasicActions
import Constants


class UCMActions:
    def __init__(self):
        self.ba = BasicActions.BasicActions()
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
        self.ba.insertCode(csprojPath, value, "<TypeScriptCompile", "<TypeScriptCompile")
        return

    def registerContentFile(self, csprojPath, fileRegisterPath):
        value = """\t<Content Include="{0}">\n""".format(fileRegisterPath.decode('string_escape'))
        self.ba.insertCode(csprojPath, value, "<Content", "<Content")
        return

    def addConstant(self, constantsFilePath, constantName, constantValue, constantType=Constants.TYPE_STRING):
        value = """\tpublic static {0}: {1} = "{2}";\n""".format(constantName, constantType, constantValue)
        self.ba.insertCode(constantsFilePath, value, "BEFORE", "}")
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
        self.ba.insertCodeByIndex(filePath, value, 0)
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

        self.ba.insertCode(bootstrapFilePath, value, context)

    def getVariableNameByClassName(self, className):
        variableName = className[0].lower() + className[1:]
        return variableName

    def getImportMapping(self):
        return self.importMapping

    def updateImportMapping(self, className, filePath):
        self.importMapping[className] = self.ba.getImportPathFromAbsolutePath(filePath)

    def createNewPage(self, workSpace, name):
        _workSpacePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App
        _featureFolderRoot = _workSpacePath + "/{0}".format(name)
        self.ba.createFolder(_featureFolderRoot)

        _bootstrapFilePath, _constantsFilePath = self.createNewFeatureBase(_featureFolderRoot, name)
        _columnsFilePath, _columnFactoryFilePath = self.createNewColumnFactory(name)

        _gridMetadataFilePath, _gridViewFilePath, _repositoryFilePath = self.createGridView(name, _featureFolderRoot,
                                                                                            _constantsFilePath,
                                                                                            _bootstrapFilePath)
        self.createBreadCrumb(name, _featureFolderRoot, _constantsFilePath, _bootstrapFilePath)
        self.createPage(name)
        self.createColumns(_columnFactoryFilePath, _columnsFilePath, _constantsFilePath)
        self.addColumns(_gridMetadataFilePath, _columnFactoryFilePath)

        return

    def setViewOptions(self, viewFilePath, viewModelName, templateName, constantsName):
        self.importDependency(viewFilePath, viewModelName)
        self.importDependency(viewFilePath, constantsName)
        value = "\t\t\tTemplateName: {0}.{1}Name,\n\t\t\tTemplatePath: {0}.{1}Path,\n\t\t\tViewModelName: {0}.{2}\n".format(
            constantsName, templateName, viewModelName)
        self.ba.insertCode(viewFilePath, value, "return <Ucm.Core.ViewOptions>{")
        return

    def registerNewDependency(self, bootstrapFilePath, constantsFilePath, dependencyName, isSinglton=False):
        self.addConstant(constantsFilePath, dependencyName, dependencyName)
        constantsFileName = self.ba.getDependencyNameFromPath(constantsFilePath)
        self.registerDependency(bootstrapFilePath, constantsFileName, dependencyName, isSinglton)
        return

    def addTemplate(self, breadCrumbTemplateName, breadCrumbTemplateFilePath, constantsFilePath):
        self.createClass(breadCrumbTemplateName, breadCrumbTemplateFilePath, Constants.CLASS_TYPE_TEMPLATE,
                         Constants.FILE_TYPE_Content)
        self.addConstant(constantsFilePath, breadCrumbTemplateName + "Name", breadCrumbTemplateName)

        self.addConstant(constantsFilePath, breadCrumbTemplateName + "Path",
                         self.ba.getImportPathFromAbsolutePath(breadCrumbTemplateFilePath))

        return

    def createColumns(self, columnFactoryFiltPath, columnsFilePath, constantsFilePath):
        while True:
            columnName = raw_input("Please Enter your column name, enter [exit] exit: ")
            if columnName == 'exit':
                columnsFileName = self.ba.getDependencyNameFromPath(columnsFilePath)
                self.importDependency(columnFactoryFiltPath, columnsFileName)
                break
            else:
                self.createColumn(columnFactoryFiltPath, columnsFilePath, constantsFilePath, columnName)
        return

    def createColumn(self, columnFactoryFiltPath, columnsFilePath, constantsFilePath, columnName):
        columnsFileName = self.ba.getDependencyNameFromPath(columnsFilePath)
        constantsFileName = self.ba.getDependencyNameFromPath(constantsFilePath)
        self.addConstant(columnsFilePath, columnName, columnName)
        self.addConstant(constantsFilePath, columnName, columnName)

        columnTypeMapping = ['Integer', 'Text', 'MultiSelectType', 'AstroTable', 'Date']
        value = """\t\tthis.AddColumnDefinition(\n"""
        columnType = input("Please choose column type: [0]Integer [1]Text [2]MultiSelectType [3]AstroTable [4]Date")
        if columnType > 4 or columnType < 0:
            columnType = 0
        width = input("Please enter the width of column (Default: 110): ")
        value += """\t\t\tthis.NewColumnDefinition({0}.{1}, Constants.{2}, {4}.{1}, {3})\n""".format(
            columnsFileName, columnName, columnTypeMapping[columnType], width, constantsFileName)
        value += """\t\t\t\t.WithDefaultHeader()\n"""
        value += """\t\t\t\t.Build());\n\n"""

        self.ba.insertCode(columnFactoryFiltPath, value, "private createColumnMetadataMapping():")

        return

    def addColumns(self, gridMetadataFilePath, columnFactoryFilePath):
        columnFactoryName = self.ba.getDependencyNameFromPath(columnFactoryFilePath)
        self.importDependency(gridMetadataFilePath, columnFactoryName)

        columnsContents = self.ba.readFile(columnFactoryFilePath)

        columnsFileNames = set([])
        index = 0
        for line in columnsContents:
            if "this.NewColumnDefinition" in line:
                index += 1
                columnsFileName, columnName = line.split('NewColumnDefinition(')[1].split(',')[0].split('.')
                insertFlag = input("Do you want to add {0} column to this grid? 1-Yes, 2-No".format(columnName))
                if insertFlag == 1:
                    columnsFileNames.add(columnsFileName)
                    value = "\t\t\tthis.{0}.CreateColumn({1}.{2}, {3}),\n".format(
                        self.getVariableNameByClassName(columnFactoryName), columnsFileName, columnName, index)

                    self.ba.insertCode(gridMetadataFilePath, value, "this.GridColumns = [")

        for className in columnsFileNames:
            self.importDependency(gridMetadataFilePath, className)

        return

    def createGridView(self, name, folderRoot, _constantsFilePath, _bootstrapFilePath):
        _gridMetadataName = name + "Grid"
        _gridViewName = name + "View"
        _repositoryName = name + "Repository"
        _gridMetadataFilePath = folderRoot + "/{0}Grid.ts".format(name)

        _gridViewFilePath = folderRoot + "/{0}View.ts".format(name)
        _constantsFilePath = folderRoot + "/{0}Constants.ts".format(name)
        _repositoryFilePath = folderRoot + "/{0}Repository.ts".format(name)
        self.createClass(_gridMetadataName, _gridMetadataFilePath, Constants.CLASS_TYPE_GRID_METADATA)
        self.addConstant(Constants.UCMA_AgentWorkspaceGridNames_Path, name, name)
        self.createClass(_gridViewName, _gridViewFilePath, Constants.CLASS_TYPE_GRID_VIEW)
        self.addConstant(_constantsFilePath, name + "Container",
                         "#" + self.getVariableNameByClassName(name) + '-content')
        self.createClass(_repositoryName, _repositoryFilePath, Constants.CLASS_TYPE_REPOSITORY)

        self.registerNewDependency(_bootstrapFilePath, _constantsFilePath, _gridViewName)
        self.registerNewDependency(_bootstrapFilePath, _constantsFilePath, _gridMetadataName)
        self.registerNewDependency(_bootstrapFilePath, _constantsFilePath, _repositoryName, True)

        return _gridMetadataFilePath, _gridViewFilePath, _repositoryFilePath

    def createPage(self, name):
        _pageName = name + "Page"
        _pageFilePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App + "/{0}.ts".format(_pageName)
        self.createClass(_pageName, _pageFilePath, Constants.CLASS_TYPE_PAGE)
        pageValue = "\t\t\t{0}: $(#{1}-content),\n".format(name, self.getVariableNameByClassName(name))
        self.ba.insertCode(Constants.UCM_APPBOOTSTRAPPER_PATH, pageValue, "Content: {")
        applicationValue = "\t\t\tAgentWorkspaceCommonBootstrapConstants.{0},\n".format(_pageName)
        self.ba.insertCode(Constants.UCM_APPLICATION_PATH, applicationValue,
                           "AgentWorkspaceCommonBootstrapConstants.FeaturePilotReadOnlyPage,")
        contentValue = "\t\t{0}?: JQuery;\n".format(_pageName)
        self.ba.insertCode(Constants.UCM_ContentCollection_PATH, contentValue, "BlockManagement?: JQuery;")

        # Register page
        self.addConstant(Constants.UCMA_AgentWorkspaceCommonBootstrapConstants_Path, _pageName, _pageName)
        self.registerDependency(Constants.UCMA_AgentWorkspaceCommonBootstrap_Path, "CommonBootstrapConstants",
                                _pageName,
                                True)

        self.addDivToIndex(_pageName)
        self.addPageLevelLoadingMask(name)
        self.registerRouting(name)

        return

    def addDivToIndex(self, pageName):
        indexValue = """\t<div class="container body-content" id="{0}-content">\n\t\t<div id="{0}-loading-mask" class="container">\n\t\t\t<span class="k-loading-text"></span>\n\t\t\t<div class="k-loading-image"></div>\n\t\t</div>\n\t</div>\n\n""".format(
            self.getVariableNameByClassName(pageName))
        self.ba.insertCode(Constants.UCM_Index_cshtml_path, indexValue, "\n",
                           """<div class="container body-content" id="validate-error-content">""")
        return

    def addPageLevelLoadingMask(self, name):
        definition = """\tpublic static {0}LoadingMask = "#{1}-loading-mask";\n""".format(name,
                                                                                          self.getVariableNameByClassName(
                                                                                              name))
        self.ba.insertCode(Constants.UCM_CORE_KendoGridExtensions_Path, definition,
                           """public static TacticReadOnlyLoadingMask = "#tacticRO-loading-mask";""")
        hideValue = """\t\tKendoGridExtensions.HideLoadingMask($(KendoGridExtensions.{0}LoadingMask));\n""".format(name)
        self.ba.insertCode(Constants.UCM_CORE_KendoGridExtensions_Path, hideValue,
                           "KendoGridExtensions.HideLoadingMask($(KendoGridExtensions",
                           "KendoGridExtensions.HideLoadingMask($(KendoGridExtensions")
        showValue = """\t\t$(KendoGridExtensions.{0}LoadingMask).show();\n""".format(name)
        self.ba.insertCode(Constants.UCM_CORE_KendoGridExtensions_Path, showValue,
                           "$(KendoGridExtensions.TacticReadOnlyLoadingMask).show();")
        return

    def registerRouting(self, name):
        value = """\tpublic static {2}Route: Ucm.Route.RouteMetadataV2 = {0}
        \t\tRouteTemplate: "/{2}",
        \t\tRouterName: RoutingConstants.{2}Event,
        \t\tPageKey: RoutingConstants.{2}Page
    {1}\n""".format(Constants.LeftBracket, Constants.RightBracket, name)
        self.ba.insertCodeAtTail(Constants.UCM_CORE_RoutingMetadata, value)
        self.addConstant(Constants.UCM_CORE_RoutingConstants, name + "Event", name)
        self.addConstant(Constants.UCM_CORE_RoutingConstants, name + "Page", name + "Page")
        self.ba.insertCode(Constants.UCMA_AgentWorkspaceRouteRegistrantV2_Path,
                           "\t\t\tRoutingMetadataV2.{0}Route,\n".format(name),
                           "RoutingMetadataV2.TacticReadOnlyRoute,")

    def createExposureKey(self, constantsFilePath, exposureKeyName):
        exposureKeyConstantsName = exposureKeyName + "_ExposureKey"
        configKeyConstantsName = exposureKeyName + "_ConfigKey"
        exposureKeyConstantsValue = exposureKeyName
        configKeyConstantsValue = exposureKeyName + "_Enabled"
        self.addConstant(constantsFilePath, exposureKeyConstantsName, exposureKeyConstantsValue)
        self.addConstant(constantsFilePath, configKeyConstantsName, configKeyConstantsValue)
        exposureKeyValue = """\t('{0}', NULL),\n""".format(exposureKeyConstantsValue)
        configValue = """\t<add key="{0}" value="false" />\n""".format(configKeyConstantsValue)
        self.ba.insertCode(Constants.UCM_EXPOSUREKEY_SQL_PATH, exposureKeyValue,
                           "('Feature_661973_AccountTeamMembersSort', NULL),")
        self.ba.insertCodeByIndex(Constants.UCM_WEBCONFIG_PATH, configValue, 337)

        return

    def createNewFeatureBase(self, featureFolderPath, testFolderRoot, featureName):
        _bootstrapName = featureName + "Bootstrap"
        _constantsName = featureName + "Constants"

        _bootstrapFilePath = featureFolderPath + "/{0}Bootstrap.ts".format(featureName)
        _constantsFilePath = featureFolderPath + "/{0}Constants.ts".format(featureName)
        self.createClass(featureName + "Bootstrap", _bootstrapFilePath, Constants.CLASS_TYPE_BOOTSTRAP)
        self.createClass(featureName + "Constants", _constantsFilePath, Constants.CLASS_TYPE_CONSTANTS)

        # Register bootstrap
        self.addConstant(Constants.UCMA_ApplicationBootstrapConstants_Path, _bootstrapName, _bootstrapName)
        self.registerDependency(Constants.UCMA_ApplicationBootstrap_Path, "ApplicationBootstrapConstants",
                                _bootstrapName, True)

        self.importDependency(_bootstrapFilePath, _constantsName)

        self.UT_ApplicationBootstrap(_bootstrapName)
        self.UT_Basic(testFolderRoot, _bootstrapFilePath, Constants.TEST_TYPE_BOOTSTRAP_TEMPLATE)

        return _bootstrapFilePath, _constantsFilePath

    def createNewColumnFactory(self, name):
        _columnFactoryFilePath = Constants.UCMA_GRIDCOUMNDEFINITION_FOLDER_PATH + "/{0}ColumnFactory.ts".format(name)
        _columnsFilePath = Constants.UCMA_GRIDCOUMNDEFINITION_FOLDER_PATH + "/{0}Columns.ts".format(name)

        self.createClass(name + "Columns", _columnsFilePath, Constants.CLASS_TYPE_BASIC)
        self.createClass(name + "ColumnFactory", _columnFactoryFilePath, Constants.CLASS_TYPE_COLUMN_FACTORY)
        self.addConstant(Constants.UCMA_AgentWorkspaceGridColumnBootstrapConstants_Path, name + "ColumnFactory",
                         name + "ColumnFactory")
        self.registerDependency(Constants.UCMA_AgentWorkspaceGridColumnBootstrap_Path,
                                self.ba.getDependencyNameFromPath(
                                    Constants.UCMA_AgentWorkspaceCommonBootstrapConstants_Path), name + "ColumnFactory")
        return _columnsFilePath, _columnFactoryFilePath

    def createBreadCrumb(self, name, featureFolderRoot, _constantsFilePath, _bootstrapFilePath):
        _constantsName = self.ba.getDependencyNameFromPath(_constantsFilePath)
        _breadCrumbViewName = name + "BreadCrumbView"
        _breadCrumbViewModelName = name + "BreadCrumbViewModel"
        _breadCrumbTemplateName = name + "BreadCrumbTemplate"

        _breadCrumbViewFilePath = featureFolderRoot + "/{0}BreadCrumbView.ts".format(name)
        _breadCrumbTemplateFilePath = featureFolderRoot + "/{0}BreadCrumbTemplate.htm".format(name)
        _breadCrumbViewModelFilePath = featureFolderRoot + "/{0}BreadCrumbViewModel.ts".format(name)

        self.createClass(name + "BreadCrumbView", _breadCrumbViewFilePath, Constants.CLASS_TYPE_VIEW)
        self.createClass(name + "BreadCrumbViewModel", _breadCrumbViewModelFilePath,
                         Constants.CLASS_TYPE_VIEW_MODEL)
        self.addTemplate(_breadCrumbTemplateName, _breadCrumbTemplateFilePath, _constantsFilePath)

        self.registerNewDependency(_bootstrapFilePath, _constantsFilePath, _breadCrumbViewName)
        self.registerNewDependency(_bootstrapFilePath, _constantsFilePath, _breadCrumbViewModelName)
        self.setViewOptions(_breadCrumbViewFilePath, _breadCrumbViewModelName, _breadCrumbTemplateName, _constantsName)

        return

    def createNewTab(self, folderRoot, testFolderRoot, name, exposureKeyName):
        _bootstrapFilePath, _constantsFilePath = self.createNewFeatureBase(folderRoot, testFolderRoot, name)
        self.createExposureKey(_constantsFilePath, exposureKeyName)
        return

    def UT_ApplicationBootstrap(self, bootStrapName):
        self.importDependency(Constants.TEST_ApplicationBootstrap_Path, bootStrapName)
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
        self.createFileByTemplate(templatePath, filePath, feataureName)
        self.registerCsproj(workSpace, Constants.FILE_TYPE_Typescript, filePath)
        return
