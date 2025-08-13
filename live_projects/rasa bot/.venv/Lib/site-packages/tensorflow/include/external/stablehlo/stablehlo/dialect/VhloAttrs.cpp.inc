/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* AttrDef Definitions                                                        *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_ATTRDEF_LIST
#undef GET_ATTRDEF_LIST

::mlir::vhlo::ArgResultAliasAttr,
::mlir::vhlo::ChannelHandleAttr,
::mlir::vhlo::ComparisonDirectionAttr,
::mlir::vhlo::ComparisonTypeAttr,
::mlir::vhlo::ConvDimensionNumbersAttr,
::mlir::vhlo::DotDimensionNumbersAttr,
::mlir::vhlo::FftTypeAttr,
::mlir::vhlo::GatherDimensionNumbersAttr,
::mlir::vhlo::OutputOperandAliasAttr,
::mlir::vhlo::PrecisionAttr,
::mlir::vhlo::RngAlgorithmAttr,
::mlir::vhlo::RngDistributionAttr,
::mlir::vhlo::ScatterDimensionNumbersAttr,
::mlir::vhlo::TransposeAttr,
::mlir::vhlo::TypeExtensionsAttr

#endif  // GET_ATTRDEF_LIST

#ifdef GET_ATTRDEF_CLASSES
#undef GET_ATTRDEF_CLASSES

