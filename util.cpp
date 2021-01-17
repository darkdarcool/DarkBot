#include <unistd.h>
#include "util.hpp"
#include <string>
#include <iostream>
#include <chrono>
#include <thread>
  //                          ^ change them to a 1 to make them bold 
unsigned int microsecond = 1000000;

void typewriter(const std::string& message, unsigned int millis_per_char) {
  for (const char c : message) {
    // flush is used to make sure the console is empty
    std::cout << c << std::flush;

    // Ask the thread to sleep for at least n millis.
    std::this_thread::sleep_for(std::chrono::milliseconds(millis_per_char));
  }
}
