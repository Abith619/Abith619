/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Enum Utility Declarations                                                  *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace vhlo {
// Which comparison operation to perform.
enum class ComparisonDirection : uint32_t {
  EQ = 0,
  NE = 1,
  GE = 2,
  GT = 3,
  LE = 4,
  LT = 5,
};

::std::optional<ComparisonDirection> symbolizeComparisonDirection(uint32_t);
::llvm::StringRef stringifyComparisonDirection(ComparisonDirection);
::std::optional<ComparisonDirection> symbolizeComparisonDirection(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForComparisonDirection() {
  return 5;
}


inline ::llvm::StringRef stringifyEnum(ComparisonDirection enumValue) {
  return stringifyComparisonDirection(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<ComparisonDirection> symbolizeEnum<ComparisonDirection>(::llvm::StringRef str) {
  return symbolizeComparisonDirection(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::ComparisonDirection, ::mlir::vhlo::ComparisonDirection> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::ComparisonDirection> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for Which comparison operation to perform.");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::ComparisonDirection> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::ComparisonDirection>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid Which comparison operation to perform. specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::ComparisonDirection value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::ComparisonDirection> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::ComparisonDirection getEmptyKey() {
    return static_cast<::mlir::vhlo::ComparisonDirection>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::ComparisonDirection getTombstoneKey() {
    return static_cast<::mlir::vhlo::ComparisonDirection>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::ComparisonDirection &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::ComparisonDirection &lhs, const ::mlir::vhlo::ComparisonDirection &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// Which comparison type to use.
enum class ComparisonType : uint32_t {
  NOTYPE = 0,
  FLOAT = 1,
  TOTALORDER = 2,
  SIGNED = 3,
  UNSIGNED = 4,
};

::std::optional<ComparisonType> symbolizeComparisonType(uint32_t);
::llvm::StringRef stringifyComparisonType(ComparisonType);
::std::optional<ComparisonType> symbolizeComparisonType(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForComparisonType() {
  return 4;
}


inline ::llvm::StringRef stringifyEnum(ComparisonType enumValue) {
  return stringifyComparisonType(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<ComparisonType> symbolizeEnum<ComparisonType>(::llvm::StringRef str) {
  return symbolizeComparisonType(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::ComparisonType, ::mlir::vhlo::ComparisonType> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::ComparisonType> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for Which comparison type to use.");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::ComparisonType> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::ComparisonType>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid Which comparison type to use. specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::ComparisonType value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::ComparisonType> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::ComparisonType getEmptyKey() {
    return static_cast<::mlir::vhlo::ComparisonType>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::ComparisonType getTombstoneKey() {
    return static_cast<::mlir::vhlo::ComparisonType>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::ComparisonType &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::ComparisonType &lhs, const ::mlir::vhlo::ComparisonType &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// Custom call API version
enum class CustomCallApiVersion : uint32_t {
  API_VERSION_UNSPECIFIED = 0,
  API_VERSION_ORIGINAL = 1,
  API_VERSION_STATUS_RETURNING = 2,
  API_VERSION_STATUS_RETURNING_UNIFIED = 3,
};

::std::optional<CustomCallApiVersion> symbolizeCustomCallApiVersion(uint32_t);
::llvm::StringRef stringifyCustomCallApiVersion(CustomCallApiVersion);
::std::optional<CustomCallApiVersion> symbolizeCustomCallApiVersion(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForCustomCallApiVersion() {
  return 3;
}


inline ::llvm::StringRef stringifyEnum(CustomCallApiVersion enumValue) {
  return stringifyCustomCallApiVersion(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<CustomCallApiVersion> symbolizeEnum<CustomCallApiVersion>(::llvm::StringRef str) {
  return symbolizeCustomCallApiVersion(str);
}

class CustomCallApiVersionAttr : public ::mlir::IntegerAttr {
public:
  using ValueType = CustomCallApiVersion;
  using ::mlir::IntegerAttr::IntegerAttr;
  static bool classof(::mlir::Attribute attr);
  static CustomCallApiVersionAttr get(::mlir::MLIRContext *context, CustomCallApiVersion val);
  CustomCallApiVersion getValue() const;
};
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::CustomCallApiVersion, ::mlir::vhlo::CustomCallApiVersion> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::CustomCallApiVersion> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for Custom call API version");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::CustomCallApiVersion> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::CustomCallApiVersion>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid Custom call API version specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::CustomCallApiVersion value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::CustomCallApiVersion> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::CustomCallApiVersion getEmptyKey() {
    return static_cast<::mlir::vhlo::CustomCallApiVersion>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::CustomCallApiVersion getTombstoneKey() {
    return static_cast<::mlir::vhlo::CustomCallApiVersion>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::CustomCallApiVersion &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::CustomCallApiVersion &lhs, const ::mlir::vhlo::CustomCallApiVersion &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// XLA fast fourier transform type.
enum class FftType : uint32_t {
  FFT = 0,
  IFFT = 1,
  RFFT = 2,
  IRFFT = 3,
};

::std::optional<FftType> symbolizeFftType(uint32_t);
::llvm::StringRef stringifyFftType(FftType);
::std::optional<FftType> symbolizeFftType(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForFftType() {
  return 3;
}


inline ::llvm::StringRef stringifyEnum(FftType enumValue) {
  return stringifyFftType(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<FftType> symbolizeEnum<FftType>(::llvm::StringRef str) {
  return symbolizeFftType(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::FftType, ::mlir::vhlo::FftType> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::FftType> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for XLA fast fourier transform type.");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::FftType> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::FftType>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid XLA fast fourier transform type. specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::FftType value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::FftType> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::FftType getEmptyKey() {
    return static_cast<::mlir::vhlo::FftType>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::FftType getTombstoneKey() {
    return static_cast<::mlir::vhlo::FftType>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::FftType &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::FftType &lhs, const ::mlir::vhlo::FftType &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// XLA precision for an operand. Has backend specific meaning.
enum class Precision : uint32_t {
  DEFAULT = 0,
  HIGH = 1,
  HIGHEST = 2,
};

::std::optional<Precision> symbolizePrecision(uint32_t);
::llvm::StringRef stringifyPrecision(Precision);
::std::optional<Precision> symbolizePrecision(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForPrecision() {
  return 2;
}


inline ::llvm::StringRef stringifyEnum(Precision enumValue) {
  return stringifyPrecision(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<Precision> symbolizeEnum<Precision>(::llvm::StringRef str) {
  return symbolizePrecision(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::Precision, ::mlir::vhlo::Precision> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::Precision> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for XLA precision for an operand. Has backend specific meaning.");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::Precision> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::Precision>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid XLA precision for an operand. Has backend specific meaning. specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::Precision value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::Precision> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::Precision getEmptyKey() {
    return static_cast<::mlir::vhlo::Precision>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::Precision getTombstoneKey() {
    return static_cast<::mlir::vhlo::Precision>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::Precision &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::Precision &lhs, const ::mlir::vhlo::Precision &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// XLA PRNG algorithm to be used.
enum class RngAlgorithm : uint32_t {
  DEFAULT = 0,
  THREE_FRY = 1,
  PHILOX = 2,
};

::std::optional<RngAlgorithm> symbolizeRngAlgorithm(uint32_t);
::llvm::StringRef stringifyRngAlgorithm(RngAlgorithm);
::std::optional<RngAlgorithm> symbolizeRngAlgorithm(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForRngAlgorithm() {
  return 2;
}


inline ::llvm::StringRef stringifyEnum(RngAlgorithm enumValue) {
  return stringifyRngAlgorithm(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<RngAlgorithm> symbolizeEnum<RngAlgorithm>(::llvm::StringRef str) {
  return symbolizeRngAlgorithm(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::RngAlgorithm, ::mlir::vhlo::RngAlgorithm> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::RngAlgorithm> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for XLA PRNG algorithm to be used.");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::RngAlgorithm> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::RngAlgorithm>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid XLA PRNG algorithm to be used. specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::RngAlgorithm value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::RngAlgorithm> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::RngAlgorithm getEmptyKey() {
    return static_cast<::mlir::vhlo::RngAlgorithm>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::RngAlgorithm getTombstoneKey() {
    return static_cast<::mlir::vhlo::RngAlgorithm>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::RngAlgorithm &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::RngAlgorithm &lhs, const ::mlir::vhlo::RngAlgorithm &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// XLA PRNG distribution to be used.
enum class RngDistribution : uint32_t {
  UNIFORM = 1,
  NORMAL = 2,
};

::std::optional<RngDistribution> symbolizeRngDistribution(uint32_t);
::llvm::StringRef stringifyRngDistribution(RngDistribution);
::std::optional<RngDistribution> symbolizeRngDistribution(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForRngDistribution() {
  return 2;
}


inline ::llvm::StringRef stringifyEnum(RngDistribution enumValue) {
  return stringifyRngDistribution(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<RngDistribution> symbolizeEnum<RngDistribution>(::llvm::StringRef str) {
  return symbolizeRngDistribution(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::RngDistribution, ::mlir::vhlo::RngDistribution> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::RngDistribution> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for XLA PRNG distribution to be used.");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::RngDistribution> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::RngDistribution>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid XLA PRNG distribution to be used. specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::RngDistribution value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::RngDistribution> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::RngDistribution getEmptyKey() {
    return static_cast<::mlir::vhlo::RngDistribution>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::RngDistribution getTombstoneKey() {
    return static_cast<::mlir::vhlo::RngDistribution>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::RngDistribution &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::RngDistribution &lhs, const ::mlir::vhlo::RngDistribution &rhs) {
    return lhs == rhs;
  }
};
}

namespace mlir {
namespace vhlo {
// Transpose options
enum class Transpose : uint32_t {
  TRANSPOSE_INVALID = 0,
  NO_TRANSPOSE = 1,
  TRANSPOSE = 2,
  ADJOINT = 3,
};

::std::optional<Transpose> symbolizeTranspose(uint32_t);
::llvm::StringRef stringifyTranspose(Transpose);
::std::optional<Transpose> symbolizeTranspose(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForTranspose() {
  return 3;
}


inline ::llvm::StringRef stringifyEnum(Transpose enumValue) {
  return stringifyTranspose(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<Transpose> symbolizeEnum<Transpose>(::llvm::StringRef str) {
  return symbolizeTranspose(str);
}
} // namespace vhlo
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::vhlo::Transpose, ::mlir::vhlo::Transpose> {
  template <typename ParserT>
  static FailureOr<::mlir::vhlo::Transpose> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for Transpose options");

    // Symbolize the keyword.
    if (::std::optional<::mlir::vhlo::Transpose> attr = ::mlir::vhlo::symbolizeEnum<::mlir::vhlo::Transpose>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid Transpose options specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::vhlo::Transpose value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::vhlo::Transpose> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::vhlo::Transpose getEmptyKey() {
    return static_cast<::mlir::vhlo::Transpose>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::vhlo::Transpose getTombstoneKey() {
    return static_cast<::mlir::vhlo::Transpose>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::vhlo::Transpose &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::vhlo::Transpose &lhs, const ::mlir::vhlo::Transpose &rhs) {
    return lhs == rhs;
  }
};
}

