from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class LoggerConan(ConanFile):
    name = "logger"
    version = "1.0"

    # Optional metadata
    license = "MIT"
    author = "keda"
    url = "https://github.com/Drake072/conan-demo-logger.git"
    description = "A simple logger for demo purpose"
    topics = ("demo", "logger")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "src/CMakeLists.txt", "src/logger.cpp", "src/include/logger.h"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self, src_folder="src")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["logger"]
