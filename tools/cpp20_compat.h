#pragma once

#include <cstring>
#include <type_traits>

#if !defined(__cpp_lib_bit_cast) || __cpp_lib_bit_cast < 201806L
namespace std {
template <class To, class From>
typename enable_if<
    sizeof(To) == sizeof(From) && is_trivially_copyable<From>::value &&
        is_trivial<To>::value,
    To>::type
bit_cast(const From& src) noexcept {
  To dst;
  std::memcpy(&dst, &src, sizeof(To));
  return dst;
}
} // namespace std
#endif
