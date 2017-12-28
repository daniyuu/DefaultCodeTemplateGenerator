import Constants


class BasicTemplateGenerator:
    def __init__(self, basicTool):
        self.basicTool = basicTool
        return

    def generate_file_by_template(self, templatePath, folder_path, name, suffix):
        file_path = folder_path + "/{0}{1}".format(name, suffix)
        self.basicTool.create_a_new_file(templatePath, file_path, name)
        return file_path

    def generate_basic_class(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicClass, folder_path, name, Constants.SuffixTS)

    def generate_constants(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicClass, folder_path, name + "Constants",
                                              Constants.SuffixTS)

    def generate_bootstrap(self, folder_path, name):
        templatePath = Constants.TemplatePathBasicBootstrap
        file_path = folder_path + "/{0}Bootstrap.ts".format(name)
        self.basicTool.create_a_new_file(templatePath, file_path, name)

        # Generate a constants file for bootstrap
        self.generate_constants(self, folder_path, name + "Bootstrap")

        self.basicTool.add_constant(Constants.UCMA_ApplicationBootstrapConstants_Path, name + "Bootstrap",
                                    name + "Bootstrap")

        self.basicTool.registerDependency(Constants.UCMA_ApplicationBootstrap_Path, "ApplicationBootstrapConstants",
                                          name + "Bootstrap", True)

        return file_path

    def generate_gridMetadata(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicGridMetadata, folder_path, name + "Grid",
                                              Constants.SuffixTS)

    def generate_columnFactory(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicColumnFactory, folder_path,
                                              name + "ColumnFactory",
                                              Constants.SuffixTS)

    def generate_page(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathPage, folder_path,
                                              name + "Page",
                                              Constants.SuffixTS)
