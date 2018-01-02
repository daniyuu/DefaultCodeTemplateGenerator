import Constants
import UCMActions


class UCMKit:
    def __init__(self):
        self.ua = UCMActions.UCMActions()
        return

    def createNewPage(self, workSpace, pageName):
        self.ua.createNewPage(workSpace, pageName)
        return


kit = UCMKit()
kit.createNewPage(Constants.UCM_A_PROJECT, 'FeaturePilotReadOnlyV2')
