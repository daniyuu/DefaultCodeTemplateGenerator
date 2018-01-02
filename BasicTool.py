import os
import Constants


class BasicTool:
    def __init__(self, importMapping):
        self.importMapping = importMapping
        return

    def insertCode(self, filePath, context, value, before=False):
        fh = open(filePath)
        contents = fh.readlines()
        fh.close()

        index = 0
        if type(context) is int:
            index = context
        else:
            for line in contents:
                index += 1
                if context in line:
                    break
            if before:
                index -= 1
        contents.insert(index, value)
        f = open(filePath, "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()
        return

    def getVariableNameByClassName(self, className):
        variableName = className[0].lower() + className[1:]
        return variableName

    def importDependency(self, file_path, className):
        value = """import {0} = require("{1}");\n""".format(className, self.importMapping[className])
        self.insertCode(file_path, 0, value)
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

        self.insertCode(bootstrapFilePath, context, value)
        return

    def getImportMapping(self):
        return self.importMapping

    def updateImportMapping(self, className, file_path):
        importPath = ""
        flag = False
        for item in file_path.split('/'):
            if item == 'Core' or item == 'App':
                flag = True
            if flag:
                if 'Core' in importPath:
                    continue
                importPath += item.split('.')[0] + "/"

        self.importMapping[className] = importPath[:-1]

    def create_folder(self, path):
        print "[Start] Create a folder..."
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print '{0}'.format(path), 'has already exist.'

        print "[Finished] Create folder {0}".format(path)

    def create_a_new_file(self, templatePath, file_path, className):
        print "[Start] Generate ", file_path
        variable_name = self.getVariableNameByClassName(className)
        fh = open(templatePath)
        template = fh.read()
        fh.close()

        fo = open(file_path, "w")
        fo.write(
            template.format(Constants.LeftBracket, Constants.RightBracket, className, variable_name))
        fo.close()
        print "[Finished] Generate ", file_path

        self.register_csproj(file_path)
        self.updateImportMapping(className, file_path)
        return

    def register_csproj(self, file_path):
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

    def add_constant(self, constants_file_path, constantName, constantValue):
        value = """\tpublic static {0}: string = "{1}";\n""".format(constantName, constantValue)
        self.insertCode(constants_file_path, "}", value, True)


