/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* AttrDef Definitions                                                        *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_ATTRDEF_LIST
#undef GET_ATTRDEF_LIST

::mlir::LLVM::CConvAttr,
::mlir::LLVM::DIBasicTypeAttr,
::mlir::LLVM::DICompileUnitAttr,
::mlir::LLVM::DICompositeTypeAttr,
::mlir::LLVM::DIDerivedTypeAttr,
::mlir::LLVM::DIFileAttr,
::mlir::LLVM::DILexicalBlockAttr,
::mlir::LLVM::DILexicalBlockFileAttr,
::mlir::LLVM::DILocalVariableAttr,
::mlir::LLVM::DISubprogramAttr,
::mlir::LLVM::DISubrangeAttr,
::mlir::LLVM::DISubroutineTypeAttr,
::mlir::LLVM::DIVoidResultTypeAttr,
::mlir::LLVM::FastmathFlagsAttr,
::mlir::LLVM::MemoryEffectsAttr,
::mlir::LLVM::LinkageAttr,
::mlir::LLVM::LoopOptionsAttr

#endif  // GET_ATTRDEF_LIST

#ifdef GET_ATTRDEF_CLASSES
#undef GET_ATTRDEF_CLASSES

static ::mlir::OptionalParseResult generatedAttributeParser(::mlir::AsmParser &parser, ::llvm::StringRef *mnemonic, ::mlir::Type type, ::mlir::Attribute &value) {
  return ::mlir::AsmParser::KeywordSwitch<::mlir::OptionalParseResult>(parser)
    .Case(::mlir::LLVM::CConvAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::CConvAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DIBasicTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DIBasicTypeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DICompileUnitAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DICompileUnitAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DICompositeTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DICompositeTypeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DIDerivedTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DIDerivedTypeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DIFileAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DIFileAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DILexicalBlockAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DILexicalBlockAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DILexicalBlockFileAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DILexicalBlockFileAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DILocalVariableAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DILocalVariableAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DISubprogramAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DISubprogramAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DISubrangeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DISubrangeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DISubroutineTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DISubroutineTypeAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::DIVoidResultTypeAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::DIVoidResultTypeAttr::get(parser.getContext());
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::FastmathFlagsAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::FastmathFlagsAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::MemoryEffectsAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::MemoryEffectsAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::LinkageAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::LinkageAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Case(::mlir::LLVM::LoopOptionsAttr::getMnemonic(), [&](llvm::StringRef, llvm::SMLoc) {
      value = ::mlir::LLVM::LoopOptionsAttr::parse(parser, type);
      return ::mlir::success(!!value);
    })
    .Default([&](llvm::StringRef keyword, llvm::SMLoc) {
      *mnemonic = keyword;
      return std::nullopt;
    });
}

static ::mlir::LogicalResult generatedAttributePrinter(::mlir::Attribute def, ::mlir::AsmPrinter &printer) {
  return ::llvm::TypeSwitch<::mlir::Attribute, ::mlir::LogicalResult>(def)    .Case<::mlir::LLVM::CConvAttr>([&](auto t) {
      printer << ::mlir::LLVM::CConvAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DIBasicTypeAttr>([&](auto t) {
      printer << ::mlir::LLVM::DIBasicTypeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DICompileUnitAttr>([&](auto t) {
      printer << ::mlir::LLVM::DICompileUnitAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DICompositeTypeAttr>([&](auto t) {
      printer << ::mlir::LLVM::DICompositeTypeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DIDerivedTypeAttr>([&](auto t) {
      printer << ::mlir::LLVM::DIDerivedTypeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DIFileAttr>([&](auto t) {
      printer << ::mlir::LLVM::DIFileAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DILexicalBlockAttr>([&](auto t) {
      printer << ::mlir::LLVM::DILexicalBlockAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DILexicalBlockFileAttr>([&](auto t) {
      printer << ::mlir::LLVM::DILexicalBlockFileAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DILocalVariableAttr>([&](auto t) {
      printer << ::mlir::LLVM::DILocalVariableAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DISubprogramAttr>([&](auto t) {
      printer << ::mlir::LLVM::DISubprogramAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DISubrangeAttr>([&](auto t) {
      printer << ::mlir::LLVM::DISubrangeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DISubroutineTypeAttr>([&](auto t) {
      printer << ::mlir::LLVM::DISubroutineTypeAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::DIVoidResultTypeAttr>([&](auto t) {
      printer << ::mlir::LLVM::DIVoidResultTypeAttr::getMnemonic();
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::FastmathFlagsAttr>([&](auto t) {
      printer << ::mlir::LLVM::FastmathFlagsAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::MemoryEffectsAttr>([&](auto t) {
      printer << ::mlir::LLVM::MemoryEffectsAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::LinkageAttr>([&](auto t) {
      printer << ::mlir::LLVM::LinkageAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Case<::mlir::LLVM::LoopOptionsAttr>([&](auto t) {
      printer << ::mlir::LLVM::LoopOptionsAttr::getMnemonic();
t.print(printer);
      return ::mlir::success();
    })
    .Default([](auto) { return ::mlir::failure(); });
}

namespace mlir {
namespace LLVM {
namespace detail {
struct CConvAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<CConv>;
  CConvAttrStorage(CConv CallingConv) : CallingConv(CallingConv) {}

  KeyTy getAsKey() const {
    return KeyTy(CallingConv);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (CallingConv == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static CConvAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto CallingConv = std::get<0>(tblgenKey);
    return new (allocator.allocate<CConvAttrStorage>()) CConvAttrStorage(CallingConv);
  }

  CConv CallingConv;
};
} // namespace detail
CConvAttr CConvAttr::get(::mlir::MLIRContext *context, CConv CallingConv) {
  return Base::get(context, CallingConv);
}

::mlir::Attribute CConvAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<CConv> _result_CallingConv;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};

  // Parse variable 'CallingConv'
  _result_CallingConv = ::mlir::FieldParser<CConv>::parse(odsParser);
  if (::mlir::failed(_result_CallingConv)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse CConvAttr parameter 'CallingConv' which is to be a `CConv`");
    return {};
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_CallingConv));
  return CConvAttr::get(odsParser.getContext(),
      CConv((*_result_CallingConv)));
}

void CConvAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  odsPrinter.printStrippedAttrOrType(getCallingConv());
  odsPrinter << ">";
}

CConv CConvAttr::getCallingConv() const {
  return getImpl()->CallingConv;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::CConvAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DIBasicTypeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<unsigned, StringAttr, uint64_t, unsigned>;
  DIBasicTypeAttrStorage(unsigned tag, StringAttr name, uint64_t sizeInBits, unsigned encoding) : tag(tag), name(name), sizeInBits(sizeInBits), encoding(encoding) {}

  KeyTy getAsKey() const {
    return KeyTy(tag, name, sizeInBits, encoding);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (tag == std::get<0>(tblgenKey)) && (name == std::get<1>(tblgenKey)) && (sizeInBits == std::get<2>(tblgenKey)) && (encoding == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static DIBasicTypeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto tag = std::get<0>(tblgenKey);
    auto name = std::get<1>(tblgenKey);
    auto sizeInBits = std::get<2>(tblgenKey);
    auto encoding = std::get<3>(tblgenKey);
    return new (allocator.allocate<DIBasicTypeAttrStorage>()) DIBasicTypeAttrStorage(tag, name, sizeInBits, encoding);
  }

  unsigned tag;
  StringAttr name;
  uint64_t sizeInBits;
  unsigned encoding;
};
} // namespace detail
DIBasicTypeAttr DIBasicTypeAttr::get(::mlir::MLIRContext *context, unsigned tag, StringAttr name, uint64_t sizeInBits, unsigned encoding) {
  return Base::get(context, tag, name, sizeInBits, encoding);
}

DIBasicTypeAttr DIBasicTypeAttr::get(::mlir::MLIRContext *context, unsigned tag, const Twine &name, uint64_t sizeInBits, unsigned encoding) {
  return Base::get(context, tag, StringAttr::get(context, name), sizeInBits,
               encoding);
}

::mlir::Attribute DIBasicTypeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<unsigned> _result_tag;
  ::mlir::FailureOr<StringAttr> _result_name;
  ::mlir::FailureOr<uint64_t> _result_sizeInBits;
  ::mlir::FailureOr<unsigned> _result_encoding;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_tag = false;
  bool _seen_name = false;
  bool _seen_sizeInBits = false;
  bool _seen_encoding = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_tag && _paramKey == "tag") {
        _seen_tag = true;

        // Parse variable 'tag'
        _result_tag =  [&]() -> FailureOr<unsigned> {
            SMLoc tagLoc = odsParser.getCurrentLocation();
            StringRef name;
            if (odsParser.parseKeyword(&name))
              return failure();

            if (unsigned tag = llvm::dwarf::getTag(name))
              return tag;
            return odsParser.emitError(tagLoc)
              << "invalid debug info debug info tag name: " << name;
          }() ;
        if (::mlir::failed(_result_tag)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIBasicTypeAttr parameter 'tag' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_name && _paramKey == "name") {
        _seen_name = true;

        // Parse variable 'name'
        _result_name = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_name)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIBasicTypeAttr parameter 'name' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_sizeInBits && _paramKey == "sizeInBits") {
        _seen_sizeInBits = true;

        // Parse variable 'sizeInBits'
        _result_sizeInBits = ::mlir::FieldParser<uint64_t>::parse(odsParser);
        if (::mlir::failed(_result_sizeInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIBasicTypeAttr parameter 'sizeInBits' which is to be a `uint64_t`");
          return {};
        }
      } else if (!_seen_encoding && _paramKey == "encoding") {
        _seen_encoding = true;

        // Parse variable 'encoding'
        _result_encoding =  [&]() -> FailureOr<unsigned> {
            SMLoc tagLoc = odsParser.getCurrentLocation();
            StringRef name;
            if (odsParser.parseKeyword(&name))
              return failure();

            if (unsigned tag = llvm::dwarf::getAttributeEncoding(name))
              return tag;
            return odsParser.emitError(tagLoc)
              << "invalid debug info debug info encoding name: " << name;
          }() ;
        if (::mlir::failed(_result_encoding)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIBasicTypeAttr parameter 'encoding' which is to be a `unsigned`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_tag) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "tag";
      return {};
    }
    if (!_seen_name) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "name";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_tag));
  assert(::mlir::succeeded(_result_name));
  return DIBasicTypeAttr::get(odsParser.getContext(),
      unsigned((*_result_tag)),
      StringAttr((*_result_name)),
      uint64_t((_result_sizeInBits.value_or(uint64_t()))),
      unsigned((_result_encoding.value_or(0))));
}

void DIBasicTypeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "tag = ";
    odsPrinter << llvm::dwarf::TagString(getTag());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "name = ";
    odsPrinter.printStrippedAttrOrType(getName());
    if (!(getSizeInBits() == uint64_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "sizeInBits = ";
      if (!(getSizeInBits() == uint64_t())) {
        odsPrinter.printStrippedAttrOrType(getSizeInBits());
      }
    }
    if (!(getEncoding() == 0)) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "encoding = ";
      if (!(getEncoding() == 0)) {
        odsPrinter << llvm::dwarf::AttributeEncodingString(getEncoding());
      }
    }
  }
  odsPrinter << ">";
}

unsigned DIBasicTypeAttr::getTag() const {
  return getImpl()->tag;
}

StringAttr DIBasicTypeAttr::getName() const {
  return getImpl()->name;
}

uint64_t DIBasicTypeAttr::getSizeInBits() const {
  return getImpl()->sizeInBits;
}

unsigned DIBasicTypeAttr::getEncoding() const {
  return getImpl()->encoding;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIBasicTypeAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DICompileUnitAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<unsigned, DIFileAttr, StringAttr, bool, DIEmissionKind>;
  DICompileUnitAttrStorage(unsigned sourceLanguage, DIFileAttr file, StringAttr producer, bool isOptimized, DIEmissionKind emissionKind) : sourceLanguage(sourceLanguage), file(file), producer(producer), isOptimized(isOptimized), emissionKind(emissionKind) {}

  KeyTy getAsKey() const {
    return KeyTy(sourceLanguage, file, producer, isOptimized, emissionKind);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (sourceLanguage == std::get<0>(tblgenKey)) && (file == std::get<1>(tblgenKey)) && (producer == std::get<2>(tblgenKey)) && (isOptimized == std::get<3>(tblgenKey)) && (emissionKind == std::get<4>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey), std::get<4>(tblgenKey));
  }

  static DICompileUnitAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto sourceLanguage = std::get<0>(tblgenKey);
    auto file = std::get<1>(tblgenKey);
    auto producer = std::get<2>(tblgenKey);
    auto isOptimized = std::get<3>(tblgenKey);
    auto emissionKind = std::get<4>(tblgenKey);
    return new (allocator.allocate<DICompileUnitAttrStorage>()) DICompileUnitAttrStorage(sourceLanguage, file, producer, isOptimized, emissionKind);
  }

  unsigned sourceLanguage;
  DIFileAttr file;
  StringAttr producer;
  bool isOptimized;
  DIEmissionKind emissionKind;
};
} // namespace detail
DICompileUnitAttr DICompileUnitAttr::get(::mlir::MLIRContext *context, unsigned sourceLanguage, DIFileAttr file, StringAttr producer, bool isOptimized, DIEmissionKind emissionKind) {
  return Base::get(context, sourceLanguage, file, producer, isOptimized, emissionKind);
}

::mlir::Attribute DICompileUnitAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<unsigned> _result_sourceLanguage;
  ::mlir::FailureOr<DIFileAttr> _result_file;
  ::mlir::FailureOr<StringAttr> _result_producer;
  ::mlir::FailureOr<bool> _result_isOptimized;
  ::mlir::FailureOr<DIEmissionKind> _result_emissionKind;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_sourceLanguage = false;
  bool _seen_file = false;
  bool _seen_producer = false;
  bool _seen_isOptimized = false;
  bool _seen_emissionKind = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_sourceLanguage && _paramKey == "sourceLanguage") {
        _seen_sourceLanguage = true;

        // Parse variable 'sourceLanguage'
        _result_sourceLanguage =  [&]() -> FailureOr<unsigned> {
            SMLoc tagLoc = odsParser.getCurrentLocation();
            StringRef name;
            if (odsParser.parseKeyword(&name))
              return failure();

            if (unsigned tag = llvm::dwarf::getLanguage(name))
              return tag;
            return odsParser.emitError(tagLoc)
              << "invalid debug info debug info language name: " << name;
          }() ;
        if (::mlir::failed(_result_sourceLanguage)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompileUnitAttr parameter 'sourceLanguage' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_file && _paramKey == "file") {
        _seen_file = true;

        // Parse variable 'file'
        _result_file = ::mlir::FieldParser<DIFileAttr>::parse(odsParser);
        if (::mlir::failed(_result_file)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompileUnitAttr parameter 'file' which is to be a `DIFileAttr`");
          return {};
        }
      } else if (!_seen_producer && _paramKey == "producer") {
        _seen_producer = true;

        // Parse variable 'producer'
        _result_producer = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_producer)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompileUnitAttr parameter 'producer' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_isOptimized && _paramKey == "isOptimized") {
        _seen_isOptimized = true;

        // Parse variable 'isOptimized'
        _result_isOptimized = ::mlir::FieldParser<bool>::parse(odsParser);
        if (::mlir::failed(_result_isOptimized)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompileUnitAttr parameter 'isOptimized' which is to be a `bool`");
          return {};
        }
      } else if (!_seen_emissionKind && _paramKey == "emissionKind") {
        _seen_emissionKind = true;

        // Parse variable 'emissionKind'
        _result_emissionKind = ::mlir::FieldParser<DIEmissionKind>::parse(odsParser);
        if (::mlir::failed(_result_emissionKind)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompileUnitAttr parameter 'emissionKind' which is to be a `DIEmissionKind`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    for (unsigned odsStructIndex = 0; odsStructIndex < 5; ++odsStructIndex) {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
      if ((odsStructIndex != 5 - 1) && odsParser.parseComma())
        return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_sourceLanguage));
  assert(::mlir::succeeded(_result_file));
  assert(::mlir::succeeded(_result_producer));
  assert(::mlir::succeeded(_result_isOptimized));
  assert(::mlir::succeeded(_result_emissionKind));
  return DICompileUnitAttr::get(odsParser.getContext(),
      unsigned((*_result_sourceLanguage)),
      DIFileAttr((*_result_file)),
      StringAttr((*_result_producer)),
      bool((*_result_isOptimized)),
      DIEmissionKind((*_result_emissionKind)));
}

void DICompileUnitAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "sourceLanguage = ";
    odsPrinter << llvm::dwarf::LanguageString(getSourceLanguage());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "file = ";
    odsPrinter.printStrippedAttrOrType(getFile());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "producer = ";
    odsPrinter.printStrippedAttrOrType(getProducer());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "isOptimized = ";
    odsPrinter.printStrippedAttrOrType(getIsOptimized());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "emissionKind = ";
    odsPrinter.printStrippedAttrOrType(getEmissionKind());
  }
  odsPrinter << ">";
}

unsigned DICompileUnitAttr::getSourceLanguage() const {
  return getImpl()->sourceLanguage;
}

DIFileAttr DICompileUnitAttr::getFile() const {
  return getImpl()->file;
}

StringAttr DICompileUnitAttr::getProducer() const {
  return getImpl()->producer;
}

bool DICompileUnitAttr::getIsOptimized() const {
  return getImpl()->isOptimized;
}

DIEmissionKind DICompileUnitAttr::getEmissionKind() const {
  return getImpl()->emissionKind;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DICompileUnitAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DICompositeTypeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<unsigned, StringAttr, DIFileAttr, uint32_t, DIScopeAttr, DITypeAttr, DIFlags, uint64_t, uint64_t, ::llvm::ArrayRef<DINodeAttr>>;
  DICompositeTypeAttrStorage(unsigned tag, StringAttr name, DIFileAttr file, uint32_t line, DIScopeAttr scope, DITypeAttr baseType, DIFlags flags, uint64_t sizeInBits, uint64_t alignInBits, ::llvm::ArrayRef<DINodeAttr> elements) : tag(tag), name(name), file(file), line(line), scope(scope), baseType(baseType), flags(flags), sizeInBits(sizeInBits), alignInBits(alignInBits), elements(elements) {}

  KeyTy getAsKey() const {
    return KeyTy(tag, name, file, line, scope, baseType, flags, sizeInBits, alignInBits, elements);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (tag == std::get<0>(tblgenKey)) && (name == std::get<1>(tblgenKey)) && (file == std::get<2>(tblgenKey)) && (line == std::get<3>(tblgenKey)) && (scope == std::get<4>(tblgenKey)) && (baseType == std::get<5>(tblgenKey)) && (flags == std::get<6>(tblgenKey)) && (sizeInBits == std::get<7>(tblgenKey)) && (alignInBits == std::get<8>(tblgenKey)) && (::llvm::ArrayRef<DINodeAttr>(elements) == ::llvm::ArrayRef<DINodeAttr>(std::get<9>(tblgenKey)));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey), std::get<4>(tblgenKey), std::get<5>(tblgenKey), std::get<6>(tblgenKey), std::get<7>(tblgenKey), std::get<8>(tblgenKey), std::get<9>(tblgenKey));
  }

  static DICompositeTypeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto tag = std::get<0>(tblgenKey);
    auto name = std::get<1>(tblgenKey);
    auto file = std::get<2>(tblgenKey);
    auto line = std::get<3>(tblgenKey);
    auto scope = std::get<4>(tblgenKey);
    auto baseType = std::get<5>(tblgenKey);
    auto flags = std::get<6>(tblgenKey);
    auto sizeInBits = std::get<7>(tblgenKey);
    auto alignInBits = std::get<8>(tblgenKey);
    auto elements = std::get<9>(tblgenKey);
    elements = allocator.copyInto(elements);
    return new (allocator.allocate<DICompositeTypeAttrStorage>()) DICompositeTypeAttrStorage(tag, name, file, line, scope, baseType, flags, sizeInBits, alignInBits, elements);
  }

  unsigned tag;
  StringAttr name;
  DIFileAttr file;
  uint32_t line;
  DIScopeAttr scope;
  DITypeAttr baseType;
  DIFlags flags;
  uint64_t sizeInBits;
  uint64_t alignInBits;
  ::llvm::ArrayRef<DINodeAttr> elements;
};
} // namespace detail
DICompositeTypeAttr DICompositeTypeAttr::get(::mlir::MLIRContext *context, unsigned tag, StringAttr name, DIFileAttr file, uint32_t line, DIScopeAttr scope, DITypeAttr baseType, DIFlags flags, uint64_t sizeInBits, uint64_t alignInBits, ::llvm::ArrayRef<DINodeAttr> elements) {
  return Base::get(context, tag, name, file, line, scope, baseType, flags, sizeInBits, alignInBits, elements);
}

::mlir::Attribute DICompositeTypeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<unsigned> _result_tag;
  ::mlir::FailureOr<StringAttr> _result_name;
  ::mlir::FailureOr<DIFileAttr> _result_file;
  ::mlir::FailureOr<uint32_t> _result_line;
  ::mlir::FailureOr<DIScopeAttr> _result_scope;
  ::mlir::FailureOr<DITypeAttr> _result_baseType;
  ::mlir::FailureOr<DIFlags> _result_flags;
  ::mlir::FailureOr<uint64_t> _result_sizeInBits;
  ::mlir::FailureOr<uint64_t> _result_alignInBits;
  ::mlir::FailureOr<::llvm::SmallVector<DINodeAttr>> _result_elements;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_tag = false;
  bool _seen_name = false;
  bool _seen_file = false;
  bool _seen_line = false;
  bool _seen_scope = false;
  bool _seen_baseType = false;
  bool _seen_flags = false;
  bool _seen_sizeInBits = false;
  bool _seen_alignInBits = false;
  bool _seen_elements = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_tag && _paramKey == "tag") {
        _seen_tag = true;

        // Parse variable 'tag'
        _result_tag =  [&]() -> FailureOr<unsigned> {
            SMLoc tagLoc = odsParser.getCurrentLocation();
            StringRef name;
            if (odsParser.parseKeyword(&name))
              return failure();

            if (unsigned tag = llvm::dwarf::getTag(name))
              return tag;
            return odsParser.emitError(tagLoc)
              << "invalid debug info debug info tag name: " << name;
          }() ;
        if (::mlir::failed(_result_tag)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'tag' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_name && _paramKey == "name") {
        _seen_name = true;

        // Parse variable 'name'
        _result_name = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_name)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'name' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_file && _paramKey == "file") {
        _seen_file = true;

        // Parse variable 'file'
        _result_file = ::mlir::FieldParser<DIFileAttr>::parse(odsParser);
        if (::mlir::failed(_result_file)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'file' which is to be a `DIFileAttr`");
          return {};
        }
      } else if (!_seen_line && _paramKey == "line") {
        _seen_line = true;

        // Parse variable 'line'
        _result_line = ::mlir::FieldParser<uint32_t>::parse(odsParser);
        if (::mlir::failed(_result_line)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'line' which is to be a `uint32_t`");
          return {};
        }
      } else if (!_seen_scope && _paramKey == "scope") {
        _seen_scope = true;

        // Parse variable 'scope'
        _result_scope = ::mlir::FieldParser<DIScopeAttr>::parse(odsParser);
        if (::mlir::failed(_result_scope)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'scope' which is to be a `DIScopeAttr`");
          return {};
        }
      } else if (!_seen_baseType && _paramKey == "baseType") {
        _seen_baseType = true;

        // Parse variable 'baseType'
        _result_baseType = ::mlir::FieldParser<DITypeAttr>::parse(odsParser);
        if (::mlir::failed(_result_baseType)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'baseType' which is to be a `DITypeAttr`");
          return {};
        }
      } else if (!_seen_flags && _paramKey == "flags") {
        _seen_flags = true;

        // Parse variable 'flags'
        _result_flags = ::mlir::FieldParser<DIFlags>::parse(odsParser);
        if (::mlir::failed(_result_flags)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'flags' which is to be a `DIFlags`");
          return {};
        }
      } else if (!_seen_sizeInBits && _paramKey == "sizeInBits") {
        _seen_sizeInBits = true;

        // Parse variable 'sizeInBits'
        _result_sizeInBits = ::mlir::FieldParser<uint64_t>::parse(odsParser);
        if (::mlir::failed(_result_sizeInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'sizeInBits' which is to be a `uint64_t`");
          return {};
        }
      } else if (!_seen_alignInBits && _paramKey == "alignInBits") {
        _seen_alignInBits = true;

        // Parse variable 'alignInBits'
        _result_alignInBits = ::mlir::FieldParser<uint64_t>::parse(odsParser);
        if (::mlir::failed(_result_alignInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'alignInBits' which is to be a `uint64_t`");
          return {};
        }
      } else if (!_seen_elements && _paramKey == "elements") {
        _seen_elements = true;

        // Parse variable 'elements'
        _result_elements = ::mlir::FieldParser<::llvm::SmallVector<DINodeAttr>>::parse(odsParser);
        if (::mlir::failed(_result_elements)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DICompositeTypeAttr parameter 'elements' which is to be a `::llvm::ArrayRef<DINodeAttr>`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_tag) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "tag";
      return {};
    }
    if (!_seen_name) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "name";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_tag));
  assert(::mlir::succeeded(_result_name));
  return DICompositeTypeAttr::get(odsParser.getContext(),
      unsigned((*_result_tag)),
      StringAttr((*_result_name)),
      DIFileAttr((_result_file.value_or(DIFileAttr()))),
      uint32_t((_result_line.value_or(uint32_t()))),
      DIScopeAttr((_result_scope.value_or(DIScopeAttr()))),
      DITypeAttr((_result_baseType.value_or(DITypeAttr()))),
      DIFlags((_result_flags.value_or(DIFlags()))),
      uint64_t((_result_sizeInBits.value_or(uint64_t()))),
      uint64_t((_result_alignInBits.value_or(uint64_t()))),
      ::llvm::ArrayRef<DINodeAttr>((_result_elements.value_or(::llvm::SmallVector<DINodeAttr>()))));
}

void DICompositeTypeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "tag = ";
    odsPrinter << llvm::dwarf::TagString(getTag());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "name = ";
    odsPrinter.printStrippedAttrOrType(getName());
    if (!(getFile() == DIFileAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "file = ";
      if (!(getFile() == DIFileAttr())) {
        odsPrinter.printStrippedAttrOrType(getFile());
      }
    }
    if (!(getLine() == uint32_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "line = ";
      if (!(getLine() == uint32_t())) {
        odsPrinter.printStrippedAttrOrType(getLine());
      }
    }
    if (!(getScope() == DIScopeAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "scope = ";
      if (!(getScope() == DIScopeAttr())) {
        odsPrinter.printStrippedAttrOrType(getScope());
      }
    }
    if (!(getBaseType() == DITypeAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "baseType = ";
      if (!(getBaseType() == DITypeAttr())) {
        odsPrinter.printStrippedAttrOrType(getBaseType());
      }
    }
    if (!(getFlags() == DIFlags())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "flags = ";
      if (!(getFlags() == DIFlags())) {
        odsPrinter.printStrippedAttrOrType(getFlags());
      }
    }
    if (!(getSizeInBits() == uint64_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "sizeInBits = ";
      if (!(getSizeInBits() == uint64_t())) {
        odsPrinter.printStrippedAttrOrType(getSizeInBits());
      }
    }
    if (!(getAlignInBits() == uint64_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "alignInBits = ";
      if (!(getAlignInBits() == uint64_t())) {
        odsPrinter.printStrippedAttrOrType(getAlignInBits());
      }
    }
    if (!(::llvm::ArrayRef<DINodeAttr>(getElements()) == ::llvm::ArrayRef<DINodeAttr>(::llvm::SmallVector<DINodeAttr>()))) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "elements = ";
      if (!(::llvm::ArrayRef<DINodeAttr>(getElements()) == ::llvm::ArrayRef<DINodeAttr>(::llvm::SmallVector<DINodeAttr>()))) {
        odsPrinter.printStrippedAttrOrType(getElements());
      }
    }
  }
  odsPrinter << ">";
}

unsigned DICompositeTypeAttr::getTag() const {
  return getImpl()->tag;
}

StringAttr DICompositeTypeAttr::getName() const {
  return getImpl()->name;
}

DIFileAttr DICompositeTypeAttr::getFile() const {
  return getImpl()->file;
}

uint32_t DICompositeTypeAttr::getLine() const {
  return getImpl()->line;
}

DIScopeAttr DICompositeTypeAttr::getScope() const {
  return getImpl()->scope;
}

DITypeAttr DICompositeTypeAttr::getBaseType() const {
  return getImpl()->baseType;
}

DIFlags DICompositeTypeAttr::getFlags() const {
  return getImpl()->flags;
}

uint64_t DICompositeTypeAttr::getSizeInBits() const {
  return getImpl()->sizeInBits;
}

uint64_t DICompositeTypeAttr::getAlignInBits() const {
  return getImpl()->alignInBits;
}

::llvm::ArrayRef<DINodeAttr> DICompositeTypeAttr::getElements() const {
  return getImpl()->elements;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DICompositeTypeAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DIDerivedTypeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<unsigned, StringAttr, DITypeAttr, uint64_t, uint32_t, uint64_t>;
  DIDerivedTypeAttrStorage(unsigned tag, StringAttr name, DITypeAttr baseType, uint64_t sizeInBits, uint32_t alignInBits, uint64_t offsetInBits) : tag(tag), name(name), baseType(baseType), sizeInBits(sizeInBits), alignInBits(alignInBits), offsetInBits(offsetInBits) {}

  KeyTy getAsKey() const {
    return KeyTy(tag, name, baseType, sizeInBits, alignInBits, offsetInBits);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (tag == std::get<0>(tblgenKey)) && (name == std::get<1>(tblgenKey)) && (baseType == std::get<2>(tblgenKey)) && (sizeInBits == std::get<3>(tblgenKey)) && (alignInBits == std::get<4>(tblgenKey)) && (offsetInBits == std::get<5>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey), std::get<4>(tblgenKey), std::get<5>(tblgenKey));
  }

  static DIDerivedTypeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto tag = std::get<0>(tblgenKey);
    auto name = std::get<1>(tblgenKey);
    auto baseType = std::get<2>(tblgenKey);
    auto sizeInBits = std::get<3>(tblgenKey);
    auto alignInBits = std::get<4>(tblgenKey);
    auto offsetInBits = std::get<5>(tblgenKey);
    return new (allocator.allocate<DIDerivedTypeAttrStorage>()) DIDerivedTypeAttrStorage(tag, name, baseType, sizeInBits, alignInBits, offsetInBits);
  }

  unsigned tag;
  StringAttr name;
  DITypeAttr baseType;
  uint64_t sizeInBits;
  uint32_t alignInBits;
  uint64_t offsetInBits;
};
} // namespace detail
DIDerivedTypeAttr DIDerivedTypeAttr::get(::mlir::MLIRContext *context, unsigned tag, StringAttr name, DITypeAttr baseType, uint64_t sizeInBits, uint32_t alignInBits, uint64_t offsetInBits) {
  return Base::get(context, tag, name, baseType, sizeInBits, alignInBits, offsetInBits);
}

::mlir::Attribute DIDerivedTypeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<unsigned> _result_tag;
  ::mlir::FailureOr<StringAttr> _result_name;
  ::mlir::FailureOr<DITypeAttr> _result_baseType;
  ::mlir::FailureOr<uint64_t> _result_sizeInBits;
  ::mlir::FailureOr<uint32_t> _result_alignInBits;
  ::mlir::FailureOr<uint64_t> _result_offsetInBits;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_tag = false;
  bool _seen_name = false;
  bool _seen_baseType = false;
  bool _seen_sizeInBits = false;
  bool _seen_alignInBits = false;
  bool _seen_offsetInBits = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_tag && _paramKey == "tag") {
        _seen_tag = true;

        // Parse variable 'tag'
        _result_tag =  [&]() -> FailureOr<unsigned> {
            SMLoc tagLoc = odsParser.getCurrentLocation();
            StringRef name;
            if (odsParser.parseKeyword(&name))
              return failure();

            if (unsigned tag = llvm::dwarf::getTag(name))
              return tag;
            return odsParser.emitError(tagLoc)
              << "invalid debug info debug info tag name: " << name;
          }() ;
        if (::mlir::failed(_result_tag)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIDerivedTypeAttr parameter 'tag' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_name && _paramKey == "name") {
        _seen_name = true;

        // Parse variable 'name'
        _result_name = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_name)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIDerivedTypeAttr parameter 'name' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_baseType && _paramKey == "baseType") {
        _seen_baseType = true;

        // Parse variable 'baseType'
        _result_baseType = ::mlir::FieldParser<DITypeAttr>::parse(odsParser);
        if (::mlir::failed(_result_baseType)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIDerivedTypeAttr parameter 'baseType' which is to be a `DITypeAttr`");
          return {};
        }
      } else if (!_seen_sizeInBits && _paramKey == "sizeInBits") {
        _seen_sizeInBits = true;

        // Parse variable 'sizeInBits'
        _result_sizeInBits = ::mlir::FieldParser<uint64_t>::parse(odsParser);
        if (::mlir::failed(_result_sizeInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIDerivedTypeAttr parameter 'sizeInBits' which is to be a `uint64_t`");
          return {};
        }
      } else if (!_seen_alignInBits && _paramKey == "alignInBits") {
        _seen_alignInBits = true;

        // Parse variable 'alignInBits'
        _result_alignInBits = ::mlir::FieldParser<uint32_t>::parse(odsParser);
        if (::mlir::failed(_result_alignInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIDerivedTypeAttr parameter 'alignInBits' which is to be a `uint32_t`");
          return {};
        }
      } else if (!_seen_offsetInBits && _paramKey == "offsetInBits") {
        _seen_offsetInBits = true;

        // Parse variable 'offsetInBits'
        _result_offsetInBits = ::mlir::FieldParser<uint64_t>::parse(odsParser);
        if (::mlir::failed(_result_offsetInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIDerivedTypeAttr parameter 'offsetInBits' which is to be a `uint64_t`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_tag) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "tag";
      return {};
    }
    if (!_seen_baseType) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "baseType";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_tag));
  assert(::mlir::succeeded(_result_baseType));
  return DIDerivedTypeAttr::get(odsParser.getContext(),
      unsigned((*_result_tag)),
      StringAttr((_result_name.value_or(StringAttr()))),
      DITypeAttr((*_result_baseType)),
      uint64_t((_result_sizeInBits.value_or(uint64_t()))),
      uint32_t((_result_alignInBits.value_or(uint32_t()))),
      uint64_t((_result_offsetInBits.value_or(uint64_t()))));
}

void DIDerivedTypeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "tag = ";
    odsPrinter << llvm::dwarf::TagString(getTag());
    if (!(getName() == StringAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "name = ";
      if (!(getName() == StringAttr())) {
        odsPrinter.printStrippedAttrOrType(getName());
      }
    }
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "baseType = ";
    odsPrinter.printStrippedAttrOrType(getBaseType());
    if (!(getSizeInBits() == uint64_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "sizeInBits = ";
      if (!(getSizeInBits() == uint64_t())) {
        odsPrinter.printStrippedAttrOrType(getSizeInBits());
      }
    }
    if (!(getAlignInBits() == uint32_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "alignInBits = ";
      if (!(getAlignInBits() == uint32_t())) {
        odsPrinter.printStrippedAttrOrType(getAlignInBits());
      }
    }
    if (!(getOffsetInBits() == uint64_t())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "offsetInBits = ";
      if (!(getOffsetInBits() == uint64_t())) {
        odsPrinter.printStrippedAttrOrType(getOffsetInBits());
      }
    }
  }
  odsPrinter << ">";
}

unsigned DIDerivedTypeAttr::getTag() const {
  return getImpl()->tag;
}

StringAttr DIDerivedTypeAttr::getName() const {
  return getImpl()->name;
}

DITypeAttr DIDerivedTypeAttr::getBaseType() const {
  return getImpl()->baseType;
}

uint64_t DIDerivedTypeAttr::getSizeInBits() const {
  return getImpl()->sizeInBits;
}

uint32_t DIDerivedTypeAttr::getAlignInBits() const {
  return getImpl()->alignInBits;
}

uint64_t DIDerivedTypeAttr::getOffsetInBits() const {
  return getImpl()->offsetInBits;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIDerivedTypeAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DIFileAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<StringAttr, StringAttr>;
  DIFileAttrStorage(StringAttr name, StringAttr directory) : name(name), directory(directory) {}

  KeyTy getAsKey() const {
    return KeyTy(name, directory);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (name == std::get<0>(tblgenKey)) && (directory == std::get<1>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey));
  }

  static DIFileAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto name = std::get<0>(tblgenKey);
    auto directory = std::get<1>(tblgenKey);
    return new (allocator.allocate<DIFileAttrStorage>()) DIFileAttrStorage(name, directory);
  }

  StringAttr name;
  StringAttr directory;
};
} // namespace detail
DIFileAttr DIFileAttr::get(::mlir::MLIRContext *context, StringAttr name, StringAttr directory) {
  return Base::get(context, name, directory);
}

DIFileAttr DIFileAttr::get(::mlir::MLIRContext *context, StringRef name, StringRef directory) {
  return Base::get(context, StringAttr::get(context, name),
               StringAttr::get(context, directory));
}

::mlir::Attribute DIFileAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<StringAttr> _result_name;
  ::mlir::FailureOr<StringAttr> _result_directory;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};

  // Parse variable 'name'
  _result_name = ::mlir::FieldParser<StringAttr>::parse(odsParser);
  if (::mlir::failed(_result_name)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIFileAttr parameter 'name' which is to be a `StringAttr`");
    return {};
  }
  // Parse literal 'in'
  if (odsParser.parseKeyword("in")) return {};

  // Parse variable 'directory'
  _result_directory = ::mlir::FieldParser<StringAttr>::parse(odsParser);
  if (::mlir::failed(_result_directory)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DIFileAttr parameter 'directory' which is to be a `StringAttr`");
    return {};
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_name));
  assert(::mlir::succeeded(_result_directory));
  return DIFileAttr::get(odsParser.getContext(),
      StringAttr((*_result_name)),
      StringAttr((*_result_directory)));
}

void DIFileAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  odsPrinter.printStrippedAttrOrType(getName());
  odsPrinter << ' ' << "in";
  odsPrinter << ' ';
  odsPrinter.printStrippedAttrOrType(getDirectory());
  odsPrinter << ">";
}

StringAttr DIFileAttr::getName() const {
  return getImpl()->name;
}

StringAttr DIFileAttr::getDirectory() const {
  return getImpl()->directory;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIFileAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DILexicalBlockAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<DIScopeAttr, DIFileAttr, unsigned, unsigned>;
  DILexicalBlockAttrStorage(DIScopeAttr scope, DIFileAttr file, unsigned line, unsigned column) : scope(scope), file(file), line(line), column(column) {}

  KeyTy getAsKey() const {
    return KeyTy(scope, file, line, column);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (scope == std::get<0>(tblgenKey)) && (file == std::get<1>(tblgenKey)) && (line == std::get<2>(tblgenKey)) && (column == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static DILexicalBlockAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto scope = std::get<0>(tblgenKey);
    auto file = std::get<1>(tblgenKey);
    auto line = std::get<2>(tblgenKey);
    auto column = std::get<3>(tblgenKey);
    return new (allocator.allocate<DILexicalBlockAttrStorage>()) DILexicalBlockAttrStorage(scope, file, line, column);
  }

  DIScopeAttr scope;
  DIFileAttr file;
  unsigned line;
  unsigned column;
};
} // namespace detail
DILexicalBlockAttr DILexicalBlockAttr::get(::mlir::MLIRContext *context, DIScopeAttr scope, DIFileAttr file, unsigned line, unsigned column) {
  return Base::get(context, scope, file, line, column);
}

DILexicalBlockAttr DILexicalBlockAttr::get(DIScopeAttr scope, DIFileAttr file, unsigned line, unsigned column) {
  return Base::get(file.getContext(), scope, file, line, column);
}

::mlir::Attribute DILexicalBlockAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<DIScopeAttr> _result_scope;
  ::mlir::FailureOr<DIFileAttr> _result_file;
  ::mlir::FailureOr<unsigned> _result_line;
  ::mlir::FailureOr<unsigned> _result_column;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_scope = false;
  bool _seen_file = false;
  bool _seen_line = false;
  bool _seen_column = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_scope && _paramKey == "scope") {
        _seen_scope = true;

        // Parse variable 'scope'
        _result_scope = ::mlir::FieldParser<DIScopeAttr>::parse(odsParser);
        if (::mlir::failed(_result_scope)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockAttr parameter 'scope' which is to be a `DIScopeAttr`");
          return {};
        }
      } else if (!_seen_file && _paramKey == "file") {
        _seen_file = true;

        // Parse variable 'file'
        _result_file = ::mlir::FieldParser<DIFileAttr>::parse(odsParser);
        if (::mlir::failed(_result_file)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockAttr parameter 'file' which is to be a `DIFileAttr`");
          return {};
        }
      } else if (!_seen_line && _paramKey == "line") {
        _seen_line = true;

        // Parse variable 'line'
        _result_line = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_line)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockAttr parameter 'line' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_column && _paramKey == "column") {
        _seen_column = true;

        // Parse variable 'column'
        _result_column = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_column)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockAttr parameter 'column' which is to be a `unsigned`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_scope) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "scope";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_scope));
  return DILexicalBlockAttr::get(odsParser.getContext(),
      DIScopeAttr((*_result_scope)),
      DIFileAttr((_result_file.value_or(DIFileAttr()))),
      unsigned((_result_line.value_or(unsigned()))),
      unsigned((_result_column.value_or(unsigned()))));
}

void DILexicalBlockAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "scope = ";
    odsPrinter.printStrippedAttrOrType(getScope());
    if (!(getFile() == DIFileAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "file = ";
      if (!(getFile() == DIFileAttr())) {
        odsPrinter.printStrippedAttrOrType(getFile());
      }
    }
    if (!(getLine() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "line = ";
      if (!(getLine() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getLine());
      }
    }
    if (!(getColumn() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "column = ";
      if (!(getColumn() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getColumn());
      }
    }
  }
  odsPrinter << ">";
}

DIScopeAttr DILexicalBlockAttr::getScope() const {
  return getImpl()->scope;
}

DIFileAttr DILexicalBlockAttr::getFile() const {
  return getImpl()->file;
}

unsigned DILexicalBlockAttr::getLine() const {
  return getImpl()->line;
}

unsigned DILexicalBlockAttr::getColumn() const {
  return getImpl()->column;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DILexicalBlockAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DILexicalBlockFileAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<DIScopeAttr, DIFileAttr, unsigned>;
  DILexicalBlockFileAttrStorage(DIScopeAttr scope, DIFileAttr file, unsigned discriminator) : scope(scope), file(file), discriminator(discriminator) {}

  KeyTy getAsKey() const {
    return KeyTy(scope, file, discriminator);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (scope == std::get<0>(tblgenKey)) && (file == std::get<1>(tblgenKey)) && (discriminator == std::get<2>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey));
  }

  static DILexicalBlockFileAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto scope = std::get<0>(tblgenKey);
    auto file = std::get<1>(tblgenKey);
    auto discriminator = std::get<2>(tblgenKey);
    return new (allocator.allocate<DILexicalBlockFileAttrStorage>()) DILexicalBlockFileAttrStorage(scope, file, discriminator);
  }

  DIScopeAttr scope;
  DIFileAttr file;
  unsigned discriminator;
};
} // namespace detail
DILexicalBlockFileAttr DILexicalBlockFileAttr::get(::mlir::MLIRContext *context, DIScopeAttr scope, DIFileAttr file, unsigned discriminator) {
  return Base::get(context, scope, file, discriminator);
}

