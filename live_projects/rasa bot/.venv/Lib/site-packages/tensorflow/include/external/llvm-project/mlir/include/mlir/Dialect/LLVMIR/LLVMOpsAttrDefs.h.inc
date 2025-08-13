/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* AttrDef Declarations                                                       *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_ATTRDEF_CLASSES
#undef GET_ATTRDEF_CLASSES


namespace mlir {
class AsmParser;
class AsmPrinter;
} // namespace mlir
namespace mlir {
namespace LLVM {
class CConvAttr;
class DIBasicTypeAttr;
class DICompileUnitAttr;
class DICompositeTypeAttr;
class DIDerivedTypeAttr;
class DIFileAttr;
class DILexicalBlockAttr;
class DILexicalBlockFileAttr;
class DILocalVariableAttr;
class DISubprogramAttr;
class DISubrangeAttr;
class DISubroutineTypeAttr;
class DIVoidResultTypeAttr;
class FastmathFlagsAttr;
class MemoryEffectsAttr;
class LinkageAttr;
class LoopOptionsAttr;
namespace detail {
struct CConvAttrStorage;
} // namespace detail
class CConvAttr : public ::mlir::Attribute::AttrBase<CConvAttr, ::mlir::Attribute, detail::CConvAttrStorage> {
public:
  using Base::Base;
  static CConvAttr get(::mlir::MLIRContext *context, CConv CallingConv);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"cconv"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  CConv getCallingConv() const;
};
namespace detail {
struct DIBasicTypeAttrStorage;
} // namespace detail
class DIBasicTypeAttr : public ::mlir::Attribute::AttrBase<DIBasicTypeAttr, DITypeAttr, detail::DIBasicTypeAttrStorage> {
public:
  using Base::Base;
  static DIBasicTypeAttr get(::mlir::MLIRContext *context, unsigned tag, StringAttr name, uint64_t sizeInBits, unsigned encoding);
  static DIBasicTypeAttr get(::mlir::MLIRContext *context, unsigned tag, const Twine &name, uint64_t sizeInBits, unsigned encoding);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_basic_type"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  unsigned getTag() const;
  StringAttr getName() const;
  uint64_t getSizeInBits() const;
  unsigned getEncoding() const;
};
namespace detail {
struct DICompileUnitAttrStorage;
} // namespace detail
class DICompileUnitAttr : public ::mlir::Attribute::AttrBase<DICompileUnitAttr, DIScopeAttr, detail::DICompileUnitAttrStorage> {
public:
  using Base::Base;
  static DICompileUnitAttr get(::mlir::MLIRContext *context, unsigned sourceLanguage, DIFileAttr file, StringAttr producer, bool isOptimized, DIEmissionKind emissionKind);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_compile_unit"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  unsigned getSourceLanguage() const;
  DIFileAttr getFile() const;
  StringAttr getProducer() const;
  bool getIsOptimized() const;
  DIEmissionKind getEmissionKind() const;
};
namespace detail {
struct DICompositeTypeAttrStorage;
} // namespace detail
class DICompositeTypeAttr : public ::mlir::Attribute::AttrBase<DICompositeTypeAttr, DITypeAttr, detail::DICompositeTypeAttrStorage> {
public:
  using Base::Base;
  static DICompositeTypeAttr get(::mlir::MLIRContext *context, unsigned tag, StringAttr name, DIFileAttr file, uint32_t line, DIScopeAttr scope, DITypeAttr baseType, DIFlags flags, uint64_t sizeInBits, uint64_t alignInBits, ::llvm::ArrayRef<DINodeAttr> elements);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_composite_type"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  unsigned getTag() const;
  StringAttr getName() const;
  DIFileAttr getFile() const;
  uint32_t getLine() const;
  DIScopeAttr getScope() const;
  DITypeAttr getBaseType() const;
  DIFlags getFlags() const;
  uint64_t getSizeInBits() const;
  uint64_t getAlignInBits() const;
  ::llvm::ArrayRef<DINodeAttr> getElements() const;
};
namespace detail {
struct DIDerivedTypeAttrStorage;
} // namespace detail
class DIDerivedTypeAttr : public ::mlir::Attribute::AttrBase<DIDerivedTypeAttr, DITypeAttr, detail::DIDerivedTypeAttrStorage> {
public:
  using Base::Base;
  static DIDerivedTypeAttr get(::mlir::MLIRContext *context, unsigned tag, StringAttr name, DITypeAttr baseType, uint64_t sizeInBits, uint32_t alignInBits, uint64_t offsetInBits);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_derived_type"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  unsigned getTag() const;
  StringAttr getName() const;
  DITypeAttr getBaseType() const;
  uint64_t getSizeInBits() const;
  uint32_t getAlignInBits() const;
  uint64_t getOffsetInBits() const;
};
namespace detail {
struct DIFileAttrStorage;
} // namespace detail
class DIFileAttr : public ::mlir::Attribute::AttrBase<DIFileAttr, DIScopeAttr, detail::DIFileAttrStorage> {
public:
  using Base::Base;
  static DIFileAttr get(::mlir::MLIRContext *context, StringAttr name, StringAttr directory);
  static DIFileAttr get(::mlir::MLIRContext *context, StringRef name, StringRef directory);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_file"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  StringAttr getName() const;
  StringAttr getDirectory() const;
};
namespace detail {
struct DILexicalBlockAttrStorage;
} // namespace detail
class DILexicalBlockAttr : public ::mlir::Attribute::AttrBase<DILexicalBlockAttr, DIScopeAttr, detail::DILexicalBlockAttrStorage> {
public:
  using Base::Base;
  static DILexicalBlockAttr get(::mlir::MLIRContext *context, DIScopeAttr scope, DIFileAttr file, unsigned line, unsigned column);
  static DILexicalBlockAttr get(DIScopeAttr scope, DIFileAttr file, unsigned line, unsigned column);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_lexical_block"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  DIScopeAttr getScope() const;
  DIFileAttr getFile() const;
  unsigned getLine() const;
  unsigned getColumn() const;
};
namespace detail {
struct DILexicalBlockFileAttrStorage;
} // namespace detail
class DILexicalBlockFileAttr : public ::mlir::Attribute::AttrBase<DILexicalBlockFileAttr, DIScopeAttr, detail::DILexicalBlockFileAttrStorage> {
public:
  using Base::Base;
  static DILexicalBlockFileAttr get(::mlir::MLIRContext *context, DIScopeAttr scope, DIFileAttr file, unsigned discriminator);
  static DILexicalBlockFileAttr get(DIScopeAttr scope, DIFileAttr file, unsigned discriminator);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_lexical_block_file"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  DIScopeAttr getScope() const;
  DIFileAttr getFile() const;
  unsigned getDiscriminator() const;
};
namespace detail {
struct DILocalVariableAttrStorage;
} // namespace detail
class DILocalVariableAttr : public ::mlir::Attribute::AttrBase<DILocalVariableAttr, DINodeAttr, detail::DILocalVariableAttrStorage> {
public:
  using Base::Base;
  static DILocalVariableAttr get(::mlir::MLIRContext *context, DIScopeAttr scope, StringAttr name, DIFileAttr file, unsigned line, unsigned arg, unsigned alignInBits, DITypeAttr type);
  static DILocalVariableAttr get(DIScopeAttr scope, StringRef name, DIFileAttr file, unsigned line, unsigned arg, unsigned alignInBits, DITypeAttr type);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_local_variable"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  DIScopeAttr getScope() const;
  StringAttr getName() const;
  DIFileAttr getFile() const;
  unsigned getLine() const;
  unsigned getArg() const;
  unsigned getAlignInBits() const;
  DITypeAttr getType() const;
};
namespace detail {
struct DISubprogramAttrStorage;
} // namespace detail
class DISubprogramAttr : public ::mlir::Attribute::AttrBase<DISubprogramAttr, DIScopeAttr, detail::DISubprogramAttrStorage> {
public:
  using Base::Base;
  static DISubprogramAttr get(::mlir::MLIRContext *context, DICompileUnitAttr compileUnit, DIScopeAttr scope, StringAttr name, StringAttr linkageName, DIFileAttr file, unsigned line, unsigned scopeLine, DISubprogramFlags subprogramFlags, DISubroutineTypeAttr type);
  static DISubprogramAttr get(DICompileUnitAttr compileUnit, DIScopeAttr scope, StringRef name, StringRef linkageName, DIFileAttr file, unsigned line, unsigned scopeLine, DISubprogramFlags subprogramFlags, DISubroutineTypeAttr type);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_subprogram"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  DICompileUnitAttr getCompileUnit() const;
  DIScopeAttr getScope() const;
  StringAttr getName() const;
  StringAttr getLinkageName() const;
  DIFileAttr getFile() const;
  unsigned getLine() const;
  unsigned getScopeLine() const;
  DISubprogramFlags getSubprogramFlags() const;
  DISubroutineTypeAttr getType() const;
};
namespace detail {
struct DISubrangeAttrStorage;
} // namespace detail
class DISubrangeAttr : public ::mlir::Attribute::AttrBase<DISubrangeAttr, DINodeAttr, detail::DISubrangeAttrStorage> {
public:
  using Base::Base;
  static DISubrangeAttr get(::mlir::MLIRContext *context, IntegerAttr count, IntegerAttr lowerBound, IntegerAttr upperBound, IntegerAttr stride);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_subrange"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  IntegerAttr getCount() const;
  IntegerAttr getLowerBound() const;
  IntegerAttr getUpperBound() const;
  IntegerAttr getStride() const;
};
namespace detail {
struct DISubroutineTypeAttrStorage;
} // namespace detail
class DISubroutineTypeAttr : public ::mlir::Attribute::AttrBase<DISubroutineTypeAttr, DITypeAttr, detail::DISubroutineTypeAttrStorage> {
public:
  using Base::Base;
  using Base::getChecked;
  static DISubroutineTypeAttr get(::mlir::MLIRContext *context, unsigned callingConvention, ::llvm::ArrayRef<DITypeAttr> types);
  static DISubroutineTypeAttr getChecked(::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError, ::mlir::MLIRContext *context, unsigned callingConvention, ::llvm::ArrayRef<DITypeAttr> types);
  static DISubroutineTypeAttr get(::mlir::MLIRContext *context, ArrayRef<DITypeAttr> types);
  static DISubroutineTypeAttr getChecked(::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError, ::mlir::MLIRContext *context, ArrayRef<DITypeAttr> types);
  static ::mlir::LogicalResult verify(::llvm::function_ref<::mlir::InFlightDiagnostic()> emitError, unsigned callingConvention, ::llvm::ArrayRef<DITypeAttr> types);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_subroutine_type"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  unsigned getCallingConvention() const;
  ::llvm::ArrayRef<DITypeAttr> getTypes() const;
};
class DIVoidResultTypeAttr : public ::mlir::Attribute::AttrBase<DIVoidResultTypeAttr, DITypeAttr, ::mlir::AttributeStorage> {
public:
  using Base::Base;
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"di_void_result_type"};
  }

};
namespace detail {
struct FastmathFlagsAttrStorage;
} // namespace detail
class FastmathFlagsAttr : public ::mlir::Attribute::AttrBase<FastmathFlagsAttr, ::mlir::Attribute, detail::FastmathFlagsAttrStorage> {
public:
  using Base::Base;
  static FastmathFlagsAttr get(::mlir::MLIRContext *context, ::mlir::LLVM::FastmathFlags value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"fastmath"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::LLVM::FastmathFlags getValue() const;
};
namespace detail {
struct MemoryEffectsAttrStorage;
} // namespace detail
class MemoryEffectsAttr : public ::mlir::Attribute::AttrBase<MemoryEffectsAttr, ::mlir::Attribute, detail::MemoryEffectsAttrStorage> {
public:
  using Base::Base;
  bool isReadWrite();
  static MemoryEffectsAttr get(::mlir::MLIRContext *context, ModRefInfo other, ModRefInfo argMem, ModRefInfo inaccessibleMem);
  static MemoryEffectsAttr get(::mlir::MLIRContext *context, ArrayRef<ModRefInfo> memInfoArgs);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"memory_effects"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ModRefInfo getOther() const;
  ModRefInfo getArgMem() const;
  ModRefInfo getInaccessibleMem() const;
};
namespace detail {
struct LinkageAttrStorage;
} // namespace detail
class LinkageAttr : public ::mlir::Attribute::AttrBase<LinkageAttr, ::mlir::Attribute, detail::LinkageAttrStorage> {
public:
  using Base::Base;
  static LinkageAttr get(::mlir::MLIRContext *context, linkage::Linkage linkage);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"linkage"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  linkage::Linkage getLinkage() const;
};
namespace detail {
struct LoopOptionsAttrStorage;
} // namespace detail
class LoopOptionsAttr : public ::mlir::Attribute::AttrBase<LoopOptionsAttr, ::mlir::Attribute, detail::LoopOptionsAttrStorage> {
public:
  using Base::Base;
  using OptionValuePair = std::pair<LoopOptionCase, int64_t>;
  using OptionsArray = ArrayRef<std::pair<LoopOptionCase, int64_t>>;
  std::optional<bool> disableUnroll();
  std::optional<bool> disableLICM();
  std::optional<int64_t> interleaveCount();
  static LoopOptionsAttr get(::mlir::MLIRContext *context, ArrayRef<std::pair<LoopOptionCase, int64_t>> sortedOptions);
  static LoopOptionsAttr get(::mlir::MLIRContext *context, LoopOptionsAttrBuilder &optionBuilders);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"loopopts"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<std::pair<LoopOptionCase, int64_t>> getOptions() const;
};
} // namespace LLVM
} // namespace mlir
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::CConvAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIBasicTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DICompileUnitAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DICompositeTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIDerivedTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIFileAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DILexicalBlockAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DILexicalBlockFileAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DILocalVariableAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DISubprogramAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DISubrangeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DISubroutineTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::DIVoidResultTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::FastmathFlagsAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::MemoryEffectsAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::LinkageAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::LLVM::LoopOptionsAttr)

#endif  // GET_ATTRDEF_CLASSES

