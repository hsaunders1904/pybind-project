#include "proj/version.h"

#include <gtest/gtest.h>

#include <regex>

TEST(version, MatchesRegex) {
  std::regex pattern("[0-9]+\\.[0-9]\\.[0-9]");

  ASSERT_TRUE(std::regex_match(proj::VERSION, pattern));
}
