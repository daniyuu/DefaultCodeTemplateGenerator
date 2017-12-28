import Constants
import BasicTool

pageName = ''
workSpace = 1
workSpacePath = Constants.UCM_ROOT
featureFolderRoot = ''


def generate_page_file(folder_path, page_name):
    print "Staring generate page file"
    templatePath = Constants.TemplatePathPage
    fh = open(templatePath)
    template = fh.read()
    fh.close()

    fo = open(folder_path + "{0}Page.ts".format(page_name), "w")
    fo.write(
        template.format(Constants.LeftBracket, Constants.RightBracket, page_name, page_name[0].lower() + page_name[1:]))
    fo.close()
    print "[Finished] Generate {0}Page.ts file".format(page_name)


def generate_basic_class(folder_path, name):
    templatePath = Constants.TemplatePathBasicClass
    file_path = folder_path + "/{0}.ts".format(name)
    basicTool.create_a_new_file(templatePath, file_path, name)
    return file_path


def generate_constants(folder_path, name):
    templatePath = Constants.TemplatePathBasicConstants
    file_path = folder_path + "/{0}Constants.ts".format(name)
    basicTool.create_a_new_file(templatePath, file_path, name)
    return file_path


def generate_bootstrap(folder_path, name):
    templatePath = Constants.TemplatePathBasicBootstrap
    file_path = folder_path + "/{0}Bootstrap.ts".format(name)
    basicTool.create_a_new_file(templatePath, file_path, name)

    # Generate a constants file for bootstrap
    generate_constants(folder_path, name + "Bootstrap")

    applicationBootstrapConstantsFilePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App + '/Common/ApplicationBootstrapConstants.ts'
    value = """\tpublic static {0}Bootstrap: string = "{0}Bootstrap";\n""".format(name)
    basicTool.insertCode(applicationBootstrapConstantsFilePath, "}", value, True)
    applicationBootstrapFilePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App + '/Common/ApplicationBootstrap.ts'

    basicTool.importDependency(applicationBootstrapFilePath, name + "Bootstrap")
    mappingVaule = """\t\tthis.singletonConstructorMapping[ApplicationBootstrapConstants.{0}Bootstrap] = this.typeConstructorCasting.Cast({0}Bootstrap);\n""".format(
        name)
    basicTool.insertCode(applicationBootstrapFilePath, "public SetSingletonConstructorMapping()", mappingVaule)

    return file_path


def generate_gridMetadata(folder_path, name):
    templatePath = Constants.TemplatePathBasicGridMetadata
    file_path = folder_path + "/{0}Grid.ts".format(name)
    basicTool.create_a_new_file(templatePath, file_path, name)
    return file_path


def generate_columnFactory(folder_path, name):
    templatePath = Constants.TemplatePathBasicColumnFactory
    file_path = folder_path + "/{0}ColumnFactory.ts".format(name)
    basicTool.create_a_new_file(templatePath, file_path, name)
    return file_path


def get_workspace():
    _workSpace = input("UCMA enter 1, UCMB enter 2: ")
    if _workSpace is 1:
        _workSpacePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App
    return _workSpace, _workSpacePath


def get_page_name():
    _pageName = raw_input("Please Enter your page name: ")
    _featureFolderRoot = workSpacePath + "/{0}".format(_pageName)
    return _pageName, _featureFolderRoot


def create_new_folder():
    basicTool.create_folder(featureFolderRoot)
    return


def add_column_to_columnsFile(columns_file_path, column_name):
    value = """\tpublic static {0}: string = "{0}";\n""".format(column_name)
    basicTool.insertCode(columns_file_path, "class ", value)


def add_a_constant(constants_file_path, constantName, constantValue):
    value = """\tpublic static {0}: string = "{1}";\n""".format(constantName, constantValue)
    basicTool.insertCode(constants_file_path, "{", value)


