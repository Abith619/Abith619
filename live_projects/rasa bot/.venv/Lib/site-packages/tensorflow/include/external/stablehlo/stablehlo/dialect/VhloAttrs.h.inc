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
namespace vhlo {
class ArgResultAliasAttr;
class ChannelHandleAttr;
class ComparisonDirectionAttr;
class ComparisonTypeAttr;
class ConvDimensionNumbersAttr;
class DotDimensionNumbersAttr;
class FftTypeAttr;
class GatherDimensionNumbersAttr;
class OutputOperandAliasAttr;
class PrecisionAttr;
class RngAlgorithmAttr;
class RngDistributionAttr;
class ScatterDimensionNumbersAttr;
class TransposeAttr;
class TypeExtensionsAttr;
namespace detail {
struct ArgResultAliasAttrStorage;
} // namespace detail
class ArgResultAliasAttr : public ::mlir::Attribute::AttrBase<ArgResultAliasAttr, ::mlir::Attribute, detail::ArgResultAliasAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in ArgResultAlias");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in ArgResultAlias");
    return *version;
  }
  static ArgResultAliasAttr get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> argTupleIndices, int64_t resultIndex, ::llvm::ArrayRef<int64_t> resultTupleIndices, bool isMustAlias);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"result_alias"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<int64_t> getArgTupleIndices() const;
  int64_t getResultIndex() const;
  ::llvm::ArrayRef<int64_t> getResultTupleIndices() const;
  bool getIsMustAlias() const;
};
namespace detail {
struct ChannelHandleAttrStorage;
} // namespace detail
class ChannelHandleAttr : public ::mlir::Attribute::AttrBase<ChannelHandleAttr, ::mlir::Attribute, detail::ChannelHandleAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in ChannelHandle");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in ChannelHandle");
    return *version;
  }
  static ChannelHandleAttr get(::mlir::MLIRContext *context, int64_t handle, int64_t type);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"channel_handle"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  int64_t getHandle() const;
  int64_t getType() const;
};
namespace detail {
struct ComparisonDirectionAttrStorage;
} // namespace detail
class ComparisonDirectionAttr : public ::mlir::Attribute::AttrBase<ComparisonDirectionAttr, ::mlir::Attribute, detail::ComparisonDirectionAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static ComparisonDirectionAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::ComparisonDirection value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"comparison_direction"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::ComparisonDirection getValue() const;
};
namespace detail {
struct ComparisonTypeAttrStorage;
} // namespace detail
class ComparisonTypeAttr : public ::mlir::Attribute::AttrBase<ComparisonTypeAttr, ::mlir::Attribute, detail::ComparisonTypeAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static ComparisonTypeAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::ComparisonType value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"comparison_type"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::ComparisonType getValue() const;
};
namespace detail {
struct ConvDimensionNumbersAttrStorage;
} // namespace detail
class ConvDimensionNumbersAttr : public ::mlir::Attribute::AttrBase<ConvDimensionNumbersAttr, ::mlir::Attribute, detail::ConvDimensionNumbersAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in ConvDimensionNumbers");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in ConvDimensionNumbers");
    return *version;
  }
  static ConvDimensionNumbersAttr get(::mlir::MLIRContext *context, int64_t inputBatchDimension, int64_t inputFeatureDimension, ::llvm::ArrayRef<int64_t> inputSpatialDimensions, int64_t kernelInputFeatureDimension, int64_t kernelOutputFeatureDimension, ::llvm::ArrayRef<int64_t> kernelSpatialDimensions, int64_t outputBatchDimension, int64_t outputFeatureDimension, ::llvm::ArrayRef<int64_t> outputSpatialDimensions);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"conv"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  int64_t getInputBatchDimension() const;
  int64_t getInputFeatureDimension() const;
  ::llvm::ArrayRef<int64_t> getInputSpatialDimensions() const;
  int64_t getKernelInputFeatureDimension() const;
  int64_t getKernelOutputFeatureDimension() const;
  ::llvm::ArrayRef<int64_t> getKernelSpatialDimensions() const;
  int64_t getOutputBatchDimension() const;
  int64_t getOutputFeatureDimension() const;
  ::llvm::ArrayRef<int64_t> getOutputSpatialDimensions() const;
};
namespace detail {
struct DotDimensionNumbersAttrStorage;
} // namespace detail
class DotDimensionNumbersAttr : public ::mlir::Attribute::AttrBase<DotDimensionNumbersAttr, ::mlir::Attribute, detail::DotDimensionNumbersAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in DotDimensionNumbers");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in DotDimensionNumbers");
    return *version;
  }
  static DotDimensionNumbersAttr get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> lhsBatchingDimensions, ::llvm::ArrayRef<int64_t> rhsBatchingDimensions, ::llvm::ArrayRef<int64_t> lhsContractingDimensions, ::llvm::ArrayRef<int64_t> rhsContractingDimensions);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"dot"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<int64_t> getLhsBatchingDimensions() const;
  ::llvm::ArrayRef<int64_t> getRhsBatchingDimensions() const;
  ::llvm::ArrayRef<int64_t> getLhsContractingDimensions() const;
  ::llvm::ArrayRef<int64_t> getRhsContractingDimensions() const;
};
namespace detail {
struct FftTypeAttrStorage;
} // namespace detail
class FftTypeAttr : public ::mlir::Attribute::AttrBase<FftTypeAttr, ::mlir::Attribute, detail::FftTypeAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static FftTypeAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::FftType value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"fft_type"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::FftType getValue() const;
};
namespace detail {
struct GatherDimensionNumbersAttrStorage;
} // namespace detail
class GatherDimensionNumbersAttr : public ::mlir::Attribute::AttrBase<GatherDimensionNumbersAttr, ::mlir::Attribute, detail::GatherDimensionNumbersAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in GatherDimensionNumbers");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in GatherDimensionNumbers");
    return *version;
  }
  static GatherDimensionNumbersAttr get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> offsetDims, ::llvm::ArrayRef<int64_t> collapsedSliceDims, ::llvm::ArrayRef<int64_t> startIndexMap, int64_t indexVectorDim);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"gather"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<int64_t> getOffsetDims() const;
  ::llvm::ArrayRef<int64_t> getCollapsedSliceDims() const;
  ::llvm::ArrayRef<int64_t> getStartIndexMap() const;
  int64_t getIndexVectorDim() const;
};
namespace detail {
struct OutputOperandAliasAttrStorage;
} // namespace detail
class OutputOperandAliasAttr : public ::mlir::Attribute::AttrBase<OutputOperandAliasAttr, ::mlir::Attribute, detail::OutputOperandAliasAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.4.0");
    if (failed(version)) llvm_unreachable("invalid version 0.4.0 in OutputOperandAlias");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in OutputOperandAlias");
    return *version;
  }
  static OutputOperandAliasAttr get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> outputTupleIndices, int64_t operandIndex, ::llvm::ArrayRef<int64_t> operandTupleIndices);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"output_operand_alias"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<int64_t> getOutputTupleIndices() const;
  int64_t getOperandIndex() const;
  ::llvm::ArrayRef<int64_t> getOperandTupleIndices() const;
};
namespace detail {
struct PrecisionAttrStorage;
} // namespace detail
class PrecisionAttr : public ::mlir::Attribute::AttrBase<PrecisionAttr, ::mlir::Attribute, detail::PrecisionAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static PrecisionAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::Precision value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"precision"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::Precision getValue() const;
};
namespace detail {
struct RngAlgorithmAttrStorage;
} // namespace detail
class RngAlgorithmAttr : public ::mlir::Attribute::AttrBase<RngAlgorithmAttr, ::mlir::Attribute, detail::RngAlgorithmAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static RngAlgorithmAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::RngAlgorithm value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"rng_algorithm"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::RngAlgorithm getValue() const;
};
namespace detail {
struct RngDistributionAttrStorage;
} // namespace detail
class RngDistributionAttr : public ::mlir::Attribute::AttrBase<RngDistributionAttr, ::mlir::Attribute, detail::RngDistributionAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static RngDistributionAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::RngDistribution value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"rng_distribution"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::RngDistribution getValue() const;
};
namespace detail {
struct ScatterDimensionNumbersAttrStorage;
} // namespace detail
class ScatterDimensionNumbersAttr : public ::mlir::Attribute::AttrBase<ScatterDimensionNumbersAttr, ::mlir::Attribute, detail::ScatterDimensionNumbersAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in ScatterDimensionNumbers");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in ScatterDimensionNumbers");
    return *version;
  }
  static ScatterDimensionNumbersAttr get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> updateWindowDims, ::llvm::ArrayRef<int64_t> insertedWindowDims, ::llvm::ArrayRef<int64_t> scatterDimsToOperandDims, int64_t indexVectorDim);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"scatter"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<int64_t> getUpdateWindowDims() const;
  ::llvm::ArrayRef<int64_t> getInsertedWindowDims() const;
  ::llvm::ArrayRef<int64_t> getScatterDimsToOperandDims() const;
  int64_t getIndexVectorDim() const;
};
namespace detail {
struct TransposeAttrStorage;
} // namespace detail
class TransposeAttr : public ::mlir::Attribute::AttrBase<TransposeAttr, ::mlir::Attribute, detail::TransposeAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    return *mlir::vhlo::Version::fromString("0.3.0");
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    return *mlir::vhlo::Version::fromString("current");
  }
  static TransposeAttr get(::mlir::MLIRContext *context, ::mlir::vhlo::Transpose value);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"transpose"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::mlir::vhlo::Transpose getValue() const;
};
namespace detail {
struct TypeExtensionsAttrStorage;
} // namespace detail
class TypeExtensionsAttr : public ::mlir::Attribute::AttrBase<TypeExtensionsAttr, ::mlir::Attribute, detail::TypeExtensionsAttrStorage, ::mlir::vhlo::VersionedAttrInterface::Trait> {
public:
  using Base::Base;
  mlir::vhlo::Version getMinVersion() {
    auto version = mlir::vhlo::Version::fromString("0.3.0");
    if (failed(version)) llvm_unreachable("invalid version 0.3.0 in TypeExtensions");
    return *version;
  }
  mlir::vhlo::Version getMaxVersion() {
    if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
    auto version = mlir::vhlo::Version::fromString("current");
    if (failed(version)) llvm_unreachable("invalid version current in TypeExtensions");
    return *version;
  }
  static TypeExtensionsAttr get(::mlir::MLIRContext *context, ::llvm::ArrayRef<int64_t> bounds);
  static constexpr ::llvm::StringLiteral getMnemonic() {
    return {"type_extensions"};
  }

  static ::mlir::Attribute parse(::mlir::AsmParser &odsParser, ::mlir::Type odsType);
  void print(::mlir::AsmPrinter &odsPrinter) const;
  ::llvm::ArrayRef<int64_t> getBounds() const;
};
} // namespace vhlo
} // namespace mlir
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::ArgResultAliasAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::ChannelHandleAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::ComparisonDirectionAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::ComparisonTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::ConvDimensionNumbersAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::DotDimensionNumbersAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::FftTypeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::GatherDimensionNumbersAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::OutputOperandAliasAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::PrecisionAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::RngAlgorithmAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::RngDistributionAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::ScatterDimensionNumbersAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::TransposeAttr)
MLIR_DECLARE_EXPLICIT_TYPE_ID(::mlir::vhlo::TypeExtensionsAttr)

#endif  // GET_ATTRDEF_CLASSES

