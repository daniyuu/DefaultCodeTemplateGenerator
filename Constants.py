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
TemplatePathBasicUT = "./templates/BasicUTTemplate.txt"
TemplatePathBootstrapUT = "./templates/BootstrapUTTemplate.txt"

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
TEST_TYPE_BASIC_UT_TEMPLATE = "TEST_TYPE_BASIC_UT_TEMPLATE"
TEST_TYPE_BOOTSTRAP_TEMPLATE = "TEST_TYPE_BOOTSTRAP_TEMPLATE"

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
    CLASS_TYPE_TEMPLATE: TemplatePathBasicTemplate,

}

TEST_TEMPLATES_PATHS = {
TEST_TYPE_BASIC_UT_TEMPLATE: TemplatePathBasicUT,
TEST_TYPE_BOOTSTRAP_TEMPLATE: TemplatePathBootstrapUT
}

UCM_ROOT = 'D:/Repo/UCM'
UCMA_Folder_Script_App = "/private/UI/UCMWeb/UCMWeb/Scripts/App"
UCMA_Folder_Script_Tests = "/private/UI/UCMWeb/UCMWeb/Scripts/Tests"

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

UCMA_AgentWorkspaceCommonBootstrapConstants_Path = UCM_ROOT + UCMA_Folder_Script_App + '/Common/AgentWorkspaceCommonBootstrapConstants.ts'

UCMA_AgentWorkspaceCommonBootstrap_Path = UCM_ROOT + UCMA_Folder_Script_App + '/Common/AgentWorkspaceCommonBootstrap.ts'

UCMA_AgentWorkspaceGridNames_Path = UCM_ROOT + UCMA_Folder_Script_App + '/Grid/AgentWorkspaceGridNames.ts'

UCMA_AgentWorkspaceGridColumnBootstrap_Path = UCM_ROOT + UCMA_Folder_Script_App + '/GridColumnDefinition/AgentWorkspaceGridColumnBootstrap.ts'

UCMA_AgentWorkspaceGridColumnBootstrapConstants_Path = UCM_ROOT + UCMA_Folder_Script_App + '/GridColumnDefinition/AgentWorkspaceGridColumnBootstrapConstants.ts'

UCMA_GRIDCOUMNDEFINITION_FOLDER_PATH = UCM_ROOT + UCMA_Folder_Script_App + '/GridColumnDefinition'

UCM_APPBOOTSTRAPPER_PATH = UCM_ROOT + UCMA_Folder_Script_App + "/appBootstrapper.ts"

UCM_APPLICATION_PATH = UCM_ROOT + UCMA_Folder_Script_App + "/Application.ts"
UCM_ContentCollection_PATH = UCM_ROOT + UCMA_Folder_Script_App + "/ContentCollection.d.ts"
UCM_Index_cshtml_path = UCM_ROOT + "/private/UI/UCMWeb/UCMWeb/Views/AgentWorkspace/Index.cshtml"

UCM_CORE_Path = UCM_ROOT + "/private/UI/UCMWeb/UCMWeb.TypeScript/Core/Core"

UCM_CORE_Grid_Path = UCM_CORE_Path + '/Grid'
UCM_CORE_KendoGridExtensions_Path = UCM_CORE_Grid_Path + '/KendoGridExtensions.ts'
UCM_CORE_RoutingMetadata = UCM_CORE_Path + "/Metadata/RoutingMetadataV2.ts"
UCM_CORE_RoutingConstants = UCM_CORE_Path + "/Routing/RoutingConstants.ts"
UCMA_AgentWorkspaceRouteRegistrantV2_Path = UCM_ROOT + UCMA_Folder_Script_App + "/Routing/AgentWorkspaceRouteRegistrantV2.ts"

UCM_EXPOSUREKEY_SQL_PATH = UCM_ROOT + "/private/Database/UcmData/Deployment/PopulateUserPreferenceAndExposureKeysData.sql"

UCM_WEBCONFIG_PATH = UCM_ROOT + "/private/UI/UCMWeb/UCMWeb/Web.config"

TEST_ApplicationBootstrap_Path = UCM_ROOT + UCMA_Folder_Script_Tests + '/Common/ApplicationBootstrap-Test.ts'
