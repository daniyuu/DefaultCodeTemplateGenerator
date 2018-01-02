import os


class BasicActions:
    def __init__(self):
        return

    def createFolder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print '{0}'.format(path), 'has already exist.'
        return

    def readFile(self, filePath):
        fh = open(filePath)
        contents = fh.readlines()
        fh.close()
        return contents

    def overrideFile(self, filePath, contents):
        f = open(filePath, "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()
        return

    def insertCodeByIndex(self, filePath, value, index):
        contents = self.readFile(filePath)
        contents.insert(index, value)
        self.overrideFile(filePath, contents)

    def insertCode(self, filePath, value, beforeContext="BEFORE", afterContext="AFTER"):
        contents = self.readFile(filePath)
        codeLine = len(contents) - 1

        for index in range(len(contents) - 1):
            currentLine = contents[index]
            nextLine = contents[index + 1]
            if (beforeContext in currentLine or beforeContext == "BEFORE") and (
                            afterContext in nextLine or afterContext == "AFTER"):
                codeLine = index + 1
                break

        contents.insert(codeLine, value)
        self.overrideFile(filePath, contents)
        return

    def changeCodeByIndex(self, filePath, value, index):
        contents = self.readFile(filePath)
        contents[index] = value
        self.overrideFile(filePath, contents)
        return

    def changeCode(self, filePath, value, condition):
        contents = self.readFile(filePath)
        codeLine = 0

        for index in range(len(contents)):
            currentLine = contents[index]
            if condition in currentLine:
                codeLine = index
                break

        contents[codeLine] = value
        self.overrideFile(filePath, contents)
        return

#
#
#
# filePath = "D:/Repo/UCM/private/UI/UCMWeb/UCMWeb/Scripts/App/Common/AgentWorkspaceCommonBootstrap.ts"
# value = """import FeaturePilotReadOnlyPage = require("App/FeaturePilotReadOnlyPage");\n"""
# ba = BasicActions()
# ba.insertCode(filePath, value, "import", "\n")