DILexicalBlockFileAttr DILexicalBlockFileAttr::get(DIScopeAttr scope, DIFileAttr file, unsigned discriminator) {
  return Base::get(file.getContext(), scope, file, discriminator);
}

::mlir::Attribute DILexicalBlockFileAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<DIScopeAttr> _result_scope;
  ::mlir::FailureOr<DIFileAttr> _result_file;
  ::mlir::FailureOr<unsigned> _result_discriminator;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_scope = false;
  bool _seen_file = false;
  bool _seen_discriminator = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_scope && _paramKey == "scope") {
        _seen_scope = true;

        // Parse variable 'scope'
        _result_scope = ::mlir::FieldParser<DIScopeAttr>::parse(odsParser);
        if (::mlir::failed(_result_scope)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockFile parameter 'scope' which is to be a `DIScopeAttr`");
          return {};
        }
      } else if (!_seen_file && _paramKey == "file") {
        _seen_file = true;

        // Parse variable 'file'
        _result_file = ::mlir::FieldParser<DIFileAttr>::parse(odsParser);
        if (::mlir::failed(_result_file)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockFile parameter 'file' which is to be a `DIFileAttr`");
          return {};
        }
      } else if (!_seen_discriminator && _paramKey == "discriminator") {
        _seen_discriminator = true;

        // Parse variable 'discriminator'
        _result_discriminator = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_discriminator)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILexicalBlockFile parameter 'discriminator' which is to be a `unsigned`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_scope) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "scope";
      return {};
    }
    if (!_seen_discriminator) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "discriminator";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_scope));
  assert(::mlir::succeeded(_result_discriminator));
  return DILexicalBlockFileAttr::get(odsParser.getContext(),
      DIScopeAttr((*_result_scope)),
      DIFileAttr((_result_file.value_or(DIFileAttr()))),
      unsigned((*_result_discriminator)));
}

void DILexicalBlockFileAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "scope = ";
    odsPrinter.printStrippedAttrOrType(getScope());
    if (!(getFile() == DIFileAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "file = ";
      if (!(getFile() == DIFileAttr())) {
        odsPrinter.printStrippedAttrOrType(getFile());
      }
    }
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "discriminator = ";
    odsPrinter.printStrippedAttrOrType(getDiscriminator());
  }
  odsPrinter << ">";
}

DIScopeAttr DILexicalBlockFileAttr::getScope() const {
  return getImpl()->scope;
}

DIFileAttr DILexicalBlockFileAttr::getFile() const {
  return getImpl()->file;
}

unsigned DILexicalBlockFileAttr::getDiscriminator() const {
  return getImpl()->discriminator;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DILexicalBlockFileAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DILocalVariableAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<DIScopeAttr, StringAttr, DIFileAttr, unsigned, unsigned, unsigned, DITypeAttr>;
  DILocalVariableAttrStorage(DIScopeAttr scope, StringAttr name, DIFileAttr file, unsigned line, unsigned arg, unsigned alignInBits, DITypeAttr type) : scope(scope), name(name), file(file), line(line), arg(arg), alignInBits(alignInBits), type(type) {}

  KeyTy getAsKey() const {
    return KeyTy(scope, name, file, line, arg, alignInBits, type);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (scope == std::get<0>(tblgenKey)) && (name == std::get<1>(tblgenKey)) && (file == std::get<2>(tblgenKey)) && (line == std::get<3>(tblgenKey)) && (arg == std::get<4>(tblgenKey)) && (alignInBits == std::get<5>(tblgenKey)) && (type == std::get<6>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey), std::get<4>(tblgenKey), std::get<5>(tblgenKey), std::get<6>(tblgenKey));
  }

  static DILocalVariableAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto scope = std::get<0>(tblgenKey);
    auto name = std::get<1>(tblgenKey);
    auto file = std::get<2>(tblgenKey);
    auto line = std::get<3>(tblgenKey);
    auto arg = std::get<4>(tblgenKey);
    auto alignInBits = std::get<5>(tblgenKey);
    auto type = std::get<6>(tblgenKey);
    return new (allocator.allocate<DILocalVariableAttrStorage>()) DILocalVariableAttrStorage(scope, name, file, line, arg, alignInBits, type);
  }

  DIScopeAttr scope;
  StringAttr name;
  DIFileAttr file;
  unsigned line;
  unsigned arg;
  unsigned alignInBits;
  DITypeAttr type;
};
} // namespace detail
DILocalVariableAttr DILocalVariableAttr::get(::mlir::MLIRContext *context, DIScopeAttr scope, StringAttr name, DIFileAttr file, unsigned line, unsigned arg, unsigned alignInBits, DITypeAttr type) {
  return Base::get(context, scope, name, file, line, arg, alignInBits, type);
}