static ::mlir::OptionalParseResult generatedAttributeParser(::mlir::AsmParser &parser, ::llvm::StringRef *mnemonic, ::mlir::Type type, ::mlir::Attribute &value) {
  return ::mlir::AsmParser::KeywordSwitch<::mlir::OptionalParseResult>(parser)
    .Case(::mlir::vhlo::ArgResultAliasAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::ArgResultAliasAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::ChannelHandleAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::ChannelHandleAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::ComparisonDirectionAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::ComparisonDirectionAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::ComparisonTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::ComparisonTypeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::ConvDimensionNumbersAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::ConvDimensionNumbersAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::DotDimensionNumbersAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::DotDimensionNumbersAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::FftTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::FftTypeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::GatherDimensionNumbersAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::GatherDimensionNumbersAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::OutputOperandAliasAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::OutputOperandAliasAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::PrecisionAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::PrecisionAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::RngAlgorithmAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::RngAlgorithmAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::RngDistributionAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::RngDistributionAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::ScatterDimensionNumbersAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::ScatterDimensionNumbersAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::TransposeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::TransposeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::vhlo::TypeExtensionsAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::vhlo::TypeExtensionsAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Default([&](llvm::StringRef keyword, llvm::SMLoc) {
      *mnemonic = keyword;
      return std::nullopt;
    });
}

static ::mlir::LogicalResult generatedAttributePrinter(::mlir::Attribute def, ::mlir::AsmPrinter &printer) {
  return ::llvm::TypeSwitch<::mlir::Attribute, ::mlir::LogicalResult>(def)    .Case<::mlir::vhlo::ArgResultAliasAttr>([&](auto t) {
      printer << ::mlir::vhlo::ArgResultAliasAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::ChannelHandleAttr>([&](auto t) {
      printer << ::mlir::vhlo::ChannelHandleAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::ComparisonDirectionAttr>([&](auto t) {
      printer << ::mlir::vhlo::ComparisonDirectionAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::ComparisonTypeAttr>([&](auto t) {
      printer << ::mlir::vhlo::ComparisonTypeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::ConvDimensionNumbersAttr>([&](auto t) {
      printer << ::mlir::vhlo::ConvDimensionNumbersAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::DotDimensionNumbersAttr>([&](auto t) {
      printer << ::mlir::vhlo::DotDimensionNumbersAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::FftTypeAttr>([&](auto t) {
      printer << ::mlir::vhlo::FftTypeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::GatherDimensionNumbersAttr>([&](auto t) {
      printer << ::mlir::vhlo::GatherDimensionNumbersAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::OutputOperandAliasAttr>([&](auto t) {
      printer << ::mlir::vhlo::OutputOperandAliasAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::PrecisionAttr>([&](auto t) {
      printer << ::mlir::vhlo::PrecisionAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::RngAlgorithmAttr>([&](auto t) {
      printer << ::mlir::vhlo::RngAlgorithmAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::RngDistributionAttr>([&](auto t) {
      printer << ::mlir::vhlo::RngDistributionAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::ScatterDimensionNumbersAttr>([&](auto t) {
      printer << ::mlir::vhlo::ScatterDimensionNumbersAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::TransposeAttr>([&](auto t) {
      printer << ::mlir::vhlo::TransposeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::vhlo::TypeExtensionsAttr>([&](auto t) {
      printer << ::mlir::vhlo::TypeExtensionsAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Default([](auto) { return ::mlir::failure(); });
}

namespace mlir {
namespace vhlo {
namespace detail {
struct ArgResultAliasAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, int64_t, ::llvm::ArrayRef<int64_t>, bool>;
  ArgResultAliasAttrStorage(::llvm::ArrayRef<int64_t> argTupleIndices, int64_t resultIndex, ::llvm::ArrayRef<int64_t> resultTupleIndices, bool isMustAlias) : argTupleIndices(argTupleIndices), resultIndex(resultIndex), resultTupleIndices(resultTupleIndices), isMustAlias(isMustAlias) {}

  KeyTy getAsKey() const {
    return KeyTy(argTupleIndices, resultIndex, resultTupleIndices, isMustAlias);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (argTupleIndices == std::get<0>(tblgenKey)) && (resultIndex == std::get<1>(tblgenKey)) && (resultTupleIndices == std::get<2>(tblgenKey)) && (isMustAlias == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static ArgResultAliasAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto argTupleIndices = std::get<0>(tblgenKey);
    auto resultIndex = std::get<1>(tblgenKey);
    auto resultTupleIndices = std::get<2>(tblgenKey);
    auto isMustAlias = std::get<3>(tblgenKey);
    argTupleIndices = allocator.copyInto(argTupleIndices);
    resultTupleIndices = allocator.copyInto(resultTupleIndices);
    return new (allocator.allocate<ArgResultAliasAttrStorage>()) ArgResultAliasAttrStorage(argTupleIndices, resultIndex, resultTupleIndices, isMustAlias);
  }

  ::llvm::ArrayRef<int64_t> argTupleIndices;
  int64_t resultIndex;
  ::llvm::ArrayRef<int64_t> resultTupleIndices;
  bool isMustAlias;
};
} // namespace detail
ArgResultAliasAttr ArgResultAliasAttr::get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> argTupleIndices, int64_t resultIndex, ::llvm::ArrayRef<int64_t> resultTupleIndices, bool isMustAlias) {
  return Base::get(context, argTupleIndices, resultIndex, resultTupleIndices, isMustAlias);
}

::mlir::Attribute ArgResultAliasAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_argTupleIndices;
  ::mlir::FailureOr<int64_t> _result_resultIndex;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_resultTupleIndices;
  ::mlir::FailureOr<bool> _result_isMustAlias;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_argTupleIndices = false;
  bool _seen_resultIndex = false;
  bool _seen_resultTupleIndices = false;
  bool _seen_isMustAlias = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_argTupleIndices && _paramKey == "argTupleIndices") {
        _seen_argTupleIndices = true;

        // Parse variable 'argTupleIndices'
        _result_argTupleIndices = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_argTupleIndices)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ArgResultAlias parameter 'argTupleIndices' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_resultIndex && _paramKey == "resultIndex") {
        _seen_resultIndex = true;

        // Parse variable 'resultIndex'
        _result_resultIndex = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_resultIndex)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ArgResultAlias parameter 'resultIndex' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_resultTupleIndices && _paramKey == "resultTupleIndices") {
        _seen_resultTupleIndices = true;

        // Parse variable 'resultTupleIndices'
        _result_resultTupleIndices = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_resultTupleIndices)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ArgResultAlias parameter 'resultTupleIndices' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_isMustAlias && _paramKey == "isMustAlias") {
        _seen_isMustAlias = true;

        // Parse variable 'isMustAlias'
        _result_isMustAlias = ::mlir::FieldParser<bool>::parse(odsParser);
        if (::mlir::failed(_result_isMustAlias)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ArgResultAlias parameter 'isMustAlias' which is to be a `bool`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 4; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 4 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_argTupleIndices));
  assert(::mlir::succeeded(_result_resultIndex));
  assert(::mlir::succeeded(_result_resultTupleIndices));
  assert(::mlir::succeeded(_result_isMustAlias));
  return ArgResultAliasAttr::get(odsParser.getContext(),
      ::llvm::ArrayRef<int64_t>((*_result_argTupleIndices)),
      int64_t((*_result_resultIndex)),
      ::llvm::ArrayRef<int64_t>((*_result_resultTupleIndices)),
      bool((*_result_isMustAlias)));
}

void ArgResultAliasAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "argTupleIndices = ";
    mlir::hlo::printDimSizes(odsPrinter, getArgTupleIndices());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "resultIndex = ";
    odsPrinter.printStrippedAttrOrType(getResultIndex());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "resultTupleIndices = ";
    mlir::hlo::printDimSizes(odsPrinter, getResultTupleIndices());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "isMustAlias = ";
    odsPrinter.printStrippedAttrOrType(getIsMustAlias());
  }
  odsPrinter << ">";
}

::llvm::ArrayRef<int64_t> ArgResultAliasAttr::getArgTupleIndices() const {
  return getImpl()->argTupleIndices;
}

int64_t ArgResultAliasAttr::getResultIndex() const {
  return getImpl()->resultIndex;
}

::llvm::ArrayRef<int64_t> ArgResultAliasAttr::getResultTupleIndices() const {
  return getImpl()->resultTupleIndices;
}

bool ArgResultAliasAttr::getIsMustAlias() const {
  return getImpl()->isMustAlias;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ArgResultAliasAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct ChannelHandleAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<int64_t, int64_t>;
  ChannelHandleAttrStorage(int64_t handle, int64_t type) : handle(handle), type(type) {}

  KeyTy getAsKey() const {
    return KeyTy(handle, type);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (handle == std::get<0>(tblgenKey)) && (type == std::get<1>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey));
  }

  static ChannelHandleAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto handle = std::get<0>(tblgenKey);
    auto type = std::get<1>(tblgenKey);
    return new (allocator.allocate<ChannelHandleAttrStorage>()) ChannelHandleAttrStorage(handle, type);
  }

  int64_t handle;
  int64_t type;
};
} // namespace detail
ChannelHandleAttr ChannelHandleAttr::get(::mlir::MLIRContext *context, int64_t handle, int64_t type) {
  return Base::get(context, handle, type);
}

::mlir::Attribute ChannelHandleAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<int64_t> _result_handle;
  ::mlir::FailureOr<int64_t> _result_type;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_handle = false;
  bool _seen_type = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_handle && _paramKey == "handle") {
        _seen_handle = true;

        // Parse variable 'handle'
        _result_handle = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_handle)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ChannelHandle parameter 'handle' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_type && _paramKey == "type") {
        _seen_type = true;

        // Parse variable 'type'
        _result_type = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_type)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ChannelHandle parameter 'type' which is to be a `int64_t`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 2; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 2 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_handle));
  assert(::mlir::succeeded(_result_type));
  return ChannelHandleAttr::get(odsParser.getContext(),
      int64_t((*_result_handle)),
      int64_t((*_result_type)));
}

void ChannelHandleAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "handle = ";
    odsPrinter.printStrippedAttrOrType(getHandle());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "type = ";
    odsPrinter.printStrippedAttrOrType(getType());
  }
  odsPrinter << ">";
}

int64_t ChannelHandleAttr::getHandle() const {
  return getImpl()->handle;
}

int64_t ChannelHandleAttr::getType() const {
  return getImpl()->type;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ChannelHandleAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct ComparisonDirectionAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::ComparisonDirection>;
  ComparisonDirectionAttrStorage(::mlir::vhlo::ComparisonDirection value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static ComparisonDirectionAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<ComparisonDirectionAttrStorage>()) ComparisonDirectionAttrStorage(value);
  }

  ::mlir::vhlo::ComparisonDirection value;
};
} // namespace detail
ComparisonDirectionAttr ComparisonDirectionAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::ComparisonDirection value) {
  return Base::get(context, value);
}

::mlir::Attribute ComparisonDirectionAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::ComparisonDirection> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::ComparisonDirection> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizeComparisonDirection(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::ComparisonDirection" << " to be one of: " << "EQ" << ", " << "NE" << ", " << "GE" << ", " << "GT" << ", " << "LE" << ", " << "LT")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ComparisonDirectionAttr parameter 'value' which is to be a `::mlir::vhlo::ComparisonDirection`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return ComparisonDirectionAttr::get(odsParser.getContext(),
      ::mlir::vhlo::ComparisonDirection((*_result_value)));
}

void ComparisonDirectionAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyComparisonDirection(getValue());
}

::mlir::vhlo::ComparisonDirection ComparisonDirectionAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ComparisonDirectionAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct ComparisonTypeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::ComparisonType>;
  ComparisonTypeAttrStorage(::mlir::vhlo::ComparisonType value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static ComparisonTypeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<ComparisonTypeAttrStorage>()) ComparisonTypeAttrStorage(value);
  }

  ::mlir::vhlo::ComparisonType value;
};
} // namespace detail
ComparisonTypeAttr ComparisonTypeAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::ComparisonType value) {
  return Base::get(context, value);
}

::mlir::Attribute ComparisonTypeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::ComparisonType> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::ComparisonType> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizeComparisonType(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::ComparisonType" << " to be one of: " << "NOTYPE" << ", " << "FLOAT" << ", " << "TOTALORDER" << ", " << "SIGNED" << ", " << "UNSIGNED")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ComparisonTypeAttr parameter 'value' which is to be a `::mlir::vhlo::ComparisonType`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return ComparisonTypeAttr::get(odsParser.getContext(),
      ::mlir::vhlo::ComparisonType((*_result_value)));
}

void ComparisonTypeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyComparisonType(getValue());
}

::mlir::vhlo::ComparisonType ComparisonTypeAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ComparisonTypeAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct ConvDimensionNumbersAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<int64_t, int64_t, ::llvm::ArrayRef<int64_t>, int64_t, int64_t, ::llvm::ArrayRef<int64_t>, int64_t, int64_t, ::llvm::ArrayRef<int64_t>>;
  ConvDimensionNumbersAttrStorage(int64_t inputBatchDimension, int64_t inputFeatureDimension, ::llvm::ArrayRef<int64_t> inputSpatialDimensions, int64_t kernelInputFeatureDimension, int64_t kernelOutputFeatureDimension, ::llvm::ArrayRef<int64_t> kernelSpatialDimensions, int64_t outputBatchDimension, int64_t outputFeatureDimension, ::llvm::ArrayRef<int64_t> outputSpatialDimensions) : inputBatchDimension(inputBatchDimension), inputFeatureDimension(inputFeatureDimension), inputSpatialDimensions(inputSpatialDimensions), kernelInputFeatureDimension(kernelInputFeatureDimension), kernelOutputFeatureDimension(kernelOutputFeatureDimension), kernelSpatialDimensions(kernelSpatialDimensions), outputBatchDimension(outputBatchDimension), outputFeatureDimension(outputFeatureDimension), outputSpatialDimensions(outputSpatialDimensions) {}

  KeyTy getAsKey() const {
    return KeyTy(inputBatchDimension, inputFeatureDimension, inputSpatialDimensions, kernelInputFeatureDimension, kernelOutputFeatureDimension, kernelSpatialDimensions, outputBatchDimension, outputFeatureDimension, outputSpatialDimensions);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (inputBatchDimension == std::get<0>(tblgenKey)) && (inputFeatureDimension == std::get<1>(tblgenKey)) && (inputSpatialDimensions == std::get<2>(tblgenKey)) && (kernelInputFeatureDimension == std::get<3>(tblgenKey)) && (kernelOutputFeatureDimension == std::get<4>(tblgenKey)) && (kernelSpatialDimensions == std::get<5>(tblgenKey)) && (outputBatchDimension == std::get<6>(tblgenKey)) && (outputFeatureDimension == std::get<7>(tblgenKey)) && (outputSpatialDimensions == std::get<8>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey), std::get<4>(tblgenKey), std::get<5>(tblgenKey), std::get<6>(tblgenKey), std::get<7>(tblgenKey), std::get<8>(tblgenKey));
  }

  static ConvDimensionNumbersAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto inputBatchDimension = std::get<0>(tblgenKey);
    auto inputFeatureDimension = std::get<1>(tblgenKey);
    auto inputSpatialDimensions = std::get<2>(tblgenKey);
    auto kernelInputFeatureDimension = std::get<3>(tblgenKey);
    auto kernelOutputFeatureDimension = std::get<4>(tblgenKey);
    auto kernelSpatialDimensions = std::get<5>(tblgenKey);
    auto outputBatchDimension = std::get<6>(tblgenKey);
    auto outputFeatureDimension = std::get<7>(tblgenKey);
    auto outputSpatialDimensions = std::get<8>(tblgenKey);
    inputSpatialDimensions = allocator.copyInto(inputSpatialDimensions);
    kernelSpatialDimensions = allocator.copyInto(kernelSpatialDimensions);
    outputSpatialDimensions = allocator.copyInto(outputSpatialDimensions);
    return new (allocator.allocate<ConvDimensionNumbersAttrStorage>()) ConvDimensionNumbersAttrStorage(inputBatchDimension, inputFeatureDimension, inputSpatialDimensions, kernelInputFeatureDimension, kernelOutputFeatureDimension, kernelSpatialDimensions, outputBatchDimension, outputFeatureDimension, outputSpatialDimensions);
  }

  int64_t inputBatchDimension;
  int64_t inputFeatureDimension;
  ::llvm::ArrayRef<int64_t> inputSpatialDimensions;
  int64_t kernelInputFeatureDimension;
  int64_t kernelOutputFeatureDimension;
  ::llvm::ArrayRef<int64_t> kernelSpatialDimensions;
  int64_t outputBatchDimension;
  int64_t outputFeatureDimension;
  ::llvm::ArrayRef<int64_t> outputSpatialDimensions;
};
} // namespace detail
ConvDimensionNumbersAttr ConvDimensionNumbersAttr::get(::mlir::MLIRContext *context, int64_t inputBatchDimension, int64_t inputFeatureDimension, ::llvm::ArrayRef<int64_t> inputSpatialDimensions, int64_t kernelInputFeatureDimension, int64_t kernelOutputFeatureDimension, ::llvm::ArrayRef<int64_t> kernelSpatialDimensions, int64_t outputBatchDimension, int64_t outputFeatureDimension, ::llvm::ArrayRef<int64_t> outputSpatialDimensions) {
  return Base::get(context, inputBatchDimension, inputFeatureDimension, inputSpatialDimensions, kernelInputFeatureDimension, kernelOutputFeatureDimension, kernelSpatialDimensions, outputBatchDimension, outputFeatureDimension, outputSpatialDimensions);
}

