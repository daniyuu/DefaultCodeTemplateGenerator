import Constants
import os
import xml.etree.ElementTree as ET

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


def register_csproj(file_path):
    print "Register this file at csproj file"
    file_register_path = "Scripts" + file_path.split("Scripts")[1].replace("/", "\\")

    fh = open(Constants.UCMA_CSPROJ_Path)
    contents = fh.readlines()
    fh.close()

    value = """\t<TypeScriptCompile Include="{0}">\n""".format(file_register_path.decode('string_escape'))
    contents.insert(400, value)

    f = open(Constants.UCMA_CSPROJ_Path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


# fo = open(Constants.UCM_ROOT + "/{0}Page.ts".format("CYY"), "w")
# fo.close()
def create_folder(path):
    print "[Start] Create a folder..."
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print '{0}'.format(path), 'has already exist.'

    print "[Finished] Create folder {0}".format(path)


# create_folder(Constants.UCM_ROOT+'/CYY')

# pageName = raw_input("What is your page name? Please input it here: ")
# print "Your page name is: ", pageName
#
# pageNewFolderPath = Constants.UCM_ROOT + '/private/UI/UCMWeb/UCMWeb/Scripts/App' + "/{0}/".format(pageName)

def create_a_new_file(templatePath, file_path, className):
    print "[Start] Generate ", file_path
    variable_name = className[0].lower() + className[1:]
    fh = open(templatePath)
    template = fh.read()
    fh.close()

    fo = open(file_path, "w")
    fo.write(
        template.format(Constants.LeftBracket, Constants.RightBracket, className, variable_name))
    fo.close()
    print "[Finished] Generate ", file_path

    register_csproj(file_path)
    return


def generate_basic_class(folder_path, name):
    templatePath = Constants.TemplatePathBasicClass
    file_path = folder_path + "/{0}.ts".format(name)
    create_a_new_file(templatePath, file_path, name)
    return file_path


def generate_bootstrap(folder_path, name):
    templatePath = Constants.TemplatePathBasicBootstrap
    file_path = folder_path + "/{0}Bootstrap.ts".format(name)
    create_a_new_file(templatePath, file_path, name)

    applicationBootstrapConstantsFilePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App + '/Common/ApplicationBootstrapConstants.ts'
    fh = open(applicationBootstrapConstantsFilePath)
    contents = fh.readlines()
    fh.close()

    index = 0
    value = """\tpublic static {0}Bootstrap: string = "{0}Bootstrap";\n""".format(name)
    for i in range(len(contents)):
        line = contents[i]
        if "}" in line:
            index = i
    contents.insert(index, value)
    f = open(applicationBootstrapConstantsFilePath, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    applicationBootstrapFilePath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App + '/Common/ApplicationBootstrap.ts'
    fh = open(applicationBootstrapFilePath)
    contents = fh.readlines()
    fh.close()
    importIndex = 0
    mappingIndex = 0
    for i in range(len(contents)):
        line = contents[i]
        if "import " in line:
            importIndex = i
        if "public SetSingletonConstructorMapping()" in line:
            mappingIndex = i

    importIndex += 1
    mappingIndex += 1
    importPath = file_path.split('/Scripts')[-1].split('.')[0]
    importValue = """import {0}Bootstrap = require("{1}");\n""".format(name, importPath)
    mappingVaule = """\t\tthis.singletonConstructorMapping[ApplicationBootstrapConstants.{0}Bootstrap] = this.typeConstructorCasting.Cast({0}Bootstrap);\n""".format(
        name)
    contents.insert(importIndex, importValue)
    contents.insert(mappingIndex + 1, mappingVaule)
    f = open(applicationBootstrapFilePath, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    return file_path


def generate_constants(folder_path, name):
    templatePath = Constants.TemplatePathBasicConstants
    file_path = folder_path + "/{0}Constants.ts".format(name)
    create_a_new_file(templatePath, file_path, name)
    return file_path


def generate_columnFactory(folder_path, name):
    templatePath = Constants.TemplatePathBasicColumnFactory
    file_path = folder_path + "/{0}ColumnFactory.ts".format(name)
    create_a_new_file(templatePath, file_path, name)
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
    create_folder(featureFolderRoot)
    return


def add_column_to_columnsFile(columns_file_path, column_name):
    fh = open(columns_file_path)
    contents = fh.readlines()
    fh.close()
    index = 0
    for line in contents:
        index += 1
        if "class " in line:
            break

    value = """\tpublic static {0}: string = "{0}";\n""".format(column_name)
    contents.insert(index, value)
    f = open(columns_file_path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def add_a_constant(constants_file_path, constantName, constantValue):
    fh = open(constants_file_path)
    contents = fh.readlines()
    fh.close()
    index = 0
    value = """\tpublic static {0}: string = "{1}";\n""".format(constantName, constantValue)
    for i in range(len(contents)):
        line = contents[i]
        if "}" in line:
            index = i

    contents.insert(index, value)
    f = open(constants_file_path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def add_column_definition(columnfactory_file_path, column_name):
    columnsFileName = columnfactory_file_path.split('/')[-1].split('ColumnFactory')[0]
    column_type_mapping = ['Integer', 'Text', 'MultiSelectType', 'AstroTable', 'Date']
    value = """\t\tthis.AddColumnDefinition(\n"""
    column_type = input("Please choose column type: [0]Integer [1]Text [2]MultiSelectType [3]AstroTable [4]Date")
    if column_type > 4 or column_type < 0:
        column_type = 0
    width = input("Please enter the width of column (Default: 110): ")
    value += """\t\t\tthis.NewColumnDefinition({0}Columns.{1}, Constants.{2}, Constants.{0}, {3})\n""".format(
        columnsFileName, column_name, column_type_mapping[column_type], width)
    value += """\t\t\t\t.WithDefaultHeader()\n"""
    value += """\t\t\t\t.Build());\n\n"""

    fh = open(columnfactory_file_path)
    contents = fh.readlines()
    fh.close()
    index = 0
    for line in contents:
        index += 1
        if "private createColumnMetadataMapping():" in line:
            break

    contents.insert(index, value)
    f = open(columnfactory_file_path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

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
print STEP_INFO.format(5, "Generate a basic bootstrap file")
constants_file_path = generate_constants(featureFolderRoot, pageName)
# Step 6: Generate a basic column file
print STEP_INFO.format(6, "Generate a basic column file")
columns_file_path = generate_basic_class(Constants.UCMA_GridColumnDefinition_Path, pageName + 'Columns')
# Step 7: Generate a basic column factory file
print STEP_INFO.format(7, "Generate a basic column factory file")
columnfactory_file_path = generate_columnFactory(Constants.UCMA_GridColumnDefinition_Path, pageName)

print STEP_INFO.format(8, "Create columns")
create_columns(columns_file_path, columnfactory_file_path, constants_file_path)