DILocalVariableAttr DILocalVariableAttr::get(DIScopeAttr scope, StringRef name, DIFileAttr file, unsigned line, unsigned arg, unsigned alignInBits, DITypeAttr type) {
  MLIRContext *ctx = file.getContext();
  return Base::get(ctx, scope, StringAttr::get(ctx, name), file, line,
               arg, alignInBits, type);
}

::mlir::Attribute DILocalVariableAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<DIScopeAttr> _result_scope;
  ::mlir::FailureOr<StringAttr> _result_name;
  ::mlir::FailureOr<DIFileAttr> _result_file;
  ::mlir::FailureOr<unsigned> _result_line;
  ::mlir::FailureOr<unsigned> _result_arg;
  ::mlir::FailureOr<unsigned> _result_alignInBits;
  ::mlir::FailureOr<DITypeAttr> _result_type;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_scope = false;
  bool _seen_name = false;
  bool _seen_file = false;
  bool _seen_line = false;
  bool _seen_arg = false;
  bool _seen_alignInBits = false;
  bool _seen_type = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_scope && _paramKey == "scope") {
        _seen_scope = true;

        // Parse variable 'scope'
        _result_scope = ::mlir::FieldParser<DIScopeAttr>::parse(odsParser);
        if (::mlir::failed(_result_scope)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'scope' which is to be a `DIScopeAttr`");
          return {};
        }
      } else if (!_seen_name && _paramKey == "name") {
        _seen_name = true;

        // Parse variable 'name'
        _result_name = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_name)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'name' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_file && _paramKey == "file") {
        _seen_file = true;

        // Parse variable 'file'
        _result_file = ::mlir::FieldParser<DIFileAttr>::parse(odsParser);
        if (::mlir::failed(_result_file)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'file' which is to be a `DIFileAttr`");
          return {};
        }
      } else if (!_seen_line && _paramKey == "line") {
        _seen_line = true;

        // Parse variable 'line'
        _result_line = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_line)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'line' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_arg && _paramKey == "arg") {
        _seen_arg = true;

        // Parse variable 'arg'
        _result_arg = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_arg)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'arg' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_alignInBits && _paramKey == "alignInBits") {
        _seen_alignInBits = true;

        // Parse variable 'alignInBits'
        _result_alignInBits = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_alignInBits)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'alignInBits' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_type && _paramKey == "type") {
        _seen_type = true;

        // Parse variable 'type'
        _result_type = ::mlir::FieldParser<DITypeAttr>::parse(odsParser);
        if (::mlir::failed(_result_type)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DILocalVariableAttr parameter 'type' which is to be a `DITypeAttr`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_scope) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "scope";
      return {};
    }
    if (!_seen_name) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "name";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_scope));
  assert(::mlir::succeeded(_result_name));
  return DILocalVariableAttr::get(odsParser.getContext(),
      DIScopeAttr((*_result_scope)),
      StringAttr((*_result_name)),
      DIFileAttr((_result_file.value_or(DIFileAttr()))),
      unsigned((_result_line.value_or(unsigned()))),
      unsigned((_result_arg.value_or(unsigned()))),
      unsigned((_result_alignInBits.value_or(unsigned()))),
      DITypeAttr((_result_type.value_or(DITypeAttr()))));
}

void DILocalVariableAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "scope = ";
    odsPrinter.printStrippedAttrOrType(getScope());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "name = ";
    odsPrinter.printStrippedAttrOrType(getName());
    if (!(getFile() == DIFileAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "file = ";
      if (!(getFile() == DIFileAttr())) {
        odsPrinter.printStrippedAttrOrType(getFile());
      }
    }
    if (!(getLine() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "line = ";
      if (!(getLine() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getLine());
      }
    }
    if (!(getArg() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "arg = ";
      if (!(getArg() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getArg());
      }
    }
    if (!(getAlignInBits() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "alignInBits = ";
      if (!(getAlignInBits() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getAlignInBits());
      }
    }
    if (!(getType() == DITypeAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "type = ";
      if (!(getType() == DITypeAttr())) {
        odsPrinter.printStrippedAttrOrType(getType());
      }
    }
  }
  odsPrinter << ">";
}

DIScopeAttr DILocalVariableAttr::getScope() const {
  return getImpl()->scope;
}

StringAttr DILocalVariableAttr::getName() const {
  return getImpl()->name;
}

DIFileAttr DILocalVariableAttr::getFile() const {
  return getImpl()->file;
}

unsigned DILocalVariableAttr::getLine() const {
  return getImpl()->line;
}

unsigned DILocalVariableAttr::getArg() const {
  return getImpl()->arg;
}

unsigned DILocalVariableAttr::getAlignInBits() const {
  return getImpl()->alignInBits;
}

DITypeAttr DILocalVariableAttr::getType() const {
  return getImpl()->type;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DILocalVariableAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DISubprogramAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<DICompileUnitAttr, DIScopeAttr, StringAttr, StringAttr, DIFileAttr, unsigned, unsigned, DISubprogramFlags, DISubroutineTypeAttr>;
  DISubprogramAttrStorage(DICompileUnitAttr compileUnit, DIScopeAttr scope, StringAttr name, StringAttr linkageName, DIFileAttr file, unsigned line, unsigned scopeLine, DISubprogramFlags subprogramFlags, DISubroutineTypeAttr type) : compileUnit(compileUnit), scope(scope), name(name), linkageName(linkageName), file(file), line(line), scopeLine(scopeLine), subprogramFlags(subprogramFlags), type(type) {}

  KeyTy getAsKey() const {
    return KeyTy(compileUnit, scope, name, linkageName, file, line, scopeLine, subprogramFlags, type);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (compileUnit == std::get<0>(tblgenKey)) && (scope == std::get<1>(tblgenKey)) && (name == std::get<2>(tblgenKey)) && (linkageName == std::get<3>(tblgenKey)) && (file == std::get<4>(tblgenKey)) && (line == std::get<5>(tblgenKey)) && (scopeLine == std::get<6>(tblgenKey)) && (subprogramFlags == std::get<7>(tblgenKey)) && (type == std::get<8>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey), std::get<4>(tblgenKey), std::get<5>(tblgenKey), std::get<6>(tblgenKey), std::get<7>(tblgenKey), std::get<8>(tblgenKey));
  }

  static DISubprogramAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto compileUnit = std::get<0>(tblgenKey);
    auto scope = std::get<1>(tblgenKey);
    auto name = std::get<2>(tblgenKey);
    auto linkageName = std::get<3>(tblgenKey);
    auto file = std::get<4>(tblgenKey);
    auto line = std::get<5>(tblgenKey);
    auto scopeLine = std::get<6>(tblgenKey);
    auto subprogramFlags = std::get<7>(tblgenKey);
    auto type = std::get<8>(tblgenKey);
    return new (allocator.allocate<DISubprogramAttrStorage>()) DISubprogramAttrStorage(compileUnit, scope, name, linkageName, file, line, scopeLine, subprogramFlags, type);
  }

  DICompileUnitAttr compileUnit;
  DIScopeAttr scope;
  StringAttr name;
  StringAttr linkageName;
  DIFileAttr file;
  unsigned line;
  unsigned scopeLine;
  DISubprogramFlags subprogramFlags;
  DISubroutineTypeAttr type;
};
} // namespace detail
DISubprogramAttr DISubprogramAttr::get(::mlir::MLIRContext *context, DICompileUnitAttr compileUnit, DIScopeAttr scope, StringAttr name, StringAttr linkageName, DIFileAttr file, unsigned line, unsigned scopeLine, DISubprogramFlags subprogramFlags, DISubroutineTypeAttr type) {
  return Base::get(context, compileUnit, scope, name, linkageName, file, line, scopeLine, subprogramFlags, type);
}