::mlir::Attribute ConvDimensionNumbersAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<int64_t> _result_inputBatchDimension;
  ::mlir::FailureOr<int64_t> _result_inputFeatureDimension;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_inputSpatialDimensions;
  ::mlir::FailureOr<int64_t> _result_kernelInputFeatureDimension;
  ::mlir::FailureOr<int64_t> _result_kernelOutputFeatureDimension;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_kernelSpatialDimensions;
  ::mlir::FailureOr<int64_t> _result_outputBatchDimension;
  ::mlir::FailureOr<int64_t> _result_outputFeatureDimension;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_outputSpatialDimensions;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_inputBatchDimension = false;
  bool _seen_inputFeatureDimension = false;
  bool _seen_inputSpatialDimensions = false;
  bool _seen_kernelInputFeatureDimension = false;
  bool _seen_kernelOutputFeatureDimension = false;
  bool _seen_kernelSpatialDimensions = false;
  bool _seen_outputBatchDimension = false;
  bool _seen_outputFeatureDimension = false;
  bool _seen_outputSpatialDimensions = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_inputBatchDimension && _paramKey == "inputBatchDimension") {
        _seen_inputBatchDimension = true;

        // Parse variable 'inputBatchDimension'
        _result_inputBatchDimension = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_inputBatchDimension)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'inputBatchDimension' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_inputFeatureDimension && _paramKey == "inputFeatureDimension") {
        _seen_inputFeatureDimension = true;

        // Parse variable 'inputFeatureDimension'
        _result_inputFeatureDimension = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_inputFeatureDimension)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'inputFeatureDimension' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_inputSpatialDimensions && _paramKey == "inputSpatialDimensions") {
        _seen_inputSpatialDimensions = true;

        // Parse variable 'inputSpatialDimensions'
        _result_inputSpatialDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_inputSpatialDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'inputSpatialDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_kernelInputFeatureDimension && _paramKey == "kernelInputFeatureDimension") {
        _seen_kernelInputFeatureDimension = true;

        // Parse variable 'kernelInputFeatureDimension'
        _result_kernelInputFeatureDimension = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_kernelInputFeatureDimension)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'kernelInputFeatureDimension' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_kernelOutputFeatureDimension && _paramKey == "kernelOutputFeatureDimension") {
        _seen_kernelOutputFeatureDimension = true;

        // Parse variable 'kernelOutputFeatureDimension'
        _result_kernelOutputFeatureDimension = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_kernelOutputFeatureDimension)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'kernelOutputFeatureDimension' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_kernelSpatialDimensions && _paramKey == "kernelSpatialDimensions") {
        _seen_kernelSpatialDimensions = true;

        // Parse variable 'kernelSpatialDimensions'
        _result_kernelSpatialDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_kernelSpatialDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'kernelSpatialDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_outputBatchDimension && _paramKey == "outputBatchDimension") {
        _seen_outputBatchDimension = true;

        // Parse variable 'outputBatchDimension'
        _result_outputBatchDimension = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_outputBatchDimension)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'outputBatchDimension' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_outputFeatureDimension && _paramKey == "outputFeatureDimension") {
        _seen_outputFeatureDimension = true;

        // Parse variable 'outputFeatureDimension'
        _result_outputFeatureDimension = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_outputFeatureDimension)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'outputFeatureDimension' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_outputSpatialDimensions && _paramKey == "outputSpatialDimensions") {
        _seen_outputSpatialDimensions = true;

        // Parse variable 'outputSpatialDimensions'
        _result_outputSpatialDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_outputSpatialDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ConvDimensionNumbers parameter 'outputSpatialDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 9; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 9 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_inputBatchDimension));
  assert(::mlir::succeeded(_result_inputFeatureDimension));
  assert(::mlir::succeeded(_result_inputSpatialDimensions));
  assert(::mlir::succeeded(_result_kernelInputFeatureDimension));
  assert(::mlir::succeeded(_result_kernelOutputFeatureDimension));
  assert(::mlir::succeeded(_result_kernelSpatialDimensions));
  assert(::mlir::succeeded(_result_outputBatchDimension));
  assert(::mlir::succeeded(_result_outputFeatureDimension));
  assert(::mlir::succeeded(_result_outputSpatialDimensions));
  return ConvDimensionNumbersAttr::get(odsParser.getContext(),
      int64_t((*_result_inputBatchDimension)),
      int64_t((*_result_inputFeatureDimension)),
      ::llvm::ArrayRef<int64_t>((*_result_inputSpatialDimensions)),
      int64_t((*_result_kernelInputFeatureDimension)),
      int64_t((*_result_kernelOutputFeatureDimension)),
      ::llvm::ArrayRef<int64_t>((*_result_kernelSpatialDimensions)),
      int64_t((*_result_outputBatchDimension)),
      int64_t((*_result_outputFeatureDimension)),
      ::llvm::ArrayRef<int64_t>((*_result_outputSpatialDimensions)));
}

void ConvDimensionNumbersAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "inputBatchDimension = ";
    odsPrinter.printStrippedAttrOrType(getInputBatchDimension());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "inputFeatureDimension = ";
    odsPrinter.printStrippedAttrOrType(getInputFeatureDimension());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "inputSpatialDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getInputSpatialDimensions());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "kernelInputFeatureDimension = ";
    odsPrinter.printStrippedAttrOrType(getKernelInputFeatureDimension());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "kernelOutputFeatureDimension = ";
    odsPrinter.printStrippedAttrOrType(getKernelOutputFeatureDimension());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "kernelSpatialDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getKernelSpatialDimensions());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "outputBatchDimension = ";
    odsPrinter.printStrippedAttrOrType(getOutputBatchDimension());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "outputFeatureDimension = ";
    odsPrinter.printStrippedAttrOrType(getOutputFeatureDimension());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "outputSpatialDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getOutputSpatialDimensions());
  }
  odsPrinter << ">";
}

int64_t ConvDimensionNumbersAttr::getInputBatchDimension() const {
  return getImpl()->inputBatchDimension;
}

int64_t ConvDimensionNumbersAttr::getInputFeatureDimension() const {
  return getImpl()->inputFeatureDimension;
}

::llvm::ArrayRef<int64_t> ConvDimensionNumbersAttr::getInputSpatialDimensions() const {
  return getImpl()->inputSpatialDimensions;
}

int64_t ConvDimensionNumbersAttr::getKernelInputFeatureDimension() const {
  return getImpl()->kernelInputFeatureDimension;
}

int64_t ConvDimensionNumbersAttr::getKernelOutputFeatureDimension() const {
  return getImpl()->kernelOutputFeatureDimension;
}

::llvm::ArrayRef<int64_t> ConvDimensionNumbersAttr::getKernelSpatialDimensions() const {
  return getImpl()->kernelSpatialDimensions;
}

int64_t ConvDimensionNumbersAttr::getOutputBatchDimension() const {
  return getImpl()->outputBatchDimension;
}

int64_t ConvDimensionNumbersAttr::getOutputFeatureDimension() const {
  return getImpl()->outputFeatureDimension;
}

::llvm::ArrayRef<int64_t> ConvDimensionNumbersAttr::getOutputSpatialDimensions() const {
  return getImpl()->outputSpatialDimensions;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ConvDimensionNumbersAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct DotDimensionNumbersAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>>;
  DotDimensionNumbersAttrStorage(::llvm::ArrayRef<int64_t> lhsBatchingDimensions, ::llvm::ArrayRef<int64_t> rhsBatchingDimensions, ::llvm::ArrayRef<int64_t> lhsContractingDimensions, ::llvm::ArrayRef<int64_t> rhsContractingDimensions) : lhsBatchingDimensions(lhsBatchingDimensions), rhsBatchingDimensions(rhsBatchingDimensions), lhsContractingDimensions(lhsContractingDimensions), rhsContractingDimensions(rhsContractingDimensions) {}

  KeyTy getAsKey() const {
    return KeyTy(lhsBatchingDimensions, rhsBatchingDimensions, lhsContractingDimensions, rhsContractingDimensions);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (lhsBatchingDimensions == std::get<0>(tblgenKey)) && (rhsBatchingDimensions == std::get<1>(tblgenKey)) && (lhsContractingDimensions == std::get<2>(tblgenKey)) && (rhsContractingDimensions == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static DotDimensionNumbersAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto lhsBatchingDimensions = std::get<0>(tblgenKey);
    auto rhsBatchingDimensions = std::get<1>(tblgenKey);
    auto lhsContractingDimensions = std::get<2>(tblgenKey);
    auto rhsContractingDimensions = std::get<3>(tblgenKey);
    lhsBatchingDimensions = allocator.copyInto(lhsBatchingDimensions);
    rhsBatchingDimensions = allocator.copyInto(rhsBatchingDimensions);
    lhsContractingDimensions = allocator.copyInto(lhsContractingDimensions);
    rhsContractingDimensions = allocator.copyInto(rhsContractingDimensions);
    return new (allocator.allocate<DotDimensionNumbersAttrStorage>()) DotDimensionNumbersAttrStorage(lhsBatchingDimensions, rhsBatchingDimensions, lhsContractingDimensions, rhsContractingDimensions);
  }

  ::llvm::ArrayRef<int64_t> lhsBatchingDimensions;
  ::llvm::ArrayRef<int64_t> rhsBatchingDimensions;
  ::llvm::ArrayRef<int64_t> lhsContractingDimensions;
  ::llvm::ArrayRef<int64_t> rhsContractingDimensions;
};
} // namespace detail
DotDimensionNumbersAttr DotDimensionNumbersAttr::get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> lhsBatchingDimensions, ::llvm::ArrayRef<int64_t> rhsBatchingDimensions, ::llvm::ArrayRef<int64_t> lhsContractingDimensions, ::llvm::ArrayRef<int64_t> rhsContractingDimensions) {
  return Base::get(context, lhsBatchingDimensions, rhsBatchingDimensions, lhsContractingDimensions, rhsContractingDimensions);
}

