import Constants


class BasicTemplateGenerator:
    def __init__(self, basicTool):
        self.basicTool = basicTool
        return

    def generate_file_by_template(self, templatePath, folder_path, name, suffix=Constants.SuffixTS):
        file_path = folder_path + "/{0}{1}".format(name, suffix)
        self.basicTool.create_a_new_file(templatePath, file_path, name)
        return file_path

    def generate_basic_class(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicClass, folder_path, name)

    def generate_constants(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicClass, folder_path, name + "Constants")

    def generate_bootstrap(self, folder_path, name):
        templatePath = Constants.TemplatePathBasicBootstrap
        file_path = folder_path + "/{0}Bootstrap.ts".format(name)
        self.basicTool.create_a_new_file(templatePath, file_path, name + "Bootstrap")

        # Generate a constants file for bootstrap
        self.generate_constants(folder_path, name + "Bootstrap")

        self.basicTool.add_constant(Constants.UCMA_ApplicationBootstrapConstants_Path, name + "Bootstrap",
                                    name + "Bootstrap")

        self.basicTool.registerDependency(Constants.UCMA_ApplicationBootstrap_Path, "ApplicationBootstrapConstants",
                                          name + "Bootstrap", True)

        return file_path

    def generate_gridMetadata(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicGridMetadata, folder_path, name + "Grid")

    def generate_columnFactory(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicColumnFactory, folder_path,
                                              name + "ColumnFactory")

    def generate_page(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathPage, folder_path, name + "Page")

    def generate_repository(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicRepository, folder_path, name + "Repository")

    def generate_breadcrumb_template(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicBreadcrumbTemplate, folder_path,
                                              name + "BreadCrumbTemplate",
                                              Constants.SuffixHTM)

    def generate_basic_template(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicTemplate, folder_path,
                                              name + "Template",
                                              Constants.SuffixHTM)

    def generate_basic_viewModel(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicViewModel, folder_path, name + "ViewModel")

    def generate_basic_view(self, folder_path, name):
        return self.generate_file_by_template(Constants.TemplatePathBasicView, folder_path, name + "View")

    def generate_BreadCrumb(self, bootstrap_file_path, constants_file_path, folder_path, name):
        viewModelPath = self.generate_basic_viewModel(folder_path, name)
        constantName = name + "ViewModel"
        constantValue = constantName
        self.basicTool.add_constant(constants_file_path, constantName, constantValue)
        self.basicTool.registerDependency(bootstrap_file_path, constants_file_path, constantName, constantValue)

        templatePath = self.generate_breadcrumb_template(folder_path, name)
        constantName = name + "BreadCrumbTemplateName"
        constantValue = name + "BreadCrumbTemplate"
        self.basicTool.add_constant(constants_file_path, constantName, constantValue)

        constantName = name + "BreadCrumbTemplatePath"
        constantValue = templatePath
        self.basicTool.add_constant(constants_file_path, constantName, constantValue)

        viewPath = self.generate_basic_view(folder_path, name)
