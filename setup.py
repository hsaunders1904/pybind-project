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
        if self.editable_mode:
            src_dir = Path(__file__).parent.absolute()
            build_dir = src_dir / "build"
            build_dir.mkdir(exist_ok=True)
            ext_path = self.get_ext_fullpath(ext.name)
            ext_dir = Path(ext_path).parent.absolute()
        else:
            src_dir = Path().absolute()
            build_dir = Path(self.build_dir)
            build_dir.mkdir(parents=True, exist_ok=True)
            ext_path = self.get_ext_fullpath(ext.name)
            ext_dir = Path(ext_path).parent.absolute()
            ext_dir.mkdir(parents=True, exist_ok=True)

        config = "Debug" if self.debug else "Release"
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={ext_dir}{os.sep}",
            f"-DCMAKE_BUILD_TYPE={'' if os.name == 'nt' else config}",
            f"-DPython3_EXECUTABLE={sys.executable}",
            "-Dproj_BUILD_PYTHON=ON",
        ]
        build_args = ["--config", config]

        self.spawn(["cmake", src_dir, "-B", build_dir] + cmake_args)
        self.spawn(["cmake", "--build", build_dir] + build_args)


setup(
    ext_modules=[CMakeExtension("pyproj.cpplib")],
    cmdclass={"build_ext": cmake_build_ext},
)
