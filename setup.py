import os
import sys
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, cmake_lists_dir=".", **kwa):
        Extension.__init__(self, name, sources=[], **kwa)
        self.cmake_lists_dir = os.path.abspath(cmake_lists_dir)


class cmake_build_ext(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        super().run()

    def build_cmake(self, ext):
        cwd = Path().absolute()
        build_temp = Path(self.build_temp)
        build_temp.mkdir(parents=True, exist_ok=True)
        ext_dir = Path(self.get_ext_fullpath(ext.name)).parent
        ext_dir.mkdir(parents=True, exist_ok=True)

        config = "Debug" if self.debug else "Release"
        cmake_args = [
            f"-DCMAKE_BUILD_TYPE={'' if os.name == 'nt' else config}"
            f"-DPython3_EXECUTABLE={sys.executable}",
        ]
        build_args = ["--config", config]

        os.chdir(str(build_temp))
        self.spawn(["cmake", str(cwd)] + cmake_args)
        self.spawn(["cmake", "--build", "."] + build_args)
        os.chdir(str(cwd))


setup(
    ext_modules=[CMakeExtension("pyproj.cpplib")],
    cmdclass={"build_ext": cmake_build_ext},
)