
class Path:

    def __init__(self, path):

        self.dir = None

        self.name = None

        self.ext = None

        self.Path = path


    @property
    def Path(self):

        return "{}\\{}.{}".format(self.dir, self.name, self.ext)


    @Path.setter
    def Path(self, path):

        path_parts = path.rsplit("\\", 1)

        self.dir = path_parts[0]

        self.File = path_parts[1]


    @property
    def File(self):

        return "{}.{}".format(self.name, self.ext)


    @File.setter
    def File(self, file):

        file_parts = file.rsplit(".", 1)

        self.name = file_parts[0]

        self.ext = file_parts[1]