::mlir::Attribute DotDimensionNumbersAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_lhsBatchingDimensions;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_rhsBatchingDimensions;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_lhsContractingDimensions;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_rhsContractingDimensions;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_lhsBatchingDimensions = false;
  bool _seen_rhsBatchingDimensions = false;
  bool _seen_lhsContractingDimensions = false;
  bool _seen_rhsContractingDimensions = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_lhsBatchingDimensions && _paramKey == "lhsBatchingDimensions") {
        _seen_lhsBatchingDimensions = true;

        // Parse variable 'lhsBatchingDimensions'
        _result_lhsBatchingDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_lhsBatchingDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_DotDimensionNumbers parameter 'lhsBatchingDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_rhsBatchingDimensions && _paramKey == "rhsBatchingDimensions") {
        _seen_rhsBatchingDimensions = true;

        // Parse variable 'rhsBatchingDimensions'
        _result_rhsBatchingDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_rhsBatchingDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_DotDimensionNumbers parameter 'rhsBatchingDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_lhsContractingDimensions && _paramKey == "lhsContractingDimensions") {
        _seen_lhsContractingDimensions = true;

        // Parse variable 'lhsContractingDimensions'
        _result_lhsContractingDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_lhsContractingDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_DotDimensionNumbers parameter 'lhsContractingDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_rhsContractingDimensions && _paramKey == "rhsContractingDimensions") {
        _seen_rhsContractingDimensions = true;

        // Parse variable 'rhsContractingDimensions'
        _result_rhsContractingDimensions = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_rhsContractingDimensions)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_DotDimensionNumbers parameter 'rhsContractingDimensions' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 4; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 4 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_lhsBatchingDimensions));
  assert(::mlir::succeeded(_result_rhsBatchingDimensions));
  assert(::mlir::succeeded(_result_lhsContractingDimensions));
  assert(::mlir::succeeded(_result_rhsContractingDimensions));
  return DotDimensionNumbersAttr::get(odsParser.getContext(),
      ::llvm::ArrayRef<int64_t>((*_result_lhsBatchingDimensions)),
      ::llvm::ArrayRef<int64_t>((*_result_rhsBatchingDimensions)),
      ::llvm::ArrayRef<int64_t>((*_result_lhsContractingDimensions)),
      ::llvm::ArrayRef<int64_t>((*_result_rhsContractingDimensions)));
}

void DotDimensionNumbersAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "lhsBatchingDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getLhsBatchingDimensions());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "rhsBatchingDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getRhsBatchingDimensions());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "lhsContractingDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getLhsContractingDimensions());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "rhsContractingDimensions = ";
    mlir::hlo::printDimSizes(odsPrinter, getRhsContractingDimensions());
  }
  odsPrinter << ">";
}

::llvm::ArrayRef<int64_t> DotDimensionNumbersAttr::getLhsBatchingDimensions() const {
  return getImpl()->lhsBatchingDimensions;
}

::llvm::ArrayRef<int64_t> DotDimensionNumbersAttr::getRhsBatchingDimensions() const {
  return getImpl()->rhsBatchingDimensions;
}

::llvm::ArrayRef<int64_t> DotDimensionNumbersAttr::getLhsContractingDimensions() const {
  return getImpl()->lhsContractingDimensions;
}

::llvm::ArrayRef<int64_t> DotDimensionNumbersAttr::getRhsContractingDimensions() const {
  return getImpl()->rhsContractingDimensions;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DotDimensionNumbersAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct FftTypeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::FftType>;
  FftTypeAttrStorage(::mlir::vhlo::FftType value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static FftTypeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<FftTypeAttrStorage>()) FftTypeAttrStorage(value);
  }

  ::mlir::vhlo::FftType value;
};
} // namespace detail
FftTypeAttr FftTypeAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::FftType value) {
  return Base::get(context, value);
}

::mlir::Attribute FftTypeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::FftType> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::FftType> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizeFftType(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::FftType" << " to be one of: " << "FFT" << ", " << "IFFT" << ", " << "RFFT" << ", " << "IRFFT")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_FftTypeAttr parameter 'value' which is to be a `::mlir::vhlo::FftType`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return FftTypeAttr::get(odsParser.getContext(),
      ::mlir::vhlo::FftType((*_result_value)));
}

void FftTypeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyFftType(getValue());
}

::mlir::vhlo::FftType FftTypeAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::FftTypeAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct GatherDimensionNumbersAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>, int64_t>;
  GatherDimensionNumbersAttrStorage(::llvm::ArrayRef<int64_t> offsetDims, ::llvm::ArrayRef<int64_t> collapsedSliceDims, ::llvm::ArrayRef<int64_t> startIndexMap, int64_t indexVectorDim) : offsetDims(offsetDims), collapsedSliceDims(collapsedSliceDims), startIndexMap(startIndexMap), indexVectorDim(indexVectorDim) {}

  KeyTy getAsKey() const {
    return KeyTy(offsetDims, collapsedSliceDims, startIndexMap, indexVectorDim);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (offsetDims == std::get<0>(tblgenKey)) && (collapsedSliceDims == std::get<1>(tblgenKey)) && (startIndexMap == std::get<2>(tblgenKey)) && (indexVectorDim == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static GatherDimensionNumbersAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto offsetDims = std::get<0>(tblgenKey);
    auto collapsedSliceDims = std::get<1>(tblgenKey);
    auto startIndexMap = std::get<2>(tblgenKey);
    auto indexVectorDim = std::get<3>(tblgenKey);
    offsetDims = allocator.copyInto(offsetDims);
    collapsedSliceDims = allocator.copyInto(collapsedSliceDims);
    startIndexMap = allocator.copyInto(startIndexMap);
    return new (allocator.allocate<GatherDimensionNumbersAttrStorage>()) GatherDimensionNumbersAttrStorage(offsetDims, collapsedSliceDims, startIndexMap, indexVectorDim);
  }

  ::llvm::ArrayRef<int64_t> offsetDims;
  ::llvm::ArrayRef<int64_t> collapsedSliceDims;
  ::llvm::ArrayRef<int64_t> startIndexMap;
  int64_t indexVectorDim;
};
} // namespace detail
GatherDimensionNumbersAttr GatherDimensionNumbersAttr::get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> offsetDims, ::llvm::ArrayRef<int64_t> collapsedSliceDims, ::llvm::ArrayRef<int64_t> startIndexMap, int64_t indexVectorDim) {
  return Base::get(context, offsetDims, collapsedSliceDims, startIndexMap, indexVectorDim);
}

