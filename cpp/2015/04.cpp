#include "common.h"
#include <cassert>
#include <cstdint>
#include <openssl/evp.h>
#include <string>

namespace {
constexpr std::size_t kMd5DigestLen = 16;

bool md5_has_leading_zeroes(const std::string &input, std::size_t zeroes) {
  unsigned char digest[kMd5DigestLen];
  unsigned int digest_len = 0;
  if (EVP_Digest(input.data(), input.size(), digest, &digest_len, EVP_md5(),
                 nullptr) != 1 ||
      digest_len != kMd5DigestLen) {
    return false;
  }

  std::size_t full_bytes = zeroes / 2;
  bool needs_half_byte = (zeroes % 2) != 0;
  for (std::size_t i = 0; i < full_bytes; ++i) {
    if (digest[i] != 0) {
      return false;
    }
  }
  if (needs_half_byte) {
    return (digest[full_bytes] & 0xF0) == 0;
  }
  return true;
}

std::uint32_t find_nonce(const std::string &input, std::size_t zeroes) {
  for (std::uint32_t i = 1;; ++i) {
    std::string candidate = input + std::to_string(i);
    if (md5_has_leading_zeroes(candidate, zeroes)) {
      return i;
    }
  }
}
} // namespace

std::uint32_t part1(const std::string &input) { return find_nonce(input, 5); }
std::uint32_t part2(const std::string &input) { return find_nonce(input, 6); }

int main() {
  const unsigned int day = 4;
  start_day(day);

  std::cout << "=== Part 1 ===\n";

  assert(part1("abcdef") == 609043);

  const std::string input = "yzbqklnj";

  std::cout << "Result = " << part1(input) << "\n";

  std::cout << "\n=== Part 2 ===\n";

  std::cout << "Result = " << part2(input) << "\n";

  return 0;
}
