#include <unistd.h>
#include "util.hpp"
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
void clearf() {
    std::cout << "\x1B[2J\x1B[H";
}
int main() {
  unsigned int microsecond = 1000000; 
  char normal[] = "\x1b[0;39m";
  char black[] = "\x1b[0;30m";
  char red[] = { 0x1b, '[', '0', ';', '3', '1', 'm', 0    };
  char green[] = { 0x1b, '[', '0', ';', '3', '2', 'm', 0  };
  char yellow[] = { 0x1b, '[', '0', ';', '3', '3', 'm', 0 };
  char blue[] = { 0x1b, '[', '0', ';', '3', '4', 'm', 0   };
  char purple[] = { 0x1b, '[', '0', ';', '3', '5', 'm', 0 };
  char cyan[] = { 0x1b, '[', '0', ';', '3', '6', 'm', 0   };
  char Lgray[] = { 0x1b, '[', '0', ';', '3', '7', 'm', 0  };
  char Dgray[] = { 0x1b, '[', '0', ';', '3', '8', 'm', 0  };
  char Bred[] = { 0x1b, '[', '1', ';', '3', '1', 'm', 0   };
  clearf();
  std::cout << cyan;

}