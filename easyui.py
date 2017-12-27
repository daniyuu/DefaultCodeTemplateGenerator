import Constants
import os


def generate_page_file(page_name):
    templatePath = Constants.TemplatePathPage
    fh = open(templatePath)
    template = fh.read()
    fh.close()

    outputPath = "./"

    fo = open(outputPath + "{0}Page.ts".format(page_name), "w")
    fo.write(
        template.format(Constants.LeftBracket, Constants.RightBracket, page_name, page_name[0].lower() + page_name[1:]))
    fo.close()


pageName = raw_input("What is your page name? Please input it here: ")
print "Your page name is: ", pageName
generate_page_file(pageName)

# dir = os.path.dirname(__file__)
# print dir


def create_folder(path):
    print "Staring create a folder..."
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print '{0}'.format(path), 'has already exist.'

    print "[Finished] Create folder {0}".format(path)