DISubprogramAttr DISubprogramAttr::get(DICompileUnitAttr compileUnit, DIScopeAttr scope, StringRef name, StringRef linkageName, DIFileAttr file, unsigned line, unsigned scopeLine, DISubprogramFlags subprogramFlags, DISubroutineTypeAttr type) {
  MLIRContext *ctx = file.getContext();
  return Base::get(ctx, compileUnit, scope, StringAttr::get(ctx, name),
               StringAttr::get(ctx, linkageName), file, line,
               scopeLine, subprogramFlags, type);
}

::mlir::Attribute DISubprogramAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<DICompileUnitAttr> _result_compileUnit;
  ::mlir::FailureOr<DIScopeAttr> _result_scope;
  ::mlir::FailureOr<StringAttr> _result_name;
  ::mlir::FailureOr<StringAttr> _result_linkageName;
  ::mlir::FailureOr<DIFileAttr> _result_file;
  ::mlir::FailureOr<unsigned> _result_line;
  ::mlir::FailureOr<unsigned> _result_scopeLine;
  ::mlir::FailureOr<DISubprogramFlags> _result_subprogramFlags;
  ::mlir::FailureOr<DISubroutineTypeAttr> _result_type;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_compileUnit = false;
  bool _seen_scope = false;
  bool _seen_name = false;
  bool _seen_linkageName = false;
  bool _seen_file = false;
  bool _seen_line = false;
  bool _seen_scopeLine = false;
  bool _seen_subprogramFlags = false;
  bool _seen_type = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_compileUnit && _paramKey == "compileUnit") {
        _seen_compileUnit = true;

        // Parse variable 'compileUnit'
        _result_compileUnit = ::mlir::FieldParser<DICompileUnitAttr>::parse(odsParser);
        if (::mlir::failed(_result_compileUnit)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'compileUnit' which is to be a `DICompileUnitAttr`");
          return {};
        }
      } else if (!_seen_scope && _paramKey == "scope") {
        _seen_scope = true;

        // Parse variable 'scope'
        _result_scope = ::mlir::FieldParser<DIScopeAttr>::parse(odsParser);
        if (::mlir::failed(_result_scope)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'scope' which is to be a `DIScopeAttr`");
          return {};
        }
      } else if (!_seen_name && _paramKey == "name") {
        _seen_name = true;

        // Parse variable 'name'
        _result_name = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_name)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'name' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_linkageName && _paramKey == "linkageName") {
        _seen_linkageName = true;

        // Parse variable 'linkageName'
        _result_linkageName = ::mlir::FieldParser<StringAttr>::parse(odsParser);
        if (::mlir::failed(_result_linkageName)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'linkageName' which is to be a `StringAttr`");
          return {};
        }
      } else if (!_seen_file && _paramKey == "file") {
        _seen_file = true;

        // Parse variable 'file'
        _result_file = ::mlir::FieldParser<DIFileAttr>::parse(odsParser);
        if (::mlir::failed(_result_file)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'file' which is to be a `DIFileAttr`");
          return {};
        }
      } else if (!_seen_line && _paramKey == "line") {
        _seen_line = true;

        // Parse variable 'line'
        _result_line = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_line)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'line' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_scopeLine && _paramKey == "scopeLine") {
        _seen_scopeLine = true;

        // Parse variable 'scopeLine'
        _result_scopeLine = ::mlir::FieldParser<unsigned>::parse(odsParser);
        if (::mlir::failed(_result_scopeLine)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'scopeLine' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_subprogramFlags && _paramKey == "subprogramFlags") {
        _seen_subprogramFlags = true;

        // Parse variable 'subprogramFlags'
        _result_subprogramFlags = ::mlir::FieldParser<DISubprogramFlags>::parse(odsParser);
        if (::mlir::failed(_result_subprogramFlags)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'subprogramFlags' which is to be a `DISubprogramFlags`");
          return {};
        }
      } else if (!_seen_type && _paramKey == "type") {
        _seen_type = true;

        // Parse variable 'type'
        _result_type = ::mlir::FieldParser<DISubroutineTypeAttr>::parse(odsParser);
        if (::mlir::failed(_result_type)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubprogramAttr parameter 'type' which is to be a `DISubroutineTypeAttr`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    do {
      ::llvm::StringRef _paramKey;
      if (odsParser.parseKeyword(&_paramKey)) {
        odsParser.emitError(odsParser.getCurrentLocation(),
                           "expected a parameter name in struct");
        return {};
      }
      if (!_loop_body(_paramKey)) return {};
    } while(!odsParser.parseOptionalComma());
    if (!_seen_compileUnit) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "compileUnit";
      return {};
    }
    if (!_seen_scope) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "scope";
      return {};
    }
    if (!_seen_name) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "name";
      return {};
    }
    if (!_seen_file) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "file";
      return {};
    }
    if (!_seen_subprogramFlags) {
      odsParser.emitError(odsParser.getCurrentLocation(), "struct is missing required parameter: ") << "subprogramFlags";
      return {};
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_compileUnit));
  assert(::mlir::succeeded(_result_scope));
  assert(::mlir::succeeded(_result_name));
  assert(::mlir::succeeded(_result_file));
  assert(::mlir::succeeded(_result_subprogramFlags));
  return DISubprogramAttr::get(odsParser.getContext(),
      DICompileUnitAttr((*_result_compileUnit)),
      DIScopeAttr((*_result_scope)),
      StringAttr((*_result_name)),
      StringAttr((_result_linkageName.value_or(StringAttr()))),
      DIFileAttr((*_result_file)),
      unsigned((_result_line.value_or(unsigned()))),
      unsigned((_result_scopeLine.value_or(unsigned()))),
      DISubprogramFlags((*_result_subprogramFlags)),
      DISubroutineTypeAttr((_result_type.value_or(DISubroutineTypeAttr()))));
}

void DISubprogramAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "compileUnit = ";
    odsPrinter.printStrippedAttrOrType(getCompileUnit());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "scope = ";
    odsPrinter.printStrippedAttrOrType(getScope());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "name = ";
    odsPrinter.printStrippedAttrOrType(getName());
    if (!(getLinkageName() == StringAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "linkageName = ";
      if (!(getLinkageName() == StringAttr())) {
        odsPrinter.printStrippedAttrOrType(getLinkageName());
      }
    }
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "file = ";
    odsPrinter.printStrippedAttrOrType(getFile());
    if (!(getLine() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "line = ";
      if (!(getLine() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getLine());
      }
    }
    if (!(getScopeLine() == unsigned())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "scopeLine = ";
      if (!(getScopeLine() == unsigned())) {
        odsPrinter.printStrippedAttrOrType(getScopeLine());
      }
    }
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "subprogramFlags = ";
    odsPrinter.printStrippedAttrOrType(getSubprogramFlags());
    if (!(getType() == DISubroutineTypeAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "type = ";
      if (!(getType() == DISubroutineTypeAttr())) {
        odsPrinter.printStrippedAttrOrType(getType());
      }
    }
  }
  odsPrinter << ">";
}

DICompileUnitAttr DISubprogramAttr::getCompileUnit() const {
  return getImpl()->compileUnit;
}

DIScopeAttr DISubprogramAttr::getScope() const {
  return getImpl()->scope;
}

StringAttr DISubprogramAttr::getName() const {
  return getImpl()->name;
}

StringAttr DISubprogramAttr::getLinkageName() const {
  return getImpl()->linkageName;
}

DIFileAttr DISubprogramAttr::getFile() const {
  return getImpl()->file;
}

unsigned DISubprogramAttr::getLine() const {
  return getImpl()->line;
}

unsigned DISubprogramAttr::getScopeLine() const {
  return getImpl()->scopeLine;
}

DISubprogramFlags DISubprogramAttr::getSubprogramFlags() const {
  return getImpl()->subprogramFlags;
}

DISubroutineTypeAttr DISubprogramAttr::getType() const {
  return getImpl()->type;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DISubprogramAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DISubrangeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<IntegerAttr, IntegerAttr, IntegerAttr, IntegerAttr>;
  DISubrangeAttrStorage(IntegerAttr count, IntegerAttr lowerBound, IntegerAttr upperBound, IntegerAttr stride) : count(count), lowerBound(lowerBound), upperBound(upperBound), stride(stride) {}

  KeyTy getAsKey() const {
    return KeyTy(count, lowerBound, upperBound, stride);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (count == std::get<0>(tblgenKey)) && (lowerBound == std::get<1>(tblgenKey)) && (upperBound == std::get<2>(tblgenKey)) && (stride == std::get<3>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
  }

  static DISubrangeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto count = std::get<0>(tblgenKey);
    auto lowerBound = std::get<1>(tblgenKey);
    auto upperBound = std::get<2>(tblgenKey);
    auto stride = std::get<3>(tblgenKey);
    return new (allocator.allocate<DISubrangeAttrStorage>()) DISubrangeAttrStorage(count, lowerBound, upperBound, stride);
  }

  IntegerAttr count;
  IntegerAttr lowerBound;
  IntegerAttr upperBound;
  IntegerAttr stride;
};
} // namespace detail
DISubrangeAttr DISubrangeAttr::get(::mlir::MLIRContext *context, IntegerAttr count, IntegerAttr lowerBound, IntegerAttr upperBound, IntegerAttr stride) {
  return Base::get(context, count, lowerBound, upperBound, stride);
}