def add_column_definition(columnfactory_file_path, column_name):
    columnsFileName = columnfactory_file_path.split('/')[-1].split('ColumnFactory')[0]
    column_type_mapping = ['Integer', 'Text', 'MultiSelectType', 'AstroTable', 'Date']
    value = """\t\tthis.AddColumnDefinition(\n"""
    column_type = input("Please choose column type: [0]Integer [1]Text [2]MultiSelectType [3]AstroTable [4]Date")
    if column_type > 4 or column_type < 0:
        column_type = 0
    width = input("Please enter the width of column (Default: 110): ")
    value += """\t\t\tthis.NewColumnDefinition({0}Columns.{1}, Constants.{2}, {0}Constants.{0}, {3})\n""".format(
        columnsFileName, column_name, column_type_mapping[column_type], width)
    value += """\t\t\t\t.WithDefaultHeader()\n"""
    value += """\t\t\t\t.Build());\n\n"""

    basicTool.insertCode(columnfactory_file_path, "private createColumnMetadataMapping():", value)

    return


def create_column(columns_file_path, columnfactory_file_path, column_name, constants_file_path):
    add_column_to_columnsFile(columns_file_path, column_name)
    add_a_constant(constants_file_path, column_name, column_name)
    add_column_definition(columnfactory_file_path, column_name)
    return


def create_columns(columns_file_path, columnfactory_file_path, constants_file_path):
    while True:
        columnName = raw_input("Please Enter your column name, enter [exit] exit: ")
        if columnName == 'exit':
            break
        else:
            create_column(columns_file_path, columnfactory_file_path, columnName, constants_file_path)
    return


def insert_a_column(gridMetadataFilePath, columnFactoryName, columnsFileName, columnName, index):
    value = "\t\t\tthis.{0}.CreateColumn({1}.{2}, {3}),\n".format(
        basicTool.getVariableNameByClassName(columnFactoryName), columnsFileName, columnName, index)
    basicTool.insertCode(gridMetadataFilePath, "this.GridColumns = [", value)
    return


def insert_columns_into_gridMetadata(columnFactoryFilePath, gridMetadataFilePath):
    fh = open(columnFactoryFilePath)
    columnsContents = fh.readlines()
    fh.close()
    columnsFileNames = set([])
    columnFactoryName = columnFactoryFilePath.split('/')[-1].split('.')[0]

    index = 0
    for line in columnsContents:
        if "this.NewColumnDefinition" in line:
            index += 1
            columnsFileName, columnName = line.split('NewColumnDefinition(')[1].split(',')[0].split('.')
            insertFlag = input("Do you want to add {0} column to this grid? 1-Yes, 2-No".format(columnName))
            if insertFlag == 1:
                columnsFileNames.add(columnsFileName)
                insert_a_column(gridMetadataFilePath, columnFactoryName, columnsFileName, columnName, index)

    for className in columnsFileNames:
        basicTool.importDependency(gridMetadataFilePath, className)
    return


basicTool = BasicTool.BasicTool()
# generate_page_file(pageNewFolderPath, pageName)
STEP_INFO = "************Step {0}: {1}************"
# Step 1: Choose UCMA/UCMB
print STEP_INFO.format(1, "Create a new page at UCMA [1] or UCMB [2]:")
workSpace, workSpacePath = get_workspace()
# Step 2: Get new page name
print STEP_INFO.format(2, "Get new page name")
pageName, featureFolderRoot = get_page_name()
# Step 3: Create a new folder for the new page
print STEP_INFO.format(3, "Create a new folder for the new page")
create_new_folder()
# Step 4: Generate a basic bootstrap file
print STEP_INFO.format(4, "Generate a basic bootstrap file")
bootstrap_file_path = generate_bootstrap(featureFolderRoot, pageName)
# Step 5: Generate a basic constants file
print STEP_INFO.format(5, "Generate a basic constants file")
constants_file_path = generate_constants(featureFolderRoot, pageName)
# Step 6: Generate a basic column file
print STEP_INFO.format(6, "Generate a basic column file")
columns_file_path = generate_basic_class(Constants.UCMA_GridColumnDefinition_Path, pageName + 'Columns')
# Step 7: Generate a basic column factory file
print STEP_INFO.format(7, "Generate a basic column factory file")
columnfactory_file_path = generate_columnFactory(Constants.UCMA_GridColumnDefinition_Path, pageName)

print STEP_INFO.format(8, "Create columns")
create_columns(columns_file_path, columnfactory_file_path, constants_file_path)

gridmetadata_file_path = generate_gridMetadata(featureFolderRoot, pageName)

insert_columns_into_gridMetadata(columnfactory_file_path, gridmetadata_file_path)