::mlir::Attribute GatherDimensionNumbersAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_offsetDims;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_collapsedSliceDims;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_startIndexMap;
  ::mlir::FailureOr<int64_t> _result_indexVectorDim;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_offsetDims = false;
  bool _seen_collapsedSliceDims = false;
  bool _seen_startIndexMap = false;
  bool _seen_indexVectorDim = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_offsetDims && _paramKey == "offsetDims") {
        _seen_offsetDims = true;

        // Parse variable 'offsetDims'
        _result_offsetDims = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_offsetDims)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_GatherDimensionNumbers parameter 'offsetDims' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_collapsedSliceDims && _paramKey == "collapsedSliceDims") {
        _seen_collapsedSliceDims = true;

        // Parse variable 'collapsedSliceDims'
        _result_collapsedSliceDims = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_collapsedSliceDims)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_GatherDimensionNumbers parameter 'collapsedSliceDims' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_startIndexMap && _paramKey == "startIndexMap") {
        _seen_startIndexMap = true;

        // Parse variable 'startIndexMap'
        _result_startIndexMap = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_startIndexMap)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_GatherDimensionNumbers parameter 'startIndexMap' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_indexVectorDim && _paramKey == "indexVectorDim") {
        _seen_indexVectorDim = true;

        // Parse variable 'indexVectorDim'
        _result_indexVectorDim = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_indexVectorDim)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_GatherDimensionNumbers parameter 'indexVectorDim' which is to be a `int64_t`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 4; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 4 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_offsetDims));
  assert(::mlir::succeeded(_result_collapsedSliceDims));
  assert(::mlir::succeeded(_result_startIndexMap));
  assert(::mlir::succeeded(_result_indexVectorDim));
  return GatherDimensionNumbersAttr::get(odsParser.getContext(),
      ::llvm::ArrayRef<int64_t>((*_result_offsetDims)),
      ::llvm::ArrayRef<int64_t>((*_result_collapsedSliceDims)),
      ::llvm::ArrayRef<int64_t>((*_result_startIndexMap)),
      int64_t((*_result_indexVectorDim)));
}

void GatherDimensionNumbersAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "offsetDims = ";
    mlir::hlo::printDimSizes(odsPrinter, getOffsetDims());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "collapsedSliceDims = ";
    mlir::hlo::printDimSizes(odsPrinter, getCollapsedSliceDims());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "startIndexMap = ";
    mlir::hlo::printDimSizes(odsPrinter, getStartIndexMap());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "indexVectorDim = ";
    odsPrinter.printStrippedAttrOrType(getIndexVectorDim());
  }
  odsPrinter << ">";
}

::llvm::ArrayRef<int64_t> GatherDimensionNumbersAttr::getOffsetDims() const {
  return getImpl()->offsetDims;
}

::llvm::ArrayRef<int64_t> GatherDimensionNumbersAttr::getCollapsedSliceDims() const {
  return getImpl()->collapsedSliceDims;
}

::llvm::ArrayRef<int64_t> GatherDimensionNumbersAttr::getStartIndexMap() const {
  return getImpl()->startIndexMap;
}

int64_t GatherDimensionNumbersAttr::getIndexVectorDim() const {
  return getImpl()->indexVectorDim;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::GatherDimensionNumbersAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct OutputOperandAliasAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, int64_t, ::llvm::ArrayRef<int64_t>>;
  OutputOperandAliasAttrStorage(::llvm::ArrayRef<int64_t> outputTupleIndices, int64_t operandIndex, ::llvm::ArrayRef<int64_t> operandTupleIndices) : outputTupleIndices(outputTupleIndices), operandIndex(operandIndex), operandTupleIndices(operandTupleIndices) {}

  KeyTy getAsKey() const {
    return KeyTy(outputTupleIndices, operandIndex, operandTupleIndices);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (outputTupleIndices == std::get<0>(tblgenKey)) && (operandIndex == std::get<1>(tblgenKey)) && (operandTupleIndices == std::get<2>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey));
  }

  static OutputOperandAliasAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto outputTupleIndices = std::get<0>(tblgenKey);
    auto operandIndex = std::get<1>(tblgenKey);
    auto operandTupleIndices = std::get<2>(tblgenKey);
    outputTupleIndices = allocator.copyInto(outputTupleIndices);
    operandTupleIndices = allocator.copyInto(operandTupleIndices);
    return new (allocator.allocate<OutputOperandAliasAttrStorage>()) OutputOperandAliasAttrStorage(outputTupleIndices, operandIndex, operandTupleIndices);
  }

  ::llvm::ArrayRef<int64_t> outputTupleIndices;
  int64_t operandIndex;
  ::llvm::ArrayRef<int64_t> operandTupleIndices;
};
} // namespace detail
OutputOperandAliasAttr OutputOperandAliasAttr::get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> outputTupleIndices, int64_t operandIndex, ::llvm::ArrayRef<int64_t> operandTupleIndices) {
  return Base::get(context, outputTupleIndices, operandIndex, operandTupleIndices);
}

::mlir::Attribute OutputOperandAliasAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_outputTupleIndices;
  ::mlir::FailureOr<int64_t> _result_operandIndex;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_operandTupleIndices;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_outputTupleIndices = false;
  bool _seen_operandIndex = false;
  bool _seen_operandTupleIndices = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_outputTupleIndices && _paramKey == "outputTupleIndices") {
        _seen_outputTupleIndices = true;

        // Parse variable 'outputTupleIndices'
        _result_outputTupleIndices = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_outputTupleIndices)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_OutputOperandAlias parameter 'outputTupleIndices' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_operandIndex && _paramKey == "operandIndex") {
        _seen_operandIndex = true;

        // Parse variable 'operandIndex'
        _result_operandIndex = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_operandIndex)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_OutputOperandAlias parameter 'operandIndex' which is to be a `int64_t`");
          return {};
        }
      } else if (!_seen_operandTupleIndices && _paramKey == "operandTupleIndices") {
        _seen_operandTupleIndices = true;

        // Parse variable 'operandTupleIndices'
        _result_operandTupleIndices = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_operandTupleIndices)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_OutputOperandAlias parameter 'operandTupleIndices' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 3; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 3 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_outputTupleIndices));
  assert(::mlir::succeeded(_result_operandIndex));
  assert(::mlir::succeeded(_result_operandTupleIndices));
  return OutputOperandAliasAttr::get(odsParser.getContext(),
      ::llvm::ArrayRef<int64_t>((*_result_outputTupleIndices)),
      int64_t((*_result_operandIndex)),
      ::llvm::ArrayRef<int64_t>((*_result_operandTupleIndices)));
}

void OutputOperandAliasAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "outputTupleIndices = ";
    mlir::hlo::printDimSizes(odsPrinter, getOutputTupleIndices());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "operandIndex = ";
    odsPrinter.printStrippedAttrOrType(getOperandIndex());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "operandTupleIndices = ";
    mlir::hlo::printDimSizes(odsPrinter, getOperandTupleIndices());
  }
  odsPrinter << ">";
}

::llvm::ArrayRef<int64_t> OutputOperandAliasAttr::getOutputTupleIndices() const {
  return getImpl()->outputTupleIndices;
}

int64_t OutputOperandAliasAttr::getOperandIndex() const {
  return getImpl()->operandIndex;
}

::llvm::ArrayRef<int64_t> OutputOperandAliasAttr::getOperandTupleIndices() const {
  return getImpl()->operandTupleIndices;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::OutputOperandAliasAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct PrecisionAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::Precision>;
  PrecisionAttrStorage(::mlir::vhlo::Precision value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static PrecisionAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<PrecisionAttrStorage>()) PrecisionAttrStorage(value);
  }

  ::mlir::vhlo::Precision value;
};
} // namespace detail
PrecisionAttr PrecisionAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::Precision value) {
  return Base::get(context, value);
}

::mlir::Attribute PrecisionAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::Precision> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::Precision> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizePrecision(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::Precision" << " to be one of: " << "DEFAULT" << ", " << "HIGH" << ", " << "HIGHEST")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_PrecisionAttr parameter 'value' which is to be a `::mlir::vhlo::Precision`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return PrecisionAttr::get(odsParser.getContext(),
      ::mlir::vhlo::Precision((*_result_value)));
}

void PrecisionAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyPrecision(getValue());
}

::mlir::vhlo::Precision PrecisionAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::PrecisionAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct RngAlgorithmAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::RngAlgorithm>;
  RngAlgorithmAttrStorage(::mlir::vhlo::RngAlgorithm value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static RngAlgorithmAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<RngAlgorithmAttrStorage>()) RngAlgorithmAttrStorage(value);
  }

  ::mlir::vhlo::RngAlgorithm value;
};
} // namespace detail
RngAlgorithmAttr RngAlgorithmAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::RngAlgorithm value) {
  return Base::get(context, value);
}

::mlir::Attribute RngAlgorithmAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::RngAlgorithm> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::RngAlgorithm> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizeRngAlgorithm(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::RngAlgorithm" << " to be one of: " << "DEFAULT" << ", " << "THREE_FRY" << ", " << "PHILOX")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_RngAlgorithmAttr parameter 'value' which is to be a `::mlir::vhlo::RngAlgorithm`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return RngAlgorithmAttr::get(odsParser.getContext(),
      ::mlir::vhlo::RngAlgorithm((*_result_value)));
}

void RngAlgorithmAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyRngAlgorithm(getValue());
}

::mlir::vhlo::RngAlgorithm RngAlgorithmAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RngAlgorithmAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct RngDistributionAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::RngDistribution>;
  RngDistributionAttrStorage(::mlir::vhlo::RngDistribution value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static RngDistributionAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<RngDistributionAttrStorage>()) RngDistributionAttrStorage(value);
  }

  ::mlir::vhlo::RngDistribution value;
};
} // namespace detail
RngDistributionAttr RngDistributionAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::RngDistribution value) {
  return Base::get(context, value);
}

::mlir::Attribute RngDistributionAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::RngDistribution> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::RngDistribution> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizeRngDistribution(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::RngDistribution" << " to be one of: " << "UNIFORM" << ", " << "NORMAL")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_RngDistributionAttr parameter 'value' which is to be a `::mlir::vhlo::RngDistribution`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return RngDistributionAttr::get(odsParser.getContext(),
      ::mlir::vhlo::RngDistribution((*_result_value)));
}

void RngDistributionAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyRngDistribution(getValue());
}

::mlir::vhlo::RngDistribution RngDistributionAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RngDistributionAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct ScatterDimensionNumbersAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>, ::llvm::ArrayRef<int64_t>, int64_t>;
  ScatterDimensionNumbersAttrStorage(::llvm::ArrayRef<int64_t> updateWindowDims, ::llvm::ArrayRef<int64_t> insertedWindowDims, ::llvm::ArrayRef<int64_t> scatterDimsToOperandDims, int64_t indexVectorDim) : updateWindowDims(updateWindowDims), insertedWindowDims(insertedWindowDims), scatterDimsToOperandDims(scatterDimsToOperandDims), indexVectorDim(indexVectorDim) {}

  KeyTy getAsKey() const {
    return KeyTy(updateWindowDims, insertedWindowDims, scatterDimsToOperandDims, indexVectorDim);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (updateWindowDims == std::get<0>(tblgenKey)) && (insertedWindowDims == std::get<1>(tblgenKey)) && (scatterDimsToOperandDims == std::get<2>(tblgenKey)) && (indexVectorDim == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static ScatterDimensionNumbersAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto updateWindowDims = std::get<0>(tblgenKey);
    auto insertedWindowDims = std::get<1>(tblgenKey);
    auto scatterDimsToOperandDims = std::get<2>(tblgenKey);
    auto indexVectorDim = std::get<3>(tblgenKey);
    updateWindowDims = allocator.copyInto(updateWindowDims);
    insertedWindowDims = allocator.copyInto(insertedWindowDims);
    scatterDimsToOperandDims = allocator.copyInto(scatterDimsToOperandDims);
    return new (allocator.allocate<ScatterDimensionNumbersAttrStorage>()) ScatterDimensionNumbersAttrStorage(updateWindowDims, insertedWindowDims, scatterDimsToOperandDims, indexVectorDim);
  }

  ::llvm::ArrayRef<int64_t> updateWindowDims;
  ::llvm::ArrayRef<int64_t> insertedWindowDims;
  ::llvm::ArrayRef<int64_t> scatterDimsToOperandDims;
  int64_t indexVectorDim;
};
} // namespace detail
ScatterDimensionNumbersAttr ScatterDimensionNumbersAttr::get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> updateWindowDims, ::llvm::ArrayRef<int64_t> insertedWindowDims, ::llvm::ArrayRef<int64_t> scatterDimsToOperandDims, int64_t indexVectorDim) {
  return Base::get(context, updateWindowDims, insertedWindowDims, scatterDimsToOperandDims, indexVectorDim);
}