::mlir::Attribute DISubrangeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<IntegerAttr> _result_count;
  ::mlir::FailureOr<IntegerAttr> _result_lowerBound;
  ::mlir::FailureOr<IntegerAttr> _result_upperBound;
  ::mlir::FailureOr<IntegerAttr> _result_stride;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_count = false;
  bool _seen_lowerBound = false;
  bool _seen_upperBound = false;
  bool _seen_stride = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_count && _paramKey == "count") {
        _seen_count = true;

        // Parse variable 'count'
        _result_count = ::mlir::FieldParser<IntegerAttr>::parse(odsParser);
        if (::mlir::failed(_result_count)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubrangeAttr parameter 'count' which is to be a `IntegerAttr`");
          return {};
        }
      } else if (!_seen_lowerBound && _paramKey == "lowerBound") {
        _seen_lowerBound = true;

        // Parse variable 'lowerBound'
        _result_lowerBound = ::mlir::FieldParser<IntegerAttr>::parse(odsParser);
        if (::mlir::failed(_result_lowerBound)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubrangeAttr parameter 'lowerBound' which is to be a `IntegerAttr`");
          return {};
        }
      } else if (!_seen_upperBound && _paramKey == "upperBound") {
        _seen_upperBound = true;

        // Parse variable 'upperBound'
        _result_upperBound = ::mlir::FieldParser<IntegerAttr>::parse(odsParser);
        if (::mlir::failed(_result_upperBound)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubrangeAttr parameter 'upperBound' which is to be a `IntegerAttr`");
          return {};
        }
      } else if (!_seen_stride && _paramKey == "stride") {
        _seen_stride = true;

        // Parse variable 'stride'
        _result_stride = ::mlir::FieldParser<IntegerAttr>::parse(odsParser);
        if (::mlir::failed(_result_stride)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubrangeAttr parameter 'stride' which is to be a `IntegerAttr`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    ::llvm::StringRef _paramKey;
    if (!odsParser.parseOptionalKeyword(&_paramKey)) {
      if (!_loop_body(_paramKey)) return {};
      while (!odsParser.parseOptionalComma()) {
        ::llvm::StringRef _paramKey;
        if (odsParser.parseKeyword(&_paramKey)) {
          odsParser.emitError(odsParser.getCurrentLocation(),
                             "expected a parameter name in struct");
          return {};
        }
        if (!_loop_body(_paramKey)) return {};
      }
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  return DISubrangeAttr::get(odsParser.getContext(),
      IntegerAttr((_result_count.value_or(IntegerAttr()))),
      IntegerAttr((_result_lowerBound.value_or(IntegerAttr()))),
      IntegerAttr((_result_upperBound.value_or(IntegerAttr()))),
      IntegerAttr((_result_stride.value_or(IntegerAttr()))));
}

void DISubrangeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!(getCount() == IntegerAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "count = ";
      if (!(getCount() == IntegerAttr())) {
        odsPrinter.printStrippedAttrOrType(getCount());
      }
    }
    if (!(getLowerBound() == IntegerAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "lowerBound = ";
      if (!(getLowerBound() == IntegerAttr())) {
        odsPrinter.printStrippedAttrOrType(getLowerBound());
      }
    }
    if (!(getUpperBound() == IntegerAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "upperBound = ";
      if (!(getUpperBound() == IntegerAttr())) {
        odsPrinter.printStrippedAttrOrType(getUpperBound());
      }
    }
    if (!(getStride() == IntegerAttr())) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "stride = ";
      if (!(getStride() == IntegerAttr())) {
        odsPrinter.printStrippedAttrOrType(getStride());
      }
    }
  }
  odsPrinter << ">";
}

IntegerAttr DISubrangeAttr::getCount() const {
  return getImpl()->count;
}

IntegerAttr DISubrangeAttr::getLowerBound() const {
  return getImpl()->lowerBound;
}

IntegerAttr DISubrangeAttr::getUpperBound() const {
  return getImpl()->upperBound;
}

IntegerAttr DISubrangeAttr::getStride() const {
  return getImpl()->stride;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DISubrangeAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct DISubroutineTypeAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<unsigned, ::llvm::ArrayRef<DITypeAttr>>;
  DISubroutineTypeAttrStorage(unsigned callingConvention, ::llvm::ArrayRef<DITypeAttr> types) : callingConvention(callingConvention), types(types) {}

  KeyTy getAsKey() const {
    return KeyTy(callingConvention, types);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (callingConvention == std::get<0>(tblgenKey)) && (::llvm::ArrayRef<DITypeAttr>(types) == ::llvm::ArrayRef<DITypeAttr>(std::get<1>(tblgenKey)));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey));
  }

  static DISubroutineTypeAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto callingConvention = std::get<0>(tblgenKey);
    auto types = std::get<1>(tblgenKey);
    types = allocator.copyInto(types);
    return new (allocator.allocate<DISubroutineTypeAttrStorage>()) DISubroutineTypeAttrStorage(callingConvention, types);
  }

  unsigned callingConvention;
  ::llvm::ArrayRef<DITypeAttr> types;
};
} // namespace detail
DISubroutineTypeAttr DISubroutineTypeAttr::get(::mlir::MLIRContext *context, unsigned callingConvention, ::llvm::ArrayRef<DITypeAttr> types) {
  return Base::get(context, callingConvention, types);
}

DISubroutineTypeAttr DISubroutineTypeAttr::getChecked(::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError, ::mlir::MLIRContext *context, unsigned callingConvention, ::llvm::ArrayRef<DITypeAttr> types) {
  return Base::getChecked(emitError, context, callingConvention, types);
}

DISubroutineTypeAttr DISubroutineTypeAttr::get(::mlir::MLIRContext *context, ArrayRef<DITypeAttr> types) {
  return Base::get(context, /*callingConvention=*/0, types);
}

DISubroutineTypeAttr DISubroutineTypeAttr::getChecked(::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError, ::mlir::MLIRContext *context, ArrayRef<DITypeAttr> types) {
  return Base::getChecked(emitError, context, /*callingConvention=*/0, types);
}

::mlir::Attribute DISubroutineTypeAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<unsigned> _result_callingConvention;
  ::mlir::FailureOr<::llvm::SmallVector<DITypeAttr>> _result_types;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_callingConvention = false;
  bool _seen_types = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_callingConvention && _paramKey == "callingConvention") {
        _seen_callingConvention = true;

        // Parse variable 'callingConvention'
        _result_callingConvention =  [&]() -> FailureOr<unsigned> {
            SMLoc tagLoc = odsParser.getCurrentLocation();
            StringRef name;
            if (odsParser.parseKeyword(&name))
              return failure();

            if (unsigned tag = llvm::dwarf::getCallingConvention(name))
              return tag;
            return odsParser.emitError(tagLoc)
              << "invalid debug info debug info calling convention name: " << name;
          }() ;
        if (::mlir::failed(_result_callingConvention)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubroutineTypeAttr parameter 'callingConvention' which is to be a `unsigned`");
          return {};
        }
      } else if (!_seen_types && _paramKey == "types") {
        _seen_types = true;

        // Parse variable 'types'
        _result_types = ::mlir::FieldParser<::llvm::SmallVector<DITypeAttr>>::parse(odsParser);
        if (::mlir::failed(_result_types)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_DISubroutineTypeAttr parameter 'types' which is to be a `::llvm::ArrayRef<DITypeAttr>`");
          return {};
        }
      } else {
        odsParser.emitError(odsParser.getCurrentLocation(), "duplicate or unknown struct parameter name: ") << _paramKey;
        return {};
      }
      return true;
    };
    ::llvm::StringRef _paramKey;
    if (!odsParser.parseOptionalKeyword(&_paramKey)) {
      if (!_loop_body(_paramKey)) return {};
      while (!odsParser.parseOptionalComma()) {
        ::llvm::StringRef _paramKey;
        if (odsParser.parseKeyword(&_paramKey)) {
          odsParser.emitError(odsParser.getCurrentLocation(),
                             "expected a parameter name in struct");
          return {};
        }
        if (!_loop_body(_paramKey)) return {};
      }
    }
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  return odsParser.getChecked<DISubroutineTypeAttr>(odsLoc, odsParser.getContext(),
      unsigned((_result_callingConvention.value_or(0))),
      ::llvm::ArrayRef<DITypeAttr>((_result_types.value_or(::llvm::SmallVector<DITypeAttr>()))));
}

void DISubroutineTypeAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!(getCallingConvention() == 0)) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "callingConvention = ";
      if (!(getCallingConvention() == 0)) {
        odsPrinter << llvm::dwarf::ConventionString(getCallingConvention());
      }
    }
    if (!(::llvm::ArrayRef<DITypeAttr>(getTypes()) == ::llvm::ArrayRef<DITypeAttr>(::llvm::SmallVector<DITypeAttr>()))) {
      if (!_firstPrinted) odsPrinter << ", ";
      _firstPrinted = false;
      odsPrinter << "types = ";
      if (!(::llvm::ArrayRef<DITypeAttr>(getTypes()) == ::llvm::ArrayRef<DITypeAttr>(::llvm::SmallVector<DITypeAttr>()))) {
        odsPrinter.printStrippedAttrOrType(getTypes());
      }
    }
  }
  odsPrinter << ">";
}

unsigned DISubroutineTypeAttr::getCallingConvention() const {
  return getImpl()->callingConvention;
}

::llvm::ArrayRef<DITypeAttr> DISubroutineTypeAttr::getTypes() const {
  return getImpl()->types;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DISubroutineTypeAttr)
namespace mlir {
namespace LLVM {
} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIVoidResultTypeAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct FastmathFlagsAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::mlir::LLVM::FastmathFlags>;
  FastmathFlagsAttrStorage(::mlir::LLVM::FastmathFlags value) : value(value) {}

