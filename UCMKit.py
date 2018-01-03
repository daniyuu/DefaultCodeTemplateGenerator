import Constants
import UCMActions


class UCMKit:
    def __init__(self):
        self.ua = UCMActions.UCMActions()
        return

    def createNewPage(self, workSpace, pageName):
        self.ua.createNewPage(workSpace, pageName)
        return

    def createNewTab(self, featureFolderPath, featureTestsFolderPath, tabName, exposureKeyName):
        self.ua.createNewTab(featureFolderPath, featureTestsFolderPath, tabName, exposureKeyName)
        return


featureFolderPath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_App + "/Pilot"
featureTestsFolderPath = Constants.UCM_ROOT + Constants.UCMA_Folder_Script_Tests + "/Pilot"
tabName = "AccountPilot"
exposureKeyName = "Feature_813093_AccountPilot"
kit = UCMKit()
kit.createNewTab(featureFolderPath, featureTestsFolderPath, tabName, exposureKeyName)