::mlir::Attribute ScatterDimensionNumbersAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_updateWindowDims;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_insertedWindowDims;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_scatterDimsToOperandDims;
  ::mlir::FailureOr<int64_t> _result_indexVectorDim;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_updateWindowDims = false;
  bool _seen_insertedWindowDims = false;
  bool _seen_scatterDimsToOperandDims = false;
  bool _seen_indexVectorDim = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_updateWindowDims && _paramKey == "updateWindowDims") {
        _seen_updateWindowDims = true;

        // Parse variable 'updateWindowDims'
        _result_updateWindowDims = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_updateWindowDims)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ScatterDimensionNumbers parameter 'updateWindowDims' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_insertedWindowDims && _paramKey == "insertedWindowDims") {
        _seen_insertedWindowDims = true;

        // Parse variable 'insertedWindowDims'
        _result_insertedWindowDims = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_insertedWindowDims)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ScatterDimensionNumbers parameter 'insertedWindowDims' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_scatterDimsToOperandDims && _paramKey == "scatterDimsToOperandDims") {
        _seen_scatterDimsToOperandDims = true;

        // Parse variable 'scatterDimsToOperandDims'
        _result_scatterDimsToOperandDims = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_scatterDimsToOperandDims)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ScatterDimensionNumbers parameter 'scatterDimsToOperandDims' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else if (!_seen_indexVectorDim && _paramKey == "indexVectorDim") {
        _seen_indexVectorDim = true;

        // Parse variable 'indexVectorDim'
        _result_indexVectorDim = ::mlir::FieldParser<int64_t>::parse(odsParser);
        if (::mlir::failed(_result_indexVectorDim)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_ScatterDimensionNumbers parameter 'indexVectorDim' which is to be a `int64_t`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 4; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 4 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_updateWindowDims));
  assert(::mlir::succeeded(_result_insertedWindowDims));
  assert(::mlir::succeeded(_result_scatterDimsToOperandDims));
  assert(::mlir::succeeded(_result_indexVectorDim));
  return ScatterDimensionNumbersAttr::get(odsParser.getContext(),
      ::llvm::ArrayRef<int64_t>((*_result_updateWindowDims)),
      ::llvm::ArrayRef<int64_t>((*_result_insertedWindowDims)),
      ::llvm::ArrayRef<int64_t>((*_result_scatterDimsToOperandDims)),
      int64_t((*_result_indexVectorDim)));
}

void ScatterDimensionNumbersAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "updateWindowDims = ";
    mlir::hlo::printDimSizes(odsPrinter, getUpdateWindowDims());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "insertedWindowDims = ";
    mlir::hlo::printDimSizes(odsPrinter, getInsertedWindowDims());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "scatterDimsToOperandDims = ";
    mlir::hlo::printDimSizes(odsPrinter, getScatterDimsToOperandDims());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "indexVectorDim = ";
    odsPrinter.printStrippedAttrOrType(getIndexVectorDim());
  }
  odsPrinter << ">";
}

::llvm::ArrayRef<int64_t> ScatterDimensionNumbersAttr::getUpdateWindowDims() const {
  return getImpl()->updateWindowDims;
}

::llvm::ArrayRef<int64_t> ScatterDimensionNumbersAttr::getInsertedWindowDims() const {
  return getImpl()->insertedWindowDims;
}

::llvm::ArrayRef<int64_t> ScatterDimensionNumbersAttr::getScatterDimsToOperandDims() const {
  return getImpl()->scatterDimsToOperandDims;
}

int64_t ScatterDimensionNumbersAttr::getIndexVectorDim() const {
  return getImpl()->indexVectorDim;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ScatterDimensionNumbersAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct TransposeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::vhlo::Transpose>;
  TransposeAttrStorage(::mlir::vhlo::Transpose value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static TransposeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<TransposeAttrStorage>()) TransposeAttrStorage(value);
  }

  ::mlir::vhlo::Transpose value;
};
} // namespace detail
TransposeAttr TransposeAttr::get(::mlir::MLIRContext *context, ::mlir::vhlo::Transpose value) {
  return Base::get(context, value);
}

::mlir::Attribute TransposeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::vhlo::Transpose> _result_value;

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::vhlo::Transpose> {
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
        return ::mlir::failure();
      auto maybeEnum = ::mlir::vhlo::symbolizeTranspose(enumKeyword);
      if (maybeEnum)
        return *maybeEnum;
      return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::vhlo::Transpose" << " to be one of: " << "TRANSPOSE_INVALID" << ", " << "NO_TRANSPOSE" << ", " << "TRANSPOSE" << ", " << "ADJOINT")};
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_TransposeAttr parameter 'value' which is to be a `::mlir::vhlo::Transpose`");
    return {};
  }
  assert(::mlir::succeeded(_result_value));
  return TransposeAttr::get(odsParser.getContext(),
      ::mlir::vhlo::Transpose((*_result_value)));
}

void TransposeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << ' ';
  odsPrinter << stringifyTranspose(getValue());
}

::mlir::vhlo::Transpose TransposeAttr::getValue() const {
  return getImpl()->value;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TransposeAttr)
namespace mlir {
namespace vhlo {
namespace detail {
struct TypeExtensionsAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>>;
  TypeExtensionsAttrStorage(::llvm::ArrayRef<int64_t> bounds) : bounds(bounds) {}

  KeyTy getAsKey() const {
    return KeyTy(bounds);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (bounds == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static TypeExtensionsAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto bounds = std::get<0>(tblgenKey);
    bounds = allocator.copyInto(bounds);
    return new (allocator.allocate<TypeExtensionsAttrStorage>()) TypeExtensionsAttrStorage(bounds);
  }

  ::llvm::ArrayRef<int64_t> bounds;
};
} // namespace detail
TypeExtensionsAttr TypeExtensionsAttr::get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> bounds) {
  return Base::get(context, bounds);
}

::mlir::Attribute TypeExtensionsAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::llvm::SmallVector<int64_t>> _result_bounds;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_bounds = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_bounds && _paramKey == "bounds") {
        _seen_bounds = true;

        // Parse variable 'bounds'
        _result_bounds = mlir::hlo::parseDimSizes(odsParser);
        if (::mlir::failed(_result_bounds)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse VHLO_TypeExtensions parameter 'bounds' which is to be a `::llvm::ArrayRef<int64_t>`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 1; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 1 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_bounds));
  return TypeExtensionsAttr::get(odsParser.getContext(),
      ::llvm::ArrayRef<int64_t>((*_result_bounds)));
}

void TypeExtensionsAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "bounds = ";
    mlir::hlo::printDimSizes(odsPrinter, getBounds());
  }
  odsPrinter << ">";
}

::llvm::ArrayRef<int64_t> TypeExtensionsAttr::getBounds() const {
  return getImpl()->bounds;
}

} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TypeExtensionsAttr)

#endif  // GET_ATTRDEF_CLASSES

