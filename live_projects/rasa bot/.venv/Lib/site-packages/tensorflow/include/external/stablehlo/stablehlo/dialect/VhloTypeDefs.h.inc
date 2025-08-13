/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* TypeDef Declarations                                                       *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_TYPEDEF_CLASSES
#undef GET_TYPEDEF_CLASSES


namespace mlir {
class AsmParser;
class AsmPrinter;
} // namespace mlir
namespace mlir {
namespace vhlo {
class TokenType;
class TokenType : public ::mlir::Type::TypeBase<TokenType, ::mlir::Type, ::mlir::TypeStorage, ::mlir::vhlo::VersionedTypeInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in Token");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in Token");
    return *version;
  }
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"token"};
  }

};
} // namespace vhlo
} // namespace mlir
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::TokenType)

#endif  // GET_TYPEDEF_CLASSES

