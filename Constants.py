LeftBracket = '{'
RightBracket = '}'

EMPTYSTRING = ""

Interface = "Interface"
Mock = "Mock"
Test = "TEST"
Plus = "Plus"
Builder = "Builder"

TypeFeatureAll = "TypeFeatureAll"
TypeApplicationInterface = "TypeApplicationInterface"

TypeInterface = "Interface"
TypeConstants = "Constants"
TypeBootstrap = "Bootstrap"
TypeView = "View"
TypeViewModel = "ViewModel"
TypeTemplate = "Template"
TypeBootstrapConstants = "BootstrapConstants"
TypeViewMock = "ViewMock"
TypeViewModelMock = "ViewModelMock"
TypeViewInterface = "ViewInterface"
TypeViewModelInterface = "ViewModelInterface"
TypeViewTest = "View-TEST"
TypeViewModelTest = "ViewModel-TEST"
TypeBootstrapTest = "Bootstrap-TEST"

TypeBuilder = "Builder"
TypeBuilderConstants = "BuilderConstants"
TypeBuilderMock = "BuilderMock"

TypePlusTestHtmlMain = "PlusTestHtmlMain"
TypePlusApplicationBootstrap = "PlusApplicationBootstrap"

TemplateApplicationInterface = "./templates/InterfaceApplicationTemplate.txt"
TemplatePathConstant = "./templates/ConstantsTemplate.txt"
TemplatePathBootstrap = "./templates/BootstrapTemplate.txt"
TemplatePathView = "./templates/ViewTemplate.txt"
TemplatePathViewModel = "./templates/ViewModelTemplate.txt"
TemplatePathTemplate = "./templates/TemplateTemplate.txt"
TemplatePathBootstrapConstants = "./templates/ConstantsBootstrapTemplate.txt"
TemplatePathViewMock = "./templates/MockViewTemplate.txt"
TemplatePathViewModelMock = "./templates/MockViewModelTemplate.txt"
TemplatePathViewInterface = "./templates/InterfaceViewTemplate.txt"
TemplatePathViewModelInterface = "./templates/InterfaceViewModelTemplate.txt"
TemplatePathViewTest = "./templates/TestViewTemplate.txt"
TemplatePathViewModelTest = "./templates/TestViewModelTemplate.txt"
TemplatePathBootstrapTest = "./templates/TestBootstrapTemplate.txt"
TemplatePathApplicationBootstrapPlus = './templates/PlusApplicationBootstrapTemplate.txt'
TemplatePathTestHtmlMainPlus = "./templates/PlusTestHtmlMainTemplate.txt"
TemplatePathBuilder = "./templates/BuilderTemplate.txt"
TemplatePathBuilderConstants = './templates/ConstantsBuilderTemplate.txt'
TemplatePathBuilderMock = "./templates/MockBuilderTemplate.txt"

TemplatePathPage = "./templates/PageTemplate.txt"
TemplatePathBasicClass = "./templates/BasicClassTemplate.txt"
TemplatePathBasicBootstrap = "./templates/BasicBootstrapTemplate.txt"
TemplatePathBasicConstants = "./templates/BasicConstantsTemplate.txt"
TemplatePathBasicColumnFactory = "./templates/BasicColumnFactoryTemplate.txt"
TemplatePathBasicGridMetadata = "./templates/BasicGridMetadataTemplate.txt"
TemplatePathBasicRepository = "./templates/BasicRepositoryTemplate.txt"
TemplatePathBasicViewModel = "./templates/BasicViewModelTemplate.txt"
TemplatePathBasicView = "./templates/BasicViewTemplate.txt"
TemplatePathBasicBreadcrumbTemplate = "./templates/BasicBreadcrumbTemplateTemplate.txt"
TemplatePathBasicTemplate = "./templates/BasicTemplateTemplate.txt"
TemplatePathBasicGridView = "./templates/BasicGridViewTemplate.txt"

FILE_TYPE_Typescript = 0
FILE_TYPE_TypescriptDefinition = 1
FILE_TYPE_Content = 2

TYPE_STRING = 'string'
TYPE_NUMBER = 'number'
TYPE_BOOLEAN = 'boolean'

SuffixTS = ".ts"
SuffixHTM = ".htm"
SuffixDTS = ".d.ts"
SuffixJS = ".js"

CLASS_TYPE_BASIC = CLASS_TYPE_CONSTANTS = "CLASS_TYPE_BASIC"
CLASS_TYPE_BOOTSTRAP = "CLASS_TYPE_BOOTSTRAP"
CLASS_TYPE_PAGE = "CLASS_TYPE_PAGE"
CLASS_TYPE_COLUMN_FACTORY = "CLASS_TYPE_COLUMN_FACTORY"
CLASS_TYPE_REPOSITORY = "CLASS_TYPE_REPOSITORY"
CLASS_TYPE_GRID_METADATA = "CLASS_TYPE_GRID_METADATA"
CLASS_TYPE_GRID_VIEW = "CLASS_TYPE_GRID_VIEW"
CLASS_TYPE_VIEW = "CLASS_TYPE_VIEW"
CLASS_TYPE_VIEW_MODEL = "CLASS_TYPE_VIEW_MODEL"
CLASS_TYPE_TEMPLATE = "CLASS_TYPE_TEMPLATE"

TEMPLATES_PATHS = {
    CLASS_TYPE_BASIC: TemplatePathBasicClass,
    CLASS_TYPE_BOOTSTRAP: TemplatePathBasicBootstrap,
    CLASS_TYPE_PAGE: TemplatePathPage,
    CLASS_TYPE_COLUMN_FACTORY: TemplatePathBasicColumnFactory,
    CLASS_TYPE_REPOSITORY: TemplatePathBasicRepository,
    CLASS_TYPE_GRID_METADATA: TemplatePathBasicGridMetadata,
    CLASS_TYPE_VIEW: TemplatePathBasicView,
    CLASS_TYPE_VIEW_MODEL: TemplatePathBasicViewModel,
    CLASS_TYPE_GRID_VIEW: TemplatePathBasicGridView,
    CLASS_TYPE_TEMPLATE: TemplatePathBasicTemplate
}

UCM_ROOT = 'D:/Repo/UCM'
UCMA_Folder_Script_App = "/private/UI/UCMWeb/UCMWeb/Scripts/App"

UCM_A_PROJECT = 0
UCM_CORE_PROJECT = 1
UCM_B_PROJECT = 2

UCMA_CSPROJ_Path = UCM_ROOT + '/private/UI/UCMWeb/UCMWeb/Microsoft.UCM.Web.csproj'
UCMCORE_CSPROJ_PATH = UCM_ROOT + '/private/UI/UCMWeb/UCMWeb.TypeScript/Core/UCMWeb.TypeScript.Core.csproj'
UCMB_CSPROJ_PATH = UCM_ROOT + '/private/UI/UCMWeb/UCMWeb.TypeScript/BusinessReporting/UCMWeb.TypeScript.BusinessReporting.csproj'

UCM_CSPROJ_PATHS = [UCMA_CSPROJ_Path, UCMCORE_CSPROJ_PATH, UCMB_CSPROJ_PATH]

UCMA_GridColumnDefinition_Path = UCM_ROOT + UCMA_Folder_Script_App + '/GridColumnDefinition'

UCMA_ApplicationBootstrap_Path = UCM_ROOT + UCMA_Folder_Script_App + '/Common/ApplicationBootstrap.ts'
UCMA_ApplicationBootstrapConstants_Path = UCM_ROOT + UCMA_Folder_Script_App + '/Common/ApplicationBootstrapConstants.ts'
