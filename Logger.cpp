#include "Logger.h"

#include <iostream>

void info(std::string msg) {
    std::cout << "LOGGER [" <<+ LOGGER_VERSION << "]: " << msg << std::endl;
}