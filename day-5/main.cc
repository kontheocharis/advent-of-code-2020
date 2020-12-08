#include <iostream>
#include <vector>

constexpr int TOTAL_ROWS = 128;

int seat_id(std::string_view boarding_pass) {

  int current_row = aaaaaaa
  for (auto direction : boarding_pass) {
    if (direction == 'F') {

    } else if (direction == 'B') {
    } else {
      break;
    }
  }

  return 0;
}

int main(int argc, char *argv[]) {
  std::vector<std::string> boarding_passes;
  for (std::string line; std::getline(std::cin, line);) {
    boarding_passes.push_back(line);
  }

  for (auto pass : boarding_passes) {
    seat_id(pass);
    // TODO
    //
  }

  return 0;
}