  KeyTy getAsKey() const {
    return KeyTy(value);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (value == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static FastmathFlagsAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto value = std::get<0>(tblgenKey);
    return new (allocator.allocate<FastmathFlagsAttrStorage>()) FastmathFlagsAttrStorage(value);
  }

  ::mlir::LLVM::FastmathFlags value;
};
} // namespace detail
FastmathFlagsAttr FastmathFlagsAttr::get(::mlir::MLIRContext *context, ::mlir::LLVM::FastmathFlags value) {
  return Base::get(context, value);
}

::mlir::Attribute FastmathFlagsAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<::mlir::LLVM::FastmathFlags> _result_value;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};

  // Parse variable 'value'
  _result_value = [&]() -> ::mlir::FailureOr<::mlir::LLVM::FastmathFlags> {
      ::mlir::LLVM::FastmathFlags flags = {};
      auto loc = odsParser.getCurrentLocation();
      ::llvm::StringRef enumKeyword;
      do {
        if (::mlir::failed(odsParser.parseKeyword(&enumKeyword)))
          return ::mlir::failure();
        auto maybeEnum = ::mlir::LLVM::symbolizeFastmathFlags(enumKeyword);
        if (!maybeEnum) {
            return {(::mlir::LogicalResult)(odsParser.emitError(loc) << "expected " << "::mlir::LLVM::FastmathFlags" << " to be one of: " << "none" << ", " << "nnan" << ", " << "ninf" << ", " << "nsz" << ", " << "arcp" << ", " << "contract" << ", " << "afn" << ", " << "reassoc" << ", " << "fast")};
        }
        flags = flags | *maybeEnum;
      } while(::mlir::succeeded(odsParser.parseOptionalComma()));
      return flags;
    }();
  if (::mlir::failed(_result_value)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_FastmathFlagsAttr parameter 'value' which is to be a `::mlir::LLVM::FastmathFlags`");
    return {};
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_value));
  return FastmathFlagsAttr::get(odsParser.getContext(),
      ::mlir::LLVM::FastmathFlags((*_result_value)));
}

void FastmathFlagsAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  odsPrinter << stringifyFastmathFlags(getValue());
  odsPrinter << ">";
}

::mlir::LLVM::FastmathFlags FastmathFlagsAttr::getValue() const {
  return getImpl()->value;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::FastmathFlagsAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct MemoryEffectsAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<ModRefInfo, ModRefInfo, ModRefInfo>;
  MemoryEffectsAttrStorage(ModRefInfo other, ModRefInfo argMem, ModRefInfo inaccessibleMem) : other(other), argMem(argMem), inaccessibleMem(inaccessibleMem) {}

  KeyTy getAsKey() const {
    return KeyTy(other, argMem, inaccessibleMem);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (other == std::get<0>(tblgenKey)) && (argMem == std::get<1>(tblgenKey)) && (inaccessibleMem == std::get<2>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey));
  }

  static MemoryEffectsAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto other = std::get<0>(tblgenKey);
    auto argMem = std::get<1>(tblgenKey);
    auto inaccessibleMem = std::get<2>(tblgenKey);
    return new (allocator.allocate<MemoryEffectsAttrStorage>()) MemoryEffectsAttrStorage(other, argMem, inaccessibleMem);
  }

  ModRefInfo other;
  ModRefInfo argMem;
  ModRefInfo inaccessibleMem;
};
} // namespace detail
MemoryEffectsAttr MemoryEffectsAttr::get(::mlir::MLIRContext *context, ModRefInfo other, ModRefInfo argMem, ModRefInfo inaccessibleMem) {
  return Base::get(context, other, argMem, inaccessibleMem);
}

::mlir::Attribute MemoryEffectsAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<ModRefInfo> _result_other;
  ::mlir::FailureOr<ModRefInfo> _result_argMem;
  ::mlir::FailureOr<ModRefInfo> _result_inaccessibleMem;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};
  // Parse parameter struct
  bool _seen_other = false;
  bool _seen_argMem = false;
  bool _seen_inaccessibleMem = false;
  {
    const auto _loop_body = [&](::llvm::StringRef _paramKey) -> bool {
      // Parse literal '='
      if (odsParser.parseEqual()) return {};
      if (!_seen_other && _paramKey == "other") {
        _seen_other = true;

        // Parse variable 'other'
        _result_other = ::mlir::FieldParser<ModRefInfo>::parse(odsParser);
        if (::mlir::failed(_result_other)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_MemoryEffectsAttr parameter 'other' which is to be a `ModRefInfo`");
          return {};
        }
      } else if (!_seen_argMem && _paramKey == "argMem") {
        _seen_argMem = true;

        // Parse variable 'argMem'
        _result_argMem = ::mlir::FieldParser<ModRefInfo>::parse(odsParser);
        if (::mlir::failed(_result_argMem)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_MemoryEffectsAttr parameter 'argMem' which is to be a `ModRefInfo`");
          return {};
        }
      } else if (!_seen_inaccessibleMem && _paramKey == "inaccessibleMem") {
        _seen_inaccessibleMem = true;

        // Parse variable 'inaccessibleMem'
        _result_inaccessibleMem = ::mlir::FieldParser<ModRefInfo>::parse(odsParser);
        if (::mlir::failed(_result_inaccessibleMem)) {
          odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LLVM_MemoryEffectsAttr parameter 'inaccessibleMem' which is to be a `ModRefInfo`");
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
  assert(::mlir::succeeded(_result_other));
  assert(::mlir::succeeded(_result_argMem));
  assert(::mlir::succeeded(_result_inaccessibleMem));
  return MemoryEffectsAttr::get(odsParser.getContext(),
      ModRefInfo((*_result_other)),
      ModRefInfo((*_result_argMem)),
      ModRefInfo((*_result_inaccessibleMem)));
}

void MemoryEffectsAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  {
    bool _firstPrinted = true;
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "other = ";
    odsPrinter.printStrippedAttrOrType(getOther());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "argMem = ";
    odsPrinter.printStrippedAttrOrType(getArgMem());
    if (!_firstPrinted) odsPrinter << ", ";
    _firstPrinted = false;
    odsPrinter << "inaccessibleMem = ";
    odsPrinter.printStrippedAttrOrType(getInaccessibleMem());
  }
  odsPrinter << ">";
}

ModRefInfo MemoryEffectsAttr::getOther() const {
  return getImpl()->other;
}

ModRefInfo MemoryEffectsAttr::getArgMem() const {
  return getImpl()->argMem;
}

ModRefInfo MemoryEffectsAttr::getInaccessibleMem() const {
  return getImpl()->inaccessibleMem;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::MemoryEffectsAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct LinkageAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<linkage::Linkage>;
  LinkageAttrStorage(linkage::Linkage linkage) : linkage(linkage) {}

  KeyTy getAsKey() const {
    return KeyTy(linkage);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (linkage == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static LinkageAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto linkage = std::get<0>(tblgenKey);
    return new (allocator.allocate<LinkageAttrStorage>()) LinkageAttrStorage(linkage);
  }

  linkage::Linkage linkage;
};
} // namespace detail
LinkageAttr LinkageAttr::get(::mlir::MLIRContext *context, linkage::Linkage linkage) {
  return Base::get(context, linkage);
}

::mlir::Attribute LinkageAttr::parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType) {
  ::mlir::Builder odsBuilder(odsParser.getContext());
  ::llvm::SMLoc odsLoc = odsParser.getCurrentLocation();
  (void) odsLoc;
  ::mlir::FailureOr<linkage::Linkage> _result_linkage;
  // Parse literal '<'
  if (odsParser.parseLess()) return {};

  // Parse variable 'linkage'
  _result_linkage = ::mlir::FieldParser<linkage::Linkage>::parse(odsParser);
  if (::mlir::failed(_result_linkage)) {
    odsParser.emitError(odsParser.getCurrentLocation(), "failed to parse LinkageAttr parameter 'linkage' which is to be a `linkage::Linkage`");
    return {};
  }
  // Parse literal '>'
  if (odsParser.parseGreater()) return {};
  assert(::mlir::succeeded(_result_linkage));
  return LinkageAttr::get(odsParser.getContext(),
      linkage::Linkage((*_result_linkage)));
}

void LinkageAttr::print(::mlir::AsmPrinter &odsPrinter) const {
  ::mlir::Builder odsBuilder(getContext());
  odsPrinter << "<";
  odsPrinter.printStrippedAttrOrType(getLinkage());
  odsPrinter << ">";
}

linkage::Linkage LinkageAttr::getLinkage() const {
  return getImpl()->linkage;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::LinkageAttr)
namespace mlir {
namespace LLVM {
namespace detail {
struct LoopOptionsAttrStorage : public ::mlir::AttributeStorage {
  using KeyTy = std::tuple<::llvm::ArrayRef<std::pair<LoopOptionCase, int64_t>>>;
  LoopOptionsAttrStorage(::llvm::ArrayRef<std::pair<LoopOptionCase, int64_t>> options) : options(options) {}

  KeyTy getAsKey() const {
    return KeyTy(options);
  }

  bool operator==(const KeyTy &tblgenKey) const {
    return (options == std::get<0>(tblgenKey));
  }

  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
    return ::llvm::hash_combine(std::get<0>(tblgenKey));
  }

  static LoopOptionsAttrStorage *construct(::mlir::AttributeStorageAllocator &allocator, const KeyTy &tblgenKey) {
    auto options = std::get<0>(tblgenKey);
    options = allocator.copyInto(options);
    return new (allocator.allocate<LoopOptionsAttrStorage>()) LoopOptionsAttrStorage(options);
  }

  ::llvm::ArrayRef<std::pair<LoopOptionCase, int64_t>> options;
};
} // namespace detail
::llvm::ArrayRef<std::pair<LoopOptionCase, int64_t>> LoopOptionsAttr::getOptions() const {
  return getImpl()->options;
}

} // namespace LLVM
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::LLVM::LoopOptionsAttr)
namespace mlir {
namespace LLVM {

/// Parse an attribute registered to this dialect.
::mlir::Attribute LLVMDialect::parseAttribute(::mlir::DialectAsmParser &parser,
                                      ::mlir::Type type) const {
  ::llvm::SMLoc typeLoc = parser.getCurrentLocation();
  ::llvm::StringRef attrTag;
  {
    ::mlir::Attribute attr;
    auto parseResult = generatedAttributeParser(parser, &attrTag, type, attr);
    if (parseResult.has_value())
      return attr;
  }
  
  parser.emitError(typeLoc) << "unknown attribute `"
      << attrTag << "` in dialect `" << getNamespace() << "`";
  return {};
}
/// Print an attribute registered to this dialect.
void LLVMDialect::printAttribute(::mlir::Attribute attr,
                         ::mlir::DialectAsmPrinter &printer) const {
  if (::mlir::succeeded(generatedAttributePrinter(attr, printer)))
    return;
  
}
} // namespace LLVM
} // namespace mlir

#endif  // GET_ATTRDEF_CLASSES

