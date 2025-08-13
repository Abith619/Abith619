/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Op Definitions                                                             *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_OP_LIST
#undef GET_OP_LIST

::mlir::vhlo::AbsOpV1,
::mlir::vhlo::AddOpV1,
::mlir::vhlo::AfterAllOpV1,
::mlir::vhlo::AllGatherOpV1,
::mlir::vhlo::AllGatherOpV2,
::mlir::vhlo::AllReduceOpV1,
::mlir::vhlo::AllToAllOpV1,
::mlir::vhlo::AllToAllOpV2,
::mlir::vhlo::AndOpV1,
::mlir::vhlo::Atan2OpV1,
::mlir::vhlo::BatchNormGradOpV1,
::mlir::vhlo::BatchNormInferenceOpV1,
::mlir::vhlo::BatchNormTrainingOpV1,
::mlir::vhlo::BitcastConvertOpV1,
::mlir::vhlo::BroadcastInDimOpV1,
::mlir::vhlo::BroadcastOpV1,
::mlir::vhlo::CaseOpV1,
::mlir::vhlo::CbrtOpV1,
::mlir::vhlo::CeilOpV1,
::mlir::vhlo::CholeskyOpV1,
::mlir::vhlo::ClampOpV1,
::mlir::vhlo::ClzOpV1,
::mlir::vhlo::CollectivePermuteOpV1,
::mlir::vhlo::CollectivePermuteOpV2,
::mlir::vhlo::CompareOpV1,
::mlir::vhlo::ComplexOpV1,
::mlir::vhlo::ComputeReshapeShapeOpV1,
::mlir::vhlo::ConcatenateOpV1,
::mlir::vhlo::ConstantOpV1,
::mlir::vhlo::ConvertOpV1,
::mlir::vhlo::ConvolutionOpV1,
::mlir::vhlo::CosineOpV1,
::mlir::vhlo::CreateTokenOpV1,
::mlir::vhlo::CrossReplicaSumOpV1,
::mlir::vhlo::CstrReshapableOpV1,
::mlir::vhlo::CustomCallOpV1,
::mlir::vhlo::CustomCallOpV2,
::mlir::vhlo::DivOpV1,
::mlir::vhlo::DotGeneralOpV1,
::mlir::vhlo::DotOpV1,
::mlir::vhlo::DynamicBroadcastInDimOpV1,
::mlir::vhlo::DynamicConvOpV1,
::mlir::vhlo::DynamicGatherOpV1,
::mlir::vhlo::DynamicIotaOpV1,
::mlir::vhlo::DynamicPadOpV1,
::mlir::vhlo::DynamicReshapeOpV1,
::mlir::vhlo::DynamicSliceOpV1,
::mlir::vhlo::DynamicUpdateSliceOpV1,
::mlir::vhlo::EinsumOpV1,
::mlir::vhlo::ExpOpV1,
::mlir::vhlo::Expm1OpV1,
::mlir::vhlo::FftOpV1,
::mlir::vhlo::FloorOpV1,
::mlir::vhlo::GatherOpV1,
::mlir::vhlo::GetDimensionSizeOpV1,
::mlir::vhlo::GetTupleElementOpV1,
::mlir::vhlo::IfOpV1,
::mlir::vhlo::ImagOpV1,
::mlir::vhlo::InfeedOpV1,
::mlir::vhlo::IotaOpV1,
::mlir::vhlo::IsFiniteOpV1,
::mlir::vhlo::Log1pOpV1,
::mlir::vhlo::LogOpV1,
::mlir::vhlo::LogisticOpV1,
::mlir::vhlo::MapOpV1,
::mlir::vhlo::MaxOpV1,
::mlir::vhlo::MinOpV1,
::mlir::vhlo::MulOpV1,
::mlir::vhlo::NegOpV1,
::mlir::vhlo::NotOpV1,
::mlir::vhlo::OptimizationBarrierOpV1,
::mlir::vhlo::OrOpV1,
::mlir::vhlo::OutfeedOpV1,
::mlir::vhlo::PadOpV1,
::mlir::vhlo::PartitionIdOpV1,
::mlir::vhlo::PopulationCountOpV1,
::mlir::vhlo::PowOpV1,
::mlir::vhlo::RealDynamicSliceOpV1,
::mlir::vhlo::RealOpV1,
::mlir::vhlo::RecvOpV1,
::mlir::vhlo::ReduceOpV1,
::mlir::vhlo::ReducePrecisionOpV1,
::mlir::vhlo::ReduceScatterOpV1,
::mlir::vhlo::ReduceWindowOpV1,
::mlir::vhlo::RemOpV1,
::mlir::vhlo::ReplicaIdOpV1,
::mlir::vhlo::ReshapeOpV1,
::mlir::vhlo::ReturnOpV1,
::mlir::vhlo::ReverseOpV1,
::mlir::vhlo::RngBitGeneratorOpV1,
::mlir::vhlo::RngOpV1,
::mlir::vhlo::RoundNearestEvenOpV1,
::mlir::vhlo::RoundOpV1,
::mlir::vhlo::RsqrtOpV1,
::mlir::vhlo::ScatterOpV1,
::mlir::vhlo::SelectAndScatterOpV1,
::mlir::vhlo::SelectOpV1,
::mlir::vhlo::SendOpV1,
::mlir::vhlo::SetDimensionSizeOpV1,
::mlir::vhlo::ShiftLeftOpV1,
::mlir::vhlo::ShiftRightArithmeticOpV1,
::mlir::vhlo::ShiftRightLogicalOpV1,
::mlir::vhlo::SignOpV1,
::mlir::vhlo::SineOpV1,
::mlir::vhlo::SliceOpV1,
::mlir::vhlo::SortOpV1,
::mlir::vhlo::SqrtOpV1,
::mlir::vhlo::SubtractOpV1,
::mlir::vhlo::TanhOpV1,
::mlir::vhlo::TorchIndexSelectOpV1,
::mlir::vhlo::TraceOpV1,
::mlir::vhlo::TransposeOpV1,
::mlir::vhlo::TriangularSolveOpV1,
::mlir::vhlo::TupleOpV1,
::mlir::vhlo::UnaryEinsumOpV1,
::mlir::vhlo::UniformDequantizeOpV1,
::mlir::vhlo::UniformQuantizeOpV1,
::mlir::vhlo::WhileOpV1,
::mlir::vhlo::XorOpV1
#endif  // GET_OP_LIST

#ifdef GET_OP_CLASSES
#undef GET_OP_CLASSES


//===----------------------------------------------------------------------===//
// Local Utility Method Definitions
//===----------------------------------------------------------------------===//

namespace mlir {
namespace vhlo {

static ::mlir::LogicalResult __mlir_ods_local_type_constraint_VhloOps0(
    ::mlir::Operation *op, ::mlir::Type type, ::llvm::StringRef valueKind,
    unsigned valueIndex) {
  if (!((true))) {
    return op->emitOpError(valueKind) << " #" << valueIndex
        << " must be any type, but got " << type;
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_VhloOps0(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  if (attr && !((true))) {
    return op->emitOpError("attribute '") << attrName
        << "' failed to satisfy constraint: any attribute";
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_region_constraint_VhloOps0(
    ::mlir::Operation *op, ::mlir::Region &region, ::llvm::StringRef regionName,
    unsigned regionIndex) {
  if (!((true))) {
    return op->emitOpError("region #") << regionIndex
        << (regionName.empty() ? " " : " ('" + regionName + "') ")
        << "failed to verify constraint: any region";
  }
  return ::mlir::success();
}
} // namespace vhlo
} // namespace mlir
namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AbsOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AbsOpV1GenericAdaptorBase::AbsOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.abs", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AbsOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AbsOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
AbsOpV1Adaptor::AbsOpV1Adaptor(AbsOpV1 op) : AbsOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AbsOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AbsOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AbsOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AbsOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange AbsOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AbsOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AbsOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AbsOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void AbsOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void AbsOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AbsOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AbsOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AbsOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AbsOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in abs");
  return *version;
}
mlir::vhlo::Version AbsOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in abs");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AbsOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AddOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AddOpV1GenericAdaptorBase::AddOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.add", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AddOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AddOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
AddOpV1Adaptor::AddOpV1Adaptor(AddOpV1 op) : AddOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AddOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AddOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AddOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AddOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value AddOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange AddOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange AddOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AddOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AddOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AddOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void AddOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void AddOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AddOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AddOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AddOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AddOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in add");
  return *version;
}
mlir::vhlo::Version AddOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in add");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AddOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AfterAllOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AfterAllOpV1GenericAdaptorBase::AfterAllOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.after_all", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AfterAllOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr AfterAllOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
AfterAllOpV1Adaptor::AfterAllOpV1Adaptor(AfterAllOpV1 op) : AfterAllOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AfterAllOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AfterAllOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range AfterAllOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range AfterAllOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange AfterAllOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AfterAllOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AfterAllOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AfterAllOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void AfterAllOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::ValueRange inputs) {
  odsState.addOperands(inputs);
  odsState.addTypes(result);
}

void AfterAllOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AfterAllOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AfterAllOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AfterAllOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in after_all");
  return *version;
}
mlir::vhlo::Version AfterAllOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in after_all");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AfterAllOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AllGatherOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AllGatherOpV1GenericAdaptorBase::AllGatherOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.all_gather", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AllGatherOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AllGatherOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute AllGatherOpV1GenericAdaptorBase::getAllGatherDimAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, AllGatherOpV1::getAllGatherDimAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllGatherOpV1GenericAdaptorBase::getAllGatherDim() {
  auto attr = getAllGatherDimAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV1GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, AllGatherOpV1::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllGatherOpV1GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV1GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, AllGatherOpV1::getChannelHandleAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> AllGatherOpV1GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
AllGatherOpV1Adaptor::AllGatherOpV1Adaptor(AllGatherOpV1 op) : AllGatherOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AllGatherOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_all_gather_dim;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_gather' op ""requires attribute 'all_gather_dim'");
    if (namedAttrIt->getName() == AllGatherOpV1::getAllGatherDimAttrName(*odsOpName)) {
      tblgen_all_gather_dim = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_gather' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == AllGatherOpV1::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == AllGatherOpV1::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_all_gather_dim && !((true)))
    return emitError(loc, "'vhlo.all_gather' op ""attribute 'all_gather_dim' failed to satisfy constraint: any attribute");

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.all_gather' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.all_gather' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AllGatherOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AllGatherOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AllGatherOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange AllGatherOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AllGatherOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AllGatherOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute AllGatherOpV1::getAllGatherDimAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getAllGatherDimAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllGatherOpV1::getAllGatherDim() {
  auto attr = getAllGatherDimAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV1::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllGatherOpV1::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV1::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getChannelHandleAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> AllGatherOpV1::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void AllGatherOpV1::setAllGatherDimAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getAllGatherDimAttrName(), attr);
}

void AllGatherOpV1::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void AllGatherOpV1::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

::mlir::Attribute AllGatherOpV1::removeChannelHandleAttr() {
  return (*this)->removeAttr(getChannelHandleAttrName());
}

void AllGatherOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute all_gather_dim, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle) {
  odsState.addOperands(operand);
  odsState.addAttribute(getAllGatherDimAttrName(odsState.name), all_gather_dim);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  odsState.addTypes(resultType0);
}

void AllGatherOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute all_gather_dim, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle) {
  odsState.addOperands(operand);
  odsState.addAttribute(getAllGatherDimAttrName(odsState.name), all_gather_dim);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AllGatherOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AllGatherOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_all_gather_dim;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'all_gather_dim'");
    if (namedAttrIt->getName() == getAllGatherDimAttrName()) {
      tblgen_all_gather_dim = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_all_gather_dim, "all_gather_dim")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AllGatherOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AllGatherOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in all_gather");
  return *version;
}
mlir::vhlo::Version AllGatherOpV1::getMaxVersion() {
  if (!strcmp("0.3.0", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in all_gather");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AllGatherOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AllGatherOpV2 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AllGatherOpV2GenericAdaptorBase::AllGatherOpV2GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.all_gather_v2", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AllGatherOpV2GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AllGatherOpV2GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute AllGatherOpV2GenericAdaptorBase::getAllGatherDimAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, AllGatherOpV2::getAllGatherDimAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllGatherOpV2GenericAdaptorBase::getAllGatherDim() {
  auto attr = getAllGatherDimAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV2GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, AllGatherOpV2::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllGatherOpV2GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV2GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, AllGatherOpV2::getChannelHandleAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> AllGatherOpV2GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute AllGatherOpV2GenericAdaptorBase::getUseGlobalDeviceIdsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, AllGatherOpV2::getUseGlobalDeviceIdsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> AllGatherOpV2GenericAdaptorBase::getUseGlobalDeviceIds() {
  auto attr = getUseGlobalDeviceIdsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
AllGatherOpV2Adaptor::AllGatherOpV2Adaptor(AllGatherOpV2 op) : AllGatherOpV2Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AllGatherOpV2Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_all_gather_dim;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_gather_v2' op ""requires attribute 'all_gather_dim'");
    if (namedAttrIt->getName() == AllGatherOpV2::getAllGatherDimAttrName(*odsOpName)) {
      tblgen_all_gather_dim = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_gather_v2' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == AllGatherOpV2::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == AllGatherOpV2::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_use_global_device_ids;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == AllGatherOpV2::getUseGlobalDeviceIdsAttrName(*odsOpName)) {
      tblgen_use_global_device_ids = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_all_gather_dim && !((true)))
    return emitError(loc, "'vhlo.all_gather_v2' op ""attribute 'all_gather_dim' failed to satisfy constraint: any attribute");

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.all_gather_v2' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.all_gather_v2' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");

  if (tblgen_use_global_device_ids && !((true)))
    return emitError(loc, "'vhlo.all_gather_v2' op ""attribute 'use_global_device_ids' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AllGatherOpV2::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AllGatherOpV2::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AllGatherOpV2::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange AllGatherOpV2::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AllGatherOpV2::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AllGatherOpV2::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute AllGatherOpV2::getAllGatherDimAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getAllGatherDimAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllGatherOpV2::getAllGatherDim() {
  auto attr = getAllGatherDimAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV2::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllGatherOpV2::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllGatherOpV2::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getChannelHandleAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> AllGatherOpV2::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute AllGatherOpV2::getUseGlobalDeviceIdsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getUseGlobalDeviceIdsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> AllGatherOpV2::getUseGlobalDeviceIds() {
  auto attr = getUseGlobalDeviceIdsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void AllGatherOpV2::setAllGatherDimAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getAllGatherDimAttrName(), attr);
}

void AllGatherOpV2::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void AllGatherOpV2::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

void AllGatherOpV2::setUseGlobalDeviceIdsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getUseGlobalDeviceIdsAttrName(), attr);
}

::mlir::Attribute AllGatherOpV2::removeChannelHandleAttr() {
  return (*this)->removeAttr(getChannelHandleAttrName());
}

::mlir::Attribute AllGatherOpV2::removeUseGlobalDeviceIdsAttr() {
  return (*this)->removeAttr(getUseGlobalDeviceIdsAttrName());
}

void AllGatherOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute all_gather_dim, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute use_global_device_ids) {
  odsState.addOperands(operand);
  odsState.addAttribute(getAllGatherDimAttrName(odsState.name), all_gather_dim);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  if (use_global_device_ids) {
    odsState.addAttribute(getUseGlobalDeviceIdsAttrName(odsState.name), use_global_device_ids);
  }
  odsState.addTypes(resultType0);
}

void AllGatherOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute all_gather_dim, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute use_global_device_ids) {
  odsState.addOperands(operand);
  odsState.addAttribute(getAllGatherDimAttrName(odsState.name), all_gather_dim);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  if (use_global_device_ids) {
    odsState.addAttribute(getUseGlobalDeviceIdsAttrName(odsState.name), use_global_device_ids);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AllGatherOpV2::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AllGatherOpV2::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_all_gather_dim;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'all_gather_dim'");
    if (namedAttrIt->getName() == getAllGatherDimAttrName()) {
      tblgen_all_gather_dim = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_use_global_device_ids;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getUseGlobalDeviceIdsAttrName()) {
      tblgen_use_global_device_ids = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_all_gather_dim, "all_gather_dim")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_use_global_device_ids, "use_global_device_ids")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AllGatherOpV2::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AllGatherOpV2::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.4.0");
  if (failed(version)) llvm_unreachable("invalid version 0.4.0 in all_gather_v2");
  return *version;
}
mlir::vhlo::Version AllGatherOpV2::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in all_gather_v2");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AllGatherOpV2)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AllReduceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AllReduceOpV1GenericAdaptorBase::AllReduceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.all_reduce", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AllReduceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AllReduceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute AllReduceOpV1GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, AllReduceOpV1::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllReduceOpV1GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllReduceOpV1GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, AllReduceOpV1::getChannelHandleAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> AllReduceOpV1GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute AllReduceOpV1GenericAdaptorBase::getUseGlobalDeviceIdsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, AllReduceOpV1::getUseGlobalDeviceIdsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> AllReduceOpV1GenericAdaptorBase::getUseGlobalDeviceIds() {
  auto attr = getUseGlobalDeviceIdsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Region &AllReduceOpV1GenericAdaptorBase::getComputation() {
  return *odsRegions[0];
}

::mlir::RegionRange AllReduceOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
AllReduceOpV1Adaptor::AllReduceOpV1Adaptor(AllReduceOpV1 op) : AllReduceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AllReduceOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_reduce' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == AllReduceOpV1::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == AllReduceOpV1::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_use_global_device_ids;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == AllReduceOpV1::getUseGlobalDeviceIdsAttrName(*odsOpName)) {
      tblgen_use_global_device_ids = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.all_reduce' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.all_reduce' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");

  if (tblgen_use_global_device_ids && !((true)))
    return emitError(loc, "'vhlo.all_reduce' op ""attribute 'use_global_device_ids' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AllReduceOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AllReduceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AllReduceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange AllReduceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AllReduceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AllReduceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &AllReduceOpV1::getComputation() {
  return (*this)->getRegion(0);
}

::mlir::Attribute AllReduceOpV1::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllReduceOpV1::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllReduceOpV1::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getChannelHandleAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> AllReduceOpV1::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute AllReduceOpV1::getUseGlobalDeviceIdsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getUseGlobalDeviceIdsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> AllReduceOpV1::getUseGlobalDeviceIds() {
  auto attr = getUseGlobalDeviceIdsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void AllReduceOpV1::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void AllReduceOpV1::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

void AllReduceOpV1::setUseGlobalDeviceIdsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getUseGlobalDeviceIdsAttrName(), attr);
}

::mlir::Attribute AllReduceOpV1::removeChannelHandleAttr() {
  return (*this)->removeAttr(getChannelHandleAttrName());
}

::mlir::Attribute AllReduceOpV1::removeUseGlobalDeviceIdsAttr() {
  return (*this)->removeAttr(getUseGlobalDeviceIdsAttrName());
}

void AllReduceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute use_global_device_ids) {
  odsState.addOperands(operand);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  if (use_global_device_ids) {
    odsState.addAttribute(getUseGlobalDeviceIdsAttrName(odsState.name), use_global_device_ids);
  }
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void AllReduceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute use_global_device_ids) {
  odsState.addOperands(operand);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  if (use_global_device_ids) {
    odsState.addAttribute(getUseGlobalDeviceIdsAttrName(odsState.name), use_global_device_ids);
  }
  (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AllReduceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AllReduceOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_use_global_device_ids;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getUseGlobalDeviceIdsAttrName()) {
      tblgen_use_global_device_ids = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_use_global_device_ids, "use_global_device_ids")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "computation", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult AllReduceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AllReduceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in all_reduce");
  return *version;
}
mlir::vhlo::Version AllReduceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in all_reduce");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AllReduceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AllToAllOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AllToAllOpV1GenericAdaptorBase::AllToAllOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.all_to_all", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AllToAllOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AllToAllOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getSplitDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, AllToAllOpV1::getSplitDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getSplitDimension() {
  auto attr = getSplitDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getConcatDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 3, AllToAllOpV1::getConcatDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getConcatDimension() {
  auto attr = getConcatDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getSplitCountAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 1, AllToAllOpV1::getSplitCountAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getSplitCount() {
  auto attr = getSplitCountAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 2, AllToAllOpV1::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV1GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

} // namespace detail
AllToAllOpV1Adaptor::AllToAllOpV1Adaptor(AllToAllOpV1 op) : AllToAllOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AllToAllOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_concat_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all' op ""requires attribute 'concat_dimension'");
    if (namedAttrIt->getName() == AllToAllOpV1::getConcatDimensionAttrName(*odsOpName)) {
      tblgen_concat_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == AllToAllOpV1::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all' op ""requires attribute 'split_count'");
    if (namedAttrIt->getName() == AllToAllOpV1::getSplitCountAttrName(*odsOpName)) {
      tblgen_split_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all' op ""requires attribute 'split_dimension'");
    if (namedAttrIt->getName() == AllToAllOpV1::getSplitDimensionAttrName(*odsOpName)) {
      tblgen_split_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_split_dimension && !((true)))
    return emitError(loc, "'vhlo.all_to_all' op ""attribute 'split_dimension' failed to satisfy constraint: any attribute");

  if (tblgen_concat_dimension && !((true)))
    return emitError(loc, "'vhlo.all_to_all' op ""attribute 'concat_dimension' failed to satisfy constraint: any attribute");

  if (tblgen_split_count && !((true)))
    return emitError(loc, "'vhlo.all_to_all' op ""attribute 'split_count' failed to satisfy constraint: any attribute");

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.all_to_all' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AllToAllOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AllToAllOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AllToAllOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange AllToAllOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AllToAllOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AllToAllOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute AllToAllOpV1::getSplitDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getSplitDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV1::getSplitDimension() {
  auto attr = getSplitDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV1::getConcatDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 3, getConcatDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV1::getConcatDimension() {
  auto attr = getConcatDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV1::getSplitCountAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 1, getSplitCountAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV1::getSplitCount() {
  auto attr = getSplitCountAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV1::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 2, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV1::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

void AllToAllOpV1::setSplitDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSplitDimensionAttrName(), attr);
}

void AllToAllOpV1::setConcatDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getConcatDimensionAttrName(), attr);
}

void AllToAllOpV1::setSplitCountAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSplitCountAttrName(), attr);
}

void AllToAllOpV1::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void AllToAllOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute split_dimension, ::mlir::Attribute concat_dimension, ::mlir::Attribute split_count, ::mlir::Attribute replica_groups) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSplitDimensionAttrName(odsState.name), split_dimension);
  odsState.addAttribute(getConcatDimensionAttrName(odsState.name), concat_dimension);
  odsState.addAttribute(getSplitCountAttrName(odsState.name), split_count);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  odsState.addTypes(resultType0);
}

void AllToAllOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute split_dimension, ::mlir::Attribute concat_dimension, ::mlir::Attribute split_count, ::mlir::Attribute replica_groups) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSplitDimensionAttrName(odsState.name), split_dimension);
  odsState.addAttribute(getConcatDimensionAttrName(odsState.name), concat_dimension);
  odsState.addAttribute(getSplitCountAttrName(odsState.name), split_count);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AllToAllOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AllToAllOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_concat_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'concat_dimension'");
    if (namedAttrIt->getName() == getConcatDimensionAttrName()) {
      tblgen_concat_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'split_count'");
    if (namedAttrIt->getName() == getSplitCountAttrName()) {
      tblgen_split_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'split_dimension'");
    if (namedAttrIt->getName() == getSplitDimensionAttrName()) {
      tblgen_split_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_split_dimension, "split_dimension")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_concat_dimension, "concat_dimension")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_split_count, "split_count")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AllToAllOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AllToAllOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in all_to_all");
  return *version;
}
mlir::vhlo::Version AllToAllOpV1::getMaxVersion() {
  if (!strcmp("0.3.0", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in all_to_all");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AllToAllOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AllToAllOpV2 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AllToAllOpV2GenericAdaptorBase::AllToAllOpV2GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.all_to_all_v2", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AllToAllOpV2GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AllToAllOpV2GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getSplitDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, AllToAllOpV2::getSplitDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getSplitDimension() {
  auto attr = getSplitDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getConcatDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 3, AllToAllOpV2::getConcatDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getConcatDimension() {
  auto attr = getConcatDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getSplitCountAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 1, AllToAllOpV2::getSplitCountAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getSplitCount() {
  auto attr = getSplitCountAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 2, AllToAllOpV2::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 4, AllToAllOpV2::getChannelHandleAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> AllToAllOpV2GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
AllToAllOpV2Adaptor::AllToAllOpV2Adaptor(AllToAllOpV2 op) : AllToAllOpV2Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AllToAllOpV2Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_concat_dimension;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all_v2' op ""requires attribute 'concat_dimension'");
    if (namedAttrIt->getName() == AllToAllOpV2::getConcatDimensionAttrName(*odsOpName)) {
      tblgen_concat_dimension = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == AllToAllOpV2::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all_v2' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == AllToAllOpV2::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all_v2' op ""requires attribute 'split_count'");
    if (namedAttrIt->getName() == AllToAllOpV2::getSplitCountAttrName(*odsOpName)) {
      tblgen_split_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.all_to_all_v2' op ""requires attribute 'split_dimension'");
    if (namedAttrIt->getName() == AllToAllOpV2::getSplitDimensionAttrName(*odsOpName)) {
      tblgen_split_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_split_dimension && !((true)))
    return emitError(loc, "'vhlo.all_to_all_v2' op ""attribute 'split_dimension' failed to satisfy constraint: any attribute");

  if (tblgen_concat_dimension && !((true)))
    return emitError(loc, "'vhlo.all_to_all_v2' op ""attribute 'concat_dimension' failed to satisfy constraint: any attribute");

  if (tblgen_split_count && !((true)))
    return emitError(loc, "'vhlo.all_to_all_v2' op ""attribute 'split_count' failed to satisfy constraint: any attribute");

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.all_to_all_v2' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.all_to_all_v2' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AllToAllOpV2::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AllToAllOpV2::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AllToAllOpV2::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange AllToAllOpV2::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AllToAllOpV2::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AllToAllOpV2::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute AllToAllOpV2::getSplitDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getSplitDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV2::getSplitDimension() {
  auto attr = getSplitDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2::getConcatDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 3, getConcatDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV2::getConcatDimension() {
  auto attr = getConcatDimensionAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2::getSplitCountAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 1, getSplitCountAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV2::getSplitCount() {
  auto attr = getSplitCountAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 2, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute AllToAllOpV2::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute AllToAllOpV2::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 4, getChannelHandleAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> AllToAllOpV2::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void AllToAllOpV2::setSplitDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSplitDimensionAttrName(), attr);
}

void AllToAllOpV2::setConcatDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getConcatDimensionAttrName(), attr);
}

void AllToAllOpV2::setSplitCountAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSplitCountAttrName(), attr);
}

void AllToAllOpV2::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void AllToAllOpV2::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

::mlir::Attribute AllToAllOpV2::removeChannelHandleAttr() {
  return (*this)->removeAttr(getChannelHandleAttrName());
}

void AllToAllOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute split_dimension, ::mlir::Attribute concat_dimension, ::mlir::Attribute split_count, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSplitDimensionAttrName(odsState.name), split_dimension);
  odsState.addAttribute(getConcatDimensionAttrName(odsState.name), concat_dimension);
  odsState.addAttribute(getSplitCountAttrName(odsState.name), split_count);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  odsState.addTypes(resultType0);
}

void AllToAllOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute split_dimension, ::mlir::Attribute concat_dimension, ::mlir::Attribute split_count, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSplitDimensionAttrName(odsState.name), split_dimension);
  odsState.addAttribute(getConcatDimensionAttrName(odsState.name), concat_dimension);
  odsState.addAttribute(getSplitCountAttrName(odsState.name), split_count);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AllToAllOpV2::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AllToAllOpV2::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_concat_dimension;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'concat_dimension'");
    if (namedAttrIt->getName() == getConcatDimensionAttrName()) {
      tblgen_concat_dimension = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_replica_groups;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'split_count'");
    if (namedAttrIt->getName() == getSplitCountAttrName()) {
      tblgen_split_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_split_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'split_dimension'");
    if (namedAttrIt->getName() == getSplitDimensionAttrName()) {
      tblgen_split_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_split_dimension, "split_dimension")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_concat_dimension, "concat_dimension")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_split_count, "split_count")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AllToAllOpV2::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AllToAllOpV2::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.4.0");
  if (failed(version)) llvm_unreachable("invalid version 0.4.0 in all_to_all_v2");
  return *version;
}
mlir::vhlo::Version AllToAllOpV2::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in all_to_all_v2");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AllToAllOpV2)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::AndOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
AndOpV1GenericAdaptorBase::AndOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.and", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> AndOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr AndOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
AndOpV1Adaptor::AndOpV1Adaptor(AndOpV1 op) : AndOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult AndOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> AndOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range AndOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AndOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value AndOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange AndOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange AndOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> AndOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range AndOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value AndOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void AndOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void AndOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void AndOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult AndOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult AndOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version AndOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in and");
  return *version;
}
mlir::vhlo::Version AndOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in and");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::AndOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::Atan2OpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
Atan2OpV1GenericAdaptorBase::Atan2OpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.atan2", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> Atan2OpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr Atan2OpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
Atan2OpV1Adaptor::Atan2OpV1Adaptor(Atan2OpV1 op) : Atan2OpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult Atan2OpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> Atan2OpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range Atan2OpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value Atan2OpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value Atan2OpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange Atan2OpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange Atan2OpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> Atan2OpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range Atan2OpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value Atan2OpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void Atan2OpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void Atan2OpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void Atan2OpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult Atan2OpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult Atan2OpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version Atan2OpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in atan2");
  return *version;
}
mlir::vhlo::Version Atan2OpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in atan2");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::Atan2OpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::BatchNormGradOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
BatchNormGradOpV1GenericAdaptorBase::BatchNormGradOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.batch_norm_grad", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> BatchNormGradOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr BatchNormGradOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute BatchNormGradOpV1GenericAdaptorBase::getEpsilonAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, BatchNormGradOpV1::getEpsilonAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BatchNormGradOpV1GenericAdaptorBase::getEpsilon() {
  auto attr = getEpsilonAttr();
  return attr;
}

::mlir::Attribute BatchNormGradOpV1GenericAdaptorBase::getFeatureIndexAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, BatchNormGradOpV1::getFeatureIndexAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BatchNormGradOpV1GenericAdaptorBase::getFeatureIndex() {
  auto attr = getFeatureIndexAttr();
  return attr;
}

} // namespace detail
BatchNormGradOpV1Adaptor::BatchNormGradOpV1Adaptor(BatchNormGradOpV1 op) : BatchNormGradOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult BatchNormGradOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_epsilon;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.batch_norm_grad' op ""requires attribute 'epsilon'");
    if (namedAttrIt->getName() == BatchNormGradOpV1::getEpsilonAttrName(*odsOpName)) {
      tblgen_epsilon = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.batch_norm_grad' op ""requires attribute 'feature_index'");
    if (namedAttrIt->getName() == BatchNormGradOpV1::getFeatureIndexAttrName(*odsOpName)) {
      tblgen_feature_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_epsilon && !((true)))
    return emitError(loc, "'vhlo.batch_norm_grad' op ""attribute 'epsilon' failed to satisfy constraint: any attribute");

  if (tblgen_feature_index && !((true)))
    return emitError(loc, "'vhlo.batch_norm_grad' op ""attribute 'feature_index' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

void BatchNormGradOpV1::getAsmResultNames(::mlir::OpAsmSetValueNameFn setNameFn) {
  auto resultGroup0 = getODSResults(0);
  if (!resultGroup0.empty())
    setNameFn(*resultGroup0.begin(), "grad_operand");
  auto resultGroup1 = getODSResults(1);
  if (!resultGroup1.empty())
    setNameFn(*resultGroup1.begin(), "grad_scale");
  auto resultGroup2 = getODSResults(2);
  if (!resultGroup2.empty())
    setNameFn(*resultGroup2.begin(), "grad_offset");
}

std::pair<unsigned, unsigned> BatchNormGradOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range BatchNormGradOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BatchNormGradOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value BatchNormGradOpV1::getScale() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value BatchNormGradOpV1::getMean() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::Value BatchNormGradOpV1::getVariance() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(3).begin());
}

::mlir::Value BatchNormGradOpV1::getGradOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(4).begin());
}

::mlir::MutableOperandRange BatchNormGradOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormGradOpV1::getScaleMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormGradOpV1::getMeanMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormGradOpV1::getVarianceMutable() {
  auto range = getODSOperandIndexAndLength(3);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormGradOpV1::getGradOutputMutable() {
  auto range = getODSOperandIndexAndLength(4);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> BatchNormGradOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range BatchNormGradOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BatchNormGradOpV1::getGradOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Value BatchNormGradOpV1::getGradScale() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(1).begin());
}

::mlir::Value BatchNormGradOpV1::getGradOffset() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(2).begin());
}

::mlir::Attribute BatchNormGradOpV1::getEpsilonAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getEpsilonAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BatchNormGradOpV1::getEpsilon() {
  auto attr = getEpsilonAttr();
  return attr;
}

::mlir::Attribute BatchNormGradOpV1::getFeatureIndexAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getFeatureIndexAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BatchNormGradOpV1::getFeatureIndex() {
  auto attr = getFeatureIndexAttr();
  return attr;
}

void BatchNormGradOpV1::setEpsilonAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEpsilonAttrName(), attr);
}

void BatchNormGradOpV1::setFeatureIndexAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFeatureIndexAttrName(), attr);
}

void BatchNormGradOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type grad_operand, ::mlir::Type grad_scale, ::mlir::Type grad_offset, ::mlir::Value operand, ::mlir::Value scale, ::mlir::Value mean, ::mlir::Value variance, ::mlir::Value grad_output, ::mlir::Attribute epsilon, ::mlir::Attribute feature_index) {
  odsState.addOperands(operand);
  odsState.addOperands(scale);
  odsState.addOperands(mean);
  odsState.addOperands(variance);
  odsState.addOperands(grad_output);
  odsState.addAttribute(getEpsilonAttrName(odsState.name), epsilon);
  odsState.addAttribute(getFeatureIndexAttrName(odsState.name), feature_index);
  odsState.addTypes(grad_operand);
  odsState.addTypes(grad_scale);
  odsState.addTypes(grad_offset);
}

void BatchNormGradOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value scale, ::mlir::Value mean, ::mlir::Value variance, ::mlir::Value grad_output, ::mlir::Attribute epsilon, ::mlir::Attribute feature_index) {
  odsState.addOperands(operand);
  odsState.addOperands(scale);
  odsState.addOperands(mean);
  odsState.addOperands(variance);
  odsState.addOperands(grad_output);
  odsState.addAttribute(getEpsilonAttrName(odsState.name), epsilon);
  odsState.addAttribute(getFeatureIndexAttrName(odsState.name), feature_index);
  assert(resultTypes.size() == 3u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void BatchNormGradOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 5u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 3u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult BatchNormGradOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_epsilon;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'epsilon'");
    if (namedAttrIt->getName() == getEpsilonAttrName()) {
      tblgen_epsilon = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'feature_index'");
    if (namedAttrIt->getName() == getFeatureIndexAttrName()) {
      tblgen_feature_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_epsilon, "epsilon")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_feature_index, "feature_index")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup3 = getODSOperands(3);

    for (auto v : valueGroup3) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup4 = getODSOperands(4);

    for (auto v : valueGroup4) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSResults(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSResults(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult BatchNormGradOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version BatchNormGradOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in batch_norm_grad");
  return *version;
}
mlir::vhlo::Version BatchNormGradOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in batch_norm_grad");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::BatchNormGradOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::BatchNormInferenceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
BatchNormInferenceOpV1GenericAdaptorBase::BatchNormInferenceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.batch_norm_inference", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> BatchNormInferenceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr BatchNormInferenceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute BatchNormInferenceOpV1GenericAdaptorBase::getEpsilonAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, BatchNormInferenceOpV1::getEpsilonAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BatchNormInferenceOpV1GenericAdaptorBase::getEpsilon() {
  auto attr = getEpsilonAttr();
  return attr;
}

::mlir::Attribute BatchNormInferenceOpV1GenericAdaptorBase::getFeatureIndexAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, BatchNormInferenceOpV1::getFeatureIndexAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BatchNormInferenceOpV1GenericAdaptorBase::getFeatureIndex() {
  auto attr = getFeatureIndexAttr();
  return attr;
}

} // namespace detail
BatchNormInferenceOpV1Adaptor::BatchNormInferenceOpV1Adaptor(BatchNormInferenceOpV1 op) : BatchNormInferenceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult BatchNormInferenceOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_epsilon;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.batch_norm_inference' op ""requires attribute 'epsilon'");
    if (namedAttrIt->getName() == BatchNormInferenceOpV1::getEpsilonAttrName(*odsOpName)) {
      tblgen_epsilon = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.batch_norm_inference' op ""requires attribute 'feature_index'");
    if (namedAttrIt->getName() == BatchNormInferenceOpV1::getFeatureIndexAttrName(*odsOpName)) {
      tblgen_feature_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_epsilon && !((true)))
    return emitError(loc, "'vhlo.batch_norm_inference' op ""attribute 'epsilon' failed to satisfy constraint: any attribute");

  if (tblgen_feature_index && !((true)))
    return emitError(loc, "'vhlo.batch_norm_inference' op ""attribute 'feature_index' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> BatchNormInferenceOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range BatchNormInferenceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BatchNormInferenceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value BatchNormInferenceOpV1::getScale() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value BatchNormInferenceOpV1::getOffset() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::Value BatchNormInferenceOpV1::getMean() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(3).begin());
}

::mlir::Value BatchNormInferenceOpV1::getVariance() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(4).begin());
}

::mlir::MutableOperandRange BatchNormInferenceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormInferenceOpV1::getScaleMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormInferenceOpV1::getOffsetMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormInferenceOpV1::getMeanMutable() {
  auto range = getODSOperandIndexAndLength(3);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormInferenceOpV1::getVarianceMutable() {
  auto range = getODSOperandIndexAndLength(4);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> BatchNormInferenceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range BatchNormInferenceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BatchNormInferenceOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute BatchNormInferenceOpV1::getEpsilonAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getEpsilonAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BatchNormInferenceOpV1::getEpsilon() {
  auto attr = getEpsilonAttr();
  return attr;
}

::mlir::Attribute BatchNormInferenceOpV1::getFeatureIndexAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getFeatureIndexAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BatchNormInferenceOpV1::getFeatureIndex() {
  auto attr = getFeatureIndexAttr();
  return attr;
}

void BatchNormInferenceOpV1::setEpsilonAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEpsilonAttrName(), attr);
}

void BatchNormInferenceOpV1::setFeatureIndexAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFeatureIndexAttrName(), attr);
}

void BatchNormInferenceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::Value scale, ::mlir::Value offset, ::mlir::Value mean, ::mlir::Value variance, ::mlir::Attribute epsilon, ::mlir::Attribute feature_index) {
  odsState.addOperands(operand);
  odsState.addOperands(scale);
  odsState.addOperands(offset);
  odsState.addOperands(mean);
  odsState.addOperands(variance);
  odsState.addAttribute(getEpsilonAttrName(odsState.name), epsilon);
  odsState.addAttribute(getFeatureIndexAttrName(odsState.name), feature_index);
  odsState.addTypes(result);
}

void BatchNormInferenceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value scale, ::mlir::Value offset, ::mlir::Value mean, ::mlir::Value variance, ::mlir::Attribute epsilon, ::mlir::Attribute feature_index) {
  odsState.addOperands(operand);
  odsState.addOperands(scale);
  odsState.addOperands(offset);
  odsState.addOperands(mean);
  odsState.addOperands(variance);
  odsState.addAttribute(getEpsilonAttrName(odsState.name), epsilon);
  odsState.addAttribute(getFeatureIndexAttrName(odsState.name), feature_index);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void BatchNormInferenceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 5u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult BatchNormInferenceOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_epsilon;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'epsilon'");
    if (namedAttrIt->getName() == getEpsilonAttrName()) {
      tblgen_epsilon = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'feature_index'");
    if (namedAttrIt->getName() == getFeatureIndexAttrName()) {
      tblgen_feature_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_epsilon, "epsilon")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_feature_index, "feature_index")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup3 = getODSOperands(3);

    for (auto v : valueGroup3) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup4 = getODSOperands(4);

    for (auto v : valueGroup4) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult BatchNormInferenceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version BatchNormInferenceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in batch_norm_inference");
  return *version;
}
mlir::vhlo::Version BatchNormInferenceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in batch_norm_inference");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::BatchNormInferenceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::BatchNormTrainingOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
BatchNormTrainingOpV1GenericAdaptorBase::BatchNormTrainingOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.batch_norm_training", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> BatchNormTrainingOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr BatchNormTrainingOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute BatchNormTrainingOpV1GenericAdaptorBase::getEpsilonAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, BatchNormTrainingOpV1::getEpsilonAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BatchNormTrainingOpV1GenericAdaptorBase::getEpsilon() {
  auto attr = getEpsilonAttr();
  return attr;
}

::mlir::Attribute BatchNormTrainingOpV1GenericAdaptorBase::getFeatureIndexAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, BatchNormTrainingOpV1::getFeatureIndexAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BatchNormTrainingOpV1GenericAdaptorBase::getFeatureIndex() {
  auto attr = getFeatureIndexAttr();
  return attr;
}

} // namespace detail
BatchNormTrainingOpV1Adaptor::BatchNormTrainingOpV1Adaptor(BatchNormTrainingOpV1 op) : BatchNormTrainingOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult BatchNormTrainingOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_epsilon;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.batch_norm_training' op ""requires attribute 'epsilon'");
    if (namedAttrIt->getName() == BatchNormTrainingOpV1::getEpsilonAttrName(*odsOpName)) {
      tblgen_epsilon = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.batch_norm_training' op ""requires attribute 'feature_index'");
    if (namedAttrIt->getName() == BatchNormTrainingOpV1::getFeatureIndexAttrName(*odsOpName)) {
      tblgen_feature_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_epsilon && !((true)))
    return emitError(loc, "'vhlo.batch_norm_training' op ""attribute 'epsilon' failed to satisfy constraint: any attribute");

  if (tblgen_feature_index && !((true)))
    return emitError(loc, "'vhlo.batch_norm_training' op ""attribute 'feature_index' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

void BatchNormTrainingOpV1::getAsmResultNames(::mlir::OpAsmSetValueNameFn setNameFn) {
  auto resultGroup0 = getODSResults(0);
  if (!resultGroup0.empty())
    setNameFn(*resultGroup0.begin(), "output");
  auto resultGroup1 = getODSResults(1);
  if (!resultGroup1.empty())
    setNameFn(*resultGroup1.begin(), "batch_mean");
  auto resultGroup2 = getODSResults(2);
  if (!resultGroup2.empty())
    setNameFn(*resultGroup2.begin(), "batch_var");
}

std::pair<unsigned, unsigned> BatchNormTrainingOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range BatchNormTrainingOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BatchNormTrainingOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value BatchNormTrainingOpV1::getScale() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value BatchNormTrainingOpV1::getOffset() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange BatchNormTrainingOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormTrainingOpV1::getScaleMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange BatchNormTrainingOpV1::getOffsetMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> BatchNormTrainingOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range BatchNormTrainingOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BatchNormTrainingOpV1::getOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Value BatchNormTrainingOpV1::getBatchMean() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(1).begin());
}

::mlir::Value BatchNormTrainingOpV1::getBatchVar() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(2).begin());
}

::mlir::Attribute BatchNormTrainingOpV1::getEpsilonAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getEpsilonAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BatchNormTrainingOpV1::getEpsilon() {
  auto attr = getEpsilonAttr();
  return attr;
}

::mlir::Attribute BatchNormTrainingOpV1::getFeatureIndexAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getFeatureIndexAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BatchNormTrainingOpV1::getFeatureIndex() {
  auto attr = getFeatureIndexAttr();
  return attr;
}

void BatchNormTrainingOpV1::setEpsilonAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEpsilonAttrName(), attr);
}

void BatchNormTrainingOpV1::setFeatureIndexAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFeatureIndexAttrName(), attr);
}

void BatchNormTrainingOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type output, ::mlir::Type batch_mean, ::mlir::Type batch_var, ::mlir::Value operand, ::mlir::Value scale, ::mlir::Value offset, ::mlir::Attribute epsilon, ::mlir::Attribute feature_index) {
  odsState.addOperands(operand);
  odsState.addOperands(scale);
  odsState.addOperands(offset);
  odsState.addAttribute(getEpsilonAttrName(odsState.name), epsilon);
  odsState.addAttribute(getFeatureIndexAttrName(odsState.name), feature_index);
  odsState.addTypes(output);
  odsState.addTypes(batch_mean);
  odsState.addTypes(batch_var);
}

void BatchNormTrainingOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value scale, ::mlir::Value offset, ::mlir::Attribute epsilon, ::mlir::Attribute feature_index) {
  odsState.addOperands(operand);
  odsState.addOperands(scale);
  odsState.addOperands(offset);
  odsState.addAttribute(getEpsilonAttrName(odsState.name), epsilon);
  odsState.addAttribute(getFeatureIndexAttrName(odsState.name), feature_index);
  assert(resultTypes.size() == 3u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void BatchNormTrainingOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 3u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult BatchNormTrainingOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_epsilon;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'epsilon'");
    if (namedAttrIt->getName() == getEpsilonAttrName()) {
      tblgen_epsilon = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'feature_index'");
    if (namedAttrIt->getName() == getFeatureIndexAttrName()) {
      tblgen_feature_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_epsilon, "epsilon")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_feature_index, "feature_index")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSResults(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSResults(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult BatchNormTrainingOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version BatchNormTrainingOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in batch_norm_training");
  return *version;
}
mlir::vhlo::Version BatchNormTrainingOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in batch_norm_training");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::BatchNormTrainingOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::BitcastConvertOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
BitcastConvertOpV1GenericAdaptorBase::BitcastConvertOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.bitcast_convert", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> BitcastConvertOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr BitcastConvertOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
BitcastConvertOpV1Adaptor::BitcastConvertOpV1Adaptor(BitcastConvertOpV1 op) : BitcastConvertOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult BitcastConvertOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> BitcastConvertOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range BitcastConvertOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BitcastConvertOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange BitcastConvertOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> BitcastConvertOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range BitcastConvertOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

void BitcastConvertOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(resultType0);
}

void BitcastConvertOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void BitcastConvertOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult BitcastConvertOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult BitcastConvertOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version BitcastConvertOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in bitcast_convert");
  return *version;
}
mlir::vhlo::Version BitcastConvertOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in bitcast_convert");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::BitcastConvertOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::BroadcastInDimOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
BroadcastInDimOpV1GenericAdaptorBase::BroadcastInDimOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.broadcast_in_dim", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> BroadcastInDimOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr BroadcastInDimOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute BroadcastInDimOpV1GenericAdaptorBase::getBroadcastDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, BroadcastInDimOpV1::getBroadcastDimensionsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BroadcastInDimOpV1GenericAdaptorBase::getBroadcastDimensions() {
  auto attr = getBroadcastDimensionsAttr();
  return attr;
}

} // namespace detail
BroadcastInDimOpV1Adaptor::BroadcastInDimOpV1Adaptor(BroadcastInDimOpV1 op) : BroadcastInDimOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult BroadcastInDimOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_broadcast_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.broadcast_in_dim' op ""requires attribute 'broadcast_dimensions'");
    if (namedAttrIt->getName() == BroadcastInDimOpV1::getBroadcastDimensionsAttrName(*odsOpName)) {
      tblgen_broadcast_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_broadcast_dimensions && !((true)))
    return emitError(loc, "'vhlo.broadcast_in_dim' op ""attribute 'broadcast_dimensions' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> BroadcastInDimOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range BroadcastInDimOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BroadcastInDimOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange BroadcastInDimOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> BroadcastInDimOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range BroadcastInDimOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute BroadcastInDimOpV1::getBroadcastDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getBroadcastDimensionsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BroadcastInDimOpV1::getBroadcastDimensions() {
  auto attr = getBroadcastDimensionsAttr();
  return attr;
}

void BroadcastInDimOpV1::setBroadcastDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBroadcastDimensionsAttrName(), attr);
}

void BroadcastInDimOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute broadcast_dimensions) {
  odsState.addOperands(operand);
  odsState.addAttribute(getBroadcastDimensionsAttrName(odsState.name), broadcast_dimensions);
  odsState.addTypes(resultType0);
}

void BroadcastInDimOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute broadcast_dimensions) {
  odsState.addOperands(operand);
  odsState.addAttribute(getBroadcastDimensionsAttrName(odsState.name), broadcast_dimensions);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void BroadcastInDimOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult BroadcastInDimOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_broadcast_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'broadcast_dimensions'");
    if (namedAttrIt->getName() == getBroadcastDimensionsAttrName()) {
      tblgen_broadcast_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_broadcast_dimensions, "broadcast_dimensions")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult BroadcastInDimOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version BroadcastInDimOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in broadcast_in_dim");
  return *version;
}
mlir::vhlo::Version BroadcastInDimOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in broadcast_in_dim");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::BroadcastInDimOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::BroadcastOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
BroadcastOpV1GenericAdaptorBase::BroadcastOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.broadcast", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> BroadcastOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr BroadcastOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute BroadcastOpV1GenericAdaptorBase::getBroadcastSizesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, BroadcastOpV1::getBroadcastSizesAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute BroadcastOpV1GenericAdaptorBase::getBroadcastSizes() {
  auto attr = getBroadcastSizesAttr();
  return attr;
}

} // namespace detail
BroadcastOpV1Adaptor::BroadcastOpV1Adaptor(BroadcastOpV1 op) : BroadcastOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult BroadcastOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_broadcast_sizes;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.broadcast' op ""requires attribute 'broadcast_sizes'");
    if (namedAttrIt->getName() == BroadcastOpV1::getBroadcastSizesAttrName(*odsOpName)) {
      tblgen_broadcast_sizes = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_broadcast_sizes && !((true)))
    return emitError(loc, "'vhlo.broadcast' op ""attribute 'broadcast_sizes' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> BroadcastOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range BroadcastOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value BroadcastOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange BroadcastOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> BroadcastOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range BroadcastOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute BroadcastOpV1::getBroadcastSizesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getBroadcastSizesAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute BroadcastOpV1::getBroadcastSizes() {
  auto attr = getBroadcastSizesAttr();
  return attr;
}

void BroadcastOpV1::setBroadcastSizesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBroadcastSizesAttrName(), attr);
}

void BroadcastOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute broadcast_sizes) {
  odsState.addOperands(operand);
  odsState.addAttribute(getBroadcastSizesAttrName(odsState.name), broadcast_sizes);
  odsState.addTypes(resultType0);
}

void BroadcastOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute broadcast_sizes) {
  odsState.addOperands(operand);
  odsState.addAttribute(getBroadcastSizesAttrName(odsState.name), broadcast_sizes);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void BroadcastOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult BroadcastOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_broadcast_sizes;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'broadcast_sizes'");
    if (namedAttrIt->getName() == getBroadcastSizesAttrName()) {
      tblgen_broadcast_sizes = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_broadcast_sizes, "broadcast_sizes")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult BroadcastOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version BroadcastOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in broadcast");
  return *version;
}
mlir::vhlo::Version BroadcastOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in broadcast");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::BroadcastOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CaseOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CaseOpV1GenericAdaptorBase::CaseOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.case", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CaseOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CaseOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::RegionRange CaseOpV1GenericAdaptorBase::getBranches() {
  return odsRegions.drop_front(0);
}

::mlir::RegionRange CaseOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
CaseOpV1Adaptor::CaseOpV1Adaptor(CaseOpV1 op) : CaseOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CaseOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CaseOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CaseOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CaseOpV1::getIndex() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CaseOpV1::getIndexMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CaseOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range CaseOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::MutableArrayRef<::mlir::Region> CaseOpV1::getBranches() {
  return (*this)->getRegions().drop_front(0);
}

void CaseOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::Value index, unsigned branchesCount) {
  odsState.addOperands(index);
  for (unsigned i = 0; i < branchesCount; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void CaseOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes, unsigned numRegions) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != numRegions; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CaseOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : getBranches())
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "branches", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult CaseOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CaseOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in case");
  return *version;
}
mlir::vhlo::Version CaseOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in case");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CaseOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CbrtOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CbrtOpV1GenericAdaptorBase::CbrtOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.cbrt", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CbrtOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CbrtOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
CbrtOpV1Adaptor::CbrtOpV1Adaptor(CbrtOpV1 op) : CbrtOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CbrtOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CbrtOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CbrtOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CbrtOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CbrtOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CbrtOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CbrtOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CbrtOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void CbrtOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void CbrtOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CbrtOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CbrtOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CbrtOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CbrtOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in cbrt");
  return *version;
}
mlir::vhlo::Version CbrtOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in cbrt");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CbrtOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CeilOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CeilOpV1GenericAdaptorBase::CeilOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.ceil", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CeilOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CeilOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
CeilOpV1Adaptor::CeilOpV1Adaptor(CeilOpV1 op) : CeilOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CeilOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CeilOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CeilOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CeilOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CeilOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CeilOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CeilOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CeilOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void CeilOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void CeilOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CeilOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CeilOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CeilOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CeilOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in ceil");
  return *version;
}
mlir::vhlo::Version CeilOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in ceil");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CeilOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CholeskyOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CholeskyOpV1GenericAdaptorBase::CholeskyOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.cholesky", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CholeskyOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CholeskyOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CholeskyOpV1GenericAdaptorBase::getLowerAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, CholeskyOpV1::getLowerAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CholeskyOpV1GenericAdaptorBase::getLower() {
  auto attr = getLowerAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
CholeskyOpV1Adaptor::CholeskyOpV1Adaptor(CholeskyOpV1 op) : CholeskyOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CholeskyOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_lower;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == CholeskyOpV1::getLowerAttrName(*odsOpName)) {
      tblgen_lower = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_lower && !((true)))
    return emitError(loc, "'vhlo.cholesky' op ""attribute 'lower' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CholeskyOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CholeskyOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CholeskyOpV1::getA() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CholeskyOpV1::getAMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CholeskyOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CholeskyOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CholeskyOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute CholeskyOpV1::getLowerAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getLowerAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CholeskyOpV1::getLower() {
  auto attr = getLowerAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void CholeskyOpV1::setLowerAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLowerAttrName(), attr);
}

::mlir::Attribute CholeskyOpV1::removeLowerAttr() {
  return (*this)->removeAttr(getLowerAttrName());
}

void CholeskyOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value a, /*optional*/::mlir::Attribute lower) {
  odsState.addOperands(a);
  if (lower) {
    odsState.addAttribute(getLowerAttrName(odsState.name), lower);
  }
  odsState.addTypes(result);
}

void CholeskyOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value a, /*optional*/::mlir::Attribute lower) {
  odsState.addOperands(a);
  if (lower) {
    odsState.addAttribute(getLowerAttrName(odsState.name), lower);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CholeskyOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CholeskyOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_lower;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getLowerAttrName()) {
      tblgen_lower = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_lower, "lower")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CholeskyOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CholeskyOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in cholesky");
  return *version;
}
mlir::vhlo::Version CholeskyOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in cholesky");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CholeskyOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ClampOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ClampOpV1GenericAdaptorBase::ClampOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.clamp", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ClampOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ClampOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ClampOpV1Adaptor::ClampOpV1Adaptor(ClampOpV1 op) : ClampOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ClampOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ClampOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ClampOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ClampOpV1::getMin() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ClampOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value ClampOpV1::getMax() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange ClampOpV1::getMinMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ClampOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ClampOpV1::getMaxMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ClampOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ClampOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ClampOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ClampOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value min, ::mlir::Value operand, ::mlir::Value max) {
  odsState.addOperands(min);
  odsState.addOperands(operand);
  odsState.addOperands(max);
  odsState.addTypes(result);
}

void ClampOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value min, ::mlir::Value operand, ::mlir::Value max) {
  odsState.addOperands(min);
  odsState.addOperands(operand);
  odsState.addOperands(max);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ClampOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ClampOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ClampOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ClampOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in clamp");
  return *version;
}
mlir::vhlo::Version ClampOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in clamp");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ClampOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ClzOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ClzOpV1GenericAdaptorBase::ClzOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.count_leading_zeros", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ClzOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ClzOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ClzOpV1Adaptor::ClzOpV1Adaptor(ClzOpV1 op) : ClzOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ClzOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ClzOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ClzOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ClzOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ClzOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ClzOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ClzOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ClzOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ClzOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void ClzOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ClzOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ClzOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ClzOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ClzOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in count_leading_zeros");
  return *version;
}
mlir::vhlo::Version ClzOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in count_leading_zeros");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ClzOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CollectivePermuteOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CollectivePermuteOpV1GenericAdaptorBase::CollectivePermuteOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.collective_permute", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CollectivePermuteOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CollectivePermuteOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CollectivePermuteOpV1GenericAdaptorBase::getSourceTargetPairsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, CollectivePermuteOpV1::getSourceTargetPairsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CollectivePermuteOpV1GenericAdaptorBase::getSourceTargetPairs() {
  auto attr = getSourceTargetPairsAttr();
  return attr;
}

} // namespace detail
CollectivePermuteOpV1Adaptor::CollectivePermuteOpV1Adaptor(CollectivePermuteOpV1 op) : CollectivePermuteOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CollectivePermuteOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_source_target_pairs;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.collective_permute' op ""requires attribute 'source_target_pairs'");
    if (namedAttrIt->getName() == CollectivePermuteOpV1::getSourceTargetPairsAttrName(*odsOpName)) {
      tblgen_source_target_pairs = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_source_target_pairs && !((true)))
    return emitError(loc, "'vhlo.collective_permute' op ""attribute 'source_target_pairs' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CollectivePermuteOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CollectivePermuteOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CollectivePermuteOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CollectivePermuteOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CollectivePermuteOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CollectivePermuteOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute CollectivePermuteOpV1::getSourceTargetPairsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getSourceTargetPairsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CollectivePermuteOpV1::getSourceTargetPairs() {
  auto attr = getSourceTargetPairsAttr();
  return attr;
}

void CollectivePermuteOpV1::setSourceTargetPairsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSourceTargetPairsAttrName(), attr);
}

void CollectivePermuteOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute source_target_pairs) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSourceTargetPairsAttrName(odsState.name), source_target_pairs);
  odsState.addTypes(resultType0);
}

void CollectivePermuteOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute source_target_pairs) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSourceTargetPairsAttrName(odsState.name), source_target_pairs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CollectivePermuteOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CollectivePermuteOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_source_target_pairs;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'source_target_pairs'");
    if (namedAttrIt->getName() == getSourceTargetPairsAttrName()) {
      tblgen_source_target_pairs = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_source_target_pairs, "source_target_pairs")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CollectivePermuteOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CollectivePermuteOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in collective_permute");
  return *version;
}
mlir::vhlo::Version CollectivePermuteOpV1::getMaxVersion() {
  if (!strcmp("0.3.0", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in collective_permute");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CollectivePermuteOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CollectivePermuteOpV2 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CollectivePermuteOpV2GenericAdaptorBase::CollectivePermuteOpV2GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.collective_permute_v2", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CollectivePermuteOpV2GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CollectivePermuteOpV2GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CollectivePermuteOpV2GenericAdaptorBase::getSourceTargetPairsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, CollectivePermuteOpV2::getSourceTargetPairsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CollectivePermuteOpV2GenericAdaptorBase::getSourceTargetPairs() {
  auto attr = getSourceTargetPairsAttr();
  return attr;
}

::mlir::Attribute CollectivePermuteOpV2GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, CollectivePermuteOpV2::getChannelHandleAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CollectivePermuteOpV2GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
CollectivePermuteOpV2Adaptor::CollectivePermuteOpV2Adaptor(CollectivePermuteOpV2 op) : CollectivePermuteOpV2Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CollectivePermuteOpV2Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_source_target_pairs;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.collective_permute_v2' op ""requires attribute 'source_target_pairs'");
    if (namedAttrIt->getName() == CollectivePermuteOpV2::getSourceTargetPairsAttrName(*odsOpName)) {
      tblgen_source_target_pairs = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == CollectivePermuteOpV2::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_source_target_pairs && !((true)))
    return emitError(loc, "'vhlo.collective_permute_v2' op ""attribute 'source_target_pairs' failed to satisfy constraint: any attribute");

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.collective_permute_v2' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CollectivePermuteOpV2::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CollectivePermuteOpV2::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CollectivePermuteOpV2::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CollectivePermuteOpV2::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CollectivePermuteOpV2::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CollectivePermuteOpV2::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute CollectivePermuteOpV2::getSourceTargetPairsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getSourceTargetPairsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CollectivePermuteOpV2::getSourceTargetPairs() {
  auto attr = getSourceTargetPairsAttr();
  return attr;
}

::mlir::Attribute CollectivePermuteOpV2::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getChannelHandleAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CollectivePermuteOpV2::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void CollectivePermuteOpV2::setSourceTargetPairsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSourceTargetPairsAttrName(), attr);
}

void CollectivePermuteOpV2::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

::mlir::Attribute CollectivePermuteOpV2::removeChannelHandleAttr() {
  return (*this)->removeAttr(getChannelHandleAttrName());
}

void CollectivePermuteOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute source_target_pairs, /*optional*/::mlir::Attribute channel_handle) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSourceTargetPairsAttrName(odsState.name), source_target_pairs);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  odsState.addTypes(resultType0);
}

void CollectivePermuteOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute source_target_pairs, /*optional*/::mlir::Attribute channel_handle) {
  odsState.addOperands(operand);
  odsState.addAttribute(getSourceTargetPairsAttrName(odsState.name), source_target_pairs);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CollectivePermuteOpV2::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CollectivePermuteOpV2::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_source_target_pairs;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'source_target_pairs'");
    if (namedAttrIt->getName() == getSourceTargetPairsAttrName()) {
      tblgen_source_target_pairs = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_source_target_pairs, "source_target_pairs")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CollectivePermuteOpV2::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CollectivePermuteOpV2::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.4.0");
  if (failed(version)) llvm_unreachable("invalid version 0.4.0 in collective_permute_v2");
  return *version;
}
mlir::vhlo::Version CollectivePermuteOpV2::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in collective_permute_v2");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CollectivePermuteOpV2)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CompareOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CompareOpV1GenericAdaptorBase::CompareOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.compare", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CompareOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CompareOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CompareOpV1GenericAdaptorBase::getComparisonDirectionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, CompareOpV1::getComparisonDirectionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CompareOpV1GenericAdaptorBase::getComparisonDirection() {
  auto attr = getComparisonDirectionAttr();
  return attr;
}

::mlir::Attribute CompareOpV1GenericAdaptorBase::getCompareTypeAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, CompareOpV1::getCompareTypeAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CompareOpV1GenericAdaptorBase::getCompareType() {
  auto attr = getCompareTypeAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
CompareOpV1Adaptor::CompareOpV1Adaptor(CompareOpV1 op) : CompareOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CompareOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_comparison_direction;
  ::mlir::Attribute tblgen_compare_type;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.compare' op ""requires attribute 'comparison_direction'");
    if (namedAttrIt->getName() == CompareOpV1::getComparisonDirectionAttrName(*odsOpName)) {
      tblgen_comparison_direction = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == CompareOpV1::getCompareTypeAttrName(*odsOpName)) {
      tblgen_compare_type = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_comparison_direction && !((true)))
    return emitError(loc, "'vhlo.compare' op ""attribute 'comparison_direction' failed to satisfy constraint: any attribute");

  if (tblgen_compare_type && !((true)))
    return emitError(loc, "'vhlo.compare' op ""attribute 'compare_type' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CompareOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CompareOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CompareOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value CompareOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange CompareOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange CompareOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CompareOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CompareOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute CompareOpV1::getComparisonDirectionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getComparisonDirectionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CompareOpV1::getComparisonDirection() {
  auto attr = getComparisonDirectionAttr();
  return attr;
}

::mlir::Attribute CompareOpV1::getCompareTypeAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getCompareTypeAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CompareOpV1::getCompareType() {
  auto attr = getCompareTypeAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void CompareOpV1::setComparisonDirectionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getComparisonDirectionAttrName(), attr);
}

void CompareOpV1::setCompareTypeAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getCompareTypeAttrName(), attr);
}

::mlir::Attribute CompareOpV1::removeCompareTypeAttr() {
  return (*this)->removeAttr(getCompareTypeAttrName());
}

void CompareOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Attribute comparison_direction, /*optional*/::mlir::Attribute compare_type) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addAttribute(getComparisonDirectionAttrName(odsState.name), comparison_direction);
  if (compare_type) {
    odsState.addAttribute(getCompareTypeAttrName(odsState.name), compare_type);
  }
  odsState.addTypes(resultType0);
}

void CompareOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Attribute comparison_direction, /*optional*/::mlir::Attribute compare_type) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addAttribute(getComparisonDirectionAttrName(odsState.name), comparison_direction);
  if (compare_type) {
    odsState.addAttribute(getCompareTypeAttrName(odsState.name), compare_type);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CompareOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CompareOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_comparison_direction;
  ::mlir::Attribute tblgen_compare_type;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'comparison_direction'");
    if (namedAttrIt->getName() == getComparisonDirectionAttrName()) {
      tblgen_comparison_direction = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getCompareTypeAttrName()) {
      tblgen_compare_type = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_comparison_direction, "comparison_direction")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_compare_type, "compare_type")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CompareOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CompareOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in compare");
  return *version;
}
mlir::vhlo::Version CompareOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in compare");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CompareOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ComplexOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ComplexOpV1GenericAdaptorBase::ComplexOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.complex", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ComplexOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ComplexOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ComplexOpV1Adaptor::ComplexOpV1Adaptor(ComplexOpV1 op) : ComplexOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ComplexOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ComplexOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ComplexOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ComplexOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ComplexOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange ComplexOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ComplexOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ComplexOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ComplexOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ComplexOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ComplexOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void ComplexOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ComplexOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ComplexOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ComplexOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ComplexOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in complex");
  return *version;
}
mlir::vhlo::Version ComplexOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in complex");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ComplexOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ComputeReshapeShapeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ComputeReshapeShapeOpV1GenericAdaptorBase::ComputeReshapeShapeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.compute_reshape_shape", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ComputeReshapeShapeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ComputeReshapeShapeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ComputeReshapeShapeOpV1Adaptor::ComputeReshapeShapeOpV1Adaptor(ComputeReshapeShapeOpV1 op) : ComputeReshapeShapeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ComputeReshapeShapeOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ComputeReshapeShapeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ComputeReshapeShapeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ComputeReshapeShapeOpV1::getNumElements() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ComputeReshapeShapeOpV1::getDynamicShape() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange ComputeReshapeShapeOpV1::getNumElementsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ComputeReshapeShapeOpV1::getDynamicShapeMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ComputeReshapeShapeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ComputeReshapeShapeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ComputeReshapeShapeOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ComputeReshapeShapeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value num_elements, ::mlir::Value dynamic_shape) {
  odsState.addOperands(num_elements);
  odsState.addOperands(dynamic_shape);
  odsState.addTypes(result);
}

void ComputeReshapeShapeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value num_elements, ::mlir::Value dynamic_shape) {
  odsState.addOperands(num_elements);
  odsState.addOperands(dynamic_shape);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ComputeReshapeShapeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ComputeReshapeShapeOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ComputeReshapeShapeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ComputeReshapeShapeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in compute_reshape_shape");
  return *version;
}
mlir::vhlo::Version ComputeReshapeShapeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in compute_reshape_shape");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ComputeReshapeShapeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ConcatenateOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ConcatenateOpV1GenericAdaptorBase::ConcatenateOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.concatenate", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ConcatenateOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr ConcatenateOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ConcatenateOpV1GenericAdaptorBase::getDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, ConcatenateOpV1::getDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ConcatenateOpV1GenericAdaptorBase::getDimension() {
  auto attr = getDimensionAttr();
  return attr;
}

} // namespace detail
ConcatenateOpV1Adaptor::ConcatenateOpV1Adaptor(ConcatenateOpV1 op) : ConcatenateOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ConcatenateOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.concatenate' op ""requires attribute 'dimension'");
    if (namedAttrIt->getName() == ConcatenateOpV1::getDimensionAttrName(*odsOpName)) {
      tblgen_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dimension && !((true)))
    return emitError(loc, "'vhlo.concatenate' op ""attribute 'dimension' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ConcatenateOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range ConcatenateOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range ConcatenateOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange ConcatenateOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ConcatenateOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ConcatenateOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute ConcatenateOpV1::getDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ConcatenateOpV1::getDimension() {
  auto attr = getDimensionAttr();
  return attr;
}

void ConcatenateOpV1::setDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionAttrName(), attr);
}

void ConcatenateOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::ValueRange inputs, ::mlir::Attribute dimension) {
  odsState.addOperands(inputs);
  odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  odsState.addTypes(resultType0);
}

void ConcatenateOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange inputs, ::mlir::Attribute dimension) {
  odsState.addOperands(inputs);
  odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ConcatenateOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ConcatenateOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension'");
    if (namedAttrIt->getName() == getDimensionAttrName()) {
      tblgen_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension, "dimension")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ConcatenateOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ConcatenateOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in concatenate");
  return *version;
}
mlir::vhlo::Version ConcatenateOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in concatenate");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ConcatenateOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ConstantOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ConstantOpV1GenericAdaptorBase::ConstantOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.constant", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ConstantOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ConstantOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ConstantOpV1GenericAdaptorBase::getValueAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, ConstantOpV1::getValueAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ConstantOpV1GenericAdaptorBase::getValue() {
  auto attr = getValueAttr();
  return attr;
}

} // namespace detail
ConstantOpV1Adaptor::ConstantOpV1Adaptor(ConstantOpV1 op) : ConstantOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ConstantOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_value;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.constant' op ""requires attribute 'value'");
    if (namedAttrIt->getName() == ConstantOpV1::getValueAttrName(*odsOpName)) {
      tblgen_value = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_value && !((true)))
    return emitError(loc, "'vhlo.constant' op ""attribute 'value' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ConstantOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ConstantOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> ConstantOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ConstantOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ConstantOpV1::getOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute ConstantOpV1::getValueAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getValueAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ConstantOpV1::getValue() {
  auto attr = getValueAttr();
  return attr;
}

void ConstantOpV1::setValueAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getValueAttrName(), attr);
}

void ConstantOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type output, ::mlir::Attribute value) {
  odsState.addAttribute(getValueAttrName(odsState.name), value);
  odsState.addTypes(output);
}

void ConstantOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Attribute value) {
  odsState.addAttribute(getValueAttrName(odsState.name), value);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ConstantOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ConstantOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_value;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'value'");
    if (namedAttrIt->getName() == getValueAttrName()) {
      tblgen_value = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_value, "value")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ConstantOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ConstantOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in constant");
  return *version;
}
mlir::vhlo::Version ConstantOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in constant");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ConstantOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ConvertOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ConvertOpV1GenericAdaptorBase::ConvertOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.convert", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ConvertOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ConvertOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ConvertOpV1Adaptor::ConvertOpV1Adaptor(ConvertOpV1 op) : ConvertOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ConvertOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ConvertOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ConvertOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ConvertOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ConvertOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ConvertOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ConvertOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ConvertOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ConvertOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void ConvertOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ConvertOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ConvertOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ConvertOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ConvertOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in convert");
  return *version;
}
mlir::vhlo::Version ConvertOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in convert");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ConvertOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ConvolutionOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ConvolutionOpV1GenericAdaptorBase::ConvolutionOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.convolution", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ConvolutionOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ConvolutionOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getWindowStridesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, ConvolutionOpV1::getWindowStridesAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ConvolutionOpV1GenericAdaptorBase::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getPaddingAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, ConvolutionOpV1::getPaddingAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ConvolutionOpV1GenericAdaptorBase::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getLhsDilationAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, ConvolutionOpV1::getLhsDilationAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ConvolutionOpV1GenericAdaptorBase::getLhsDilation() {
  auto attr = getLhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getRhsDilationAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, ConvolutionOpV1::getRhsDilationAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ConvolutionOpV1GenericAdaptorBase::getRhsDilation() {
  auto attr = getRhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getWindowReversalAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, ConvolutionOpV1::getWindowReversalAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ConvolutionOpV1GenericAdaptorBase::getWindowReversal() {
  auto attr = getWindowReversalAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getDimensionNumbersAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, ConvolutionOpV1::getDimensionNumbersAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getFeatureGroupCountAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, ConvolutionOpV1::getFeatureGroupCountAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getFeatureGroupCount() {
  auto attr = getFeatureGroupCountAttr();
  return attr;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getBatchGroupCountAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, ConvolutionOpV1::getBatchGroupCountAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getBatchGroupCount() {
  auto attr = getBatchGroupCountAttr();
  return attr;
}

::mlir::Attribute ConvolutionOpV1GenericAdaptorBase::getPrecisionConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, ConvolutionOpV1::getPrecisionConfigAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ConvolutionOpV1GenericAdaptorBase::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
ConvolutionOpV1Adaptor::ConvolutionOpV1Adaptor(ConvolutionOpV1 op) : ConvolutionOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ConvolutionOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_batch_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.convolution' op ""requires attribute 'batch_group_count'");
    if (namedAttrIt->getName() == ConvolutionOpV1::getBatchGroupCountAttrName(*odsOpName)) {
      tblgen_batch_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.convolution' op ""requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == ConvolutionOpV1::getDimensionNumbersAttrName(*odsOpName)) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.convolution' op ""requires attribute 'feature_group_count'");
    if (namedAttrIt->getName() == ConvolutionOpV1::getFeatureGroupCountAttrName(*odsOpName)) {
      tblgen_feature_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_lhs_dilation;
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_precision_config;
  ::mlir::Attribute tblgen_rhs_dilation;
  ::mlir::Attribute tblgen_window_reversal;
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == ConvolutionOpV1::getLhsDilationAttrName(*odsOpName)) {
      tblgen_lhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ConvolutionOpV1::getPaddingAttrName(*odsOpName)) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ConvolutionOpV1::getPrecisionConfigAttrName(*odsOpName)) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ConvolutionOpV1::getRhsDilationAttrName(*odsOpName)) {
      tblgen_rhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ConvolutionOpV1::getWindowReversalAttrName(*odsOpName)) {
      tblgen_window_reversal = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ConvolutionOpV1::getWindowStridesAttrName(*odsOpName)) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_window_strides && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'window_strides' failed to satisfy constraint: any attribute");

  if (tblgen_padding && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'padding' failed to satisfy constraint: any attribute");

  if (tblgen_lhs_dilation && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'lhs_dilation' failed to satisfy constraint: any attribute");

  if (tblgen_rhs_dilation && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'rhs_dilation' failed to satisfy constraint: any attribute");

  if (tblgen_window_reversal && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'window_reversal' failed to satisfy constraint: any attribute");

  if (tblgen_dimension_numbers && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'dimension_numbers' failed to satisfy constraint: any attribute");

  if (tblgen_feature_group_count && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'feature_group_count' failed to satisfy constraint: any attribute");

  if (tblgen_batch_group_count && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'batch_group_count' failed to satisfy constraint: any attribute");

  if (tblgen_precision_config && !((true)))
    return emitError(loc, "'vhlo.convolution' op ""attribute 'precision_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ConvolutionOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ConvolutionOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ConvolutionOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ConvolutionOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange ConvolutionOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ConvolutionOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ConvolutionOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ConvolutionOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute ConvolutionOpV1::getWindowStridesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getWindowStridesAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ConvolutionOpV1::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1::getPaddingAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getPaddingAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ConvolutionOpV1::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1::getLhsDilationAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getLhsDilationAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ConvolutionOpV1::getLhsDilation() {
  auto attr = getLhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1::getRhsDilationAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getRhsDilationAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ConvolutionOpV1::getRhsDilation() {
  auto attr = getRhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1::getWindowReversalAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getWindowReversalAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ConvolutionOpV1::getWindowReversal() {
  auto attr = getWindowReversalAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ConvolutionOpV1::getDimensionNumbersAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getDimensionNumbersAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ConvolutionOpV1::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute ConvolutionOpV1::getFeatureGroupCountAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getFeatureGroupCountAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ConvolutionOpV1::getFeatureGroupCount() {
  auto attr = getFeatureGroupCountAttr();
  return attr;
}

::mlir::Attribute ConvolutionOpV1::getBatchGroupCountAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getBatchGroupCountAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ConvolutionOpV1::getBatchGroupCount() {
  auto attr = getBatchGroupCountAttr();
  return attr;
}

::mlir::Attribute ConvolutionOpV1::getPrecisionConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getPrecisionConfigAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ConvolutionOpV1::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void ConvolutionOpV1::setWindowStridesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowStridesAttrName(), attr);
}

void ConvolutionOpV1::setPaddingAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPaddingAttrName(), attr);
}

void ConvolutionOpV1::setLhsDilationAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLhsDilationAttrName(), attr);
}

void ConvolutionOpV1::setRhsDilationAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getRhsDilationAttrName(), attr);
}

void ConvolutionOpV1::setWindowReversalAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowReversalAttrName(), attr);
}

void ConvolutionOpV1::setDimensionNumbersAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionNumbersAttrName(), attr);
}

void ConvolutionOpV1::setFeatureGroupCountAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFeatureGroupCountAttrName(), attr);
}

void ConvolutionOpV1::setBatchGroupCountAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBatchGroupCountAttrName(), attr);
}

void ConvolutionOpV1::setPrecisionConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPrecisionConfigAttrName(), attr);
}

::mlir::Attribute ConvolutionOpV1::removeWindowStridesAttr() {
  return (*this)->removeAttr(getWindowStridesAttrName());
}

::mlir::Attribute ConvolutionOpV1::removePaddingAttr() {
  return (*this)->removeAttr(getPaddingAttrName());
}

::mlir::Attribute ConvolutionOpV1::removeLhsDilationAttr() {
  return (*this)->removeAttr(getLhsDilationAttrName());
}

::mlir::Attribute ConvolutionOpV1::removeRhsDilationAttr() {
  return (*this)->removeAttr(getRhsDilationAttrName());
}

::mlir::Attribute ConvolutionOpV1::removeWindowReversalAttr() {
  return (*this)->removeAttr(getWindowReversalAttrName());
}

::mlir::Attribute ConvolutionOpV1::removePrecisionConfigAttr() {
  return (*this)->removeAttr(getPrecisionConfigAttrName());
}

void ConvolutionOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value lhs, ::mlir::Value rhs, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute padding, /*optional*/::mlir::Attribute lhs_dilation, /*optional*/::mlir::Attribute rhs_dilation, /*optional*/::mlir::Attribute window_reversal, ::mlir::Attribute dimension_numbers, ::mlir::Attribute feature_group_count, ::mlir::Attribute batch_group_count, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  if (lhs_dilation) {
    odsState.addAttribute(getLhsDilationAttrName(odsState.name), lhs_dilation);
  }
  if (rhs_dilation) {
    odsState.addAttribute(getRhsDilationAttrName(odsState.name), rhs_dilation);
  }
  if (window_reversal) {
    odsState.addAttribute(getWindowReversalAttrName(odsState.name), window_reversal);
  }
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  odsState.addAttribute(getFeatureGroupCountAttrName(odsState.name), feature_group_count);
  odsState.addAttribute(getBatchGroupCountAttrName(odsState.name), batch_group_count);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  odsState.addTypes(resultType0);
}

void ConvolutionOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute padding, /*optional*/::mlir::Attribute lhs_dilation, /*optional*/::mlir::Attribute rhs_dilation, /*optional*/::mlir::Attribute window_reversal, ::mlir::Attribute dimension_numbers, ::mlir::Attribute feature_group_count, ::mlir::Attribute batch_group_count, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  if (lhs_dilation) {
    odsState.addAttribute(getLhsDilationAttrName(odsState.name), lhs_dilation);
  }
  if (rhs_dilation) {
    odsState.addAttribute(getRhsDilationAttrName(odsState.name), rhs_dilation);
  }
  if (window_reversal) {
    odsState.addAttribute(getWindowReversalAttrName(odsState.name), window_reversal);
  }
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  odsState.addAttribute(getFeatureGroupCountAttrName(odsState.name), feature_group_count);
  odsState.addAttribute(getBatchGroupCountAttrName(odsState.name), batch_group_count);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ConvolutionOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ConvolutionOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_batch_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'batch_group_count'");
    if (namedAttrIt->getName() == getBatchGroupCountAttrName()) {
      tblgen_batch_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == getDimensionNumbersAttrName()) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'feature_group_count'");
    if (namedAttrIt->getName() == getFeatureGroupCountAttrName()) {
      tblgen_feature_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_lhs_dilation;
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_precision_config;
  ::mlir::Attribute tblgen_rhs_dilation;
  ::mlir::Attribute tblgen_window_reversal;
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getLhsDilationAttrName()) {
      tblgen_lhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getPaddingAttrName()) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getPrecisionConfigAttrName()) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getRhsDilationAttrName()) {
      tblgen_rhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowReversalAttrName()) {
      tblgen_window_reversal = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowStridesAttrName()) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_strides, "window_strides")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_padding, "padding")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_lhs_dilation, "lhs_dilation")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_rhs_dilation, "rhs_dilation")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_reversal, "window_reversal")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension_numbers, "dimension_numbers")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_feature_group_count, "feature_group_count")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_batch_group_count, "batch_group_count")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_precision_config, "precision_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ConvolutionOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ConvolutionOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in convolution");
  return *version;
}
mlir::vhlo::Version ConvolutionOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in convolution");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ConvolutionOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CosineOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CosineOpV1GenericAdaptorBase::CosineOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.cosine", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CosineOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CosineOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
CosineOpV1Adaptor::CosineOpV1Adaptor(CosineOpV1 op) : CosineOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CosineOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CosineOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CosineOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CosineOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CosineOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CosineOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CosineOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CosineOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void CosineOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void CosineOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CosineOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CosineOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CosineOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CosineOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in cosine");
  return *version;
}
mlir::vhlo::Version CosineOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in cosine");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CosineOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CreateTokenOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CreateTokenOpV1GenericAdaptorBase::CreateTokenOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.create_token", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CreateTokenOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CreateTokenOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
CreateTokenOpV1Adaptor::CreateTokenOpV1Adaptor(CreateTokenOpV1 op) : CreateTokenOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CreateTokenOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CreateTokenOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CreateTokenOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> CreateTokenOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CreateTokenOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CreateTokenOpV1::getOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void CreateTokenOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type output) {
  odsState.addTypes(output);
}

void CreateTokenOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes) {
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CreateTokenOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CreateTokenOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CreateTokenOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CreateTokenOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in create_token");
  return *version;
}
mlir::vhlo::Version CreateTokenOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in create_token");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CreateTokenOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CrossReplicaSumOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CrossReplicaSumOpV1GenericAdaptorBase::CrossReplicaSumOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.cross-replica-sum", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CrossReplicaSumOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CrossReplicaSumOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CrossReplicaSumOpV1GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, CrossReplicaSumOpV1::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CrossReplicaSumOpV1GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

} // namespace detail
CrossReplicaSumOpV1Adaptor::CrossReplicaSumOpV1Adaptor(CrossReplicaSumOpV1 op) : CrossReplicaSumOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CrossReplicaSumOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_replica_groups;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.cross-replica-sum' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == CrossReplicaSumOpV1::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.cross-replica-sum' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CrossReplicaSumOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CrossReplicaSumOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CrossReplicaSumOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange CrossReplicaSumOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CrossReplicaSumOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CrossReplicaSumOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute CrossReplicaSumOpV1::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CrossReplicaSumOpV1::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

void CrossReplicaSumOpV1::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void CrossReplicaSumOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute replica_groups) {
  odsState.addOperands(operand);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  odsState.addTypes(resultType0);
}

void CrossReplicaSumOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute replica_groups) {
  odsState.addOperands(operand);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CrossReplicaSumOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CrossReplicaSumOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_replica_groups;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CrossReplicaSumOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CrossReplicaSumOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in cross-replica-sum");
  return *version;
}
mlir::vhlo::Version CrossReplicaSumOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in cross-replica-sum");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CrossReplicaSumOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CstrReshapableOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CstrReshapableOpV1GenericAdaptorBase::CstrReshapableOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.cstr_reshapable", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CstrReshapableOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr CstrReshapableOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
CstrReshapableOpV1Adaptor::CstrReshapableOpV1Adaptor(CstrReshapableOpV1 op) : CstrReshapableOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CstrReshapableOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CstrReshapableOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range CstrReshapableOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CstrReshapableOpV1::getNumElements() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value CstrReshapableOpV1::getDynamicShape() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange CstrReshapableOpV1::getNumElementsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange CstrReshapableOpV1::getDynamicShapeMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CstrReshapableOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range CstrReshapableOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value CstrReshapableOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void CstrReshapableOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value num_elements, ::mlir::Value dynamic_shape) {
  odsState.addOperands(num_elements);
  odsState.addOperands(dynamic_shape);
  odsState.addTypes(result);
}

void CstrReshapableOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value num_elements, ::mlir::Value dynamic_shape) {
  odsState.addOperands(num_elements);
  odsState.addOperands(dynamic_shape);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void CstrReshapableOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CstrReshapableOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CstrReshapableOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CstrReshapableOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in cstr_reshapable");
  return *version;
}
mlir::vhlo::Version CstrReshapableOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in cstr_reshapable");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CstrReshapableOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CustomCallOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CustomCallOpV1GenericAdaptorBase::CustomCallOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.custom_call", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CustomCallOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr CustomCallOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getCallTargetNameAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, CustomCallOpV1::getCallTargetNameAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getCallTargetName() {
  auto attr = getCallTargetNameAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getHasSideEffectAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV1::getHasSideEffectAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV1GenericAdaptorBase::getHasSideEffect() {
  auto attr = getHasSideEffectAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getBackendConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, CustomCallOpV1::getBackendConfigAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getBackendConfig() {
  auto attr = getBackendConfigAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getApiVersionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, CustomCallOpV1::getApiVersionAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV1GenericAdaptorBase::getApiVersion() {
  auto attr = getApiVersionAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getCalledComputationsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV1::getCalledComputationsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV1GenericAdaptorBase::getCalledComputations() {
  auto attr = getCalledComputationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getOperandLayoutsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV1::getOperandLayoutsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV1GenericAdaptorBase::getOperandLayouts() {
  auto attr = getOperandLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1GenericAdaptorBase::getResultLayoutsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV1::getResultLayoutsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV1GenericAdaptorBase::getResultLayouts() {
  auto attr = getResultLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
CustomCallOpV1Adaptor::CustomCallOpV1Adaptor(CustomCallOpV1 op) : CustomCallOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CustomCallOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_backend_config;
  ::mlir::Attribute tblgen_api_version;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.custom_call' op ""requires attribute 'backend_config'");
    if (namedAttrIt->getName() == CustomCallOpV1::getBackendConfigAttrName(*odsOpName)) {
      tblgen_backend_config = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == CustomCallOpV1::getApiVersionAttrName(*odsOpName)) {
      tblgen_api_version = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_call_target_name;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.custom_call' op ""requires attribute 'call_target_name'");
    if (namedAttrIt->getName() == CustomCallOpV1::getCallTargetNameAttrName(*odsOpName)) {
      tblgen_call_target_name = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_called_computations;
  ::mlir::Attribute tblgen_has_side_effect;
  ::mlir::Attribute tblgen_operand_layouts;
  ::mlir::Attribute tblgen_result_layouts;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == CustomCallOpV1::getCalledComputationsAttrName(*odsOpName)) {
      tblgen_called_computations = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV1::getHasSideEffectAttrName(*odsOpName)) {
      tblgen_has_side_effect = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV1::getOperandLayoutsAttrName(*odsOpName)) {
      tblgen_operand_layouts = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV1::getResultLayoutsAttrName(*odsOpName)) {
      tblgen_result_layouts = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_call_target_name && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'call_target_name' failed to satisfy constraint: any attribute");

  if (tblgen_has_side_effect && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'has_side_effect' failed to satisfy constraint: any attribute");

  if (tblgen_backend_config && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'backend_config' failed to satisfy constraint: any attribute");

  if (tblgen_api_version && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'api_version' failed to satisfy constraint: any attribute");

  if (tblgen_called_computations && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'called_computations' failed to satisfy constraint: any attribute");

  if (tblgen_operand_layouts && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'operand_layouts' failed to satisfy constraint: any attribute");

  if (tblgen_result_layouts && !((true)))
    return emitError(loc, "'vhlo.custom_call' op ""attribute 'result_layouts' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CustomCallOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range CustomCallOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range CustomCallOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange CustomCallOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CustomCallOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range CustomCallOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute CustomCallOpV1::getCallTargetNameAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getCallTargetNameAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CustomCallOpV1::getCallTargetName() {
  auto attr = getCallTargetNameAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV1::getHasSideEffectAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getHasSideEffectAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV1::getHasSideEffect() {
  auto attr = getHasSideEffectAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1::getBackendConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getBackendConfigAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CustomCallOpV1::getBackendConfig() {
  auto attr = getBackendConfigAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV1::getApiVersionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getApiVersionAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV1::getApiVersion() {
  auto attr = getApiVersionAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1::getCalledComputationsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getCalledComputationsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV1::getCalledComputations() {
  auto attr = getCalledComputationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1::getOperandLayoutsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getOperandLayoutsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV1::getOperandLayouts() {
  auto attr = getOperandLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV1::getResultLayoutsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getResultLayoutsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV1::getResultLayouts() {
  auto attr = getResultLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void CustomCallOpV1::setCallTargetNameAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getCallTargetNameAttrName(), attr);
}

void CustomCallOpV1::setHasSideEffectAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getHasSideEffectAttrName(), attr);
}

void CustomCallOpV1::setBackendConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBackendConfigAttrName(), attr);
}

void CustomCallOpV1::setApiVersionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getApiVersionAttrName(), attr);
}

void CustomCallOpV1::setCalledComputationsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getCalledComputationsAttrName(), attr);
}

void CustomCallOpV1::setOperandLayoutsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getOperandLayoutsAttrName(), attr);
}

void CustomCallOpV1::setResultLayoutsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getResultLayoutsAttrName(), attr);
}

::mlir::Attribute CustomCallOpV1::removeHasSideEffectAttr() {
  return (*this)->removeAttr(getHasSideEffectAttrName());
}

::mlir::Attribute CustomCallOpV1::removeApiVersionAttr() {
  return (*this)->removeAttr(getApiVersionAttrName());
}

::mlir::Attribute CustomCallOpV1::removeCalledComputationsAttr() {
  return (*this)->removeAttr(getCalledComputationsAttrName());
}

::mlir::Attribute CustomCallOpV1::removeOperandLayoutsAttr() {
  return (*this)->removeAttr(getOperandLayoutsAttrName());
}

::mlir::Attribute CustomCallOpV1::removeResultLayoutsAttr() {
  return (*this)->removeAttr(getResultLayoutsAttrName());
}

void CustomCallOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::ValueRange inputs, ::mlir::Attribute call_target_name, /*optional*/::mlir::Attribute has_side_effect, ::mlir::Attribute backend_config, /*optional*/::mlir::Attribute api_version, /*optional*/::mlir::Attribute called_computations, /*optional*/::mlir::Attribute operand_layouts, /*optional*/::mlir::Attribute result_layouts) {
  odsState.addOperands(inputs);
  odsState.addAttribute(getCallTargetNameAttrName(odsState.name), call_target_name);
  if (has_side_effect) {
    odsState.addAttribute(getHasSideEffectAttrName(odsState.name), has_side_effect);
  }
  odsState.addAttribute(getBackendConfigAttrName(odsState.name), backend_config);
  if (api_version) {
    odsState.addAttribute(getApiVersionAttrName(odsState.name), api_version);
  }
  if (called_computations) {
    odsState.addAttribute(getCalledComputationsAttrName(odsState.name), called_computations);
  }
  if (operand_layouts) {
    odsState.addAttribute(getOperandLayoutsAttrName(odsState.name), operand_layouts);
  }
  if (result_layouts) {
    odsState.addAttribute(getResultLayoutsAttrName(odsState.name), result_layouts);
  }
  odsState.addTypes(resultType0);
}

void CustomCallOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CustomCallOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_backend_config;
  ::mlir::Attribute tblgen_api_version;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'backend_config'");
    if (namedAttrIt->getName() == getBackendConfigAttrName()) {
      tblgen_backend_config = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getApiVersionAttrName()) {
      tblgen_api_version = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_call_target_name;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'call_target_name'");
    if (namedAttrIt->getName() == getCallTargetNameAttrName()) {
      tblgen_call_target_name = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_called_computations;
  ::mlir::Attribute tblgen_has_side_effect;
  ::mlir::Attribute tblgen_operand_layouts;
  ::mlir::Attribute tblgen_result_layouts;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getCalledComputationsAttrName()) {
      tblgen_called_computations = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getHasSideEffectAttrName()) {
      tblgen_has_side_effect = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getOperandLayoutsAttrName()) {
      tblgen_operand_layouts = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getResultLayoutsAttrName()) {
      tblgen_result_layouts = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_call_target_name, "call_target_name")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_has_side_effect, "has_side_effect")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_backend_config, "backend_config")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_api_version, "api_version")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_called_computations, "called_computations")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_operand_layouts, "operand_layouts")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_result_layouts, "result_layouts")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CustomCallOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CustomCallOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in custom_call");
  return *version;
}
mlir::vhlo::Version CustomCallOpV1::getMaxVersion() {
  if (!strcmp("0.3.0", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in custom_call");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CustomCallOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::CustomCallOpV2 definitions
//===----------------------------------------------------------------------===//

namespace detail {
CustomCallOpV2GenericAdaptorBase::CustomCallOpV2GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.custom_call_v2", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> CustomCallOpV2GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr CustomCallOpV2GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getCallTargetNameAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, CustomCallOpV2::getCallTargetNameAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getCallTargetName() {
  auto attr = getCallTargetNameAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getHasSideEffectAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV2::getHasSideEffectAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV2GenericAdaptorBase::getHasSideEffect() {
  auto attr = getHasSideEffectAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getBackendConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, CustomCallOpV2::getBackendConfigAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getBackendConfig() {
  auto attr = getBackendConfigAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getApiVersionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, CustomCallOpV2::getApiVersionAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV2GenericAdaptorBase::getApiVersion() {
  auto attr = getApiVersionAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getCalledComputationsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV2::getCalledComputationsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV2GenericAdaptorBase::getCalledComputations() {
  auto attr = getCalledComputationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getOperandLayoutsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV2::getOperandLayoutsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV2GenericAdaptorBase::getOperandLayouts() {
  auto attr = getOperandLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getResultLayoutsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV2::getResultLayoutsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV2GenericAdaptorBase::getResultLayouts() {
  auto attr = getResultLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2GenericAdaptorBase::getOutputOperandAliasesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, CustomCallOpV2::getOutputOperandAliasesAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> CustomCallOpV2GenericAdaptorBase::getOutputOperandAliases() {
  auto attr = getOutputOperandAliasesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
CustomCallOpV2Adaptor::CustomCallOpV2Adaptor(CustomCallOpV2 op) : CustomCallOpV2Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult CustomCallOpV2Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_backend_config;
  ::mlir::Attribute tblgen_api_version;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.custom_call_v2' op ""requires attribute 'backend_config'");
    if (namedAttrIt->getName() == CustomCallOpV2::getBackendConfigAttrName(*odsOpName)) {
      tblgen_backend_config = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == CustomCallOpV2::getApiVersionAttrName(*odsOpName)) {
      tblgen_api_version = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_call_target_name;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.custom_call_v2' op ""requires attribute 'call_target_name'");
    if (namedAttrIt->getName() == CustomCallOpV2::getCallTargetNameAttrName(*odsOpName)) {
      tblgen_call_target_name = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_called_computations;
  ::mlir::Attribute tblgen_has_side_effect;
  ::mlir::Attribute tblgen_operand_layouts;
  ::mlir::Attribute tblgen_output_operand_aliases;
  ::mlir::Attribute tblgen_result_layouts;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == CustomCallOpV2::getCalledComputationsAttrName(*odsOpName)) {
      tblgen_called_computations = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV2::getHasSideEffectAttrName(*odsOpName)) {
      tblgen_has_side_effect = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV2::getOperandLayoutsAttrName(*odsOpName)) {
      tblgen_operand_layouts = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV2::getOutputOperandAliasesAttrName(*odsOpName)) {
      tblgen_output_operand_aliases = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == CustomCallOpV2::getResultLayoutsAttrName(*odsOpName)) {
      tblgen_result_layouts = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_call_target_name && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'call_target_name' failed to satisfy constraint: any attribute");

  if (tblgen_has_side_effect && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'has_side_effect' failed to satisfy constraint: any attribute");

  if (tblgen_backend_config && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'backend_config' failed to satisfy constraint: any attribute");

  if (tblgen_api_version && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'api_version' failed to satisfy constraint: any attribute");

  if (tblgen_called_computations && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'called_computations' failed to satisfy constraint: any attribute");

  if (tblgen_operand_layouts && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'operand_layouts' failed to satisfy constraint: any attribute");

  if (tblgen_result_layouts && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'result_layouts' failed to satisfy constraint: any attribute");

  if (tblgen_output_operand_aliases && !((true)))
    return emitError(loc, "'vhlo.custom_call_v2' op ""attribute 'output_operand_aliases' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> CustomCallOpV2::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range CustomCallOpV2::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range CustomCallOpV2::getInputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange CustomCallOpV2::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> CustomCallOpV2::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range CustomCallOpV2::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute CustomCallOpV2::getCallTargetNameAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getCallTargetNameAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CustomCallOpV2::getCallTargetName() {
  auto attr = getCallTargetNameAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV2::getHasSideEffectAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getHasSideEffectAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV2::getHasSideEffect() {
  auto attr = getHasSideEffectAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2::getBackendConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getBackendConfigAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute CustomCallOpV2::getBackendConfig() {
  auto attr = getBackendConfigAttr();
  return attr;
}

::mlir::Attribute CustomCallOpV2::getApiVersionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getApiVersionAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV2::getApiVersion() {
  auto attr = getApiVersionAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2::getCalledComputationsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getCalledComputationsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV2::getCalledComputations() {
  auto attr = getCalledComputationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2::getOperandLayoutsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getOperandLayoutsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV2::getOperandLayouts() {
  auto attr = getOperandLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2::getResultLayoutsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getResultLayoutsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV2::getResultLayouts() {
  auto attr = getResultLayoutsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute CustomCallOpV2::getOutputOperandAliasesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getOutputOperandAliasesAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> CustomCallOpV2::getOutputOperandAliases() {
  auto attr = getOutputOperandAliasesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void CustomCallOpV2::setCallTargetNameAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getCallTargetNameAttrName(), attr);
}

void CustomCallOpV2::setHasSideEffectAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getHasSideEffectAttrName(), attr);
}

void CustomCallOpV2::setBackendConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBackendConfigAttrName(), attr);
}

void CustomCallOpV2::setApiVersionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getApiVersionAttrName(), attr);
}

void CustomCallOpV2::setCalledComputationsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getCalledComputationsAttrName(), attr);
}

void CustomCallOpV2::setOperandLayoutsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getOperandLayoutsAttrName(), attr);
}

void CustomCallOpV2::setResultLayoutsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getResultLayoutsAttrName(), attr);
}

void CustomCallOpV2::setOutputOperandAliasesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getOutputOperandAliasesAttrName(), attr);
}

::mlir::Attribute CustomCallOpV2::removeHasSideEffectAttr() {
  return (*this)->removeAttr(getHasSideEffectAttrName());
}

::mlir::Attribute CustomCallOpV2::removeApiVersionAttr() {
  return (*this)->removeAttr(getApiVersionAttrName());
}

::mlir::Attribute CustomCallOpV2::removeCalledComputationsAttr() {
  return (*this)->removeAttr(getCalledComputationsAttrName());
}

::mlir::Attribute CustomCallOpV2::removeOperandLayoutsAttr() {
  return (*this)->removeAttr(getOperandLayoutsAttrName());
}

::mlir::Attribute CustomCallOpV2::removeResultLayoutsAttr() {
  return (*this)->removeAttr(getResultLayoutsAttrName());
}

::mlir::Attribute CustomCallOpV2::removeOutputOperandAliasesAttr() {
  return (*this)->removeAttr(getOutputOperandAliasesAttrName());
}

void CustomCallOpV2::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::ValueRange inputs, ::mlir::Attribute call_target_name, /*optional*/::mlir::Attribute has_side_effect, ::mlir::Attribute backend_config, /*optional*/::mlir::Attribute api_version, /*optional*/::mlir::Attribute called_computations, /*optional*/::mlir::Attribute operand_layouts, /*optional*/::mlir::Attribute result_layouts, /*optional*/::mlir::Attribute output_operand_aliases) {
  odsState.addOperands(inputs);
  odsState.addAttribute(getCallTargetNameAttrName(odsState.name), call_target_name);
  if (has_side_effect) {
    odsState.addAttribute(getHasSideEffectAttrName(odsState.name), has_side_effect);
  }
  odsState.addAttribute(getBackendConfigAttrName(odsState.name), backend_config);
  if (api_version) {
    odsState.addAttribute(getApiVersionAttrName(odsState.name), api_version);
  }
  if (called_computations) {
    odsState.addAttribute(getCalledComputationsAttrName(odsState.name), called_computations);
  }
  if (operand_layouts) {
    odsState.addAttribute(getOperandLayoutsAttrName(odsState.name), operand_layouts);
  }
  if (result_layouts) {
    odsState.addAttribute(getResultLayoutsAttrName(odsState.name), result_layouts);
  }
  if (output_operand_aliases) {
    odsState.addAttribute(getOutputOperandAliasesAttrName(odsState.name), output_operand_aliases);
  }
  odsState.addTypes(resultType0);
}

void CustomCallOpV2::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult CustomCallOpV2::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_backend_config;
  ::mlir::Attribute tblgen_api_version;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'backend_config'");
    if (namedAttrIt->getName() == getBackendConfigAttrName()) {
      tblgen_backend_config = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getApiVersionAttrName()) {
      tblgen_api_version = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_call_target_name;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'call_target_name'");
    if (namedAttrIt->getName() == getCallTargetNameAttrName()) {
      tblgen_call_target_name = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_called_computations;
  ::mlir::Attribute tblgen_has_side_effect;
  ::mlir::Attribute tblgen_operand_layouts;
  ::mlir::Attribute tblgen_output_operand_aliases;
  ::mlir::Attribute tblgen_result_layouts;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getCalledComputationsAttrName()) {
      tblgen_called_computations = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getHasSideEffectAttrName()) {
      tblgen_has_side_effect = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getOperandLayoutsAttrName()) {
      tblgen_operand_layouts = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getOutputOperandAliasesAttrName()) {
      tblgen_output_operand_aliases = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getResultLayoutsAttrName()) {
      tblgen_result_layouts = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_call_target_name, "call_target_name")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_has_side_effect, "has_side_effect")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_backend_config, "backend_config")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_api_version, "api_version")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_called_computations, "called_computations")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_operand_layouts, "operand_layouts")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_result_layouts, "result_layouts")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_output_operand_aliases, "output_operand_aliases")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult CustomCallOpV2::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version CustomCallOpV2::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.4.0");
  if (failed(version)) llvm_unreachable("invalid version 0.4.0 in custom_call_v2");
  return *version;
}
mlir::vhlo::Version CustomCallOpV2::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in custom_call_v2");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::CustomCallOpV2)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DivOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DivOpV1GenericAdaptorBase::DivOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.divide", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DivOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DivOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
DivOpV1Adaptor::DivOpV1Adaptor(DivOpV1 op) : DivOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DivOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DivOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DivOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DivOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DivOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange DivOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DivOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DivOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DivOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DivOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void DivOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void DivOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DivOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DivOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DivOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DivOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in divide");
  return *version;
}
mlir::vhlo::Version DivOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in divide");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DivOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DotGeneralOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DotGeneralOpV1GenericAdaptorBase::DotGeneralOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dot_general", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DotGeneralOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DotGeneralOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DotGeneralOpV1GenericAdaptorBase::getDotDimensionNumbersAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, DotGeneralOpV1::getDotDimensionNumbersAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DotGeneralOpV1GenericAdaptorBase::getDotDimensionNumbers() {
  auto attr = getDotDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute DotGeneralOpV1GenericAdaptorBase::getPrecisionConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, DotGeneralOpV1::getPrecisionConfigAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DotGeneralOpV1GenericAdaptorBase::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
DotGeneralOpV1Adaptor::DotGeneralOpV1Adaptor(DotGeneralOpV1 op) : DotGeneralOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DotGeneralOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dot_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dot_general' op ""requires attribute 'dot_dimension_numbers'");
    if (namedAttrIt->getName() == DotGeneralOpV1::getDotDimensionNumbersAttrName(*odsOpName)) {
      tblgen_dot_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_precision_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == DotGeneralOpV1::getPrecisionConfigAttrName(*odsOpName)) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_dot_dimension_numbers && !((true)))
    return emitError(loc, "'vhlo.dot_general' op ""attribute 'dot_dimension_numbers' failed to satisfy constraint: any attribute");

  if (tblgen_precision_config && !((true)))
    return emitError(loc, "'vhlo.dot_general' op ""attribute 'precision_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DotGeneralOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DotGeneralOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DotGeneralOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DotGeneralOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange DotGeneralOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DotGeneralOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DotGeneralOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DotGeneralOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute DotGeneralOpV1::getDotDimensionNumbersAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDotDimensionNumbersAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DotGeneralOpV1::getDotDimensionNumbers() {
  auto attr = getDotDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute DotGeneralOpV1::getPrecisionConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getPrecisionConfigAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DotGeneralOpV1::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void DotGeneralOpV1::setDotDimensionNumbersAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDotDimensionNumbersAttrName(), attr);
}

void DotGeneralOpV1::setPrecisionConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPrecisionConfigAttrName(), attr);
}

::mlir::Attribute DotGeneralOpV1::removePrecisionConfigAttr() {
  return (*this)->removeAttr(getPrecisionConfigAttrName());
}

void DotGeneralOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Attribute dot_dimension_numbers, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addAttribute(getDotDimensionNumbersAttrName(odsState.name), dot_dimension_numbers);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  odsState.addTypes(resultType0);
}

void DotGeneralOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Attribute dot_dimension_numbers, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addAttribute(getDotDimensionNumbersAttrName(odsState.name), dot_dimension_numbers);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DotGeneralOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DotGeneralOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dot_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dot_dimension_numbers'");
    if (namedAttrIt->getName() == getDotDimensionNumbersAttrName()) {
      tblgen_dot_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_precision_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getPrecisionConfigAttrName()) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dot_dimension_numbers, "dot_dimension_numbers")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_precision_config, "precision_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DotGeneralOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DotGeneralOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dot_general");
  return *version;
}
mlir::vhlo::Version DotGeneralOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dot_general");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DotGeneralOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DotOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DotOpV1GenericAdaptorBase::DotOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dot", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DotOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DotOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DotOpV1GenericAdaptorBase::getPrecisionConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, DotOpV1::getPrecisionConfigAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DotOpV1GenericAdaptorBase::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
DotOpV1Adaptor::DotOpV1Adaptor(DotOpV1 op) : DotOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DotOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_precision_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == DotOpV1::getPrecisionConfigAttrName(*odsOpName)) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_precision_config && !((true)))
    return emitError(loc, "'vhlo.dot' op ""attribute 'precision_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DotOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DotOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DotOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DotOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange DotOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DotOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DotOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DotOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute DotOpV1::getPrecisionConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getPrecisionConfigAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DotOpV1::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void DotOpV1::setPrecisionConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPrecisionConfigAttrName(), attr);
}

::mlir::Attribute DotOpV1::removePrecisionConfigAttr() {
  return (*this)->removeAttr(getPrecisionConfigAttrName());
}

void DotOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value lhs, ::mlir::Value rhs, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  odsState.addTypes(resultType0);
}

void DotOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DotOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DotOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_precision_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getPrecisionConfigAttrName()) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_precision_config, "precision_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DotOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DotOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dot");
  return *version;
}
mlir::vhlo::Version DotOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dot");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DotOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicBroadcastInDimOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicBroadcastInDimOpV1GenericAdaptorBase::DynamicBroadcastInDimOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_broadcast_in_dim", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicBroadcastInDimOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DynamicBroadcastInDimOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DynamicBroadcastInDimOpV1GenericAdaptorBase::getBroadcastDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, DynamicBroadcastInDimOpV1::getBroadcastDimensionsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicBroadcastInDimOpV1GenericAdaptorBase::getBroadcastDimensions() {
  auto attr = getBroadcastDimensionsAttr();
  return attr;
}

::mlir::Attribute DynamicBroadcastInDimOpV1GenericAdaptorBase::getKnownExpandingDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, DynamicBroadcastInDimOpV1::getKnownExpandingDimensionsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicBroadcastInDimOpV1GenericAdaptorBase::getKnownExpandingDimensions() {
  auto attr = getKnownExpandingDimensionsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicBroadcastInDimOpV1GenericAdaptorBase::getKnownNonexpandingDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, DynamicBroadcastInDimOpV1::getKnownNonexpandingDimensionsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicBroadcastInDimOpV1GenericAdaptorBase::getKnownNonexpandingDimensions() {
  auto attr = getKnownNonexpandingDimensionsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
DynamicBroadcastInDimOpV1Adaptor::DynamicBroadcastInDimOpV1Adaptor(DynamicBroadcastInDimOpV1 op) : DynamicBroadcastInDimOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicBroadcastInDimOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_broadcast_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_broadcast_in_dim' op ""requires attribute 'broadcast_dimensions'");
    if (namedAttrIt->getName() == DynamicBroadcastInDimOpV1::getBroadcastDimensionsAttrName(*odsOpName)) {
      tblgen_broadcast_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_known_expanding_dimensions;
  ::mlir::Attribute tblgen_known_nonexpanding_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == DynamicBroadcastInDimOpV1::getKnownExpandingDimensionsAttrName(*odsOpName)) {
      tblgen_known_expanding_dimensions = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == DynamicBroadcastInDimOpV1::getKnownNonexpandingDimensionsAttrName(*odsOpName)) {
      tblgen_known_nonexpanding_dimensions = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_broadcast_dimensions && !((true)))
    return emitError(loc, "'vhlo.dynamic_broadcast_in_dim' op ""attribute 'broadcast_dimensions' failed to satisfy constraint: any attribute");

  if (tblgen_known_expanding_dimensions && !((true)))
    return emitError(loc, "'vhlo.dynamic_broadcast_in_dim' op ""attribute 'known_expanding_dimensions' failed to satisfy constraint: any attribute");

  if (tblgen_known_nonexpanding_dimensions && !((true)))
    return emitError(loc, "'vhlo.dynamic_broadcast_in_dim' op ""attribute 'known_nonexpanding_dimensions' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicBroadcastInDimOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DynamicBroadcastInDimOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicBroadcastInDimOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DynamicBroadcastInDimOpV1::getOutputDimensions() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange DynamicBroadcastInDimOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicBroadcastInDimOpV1::getOutputDimensionsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicBroadcastInDimOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicBroadcastInDimOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute DynamicBroadcastInDimOpV1::getBroadcastDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getBroadcastDimensionsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicBroadcastInDimOpV1::getBroadcastDimensions() {
  auto attr = getBroadcastDimensionsAttr();
  return attr;
}

::mlir::Attribute DynamicBroadcastInDimOpV1::getKnownExpandingDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getKnownExpandingDimensionsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicBroadcastInDimOpV1::getKnownExpandingDimensions() {
  auto attr = getKnownExpandingDimensionsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicBroadcastInDimOpV1::getKnownNonexpandingDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getKnownNonexpandingDimensionsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicBroadcastInDimOpV1::getKnownNonexpandingDimensions() {
  auto attr = getKnownNonexpandingDimensionsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void DynamicBroadcastInDimOpV1::setBroadcastDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBroadcastDimensionsAttrName(), attr);
}

void DynamicBroadcastInDimOpV1::setKnownExpandingDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getKnownExpandingDimensionsAttrName(), attr);
}

void DynamicBroadcastInDimOpV1::setKnownNonexpandingDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getKnownNonexpandingDimensionsAttrName(), attr);
}

::mlir::Attribute DynamicBroadcastInDimOpV1::removeKnownExpandingDimensionsAttr() {
  return (*this)->removeAttr(getKnownExpandingDimensionsAttrName());
}

::mlir::Attribute DynamicBroadcastInDimOpV1::removeKnownNonexpandingDimensionsAttr() {
  return (*this)->removeAttr(getKnownNonexpandingDimensionsAttrName());
}

void DynamicBroadcastInDimOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value output_dimensions, ::mlir::Attribute broadcast_dimensions, /*optional*/::mlir::Attribute known_expanding_dimensions, /*optional*/::mlir::Attribute known_nonexpanding_dimensions) {
  odsState.addOperands(operand);
  odsState.addOperands(output_dimensions);
  odsState.addAttribute(getBroadcastDimensionsAttrName(odsState.name), broadcast_dimensions);
  if (known_expanding_dimensions) {
    odsState.addAttribute(getKnownExpandingDimensionsAttrName(odsState.name), known_expanding_dimensions);
  }
  if (known_nonexpanding_dimensions) {
    odsState.addAttribute(getKnownNonexpandingDimensionsAttrName(odsState.name), known_nonexpanding_dimensions);
  }
  odsState.addTypes(resultType0);
}

void DynamicBroadcastInDimOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value output_dimensions, ::mlir::Attribute broadcast_dimensions, /*optional*/::mlir::Attribute known_expanding_dimensions, /*optional*/::mlir::Attribute known_nonexpanding_dimensions) {
  odsState.addOperands(operand);
  odsState.addOperands(output_dimensions);
  odsState.addAttribute(getBroadcastDimensionsAttrName(odsState.name), broadcast_dimensions);
  if (known_expanding_dimensions) {
    odsState.addAttribute(getKnownExpandingDimensionsAttrName(odsState.name), known_expanding_dimensions);
  }
  if (known_nonexpanding_dimensions) {
    odsState.addAttribute(getKnownNonexpandingDimensionsAttrName(odsState.name), known_nonexpanding_dimensions);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicBroadcastInDimOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicBroadcastInDimOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_broadcast_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'broadcast_dimensions'");
    if (namedAttrIt->getName() == getBroadcastDimensionsAttrName()) {
      tblgen_broadcast_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_known_expanding_dimensions;
  ::mlir::Attribute tblgen_known_nonexpanding_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getKnownExpandingDimensionsAttrName()) {
      tblgen_known_expanding_dimensions = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getKnownNonexpandingDimensionsAttrName()) {
      tblgen_known_nonexpanding_dimensions = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_broadcast_dimensions, "broadcast_dimensions")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_known_expanding_dimensions, "known_expanding_dimensions")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_known_nonexpanding_dimensions, "known_nonexpanding_dimensions")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicBroadcastInDimOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicBroadcastInDimOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_broadcast_in_dim");
  return *version;
}
mlir::vhlo::Version DynamicBroadcastInDimOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_broadcast_in_dim");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicBroadcastInDimOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicConvOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicConvOpV1GenericAdaptorBase::DynamicConvOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_conv", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicConvOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DynamicConvOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getWindowStridesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, DynamicConvOpV1::getWindowStridesAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicConvOpV1GenericAdaptorBase::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getPaddingAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, DynamicConvOpV1::getPaddingAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicConvOpV1GenericAdaptorBase::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getLhsDilationAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, DynamicConvOpV1::getLhsDilationAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicConvOpV1GenericAdaptorBase::getLhsDilation() {
  auto attr = getLhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getRhsDilationAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, DynamicConvOpV1::getRhsDilationAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicConvOpV1GenericAdaptorBase::getRhsDilation() {
  auto attr = getRhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getWindowReversalAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, DynamicConvOpV1::getWindowReversalAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicConvOpV1GenericAdaptorBase::getWindowReversal() {
  auto attr = getWindowReversalAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getDimensionNumbersAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, DynamicConvOpV1::getDimensionNumbersAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getFeatureGroupCountAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, DynamicConvOpV1::getFeatureGroupCountAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getFeatureGroupCount() {
  auto attr = getFeatureGroupCountAttr();
  return attr;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getBatchGroupCountAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, DynamicConvOpV1::getBatchGroupCountAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getBatchGroupCount() {
  auto attr = getBatchGroupCountAttr();
  return attr;
}

::mlir::Attribute DynamicConvOpV1GenericAdaptorBase::getPrecisionConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, DynamicConvOpV1::getPrecisionConfigAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicConvOpV1GenericAdaptorBase::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
DynamicConvOpV1Adaptor::DynamicConvOpV1Adaptor(DynamicConvOpV1 op) : DynamicConvOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicConvOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_batch_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_conv' op ""requires attribute 'batch_group_count'");
    if (namedAttrIt->getName() == DynamicConvOpV1::getBatchGroupCountAttrName(*odsOpName)) {
      tblgen_batch_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_conv' op ""requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == DynamicConvOpV1::getDimensionNumbersAttrName(*odsOpName)) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_conv' op ""requires attribute 'feature_group_count'");
    if (namedAttrIt->getName() == DynamicConvOpV1::getFeatureGroupCountAttrName(*odsOpName)) {
      tblgen_feature_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_lhs_dilation;
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_precision_config;
  ::mlir::Attribute tblgen_rhs_dilation;
  ::mlir::Attribute tblgen_window_reversal;
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == DynamicConvOpV1::getLhsDilationAttrName(*odsOpName)) {
      tblgen_lhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == DynamicConvOpV1::getPaddingAttrName(*odsOpName)) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == DynamicConvOpV1::getPrecisionConfigAttrName(*odsOpName)) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == DynamicConvOpV1::getRhsDilationAttrName(*odsOpName)) {
      tblgen_rhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == DynamicConvOpV1::getWindowReversalAttrName(*odsOpName)) {
      tblgen_window_reversal = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == DynamicConvOpV1::getWindowStridesAttrName(*odsOpName)) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_window_strides && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'window_strides' failed to satisfy constraint: any attribute");

  if (tblgen_padding && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'padding' failed to satisfy constraint: any attribute");

  if (tblgen_lhs_dilation && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'lhs_dilation' failed to satisfy constraint: any attribute");

  if (tblgen_rhs_dilation && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'rhs_dilation' failed to satisfy constraint: any attribute");

  if (tblgen_window_reversal && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'window_reversal' failed to satisfy constraint: any attribute");

  if (tblgen_dimension_numbers && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'dimension_numbers' failed to satisfy constraint: any attribute");

  if (tblgen_feature_group_count && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'feature_group_count' failed to satisfy constraint: any attribute");

  if (tblgen_batch_group_count && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'batch_group_count' failed to satisfy constraint: any attribute");

  if (tblgen_precision_config && !((true)))
    return emitError(loc, "'vhlo.dynamic_conv' op ""attribute 'precision_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicConvOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DynamicConvOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicConvOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DynamicConvOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value DynamicConvOpV1::getDPadding() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange DynamicConvOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicConvOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicConvOpV1::getDPaddingMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicConvOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicConvOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute DynamicConvOpV1::getWindowStridesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getWindowStridesAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicConvOpV1::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1::getPaddingAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getPaddingAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicConvOpV1::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1::getLhsDilationAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getLhsDilationAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicConvOpV1::getLhsDilation() {
  auto attr = getLhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1::getRhsDilationAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getRhsDilationAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicConvOpV1::getRhsDilation() {
  auto attr = getRhsDilationAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1::getWindowReversalAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getWindowReversalAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicConvOpV1::getWindowReversal() {
  auto attr = getWindowReversalAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute DynamicConvOpV1::getDimensionNumbersAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getDimensionNumbersAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicConvOpV1::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute DynamicConvOpV1::getFeatureGroupCountAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getFeatureGroupCountAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicConvOpV1::getFeatureGroupCount() {
  auto attr = getFeatureGroupCountAttr();
  return attr;
}

::mlir::Attribute DynamicConvOpV1::getBatchGroupCountAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getBatchGroupCountAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicConvOpV1::getBatchGroupCount() {
  auto attr = getBatchGroupCountAttr();
  return attr;
}

::mlir::Attribute DynamicConvOpV1::getPrecisionConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getPrecisionConfigAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicConvOpV1::getPrecisionConfig() {
  auto attr = getPrecisionConfigAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void DynamicConvOpV1::setWindowStridesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowStridesAttrName(), attr);
}

void DynamicConvOpV1::setPaddingAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPaddingAttrName(), attr);
}

void DynamicConvOpV1::setLhsDilationAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLhsDilationAttrName(), attr);
}

void DynamicConvOpV1::setRhsDilationAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getRhsDilationAttrName(), attr);
}

void DynamicConvOpV1::setWindowReversalAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowReversalAttrName(), attr);
}

void DynamicConvOpV1::setDimensionNumbersAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionNumbersAttrName(), attr);
}

void DynamicConvOpV1::setFeatureGroupCountAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFeatureGroupCountAttrName(), attr);
}

void DynamicConvOpV1::setBatchGroupCountAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBatchGroupCountAttrName(), attr);
}

void DynamicConvOpV1::setPrecisionConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPrecisionConfigAttrName(), attr);
}

::mlir::Attribute DynamicConvOpV1::removeWindowStridesAttr() {
  return (*this)->removeAttr(getWindowStridesAttrName());
}

::mlir::Attribute DynamicConvOpV1::removePaddingAttr() {
  return (*this)->removeAttr(getPaddingAttrName());
}

::mlir::Attribute DynamicConvOpV1::removeLhsDilationAttr() {
  return (*this)->removeAttr(getLhsDilationAttrName());
}

::mlir::Attribute DynamicConvOpV1::removeRhsDilationAttr() {
  return (*this)->removeAttr(getRhsDilationAttrName());
}

::mlir::Attribute DynamicConvOpV1::removeWindowReversalAttr() {
  return (*this)->removeAttr(getWindowReversalAttrName());
}

::mlir::Attribute DynamicConvOpV1::removePrecisionConfigAttr() {
  return (*this)->removeAttr(getPrecisionConfigAttrName());
}

void DynamicConvOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Value d_padding, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute padding, /*optional*/::mlir::Attribute lhs_dilation, /*optional*/::mlir::Attribute rhs_dilation, /*optional*/::mlir::Attribute window_reversal, ::mlir::Attribute dimension_numbers, ::mlir::Attribute feature_group_count, ::mlir::Attribute batch_group_count, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addOperands(d_padding);
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  if (lhs_dilation) {
    odsState.addAttribute(getLhsDilationAttrName(odsState.name), lhs_dilation);
  }
  if (rhs_dilation) {
    odsState.addAttribute(getRhsDilationAttrName(odsState.name), rhs_dilation);
  }
  if (window_reversal) {
    odsState.addAttribute(getWindowReversalAttrName(odsState.name), window_reversal);
  }
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  odsState.addAttribute(getFeatureGroupCountAttrName(odsState.name), feature_group_count);
  odsState.addAttribute(getBatchGroupCountAttrName(odsState.name), batch_group_count);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  odsState.addTypes(resultType0);
}

void DynamicConvOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Value d_padding, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute padding, /*optional*/::mlir::Attribute lhs_dilation, /*optional*/::mlir::Attribute rhs_dilation, /*optional*/::mlir::Attribute window_reversal, ::mlir::Attribute dimension_numbers, ::mlir::Attribute feature_group_count, ::mlir::Attribute batch_group_count, /*optional*/::mlir::Attribute precision_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addOperands(d_padding);
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  if (lhs_dilation) {
    odsState.addAttribute(getLhsDilationAttrName(odsState.name), lhs_dilation);
  }
  if (rhs_dilation) {
    odsState.addAttribute(getRhsDilationAttrName(odsState.name), rhs_dilation);
  }
  if (window_reversal) {
    odsState.addAttribute(getWindowReversalAttrName(odsState.name), window_reversal);
  }
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  odsState.addAttribute(getFeatureGroupCountAttrName(odsState.name), feature_group_count);
  odsState.addAttribute(getBatchGroupCountAttrName(odsState.name), batch_group_count);
  if (precision_config) {
    odsState.addAttribute(getPrecisionConfigAttrName(odsState.name), precision_config);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicConvOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicConvOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_batch_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'batch_group_count'");
    if (namedAttrIt->getName() == getBatchGroupCountAttrName()) {
      tblgen_batch_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == getDimensionNumbersAttrName()) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_feature_group_count;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'feature_group_count'");
    if (namedAttrIt->getName() == getFeatureGroupCountAttrName()) {
      tblgen_feature_group_count = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_lhs_dilation;
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_precision_config;
  ::mlir::Attribute tblgen_rhs_dilation;
  ::mlir::Attribute tblgen_window_reversal;
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getLhsDilationAttrName()) {
      tblgen_lhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getPaddingAttrName()) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getPrecisionConfigAttrName()) {
      tblgen_precision_config = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getRhsDilationAttrName()) {
      tblgen_rhs_dilation = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowReversalAttrName()) {
      tblgen_window_reversal = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowStridesAttrName()) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_strides, "window_strides")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_padding, "padding")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_lhs_dilation, "lhs_dilation")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_rhs_dilation, "rhs_dilation")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_reversal, "window_reversal")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension_numbers, "dimension_numbers")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_feature_group_count, "feature_group_count")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_batch_group_count, "batch_group_count")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_precision_config, "precision_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicConvOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicConvOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_conv");
  return *version;
}
mlir::vhlo::Version DynamicConvOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_conv");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicConvOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicGatherOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicGatherOpV1GenericAdaptorBase::DynamicGatherOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_gather", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicGatherOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DynamicGatherOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DynamicGatherOpV1GenericAdaptorBase::getDimensionNumbersAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, DynamicGatherOpV1::getDimensionNumbersAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicGatherOpV1GenericAdaptorBase::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute DynamicGatherOpV1GenericAdaptorBase::getIndicesAreSortedAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, DynamicGatherOpV1::getIndicesAreSortedAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> DynamicGatherOpV1GenericAdaptorBase::getIndicesAreSorted() {
  auto attr = getIndicesAreSortedAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
DynamicGatherOpV1Adaptor::DynamicGatherOpV1Adaptor(DynamicGatherOpV1 op) : DynamicGatherOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicGatherOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_gather' op ""requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == DynamicGatherOpV1::getDimensionNumbersAttrName(*odsOpName)) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_indices_are_sorted;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == DynamicGatherOpV1::getIndicesAreSortedAttrName(*odsOpName)) {
      tblgen_indices_are_sorted = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_dimension_numbers && !((true)))
    return emitError(loc, "'vhlo.dynamic_gather' op ""attribute 'dimension_numbers' failed to satisfy constraint: any attribute");

  if (tblgen_indices_are_sorted && !((true)))
    return emitError(loc, "'vhlo.dynamic_gather' op ""attribute 'indices_are_sorted' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicGatherOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DynamicGatherOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicGatherOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DynamicGatherOpV1::getStartIndices() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value DynamicGatherOpV1::getSliceSizes() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange DynamicGatherOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicGatherOpV1::getStartIndicesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicGatherOpV1::getSliceSizesMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicGatherOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicGatherOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute DynamicGatherOpV1::getDimensionNumbersAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionNumbersAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicGatherOpV1::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute DynamicGatherOpV1::getIndicesAreSortedAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getIndicesAreSortedAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> DynamicGatherOpV1::getIndicesAreSorted() {
  auto attr = getIndicesAreSortedAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void DynamicGatherOpV1::setDimensionNumbersAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionNumbersAttrName(), attr);
}

void DynamicGatherOpV1::setIndicesAreSortedAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIndicesAreSortedAttrName(), attr);
}

::mlir::Attribute DynamicGatherOpV1::removeIndicesAreSortedAttr() {
  return (*this)->removeAttr(getIndicesAreSortedAttrName());
}

void DynamicGatherOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value start_indices, ::mlir::Value slice_sizes, ::mlir::Attribute dimension_numbers, /*optional*/::mlir::Attribute indices_are_sorted) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addOperands(slice_sizes);
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  if (indices_are_sorted) {
    odsState.addAttribute(getIndicesAreSortedAttrName(odsState.name), indices_are_sorted);
  }
  odsState.addTypes(resultType0);
}

void DynamicGatherOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value start_indices, ::mlir::Value slice_sizes, ::mlir::Attribute dimension_numbers, /*optional*/::mlir::Attribute indices_are_sorted) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addOperands(slice_sizes);
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  if (indices_are_sorted) {
    odsState.addAttribute(getIndicesAreSortedAttrName(odsState.name), indices_are_sorted);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicGatherOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicGatherOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == getDimensionNumbersAttrName()) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_indices_are_sorted;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getIndicesAreSortedAttrName()) {
      tblgen_indices_are_sorted = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension_numbers, "dimension_numbers")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_indices_are_sorted, "indices_are_sorted")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicGatherOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicGatherOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_gather");
  return *version;
}
mlir::vhlo::Version DynamicGatherOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_gather");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicGatherOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicIotaOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicIotaOpV1GenericAdaptorBase::DynamicIotaOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_iota", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicIotaOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DynamicIotaOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DynamicIotaOpV1GenericAdaptorBase::getIotaDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, DynamicIotaOpV1::getIotaDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicIotaOpV1GenericAdaptorBase::getIotaDimension() {
  auto attr = getIotaDimensionAttr();
  return attr;
}

} // namespace detail
DynamicIotaOpV1Adaptor::DynamicIotaOpV1Adaptor(DynamicIotaOpV1 op) : DynamicIotaOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicIotaOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_iota_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_iota' op ""requires attribute 'iota_dimension'");
    if (namedAttrIt->getName() == DynamicIotaOpV1::getIotaDimensionAttrName(*odsOpName)) {
      tblgen_iota_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_iota_dimension && !((true)))
    return emitError(loc, "'vhlo.dynamic_iota' op ""attribute 'iota_dimension' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicIotaOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DynamicIotaOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicIotaOpV1::getOutputShape() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange DynamicIotaOpV1::getOutputShapeMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicIotaOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicIotaOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicIotaOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute DynamicIotaOpV1::getIotaDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getIotaDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicIotaOpV1::getIotaDimension() {
  auto attr = getIotaDimensionAttr();
  return attr;
}

void DynamicIotaOpV1::setIotaDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIotaDimensionAttrName(), attr);
}

void DynamicIotaOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value output_shape, ::mlir::Attribute iota_dimension) {
  odsState.addOperands(output_shape);
  odsState.addAttribute(getIotaDimensionAttrName(odsState.name), iota_dimension);
  odsState.addTypes(result);
}

void DynamicIotaOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value output_shape, ::mlir::Attribute iota_dimension) {
  odsState.addOperands(output_shape);
  odsState.addAttribute(getIotaDimensionAttrName(odsState.name), iota_dimension);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicIotaOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicIotaOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_iota_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'iota_dimension'");
    if (namedAttrIt->getName() == getIotaDimensionAttrName()) {
      tblgen_iota_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_iota_dimension, "iota_dimension")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicIotaOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicIotaOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_iota");
  return *version;
}
mlir::vhlo::Version DynamicIotaOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_iota");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicIotaOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicPadOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicPadOpV1GenericAdaptorBase::DynamicPadOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_pad", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicPadOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DynamicPadOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
DynamicPadOpV1Adaptor::DynamicPadOpV1Adaptor(DynamicPadOpV1 op) : DynamicPadOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicPadOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicPadOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DynamicPadOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicPadOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DynamicPadOpV1::getPaddingValue() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value DynamicPadOpV1::getEdgePaddingLow() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::Value DynamicPadOpV1::getEdgePaddingHigh() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(3).begin());
}

::mlir::Value DynamicPadOpV1::getInteriorPadding() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(4).begin());
}

::mlir::MutableOperandRange DynamicPadOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicPadOpV1::getPaddingValueMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicPadOpV1::getEdgePaddingLowMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicPadOpV1::getEdgePaddingHighMutable() {
  auto range = getODSOperandIndexAndLength(3);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicPadOpV1::getInteriorPaddingMutable() {
  auto range = getODSOperandIndexAndLength(4);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicPadOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicPadOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicPadOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void DynamicPadOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::Value padding_value, ::mlir::Value edge_padding_low, ::mlir::Value edge_padding_high, ::mlir::Value interior_padding) {
  odsState.addOperands(operand);
  odsState.addOperands(padding_value);
  odsState.addOperands(edge_padding_low);
  odsState.addOperands(edge_padding_high);
  odsState.addOperands(interior_padding);
  odsState.addTypes(result);
}

void DynamicPadOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value padding_value, ::mlir::Value edge_padding_low, ::mlir::Value edge_padding_high, ::mlir::Value interior_padding) {
  odsState.addOperands(operand);
  odsState.addOperands(padding_value);
  odsState.addOperands(edge_padding_low);
  odsState.addOperands(edge_padding_high);
  odsState.addOperands(interior_padding);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicPadOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 5u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicPadOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup3 = getODSOperands(3);

    for (auto v : valueGroup3) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup4 = getODSOperands(4);

    for (auto v : valueGroup4) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicPadOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicPadOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_pad");
  return *version;
}
mlir::vhlo::Version DynamicPadOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_pad");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicPadOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicReshapeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicReshapeOpV1GenericAdaptorBase::DynamicReshapeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_reshape", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicReshapeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr DynamicReshapeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
DynamicReshapeOpV1Adaptor::DynamicReshapeOpV1Adaptor(DynamicReshapeOpV1 op) : DynamicReshapeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicReshapeOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicReshapeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range DynamicReshapeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicReshapeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DynamicReshapeOpV1::getOutputShape() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange DynamicReshapeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicReshapeOpV1::getOutputShapeMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicReshapeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicReshapeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicReshapeOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void DynamicReshapeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::Value output_shape) {
  odsState.addOperands(operand);
  odsState.addOperands(output_shape);
  odsState.addTypes(result);
}

void DynamicReshapeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value output_shape) {
  odsState.addOperands(operand);
  odsState.addOperands(output_shape);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicReshapeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicReshapeOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicReshapeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicReshapeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_reshape");
  return *version;
}
mlir::vhlo::Version DynamicReshapeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_reshape");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicReshapeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicSliceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicSliceOpV1GenericAdaptorBase::DynamicSliceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_slice", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicSliceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {false, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 1) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr DynamicSliceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute DynamicSliceOpV1GenericAdaptorBase::getSliceSizesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, DynamicSliceOpV1::getSliceSizesAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute DynamicSliceOpV1GenericAdaptorBase::getSliceSizes() {
  auto attr = getSliceSizesAttr();
  return attr;
}

} // namespace detail
DynamicSliceOpV1Adaptor::DynamicSliceOpV1Adaptor(DynamicSliceOpV1 op) : DynamicSliceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicSliceOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_slice_sizes;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.dynamic_slice' op ""requires attribute 'slice_sizes'");
    if (namedAttrIt->getName() == DynamicSliceOpV1::getSliceSizesAttrName(*odsOpName)) {
      tblgen_slice_sizes = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_slice_sizes && !((true)))
    return emitError(loc, "'vhlo.dynamic_slice' op ""attribute 'slice_sizes' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicSliceOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {false, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 1) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range DynamicSliceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicSliceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Operation::operand_range DynamicSliceOpV1::getStartIndices() {
  return getODSOperands(1);
}

::mlir::MutableOperandRange DynamicSliceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicSliceOpV1::getStartIndicesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicSliceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicSliceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicSliceOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute DynamicSliceOpV1::getSliceSizesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getSliceSizesAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute DynamicSliceOpV1::getSliceSizes() {
  auto attr = getSliceSizesAttr();
  return attr;
}

void DynamicSliceOpV1::setSliceSizesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSliceSizesAttrName(), attr);
}

void DynamicSliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::ValueRange start_indices, ::mlir::Attribute slice_sizes) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addAttribute(getSliceSizesAttrName(odsState.name), slice_sizes);
  odsState.addTypes(result);
}

void DynamicSliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::ValueRange start_indices, ::mlir::Attribute slice_sizes) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addAttribute(getSliceSizesAttrName(odsState.name), slice_sizes);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicSliceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() >= 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicSliceOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_slice_sizes;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'slice_sizes'");
    if (namedAttrIt->getName() == getSliceSizesAttrName()) {
      tblgen_slice_sizes = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_slice_sizes, "slice_sizes")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicSliceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicSliceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_slice");
  return *version;
}
mlir::vhlo::Version DynamicSliceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_slice");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicSliceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::DynamicUpdateSliceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
DynamicUpdateSliceOpV1GenericAdaptorBase::DynamicUpdateSliceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.dynamic_update_slice", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> DynamicUpdateSliceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {false, false, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 2) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr DynamicUpdateSliceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
DynamicUpdateSliceOpV1Adaptor::DynamicUpdateSliceOpV1Adaptor(DynamicUpdateSliceOpV1 op) : DynamicUpdateSliceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult DynamicUpdateSliceOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> DynamicUpdateSliceOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {false, false, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 2) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range DynamicUpdateSliceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicUpdateSliceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value DynamicUpdateSliceOpV1::getUpdate() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Operation::operand_range DynamicUpdateSliceOpV1::getStartIndices() {
  return getODSOperands(2);
}

::mlir::MutableOperandRange DynamicUpdateSliceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicUpdateSliceOpV1::getUpdateMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange DynamicUpdateSliceOpV1::getStartIndicesMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> DynamicUpdateSliceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range DynamicUpdateSliceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value DynamicUpdateSliceOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void DynamicUpdateSliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::Value update, ::mlir::ValueRange start_indices) {
  odsState.addOperands(operand);
  odsState.addOperands(update);
  odsState.addOperands(start_indices);
  odsState.addTypes(result);
}

void DynamicUpdateSliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value update, ::mlir::ValueRange start_indices) {
  odsState.addOperands(operand);
  odsState.addOperands(update);
  odsState.addOperands(start_indices);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void DynamicUpdateSliceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() >= 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult DynamicUpdateSliceOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult DynamicUpdateSliceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version DynamicUpdateSliceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in dynamic_update_slice");
  return *version;
}
mlir::vhlo::Version DynamicUpdateSliceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in dynamic_update_slice");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::DynamicUpdateSliceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::EinsumOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
EinsumOpV1GenericAdaptorBase::EinsumOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.einsum", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> EinsumOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr EinsumOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute EinsumOpV1GenericAdaptorBase::getEinsumConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, EinsumOpV1::getEinsumConfigAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute EinsumOpV1GenericAdaptorBase::getEinsumConfig() {
  auto attr = getEinsumConfigAttr();
  return attr;
}

} // namespace detail
EinsumOpV1Adaptor::EinsumOpV1Adaptor(EinsumOpV1 op) : EinsumOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult EinsumOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_einsum_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.einsum' op ""requires attribute 'einsum_config'");
    if (namedAttrIt->getName() == EinsumOpV1::getEinsumConfigAttrName(*odsOpName)) {
      tblgen_einsum_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_einsum_config && !((true)))
    return emitError(loc, "'vhlo.einsum' op ""attribute 'einsum_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> EinsumOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range EinsumOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value EinsumOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value EinsumOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange EinsumOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange EinsumOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> EinsumOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range EinsumOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute EinsumOpV1::getEinsumConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getEinsumConfigAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute EinsumOpV1::getEinsumConfig() {
  auto attr = getEinsumConfigAttr();
  return attr;
}

void EinsumOpV1::setEinsumConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEinsumConfigAttrName(), attr);
}

void EinsumOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Attribute einsum_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addAttribute(getEinsumConfigAttrName(odsState.name), einsum_config);
  odsState.addTypes(resultType0);
}

void EinsumOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs, ::mlir::Attribute einsum_config) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addAttribute(getEinsumConfigAttrName(odsState.name), einsum_config);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void EinsumOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult EinsumOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_einsum_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'einsum_config'");
    if (namedAttrIt->getName() == getEinsumConfigAttrName()) {
      tblgen_einsum_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_einsum_config, "einsum_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult EinsumOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version EinsumOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in einsum");
  return *version;
}
mlir::vhlo::Version EinsumOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in einsum");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::EinsumOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ExpOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ExpOpV1GenericAdaptorBase::ExpOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.exponential", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ExpOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ExpOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ExpOpV1Adaptor::ExpOpV1Adaptor(ExpOpV1 op) : ExpOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ExpOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ExpOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ExpOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ExpOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ExpOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ExpOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ExpOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ExpOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ExpOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void ExpOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ExpOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ExpOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ExpOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ExpOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in exponential");
  return *version;
}
mlir::vhlo::Version ExpOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in exponential");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ExpOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::Expm1OpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
Expm1OpV1GenericAdaptorBase::Expm1OpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.exponential_minus_one", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> Expm1OpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr Expm1OpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
Expm1OpV1Adaptor::Expm1OpV1Adaptor(Expm1OpV1 op) : Expm1OpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult Expm1OpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> Expm1OpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range Expm1OpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value Expm1OpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange Expm1OpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> Expm1OpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range Expm1OpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value Expm1OpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void Expm1OpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void Expm1OpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void Expm1OpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult Expm1OpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult Expm1OpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version Expm1OpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in exponential_minus_one");
  return *version;
}
mlir::vhlo::Version Expm1OpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in exponential_minus_one");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::Expm1OpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::FftOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
FftOpV1GenericAdaptorBase::FftOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.fft", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> FftOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr FftOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute FftOpV1GenericAdaptorBase::getFftTypeAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, FftOpV1::getFftTypeAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute FftOpV1GenericAdaptorBase::getFftType() {
  auto attr = getFftTypeAttr();
  return attr;
}

::mlir::Attribute FftOpV1GenericAdaptorBase::getFftLengthAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, FftOpV1::getFftLengthAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute FftOpV1GenericAdaptorBase::getFftLength() {
  auto attr = getFftLengthAttr();
  return attr;
}

} // namespace detail
FftOpV1Adaptor::FftOpV1Adaptor(FftOpV1 op) : FftOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult FftOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_fft_length;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.fft' op ""requires attribute 'fft_length'");
    if (namedAttrIt->getName() == FftOpV1::getFftLengthAttrName(*odsOpName)) {
      tblgen_fft_length = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_fft_type;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.fft' op ""requires attribute 'fft_type'");
    if (namedAttrIt->getName() == FftOpV1::getFftTypeAttrName(*odsOpName)) {
      tblgen_fft_type = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_fft_type && !((true)))
    return emitError(loc, "'vhlo.fft' op ""attribute 'fft_type' failed to satisfy constraint: any attribute");

  if (tblgen_fft_length && !((true)))
    return emitError(loc, "'vhlo.fft' op ""attribute 'fft_length' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> FftOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range FftOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value FftOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange FftOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> FftOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range FftOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute FftOpV1::getFftTypeAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getFftTypeAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute FftOpV1::getFftType() {
  auto attr = getFftTypeAttr();
  return attr;
}

::mlir::Attribute FftOpV1::getFftLengthAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getFftLengthAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute FftOpV1::getFftLength() {
  auto attr = getFftLengthAttr();
  return attr;
}

void FftOpV1::setFftTypeAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFftTypeAttrName(), attr);
}

void FftOpV1::setFftLengthAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getFftLengthAttrName(), attr);
}

void FftOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute fft_type, ::mlir::Attribute fft_length) {
  odsState.addOperands(operand);
  odsState.addAttribute(getFftTypeAttrName(odsState.name), fft_type);
  odsState.addAttribute(getFftLengthAttrName(odsState.name), fft_length);
  odsState.addTypes(resultType0);
}

void FftOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute fft_type, ::mlir::Attribute fft_length) {
  odsState.addOperands(operand);
  odsState.addAttribute(getFftTypeAttrName(odsState.name), fft_type);
  odsState.addAttribute(getFftLengthAttrName(odsState.name), fft_length);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void FftOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult FftOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_fft_length;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'fft_length'");
    if (namedAttrIt->getName() == getFftLengthAttrName()) {
      tblgen_fft_length = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_fft_type;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'fft_type'");
    if (namedAttrIt->getName() == getFftTypeAttrName()) {
      tblgen_fft_type = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_fft_type, "fft_type")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_fft_length, "fft_length")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult FftOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version FftOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in fft");
  return *version;
}
mlir::vhlo::Version FftOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in fft");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::FftOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::FloorOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
FloorOpV1GenericAdaptorBase::FloorOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.floor", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> FloorOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr FloorOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
FloorOpV1Adaptor::FloorOpV1Adaptor(FloorOpV1 op) : FloorOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult FloorOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> FloorOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range FloorOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value FloorOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange FloorOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> FloorOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range FloorOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value FloorOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void FloorOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void FloorOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void FloorOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult FloorOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult FloorOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version FloorOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in floor");
  return *version;
}
mlir::vhlo::Version FloorOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in floor");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::FloorOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::GatherOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
GatherOpV1GenericAdaptorBase::GatherOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.gather", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> GatherOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr GatherOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute GatherOpV1GenericAdaptorBase::getDimensionNumbersAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, GatherOpV1::getDimensionNumbersAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute GatherOpV1GenericAdaptorBase::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute GatherOpV1GenericAdaptorBase::getSliceSizesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, GatherOpV1::getSliceSizesAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute GatherOpV1GenericAdaptorBase::getSliceSizes() {
  auto attr = getSliceSizesAttr();
  return attr;
}

::mlir::Attribute GatherOpV1GenericAdaptorBase::getIndicesAreSortedAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, GatherOpV1::getIndicesAreSortedAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> GatherOpV1GenericAdaptorBase::getIndicesAreSorted() {
  auto attr = getIndicesAreSortedAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
GatherOpV1Adaptor::GatherOpV1Adaptor(GatherOpV1 op) : GatherOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult GatherOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.gather' op ""requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == GatherOpV1::getDimensionNumbersAttrName(*odsOpName)) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_slice_sizes;
  ::mlir::Attribute tblgen_indices_are_sorted;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.gather' op ""requires attribute 'slice_sizes'");
    if (namedAttrIt->getName() == GatherOpV1::getSliceSizesAttrName(*odsOpName)) {
      tblgen_slice_sizes = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == GatherOpV1::getIndicesAreSortedAttrName(*odsOpName)) {
      tblgen_indices_are_sorted = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_dimension_numbers && !((true)))
    return emitError(loc, "'vhlo.gather' op ""attribute 'dimension_numbers' failed to satisfy constraint: any attribute");

  if (tblgen_slice_sizes && !((true)))
    return emitError(loc, "'vhlo.gather' op ""attribute 'slice_sizes' failed to satisfy constraint: any attribute");

  if (tblgen_indices_are_sorted && !((true)))
    return emitError(loc, "'vhlo.gather' op ""attribute 'indices_are_sorted' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> GatherOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range GatherOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value GatherOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value GatherOpV1::getStartIndices() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange GatherOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange GatherOpV1::getStartIndicesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> GatherOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range GatherOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute GatherOpV1::getDimensionNumbersAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getDimensionNumbersAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute GatherOpV1::getDimensionNumbers() {
  auto attr = getDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute GatherOpV1::getSliceSizesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getSliceSizesAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute GatherOpV1::getSliceSizes() {
  auto attr = getSliceSizesAttr();
  return attr;
}

::mlir::Attribute GatherOpV1::getIndicesAreSortedAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getIndicesAreSortedAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> GatherOpV1::getIndicesAreSorted() {
  auto attr = getIndicesAreSortedAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void GatherOpV1::setDimensionNumbersAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionNumbersAttrName(), attr);
}

void GatherOpV1::setSliceSizesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getSliceSizesAttrName(), attr);
}

void GatherOpV1::setIndicesAreSortedAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIndicesAreSortedAttrName(), attr);
}

::mlir::Attribute GatherOpV1::removeIndicesAreSortedAttr() {
  return (*this)->removeAttr(getIndicesAreSortedAttrName());
}

void GatherOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value start_indices, ::mlir::Attribute dimension_numbers, ::mlir::Attribute slice_sizes, /*optional*/::mlir::Attribute indices_are_sorted) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  odsState.addAttribute(getSliceSizesAttrName(odsState.name), slice_sizes);
  if (indices_are_sorted) {
    odsState.addAttribute(getIndicesAreSortedAttrName(odsState.name), indices_are_sorted);
  }
  odsState.addTypes(resultType0);
}

void GatherOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value start_indices, ::mlir::Attribute dimension_numbers, ::mlir::Attribute slice_sizes, /*optional*/::mlir::Attribute indices_are_sorted) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addAttribute(getDimensionNumbersAttrName(odsState.name), dimension_numbers);
  odsState.addAttribute(getSliceSizesAttrName(odsState.name), slice_sizes);
  if (indices_are_sorted) {
    odsState.addAttribute(getIndicesAreSortedAttrName(odsState.name), indices_are_sorted);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void GatherOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult GatherOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension_numbers;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension_numbers'");
    if (namedAttrIt->getName() == getDimensionNumbersAttrName()) {
      tblgen_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_slice_sizes;
  ::mlir::Attribute tblgen_indices_are_sorted;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'slice_sizes'");
    if (namedAttrIt->getName() == getSliceSizesAttrName()) {
      tblgen_slice_sizes = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getIndicesAreSortedAttrName()) {
      tblgen_indices_are_sorted = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension_numbers, "dimension_numbers")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_slice_sizes, "slice_sizes")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_indices_are_sorted, "indices_are_sorted")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult GatherOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version GatherOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in gather");
  return *version;
}
mlir::vhlo::Version GatherOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in gather");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::GatherOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::GetDimensionSizeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
GetDimensionSizeOpV1GenericAdaptorBase::GetDimensionSizeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.get_dimension_size", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> GetDimensionSizeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr GetDimensionSizeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute GetDimensionSizeOpV1GenericAdaptorBase::getDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, GetDimensionSizeOpV1::getDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute GetDimensionSizeOpV1GenericAdaptorBase::getDimension() {
  auto attr = getDimensionAttr();
  return attr;
}

} // namespace detail
GetDimensionSizeOpV1Adaptor::GetDimensionSizeOpV1Adaptor(GetDimensionSizeOpV1 op) : GetDimensionSizeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult GetDimensionSizeOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.get_dimension_size' op ""requires attribute 'dimension'");
    if (namedAttrIt->getName() == GetDimensionSizeOpV1::getDimensionAttrName(*odsOpName)) {
      tblgen_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dimension && !((true)))
    return emitError(loc, "'vhlo.get_dimension_size' op ""attribute 'dimension' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> GetDimensionSizeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range GetDimensionSizeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value GetDimensionSizeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange GetDimensionSizeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> GetDimensionSizeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range GetDimensionSizeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute GetDimensionSizeOpV1::getDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute GetDimensionSizeOpV1::getDimension() {
  auto attr = getDimensionAttr();
  return attr;
}

void GetDimensionSizeOpV1::setDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionAttrName(), attr);
}

void GetDimensionSizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute dimension) {
  odsState.addOperands(operand);
  odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  odsState.addTypes(resultType0);
}

void GetDimensionSizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute dimension) {
  odsState.addOperands(operand);
  odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void GetDimensionSizeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult GetDimensionSizeOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension'");
    if (namedAttrIt->getName() == getDimensionAttrName()) {
      tblgen_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension, "dimension")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult GetDimensionSizeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version GetDimensionSizeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in get_dimension_size");
  return *version;
}
mlir::vhlo::Version GetDimensionSizeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in get_dimension_size");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::GetDimensionSizeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::GetTupleElementOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
GetTupleElementOpV1GenericAdaptorBase::GetTupleElementOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.get_tuple_element", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> GetTupleElementOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr GetTupleElementOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute GetTupleElementOpV1GenericAdaptorBase::getIndexAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, GetTupleElementOpV1::getIndexAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute GetTupleElementOpV1GenericAdaptorBase::getIndex() {
  auto attr = getIndexAttr();
  return attr;
}

} // namespace detail
GetTupleElementOpV1Adaptor::GetTupleElementOpV1Adaptor(GetTupleElementOpV1 op) : GetTupleElementOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult GetTupleElementOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.get_tuple_element' op ""requires attribute 'index'");
    if (namedAttrIt->getName() == GetTupleElementOpV1::getIndexAttrName(*odsOpName)) {
      tblgen_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_index && !((true)))
    return emitError(loc, "'vhlo.get_tuple_element' op ""attribute 'index' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> GetTupleElementOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range GetTupleElementOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value GetTupleElementOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange GetTupleElementOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> GetTupleElementOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range GetTupleElementOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute GetTupleElementOpV1::getIndexAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getIndexAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute GetTupleElementOpV1::getIndex() {
  auto attr = getIndexAttr();
  return attr;
}

void GetTupleElementOpV1::setIndexAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIndexAttrName(), attr);
}

void GetTupleElementOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute index) {
  odsState.addOperands(operand);
  odsState.addAttribute(getIndexAttrName(odsState.name), index);
  odsState.addTypes(resultType0);
}

void GetTupleElementOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute index) {
  odsState.addOperands(operand);
  odsState.addAttribute(getIndexAttrName(odsState.name), index);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void GetTupleElementOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult GetTupleElementOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_index;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'index'");
    if (namedAttrIt->getName() == getIndexAttrName()) {
      tblgen_index = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_index, "index")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult GetTupleElementOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version GetTupleElementOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in get_tuple_element");
  return *version;
}
mlir::vhlo::Version GetTupleElementOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in get_tuple_element");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::GetTupleElementOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::IfOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
IfOpV1GenericAdaptorBase::IfOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.if", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> IfOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr IfOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Region &IfOpV1GenericAdaptorBase::getTrueBranch() {
  return *odsRegions[0];
}

::mlir::Region &IfOpV1GenericAdaptorBase::getFalseBranch() {
  return *odsRegions[1];
}

::mlir::RegionRange IfOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
IfOpV1Adaptor::IfOpV1Adaptor(IfOpV1 op) : IfOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult IfOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> IfOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range IfOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value IfOpV1::getPred() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange IfOpV1::getPredMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> IfOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range IfOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &IfOpV1::getTrueBranch() {
  return (*this)->getRegion(0);
}

::mlir::Region &IfOpV1::getFalseBranch() {
  return (*this)->getRegion(1);
}

void IfOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::Value pred) {
  odsState.addOperands(pred);
  (void)odsState.addRegion();
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void IfOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 2; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult IfOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "true_branch", index++)))
        return ::mlir::failure();

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(1)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "false_branch", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult IfOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version IfOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in if");
  return *version;
}
mlir::vhlo::Version IfOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in if");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::IfOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ImagOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ImagOpV1GenericAdaptorBase::ImagOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.imag", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ImagOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ImagOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ImagOpV1Adaptor::ImagOpV1Adaptor(ImagOpV1 op) : ImagOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ImagOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ImagOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ImagOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ImagOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ImagOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ImagOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ImagOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ImagOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ImagOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void ImagOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ImagOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ImagOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ImagOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ImagOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in imag");
  return *version;
}
mlir::vhlo::Version ImagOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in imag");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ImagOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::InfeedOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
InfeedOpV1GenericAdaptorBase::InfeedOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.infeed", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> InfeedOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr InfeedOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute InfeedOpV1GenericAdaptorBase::getInfeedConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, InfeedOpV1::getInfeedConfigAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute InfeedOpV1GenericAdaptorBase::getInfeedConfig() {
  auto attr = getInfeedConfigAttr();
  return attr;
}

::mlir::Attribute InfeedOpV1GenericAdaptorBase::getLayoutAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, InfeedOpV1::getLayoutAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> InfeedOpV1GenericAdaptorBase::getLayout() {
  auto attr = getLayoutAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
InfeedOpV1Adaptor::InfeedOpV1Adaptor(InfeedOpV1 op) : InfeedOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult InfeedOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_infeed_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.infeed' op ""requires attribute 'infeed_config'");
    if (namedAttrIt->getName() == InfeedOpV1::getInfeedConfigAttrName(*odsOpName)) {
      tblgen_infeed_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_layout;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == InfeedOpV1::getLayoutAttrName(*odsOpName)) {
      tblgen_layout = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_infeed_config && !((true)))
    return emitError(loc, "'vhlo.infeed' op ""attribute 'infeed_config' failed to satisfy constraint: any attribute");

  if (tblgen_layout && !((true)))
    return emitError(loc, "'vhlo.infeed' op ""attribute 'layout' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> InfeedOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range InfeedOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value InfeedOpV1::getToken() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange InfeedOpV1::getTokenMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> InfeedOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range InfeedOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute InfeedOpV1::getInfeedConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getInfeedConfigAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute InfeedOpV1::getInfeedConfig() {
  auto attr = getInfeedConfigAttr();
  return attr;
}

::mlir::Attribute InfeedOpV1::getLayoutAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getLayoutAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> InfeedOpV1::getLayout() {
  auto attr = getLayoutAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void InfeedOpV1::setInfeedConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getInfeedConfigAttrName(), attr);
}

void InfeedOpV1::setLayoutAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLayoutAttrName(), attr);
}

::mlir::Attribute InfeedOpV1::removeLayoutAttr() {
  return (*this)->removeAttr(getLayoutAttrName());
}

void InfeedOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::Value token, ::mlir::Attribute infeed_config, /*optional*/::mlir::Attribute layout) {
  odsState.addOperands(token);
  odsState.addAttribute(getInfeedConfigAttrName(odsState.name), infeed_config);
  if (layout) {
    odsState.addAttribute(getLayoutAttrName(odsState.name), layout);
  }
  odsState.addTypes(resultType0);
}

void InfeedOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult InfeedOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_infeed_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'infeed_config'");
    if (namedAttrIt->getName() == getInfeedConfigAttrName()) {
      tblgen_infeed_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_layout;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getLayoutAttrName()) {
      tblgen_layout = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_infeed_config, "infeed_config")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_layout, "layout")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult InfeedOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version InfeedOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in infeed");
  return *version;
}
mlir::vhlo::Version InfeedOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in infeed");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::InfeedOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::IotaOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
IotaOpV1GenericAdaptorBase::IotaOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.iota", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> IotaOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr IotaOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute IotaOpV1GenericAdaptorBase::getIotaDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, IotaOpV1::getIotaDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute IotaOpV1GenericAdaptorBase::getIotaDimension() {
  auto attr = getIotaDimensionAttr();
  return attr;
}

} // namespace detail
IotaOpV1Adaptor::IotaOpV1Adaptor(IotaOpV1 op) : IotaOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult IotaOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_iota_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.iota' op ""requires attribute 'iota_dimension'");
    if (namedAttrIt->getName() == IotaOpV1::getIotaDimensionAttrName(*odsOpName)) {
      tblgen_iota_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_iota_dimension && !((true)))
    return emitError(loc, "'vhlo.iota' op ""attribute 'iota_dimension' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> IotaOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range IotaOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> IotaOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range IotaOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value IotaOpV1::getOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute IotaOpV1::getIotaDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getIotaDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute IotaOpV1::getIotaDimension() {
  auto attr = getIotaDimensionAttr();
  return attr;
}

void IotaOpV1::setIotaDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIotaDimensionAttrName(), attr);
}

void IotaOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type output, ::mlir::Attribute iota_dimension) {
  odsState.addAttribute(getIotaDimensionAttrName(odsState.name), iota_dimension);
  odsState.addTypes(output);
}

void IotaOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Attribute iota_dimension) {
  odsState.addAttribute(getIotaDimensionAttrName(odsState.name), iota_dimension);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void IotaOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult IotaOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_iota_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'iota_dimension'");
    if (namedAttrIt->getName() == getIotaDimensionAttrName()) {
      tblgen_iota_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_iota_dimension, "iota_dimension")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult IotaOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version IotaOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in iota");
  return *version;
}
mlir::vhlo::Version IotaOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in iota");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::IotaOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::IsFiniteOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
IsFiniteOpV1GenericAdaptorBase::IsFiniteOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.is_finite", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> IsFiniteOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr IsFiniteOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
IsFiniteOpV1Adaptor::IsFiniteOpV1Adaptor(IsFiniteOpV1 op) : IsFiniteOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult IsFiniteOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> IsFiniteOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range IsFiniteOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value IsFiniteOpV1::getX() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange IsFiniteOpV1::getXMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> IsFiniteOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range IsFiniteOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value IsFiniteOpV1::getY() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void IsFiniteOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type y, ::mlir::Value x) {
  odsState.addOperands(x);
  odsState.addTypes(y);
}

void IsFiniteOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value x) {
  odsState.addOperands(x);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void IsFiniteOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult IsFiniteOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult IsFiniteOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version IsFiniteOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in is_finite");
  return *version;
}
mlir::vhlo::Version IsFiniteOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in is_finite");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::IsFiniteOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::Log1pOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
Log1pOpV1GenericAdaptorBase::Log1pOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.log_plus_one", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> Log1pOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr Log1pOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
Log1pOpV1Adaptor::Log1pOpV1Adaptor(Log1pOpV1 op) : Log1pOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult Log1pOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> Log1pOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range Log1pOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value Log1pOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange Log1pOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> Log1pOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range Log1pOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value Log1pOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void Log1pOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void Log1pOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void Log1pOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult Log1pOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult Log1pOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version Log1pOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in log_plus_one");
  return *version;
}
mlir::vhlo::Version Log1pOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in log_plus_one");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::Log1pOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::LogOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
LogOpV1GenericAdaptorBase::LogOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.log", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> LogOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr LogOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
LogOpV1Adaptor::LogOpV1Adaptor(LogOpV1 op) : LogOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult LogOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> LogOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range LogOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value LogOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange LogOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> LogOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range LogOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value LogOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void LogOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void LogOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void LogOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult LogOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult LogOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version LogOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in log");
  return *version;
}
mlir::vhlo::Version LogOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in log");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::LogOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::LogisticOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
LogisticOpV1GenericAdaptorBase::LogisticOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.logistic", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> LogisticOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr LogisticOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
LogisticOpV1Adaptor::LogisticOpV1Adaptor(LogisticOpV1 op) : LogisticOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult LogisticOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> LogisticOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range LogisticOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value LogisticOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange LogisticOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> LogisticOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range LogisticOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value LogisticOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void LogisticOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void LogisticOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void LogisticOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult LogisticOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult LogisticOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version LogisticOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in logistic");
  return *version;
}
mlir::vhlo::Version LogisticOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in logistic");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::LogisticOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::MapOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
MapOpV1GenericAdaptorBase::MapOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.map", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> MapOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr MapOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute MapOpV1GenericAdaptorBase::getDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, MapOpV1::getDimensionsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute MapOpV1GenericAdaptorBase::getDimensions() {
  auto attr = getDimensionsAttr();
  return attr;
}

::mlir::Region &MapOpV1GenericAdaptorBase::getComputation() {
  return *odsRegions[0];
}

::mlir::RegionRange MapOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
MapOpV1Adaptor::MapOpV1Adaptor(MapOpV1 op) : MapOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult MapOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.map' op ""requires attribute 'dimensions'");
    if (namedAttrIt->getName() == MapOpV1::getDimensionsAttrName(*odsOpName)) {
      tblgen_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dimensions && !((true)))
    return emitError(loc, "'vhlo.map' op ""attribute 'dimensions' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> MapOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range MapOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range MapOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange MapOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> MapOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range MapOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &MapOpV1::getComputation() {
  return (*this)->getRegion(0);
}

::mlir::Attribute MapOpV1::getDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute MapOpV1::getDimensions() {
  auto attr = getDimensionsAttr();
  return attr;
}

void MapOpV1::setDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionsAttrName(), attr);
}

void MapOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::ValueRange inputs, ::mlir::Attribute dimensions) {
  odsState.addOperands(inputs);
  odsState.addAttribute(getDimensionsAttrName(odsState.name), dimensions);
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void MapOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange inputs, ::mlir::Attribute dimensions) {
  odsState.addOperands(inputs);
  odsState.addAttribute(getDimensionsAttrName(odsState.name), dimensions);
  (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void MapOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult MapOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimensions'");
    if (namedAttrIt->getName() == getDimensionsAttrName()) {
      tblgen_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimensions, "dimensions")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "computation", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult MapOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version MapOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in map");
  return *version;
}
mlir::vhlo::Version MapOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in map");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::MapOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::MaxOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
MaxOpV1GenericAdaptorBase::MaxOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.maximum", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> MaxOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr MaxOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
MaxOpV1Adaptor::MaxOpV1Adaptor(MaxOpV1 op) : MaxOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult MaxOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> MaxOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range MaxOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value MaxOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value MaxOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange MaxOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange MaxOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> MaxOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range MaxOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value MaxOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void MaxOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void MaxOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void MaxOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult MaxOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult MaxOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version MaxOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in maximum");
  return *version;
}
mlir::vhlo::Version MaxOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in maximum");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::MaxOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::MinOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
MinOpV1GenericAdaptorBase::MinOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.minimum", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> MinOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr MinOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
MinOpV1Adaptor::MinOpV1Adaptor(MinOpV1 op) : MinOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult MinOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> MinOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range MinOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value MinOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value MinOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange MinOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange MinOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> MinOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range MinOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value MinOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void MinOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void MinOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void MinOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult MinOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult MinOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version MinOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in minimum");
  return *version;
}
mlir::vhlo::Version MinOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in minimum");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::MinOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::MulOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
MulOpV1GenericAdaptorBase::MulOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.multiply", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> MulOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr MulOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
MulOpV1Adaptor::MulOpV1Adaptor(MulOpV1 op) : MulOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult MulOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> MulOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range MulOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value MulOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value MulOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange MulOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange MulOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> MulOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range MulOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value MulOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void MulOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void MulOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void MulOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult MulOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult MulOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version MulOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in multiply");
  return *version;
}
mlir::vhlo::Version MulOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in multiply");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::MulOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::NegOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
NegOpV1GenericAdaptorBase::NegOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.negate", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> NegOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr NegOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
NegOpV1Adaptor::NegOpV1Adaptor(NegOpV1 op) : NegOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult NegOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> NegOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range NegOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value NegOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange NegOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> NegOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range NegOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value NegOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void NegOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void NegOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void NegOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult NegOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult NegOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version NegOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in negate");
  return *version;
}
mlir::vhlo::Version NegOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in negate");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::NegOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::NotOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
NotOpV1GenericAdaptorBase::NotOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.not", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> NotOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr NotOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
NotOpV1Adaptor::NotOpV1Adaptor(NotOpV1 op) : NotOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult NotOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> NotOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range NotOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value NotOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange NotOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> NotOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range NotOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value NotOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void NotOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void NotOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void NotOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult NotOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult NotOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version NotOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in not");
  return *version;
}
mlir::vhlo::Version NotOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in not");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::NotOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::OptimizationBarrierOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
OptimizationBarrierOpV1GenericAdaptorBase::OptimizationBarrierOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.optimization_barrier", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> OptimizationBarrierOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr OptimizationBarrierOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
OptimizationBarrierOpV1Adaptor::OptimizationBarrierOpV1Adaptor(OptimizationBarrierOpV1 op) : OptimizationBarrierOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult OptimizationBarrierOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> OptimizationBarrierOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range OptimizationBarrierOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range OptimizationBarrierOpV1::getOperand() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange OptimizationBarrierOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> OptimizationBarrierOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range OptimizationBarrierOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::result_range OptimizationBarrierOpV1::getResult() {
  return getODSResults(0);
}

void OptimizationBarrierOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult OptimizationBarrierOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult OptimizationBarrierOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version OptimizationBarrierOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in optimization_barrier");
  return *version;
}
mlir::vhlo::Version OptimizationBarrierOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in optimization_barrier");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::OptimizationBarrierOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::OrOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
OrOpV1GenericAdaptorBase::OrOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.or", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> OrOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr OrOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
OrOpV1Adaptor::OrOpV1Adaptor(OrOpV1 op) : OrOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult OrOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> OrOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range OrOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value OrOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value OrOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange OrOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange OrOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> OrOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range OrOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value OrOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void OrOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void OrOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void OrOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult OrOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult OrOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version OrOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in or");
  return *version;
}
mlir::vhlo::Version OrOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in or");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::OrOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::OutfeedOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
OutfeedOpV1GenericAdaptorBase::OutfeedOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.outfeed", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> OutfeedOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true, false};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 1) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr OutfeedOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute OutfeedOpV1GenericAdaptorBase::getOutfeedConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, OutfeedOpV1::getOutfeedConfigAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute OutfeedOpV1GenericAdaptorBase::getOutfeedConfig() {
  auto attr = getOutfeedConfigAttr();
  return attr;
}

} // namespace detail
OutfeedOpV1Adaptor::OutfeedOpV1Adaptor(OutfeedOpV1 op) : OutfeedOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult OutfeedOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_outfeed_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.outfeed' op ""requires attribute 'outfeed_config'");
    if (namedAttrIt->getName() == OutfeedOpV1::getOutfeedConfigAttrName(*odsOpName)) {
      tblgen_outfeed_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_outfeed_config && !((true)))
    return emitError(loc, "'vhlo.outfeed' op ""attribute 'outfeed_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> OutfeedOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true, false};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 1) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range OutfeedOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range OutfeedOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::Value OutfeedOpV1::getToken() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange OutfeedOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange OutfeedOpV1::getTokenMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> OutfeedOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range OutfeedOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute OutfeedOpV1::getOutfeedConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getOutfeedConfigAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute OutfeedOpV1::getOutfeedConfig() {
  auto attr = getOutfeedConfigAttr();
  return attr;
}

void OutfeedOpV1::setOutfeedConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getOutfeedConfigAttrName(), attr);
}

void OutfeedOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::ValueRange inputs, ::mlir::Value token, ::mlir::Attribute outfeed_config) {
  odsState.addOperands(inputs);
  odsState.addOperands(token);
  odsState.addAttribute(getOutfeedConfigAttrName(odsState.name), outfeed_config);
  odsState.addTypes(resultType0);
}

void OutfeedOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange inputs, ::mlir::Value token, ::mlir::Attribute outfeed_config) {
  odsState.addOperands(inputs);
  odsState.addOperands(token);
  odsState.addAttribute(getOutfeedConfigAttrName(odsState.name), outfeed_config);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void OutfeedOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() >= 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult OutfeedOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_outfeed_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'outfeed_config'");
    if (namedAttrIt->getName() == getOutfeedConfigAttrName()) {
      tblgen_outfeed_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_outfeed_config, "outfeed_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult OutfeedOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version OutfeedOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in outfeed");
  return *version;
}
mlir::vhlo::Version OutfeedOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in outfeed");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::OutfeedOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::PadOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
PadOpV1GenericAdaptorBase::PadOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.pad", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> PadOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr PadOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute PadOpV1GenericAdaptorBase::getEdgePaddingLowAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, PadOpV1::getEdgePaddingLowAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute PadOpV1GenericAdaptorBase::getEdgePaddingLow() {
  auto attr = getEdgePaddingLowAttr();
  return attr;
}

::mlir::Attribute PadOpV1GenericAdaptorBase::getEdgePaddingHighAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, PadOpV1::getEdgePaddingHighAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute PadOpV1GenericAdaptorBase::getEdgePaddingHigh() {
  auto attr = getEdgePaddingHighAttr();
  return attr;
}

::mlir::Attribute PadOpV1GenericAdaptorBase::getInteriorPaddingAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, PadOpV1::getInteriorPaddingAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute PadOpV1GenericAdaptorBase::getInteriorPadding() {
  auto attr = getInteriorPaddingAttr();
  return attr;
}

} // namespace detail
PadOpV1Adaptor::PadOpV1Adaptor(PadOpV1 op) : PadOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult PadOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_edge_padding_high;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.pad' op ""requires attribute 'edge_padding_high'");
    if (namedAttrIt->getName() == PadOpV1::getEdgePaddingHighAttrName(*odsOpName)) {
      tblgen_edge_padding_high = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_edge_padding_low;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.pad' op ""requires attribute 'edge_padding_low'");
    if (namedAttrIt->getName() == PadOpV1::getEdgePaddingLowAttrName(*odsOpName)) {
      tblgen_edge_padding_low = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_interior_padding;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.pad' op ""requires attribute 'interior_padding'");
    if (namedAttrIt->getName() == PadOpV1::getInteriorPaddingAttrName(*odsOpName)) {
      tblgen_interior_padding = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_edge_padding_low && !((true)))
    return emitError(loc, "'vhlo.pad' op ""attribute 'edge_padding_low' failed to satisfy constraint: any attribute");

  if (tblgen_edge_padding_high && !((true)))
    return emitError(loc, "'vhlo.pad' op ""attribute 'edge_padding_high' failed to satisfy constraint: any attribute");

  if (tblgen_interior_padding && !((true)))
    return emitError(loc, "'vhlo.pad' op ""attribute 'interior_padding' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> PadOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range PadOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value PadOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value PadOpV1::getPaddingValue() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange PadOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange PadOpV1::getPaddingValueMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> PadOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range PadOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute PadOpV1::getEdgePaddingLowAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getEdgePaddingLowAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute PadOpV1::getEdgePaddingLow() {
  auto attr = getEdgePaddingLowAttr();
  return attr;
}

::mlir::Attribute PadOpV1::getEdgePaddingHighAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getEdgePaddingHighAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute PadOpV1::getEdgePaddingHigh() {
  auto attr = getEdgePaddingHighAttr();
  return attr;
}

::mlir::Attribute PadOpV1::getInteriorPaddingAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getInteriorPaddingAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute PadOpV1::getInteriorPadding() {
  auto attr = getInteriorPaddingAttr();
  return attr;
}

void PadOpV1::setEdgePaddingLowAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEdgePaddingLowAttrName(), attr);
}

void PadOpV1::setEdgePaddingHighAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEdgePaddingHighAttrName(), attr);
}

void PadOpV1::setInteriorPaddingAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getInteriorPaddingAttrName(), attr);
}

void PadOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value padding_value, ::mlir::Attribute edge_padding_low, ::mlir::Attribute edge_padding_high, ::mlir::Attribute interior_padding) {
  odsState.addOperands(operand);
  odsState.addOperands(padding_value);
  odsState.addAttribute(getEdgePaddingLowAttrName(odsState.name), edge_padding_low);
  odsState.addAttribute(getEdgePaddingHighAttrName(odsState.name), edge_padding_high);
  odsState.addAttribute(getInteriorPaddingAttrName(odsState.name), interior_padding);
  odsState.addTypes(resultType0);
}

void PadOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value padding_value, ::mlir::Attribute edge_padding_low, ::mlir::Attribute edge_padding_high, ::mlir::Attribute interior_padding) {
  odsState.addOperands(operand);
  odsState.addOperands(padding_value);
  odsState.addAttribute(getEdgePaddingLowAttrName(odsState.name), edge_padding_low);
  odsState.addAttribute(getEdgePaddingHighAttrName(odsState.name), edge_padding_high);
  odsState.addAttribute(getInteriorPaddingAttrName(odsState.name), interior_padding);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void PadOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult PadOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_edge_padding_high;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'edge_padding_high'");
    if (namedAttrIt->getName() == getEdgePaddingHighAttrName()) {
      tblgen_edge_padding_high = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_edge_padding_low;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'edge_padding_low'");
    if (namedAttrIt->getName() == getEdgePaddingLowAttrName()) {
      tblgen_edge_padding_low = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_interior_padding;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'interior_padding'");
    if (namedAttrIt->getName() == getInteriorPaddingAttrName()) {
      tblgen_interior_padding = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_edge_padding_low, "edge_padding_low")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_edge_padding_high, "edge_padding_high")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_interior_padding, "interior_padding")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult PadOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version PadOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in pad");
  return *version;
}
mlir::vhlo::Version PadOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in pad");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::PadOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::PartitionIdOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
PartitionIdOpV1GenericAdaptorBase::PartitionIdOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.partition_id", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> PartitionIdOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr PartitionIdOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
PartitionIdOpV1Adaptor::PartitionIdOpV1Adaptor(PartitionIdOpV1 op) : PartitionIdOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult PartitionIdOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> PartitionIdOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range PartitionIdOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> PartitionIdOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range PartitionIdOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

void PartitionIdOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0) {
  odsState.addTypes(resultType0);
}

void PartitionIdOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes) {
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void PartitionIdOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult PartitionIdOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult PartitionIdOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version PartitionIdOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.4.0");
  if (failed(version)) llvm_unreachable("invalid version 0.4.0 in partition_id");
  return *version;
}
mlir::vhlo::Version PartitionIdOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in partition_id");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::PartitionIdOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::PopulationCountOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
PopulationCountOpV1GenericAdaptorBase::PopulationCountOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.popcnt", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> PopulationCountOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr PopulationCountOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
PopulationCountOpV1Adaptor::PopulationCountOpV1Adaptor(PopulationCountOpV1 op) : PopulationCountOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult PopulationCountOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> PopulationCountOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range PopulationCountOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value PopulationCountOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange PopulationCountOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> PopulationCountOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range PopulationCountOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value PopulationCountOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void PopulationCountOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void PopulationCountOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void PopulationCountOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult PopulationCountOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult PopulationCountOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version PopulationCountOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in popcnt");
  return *version;
}
mlir::vhlo::Version PopulationCountOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in popcnt");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::PopulationCountOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::PowOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
PowOpV1GenericAdaptorBase::PowOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.power", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> PowOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr PowOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
PowOpV1Adaptor::PowOpV1Adaptor(PowOpV1 op) : PowOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult PowOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> PowOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range PowOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value PowOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value PowOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange PowOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange PowOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> PowOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range PowOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value PowOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void PowOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void PowOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void PowOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult PowOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult PowOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version PowOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in power");
  return *version;
}
mlir::vhlo::Version PowOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in power");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::PowOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RealDynamicSliceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RealDynamicSliceOpV1GenericAdaptorBase::RealDynamicSliceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.real_dynamic_slice", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RealDynamicSliceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RealDynamicSliceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
RealDynamicSliceOpV1Adaptor::RealDynamicSliceOpV1Adaptor(RealDynamicSliceOpV1 op) : RealDynamicSliceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RealDynamicSliceOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RealDynamicSliceOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RealDynamicSliceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RealDynamicSliceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value RealDynamicSliceOpV1::getStartIndices() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value RealDynamicSliceOpV1::getLimitIndices() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::Value RealDynamicSliceOpV1::getStrides() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(3).begin());
}

::mlir::MutableOperandRange RealDynamicSliceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange RealDynamicSliceOpV1::getStartIndicesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange RealDynamicSliceOpV1::getLimitIndicesMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange RealDynamicSliceOpV1::getStridesMutable() {
  auto range = getODSOperandIndexAndLength(3);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RealDynamicSliceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RealDynamicSliceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RealDynamicSliceOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void RealDynamicSliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::Value start_indices, ::mlir::Value limit_indices, ::mlir::Value strides) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addOperands(limit_indices);
  odsState.addOperands(strides);
  odsState.addTypes(result);
}

void RealDynamicSliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value start_indices, ::mlir::Value limit_indices, ::mlir::Value strides) {
  odsState.addOperands(operand);
  odsState.addOperands(start_indices);
  odsState.addOperands(limit_indices);
  odsState.addOperands(strides);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RealDynamicSliceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 4u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RealDynamicSliceOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup3 = getODSOperands(3);

    for (auto v : valueGroup3) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RealDynamicSliceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RealDynamicSliceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in real_dynamic_slice");
  return *version;
}
mlir::vhlo::Version RealDynamicSliceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in real_dynamic_slice");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RealDynamicSliceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RealOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RealOpV1GenericAdaptorBase::RealOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.real", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RealOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RealOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
RealOpV1Adaptor::RealOpV1Adaptor(RealOpV1 op) : RealOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RealOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RealOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RealOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RealOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange RealOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RealOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RealOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RealOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void RealOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void RealOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RealOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RealOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RealOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RealOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in real");
  return *version;
}
mlir::vhlo::Version RealOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in real");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RealOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RecvOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RecvOpV1GenericAdaptorBase::RecvOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.recv", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RecvOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RecvOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute RecvOpV1GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, RecvOpV1::getChannelHandleAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute RecvOpV1GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr;
}

::mlir::Attribute RecvOpV1GenericAdaptorBase::getIsHostTransferAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, RecvOpV1::getIsHostTransferAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> RecvOpV1GenericAdaptorBase::getIsHostTransfer() {
  auto attr = getIsHostTransferAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
RecvOpV1Adaptor::RecvOpV1Adaptor(RecvOpV1 op) : RecvOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RecvOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.recv' op ""requires attribute 'channel_handle'");
    if (namedAttrIt->getName() == RecvOpV1::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_is_host_transfer;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == RecvOpV1::getIsHostTransferAttrName(*odsOpName)) {
      tblgen_is_host_transfer = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.recv' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");

  if (tblgen_is_host_transfer && !((true)))
    return emitError(loc, "'vhlo.recv' op ""attribute 'is_host_transfer' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RecvOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RecvOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RecvOpV1::getToken() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange RecvOpV1::getTokenMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RecvOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range RecvOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute RecvOpV1::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getChannelHandleAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute RecvOpV1::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr;
}

::mlir::Attribute RecvOpV1::getIsHostTransferAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getIsHostTransferAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> RecvOpV1::getIsHostTransfer() {
  auto attr = getIsHostTransferAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void RecvOpV1::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

void RecvOpV1::setIsHostTransferAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIsHostTransferAttrName(), attr);
}

::mlir::Attribute RecvOpV1::removeIsHostTransferAttr() {
  return (*this)->removeAttr(getIsHostTransferAttrName());
}

void RecvOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::Value token, ::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute is_host_transfer) {
  odsState.addOperands(token);
  odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  if (is_host_transfer) {
    odsState.addAttribute(getIsHostTransferAttrName(odsState.name), is_host_transfer);
  }
  odsState.addTypes(resultType0);
}

void RecvOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RecvOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'channel_handle'");
    if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_is_host_transfer;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getIsHostTransferAttrName()) {
      tblgen_is_host_transfer = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_is_host_transfer, "is_host_transfer")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RecvOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RecvOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in recv");
  return *version;
}
mlir::vhlo::Version RecvOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in recv");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RecvOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReduceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReduceOpV1GenericAdaptorBase::ReduceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.reduce", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReduceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 2;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr ReduceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ReduceOpV1GenericAdaptorBase::getDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, ReduceOpV1::getDimensionsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReduceOpV1GenericAdaptorBase::getDimensions() {
  auto attr = getDimensionsAttr();
  return attr;
}

::mlir::Region &ReduceOpV1GenericAdaptorBase::getBody() {
  return *odsRegions[0];
}

::mlir::RegionRange ReduceOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
ReduceOpV1Adaptor::ReduceOpV1Adaptor(ReduceOpV1 op) : ReduceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReduceOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reduce' op ""requires attribute 'dimensions'");
    if (namedAttrIt->getName() == ReduceOpV1::getDimensionsAttrName(*odsOpName)) {
      tblgen_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dimensions && !((true)))
    return emitError(loc, "'vhlo.reduce' op ""attribute 'dimensions' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReduceOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 2;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range ReduceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range ReduceOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::Operation::operand_range ReduceOpV1::getInitValues() {
  return getODSOperands(1);
}

::mlir::MutableOperandRange ReduceOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ReduceOpV1::getInitValuesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReduceOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range ReduceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &ReduceOpV1::getBody() {
  return (*this)->getRegion(0);
}

::mlir::Attribute ReduceOpV1::getDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReduceOpV1::getDimensions() {
  auto attr = getDimensionsAttr();
  return attr;
}

void ReduceOpV1::setDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionsAttrName(), attr);
}

void ReduceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::ValueRange inputs, ::mlir::ValueRange init_values, ::mlir::Attribute dimensions) {
  odsState.addOperands(inputs);
  odsState.addOperands(init_values);
  odsState.addAttribute(getDimensionsAttrName(odsState.name), dimensions);
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void ReduceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReduceOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimensions'");
    if (namedAttrIt->getName() == getDimensionsAttrName()) {
      tblgen_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimensions, "dimensions")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "body", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReduceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReduceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in reduce");
  return *version;
}
mlir::vhlo::Version ReduceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in reduce");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReduceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReducePrecisionOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReducePrecisionOpV1GenericAdaptorBase::ReducePrecisionOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.reduce_precision", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReducePrecisionOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ReducePrecisionOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ReducePrecisionOpV1GenericAdaptorBase::getExponentBitsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, ReducePrecisionOpV1::getExponentBitsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReducePrecisionOpV1GenericAdaptorBase::getExponentBits() {
  auto attr = getExponentBitsAttr();
  return attr;
}

::mlir::Attribute ReducePrecisionOpV1GenericAdaptorBase::getMantissaBitsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, ReducePrecisionOpV1::getMantissaBitsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReducePrecisionOpV1GenericAdaptorBase::getMantissaBits() {
  auto attr = getMantissaBitsAttr();
  return attr;
}

} // namespace detail
ReducePrecisionOpV1Adaptor::ReducePrecisionOpV1Adaptor(ReducePrecisionOpV1 op) : ReducePrecisionOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReducePrecisionOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_exponent_bits;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reduce_precision' op ""requires attribute 'exponent_bits'");
    if (namedAttrIt->getName() == ReducePrecisionOpV1::getExponentBitsAttrName(*odsOpName)) {
      tblgen_exponent_bits = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_mantissa_bits;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reduce_precision' op ""requires attribute 'mantissa_bits'");
    if (namedAttrIt->getName() == ReducePrecisionOpV1::getMantissaBitsAttrName(*odsOpName)) {
      tblgen_mantissa_bits = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_exponent_bits && !((true)))
    return emitError(loc, "'vhlo.reduce_precision' op ""attribute 'exponent_bits' failed to satisfy constraint: any attribute");

  if (tblgen_mantissa_bits && !((true)))
    return emitError(loc, "'vhlo.reduce_precision' op ""attribute 'mantissa_bits' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReducePrecisionOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ReducePrecisionOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ReducePrecisionOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ReducePrecisionOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReducePrecisionOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ReducePrecisionOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ReducePrecisionOpV1::getOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute ReducePrecisionOpV1::getExponentBitsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getExponentBitsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReducePrecisionOpV1::getExponentBits() {
  auto attr = getExponentBitsAttr();
  return attr;
}

::mlir::Attribute ReducePrecisionOpV1::getMantissaBitsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getMantissaBitsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReducePrecisionOpV1::getMantissaBits() {
  auto attr = getMantissaBitsAttr();
  return attr;
}

void ReducePrecisionOpV1::setExponentBitsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getExponentBitsAttrName(), attr);
}

void ReducePrecisionOpV1::setMantissaBitsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getMantissaBitsAttrName(), attr);
}

void ReducePrecisionOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type output, ::mlir::Value operand, ::mlir::Attribute exponent_bits, ::mlir::Attribute mantissa_bits) {
  odsState.addOperands(operand);
  odsState.addAttribute(getExponentBitsAttrName(odsState.name), exponent_bits);
  odsState.addAttribute(getMantissaBitsAttrName(odsState.name), mantissa_bits);
  odsState.addTypes(output);
}

void ReducePrecisionOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute exponent_bits, ::mlir::Attribute mantissa_bits) {
  odsState.addOperands(operand);
  odsState.addAttribute(getExponentBitsAttrName(odsState.name), exponent_bits);
  odsState.addAttribute(getMantissaBitsAttrName(odsState.name), mantissa_bits);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ReducePrecisionOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReducePrecisionOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_exponent_bits;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'exponent_bits'");
    if (namedAttrIt->getName() == getExponentBitsAttrName()) {
      tblgen_exponent_bits = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_mantissa_bits;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'mantissa_bits'");
    if (namedAttrIt->getName() == getMantissaBitsAttrName()) {
      tblgen_mantissa_bits = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_exponent_bits, "exponent_bits")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_mantissa_bits, "mantissa_bits")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReducePrecisionOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReducePrecisionOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in reduce_precision");
  return *version;
}
mlir::vhlo::Version ReducePrecisionOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in reduce_precision");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReducePrecisionOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReduceScatterOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReduceScatterOpV1GenericAdaptorBase::ReduceScatterOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.reduce_scatter", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReduceScatterOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ReduceScatterOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ReduceScatterOpV1GenericAdaptorBase::getScatterDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, ReduceScatterOpV1::getScatterDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReduceScatterOpV1GenericAdaptorBase::getScatterDimension() {
  auto attr = getScatterDimensionAttr();
  return attr;
}

::mlir::Attribute ReduceScatterOpV1GenericAdaptorBase::getReplicaGroupsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, ReduceScatterOpV1::getReplicaGroupsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReduceScatterOpV1GenericAdaptorBase::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute ReduceScatterOpV1GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, ReduceScatterOpV1::getChannelHandleAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ReduceScatterOpV1GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceScatterOpV1GenericAdaptorBase::getUseGlobalDeviceIdsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, ReduceScatterOpV1::getUseGlobalDeviceIdsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ReduceScatterOpV1GenericAdaptorBase::getUseGlobalDeviceIds() {
  auto attr = getUseGlobalDeviceIdsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Region &ReduceScatterOpV1GenericAdaptorBase::getComputation() {
  return *odsRegions[0];
}

::mlir::RegionRange ReduceScatterOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
ReduceScatterOpV1Adaptor::ReduceScatterOpV1Adaptor(ReduceScatterOpV1 op) : ReduceScatterOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReduceScatterOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reduce_scatter' op ""requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == ReduceScatterOpV1::getReplicaGroupsAttrName(*odsOpName)) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == ReduceScatterOpV1::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_scatter_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reduce_scatter' op ""requires attribute 'scatter_dimension'");
    if (namedAttrIt->getName() == ReduceScatterOpV1::getScatterDimensionAttrName(*odsOpName)) {
      tblgen_scatter_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_use_global_device_ids;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == ReduceScatterOpV1::getUseGlobalDeviceIdsAttrName(*odsOpName)) {
      tblgen_use_global_device_ids = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_scatter_dimension && !((true)))
    return emitError(loc, "'vhlo.reduce_scatter' op ""attribute 'scatter_dimension' failed to satisfy constraint: any attribute");

  if (tblgen_replica_groups && !((true)))
    return emitError(loc, "'vhlo.reduce_scatter' op ""attribute 'replica_groups' failed to satisfy constraint: any attribute");

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.reduce_scatter' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");

  if (tblgen_use_global_device_ids && !((true)))
    return emitError(loc, "'vhlo.reduce_scatter' op ""attribute 'use_global_device_ids' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReduceScatterOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ReduceScatterOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ReduceScatterOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ReduceScatterOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReduceScatterOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ReduceScatterOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &ReduceScatterOpV1::getComputation() {
  return (*this)->getRegion(0);
}

::mlir::Attribute ReduceScatterOpV1::getScatterDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getScatterDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReduceScatterOpV1::getScatterDimension() {
  auto attr = getScatterDimensionAttr();
  return attr;
}

::mlir::Attribute ReduceScatterOpV1::getReplicaGroupsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getReplicaGroupsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReduceScatterOpV1::getReplicaGroups() {
  auto attr = getReplicaGroupsAttr();
  return attr;
}

::mlir::Attribute ReduceScatterOpV1::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getChannelHandleAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ReduceScatterOpV1::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceScatterOpV1::getUseGlobalDeviceIdsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getUseGlobalDeviceIdsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ReduceScatterOpV1::getUseGlobalDeviceIds() {
  auto attr = getUseGlobalDeviceIdsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void ReduceScatterOpV1::setScatterDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getScatterDimensionAttrName(), attr);
}

void ReduceScatterOpV1::setReplicaGroupsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getReplicaGroupsAttrName(), attr);
}

void ReduceScatterOpV1::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

void ReduceScatterOpV1::setUseGlobalDeviceIdsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getUseGlobalDeviceIdsAttrName(), attr);
}

::mlir::Attribute ReduceScatterOpV1::removeChannelHandleAttr() {
  return (*this)->removeAttr(getChannelHandleAttrName());
}

::mlir::Attribute ReduceScatterOpV1::removeUseGlobalDeviceIdsAttr() {
  return (*this)->removeAttr(getUseGlobalDeviceIdsAttrName());
}

void ReduceScatterOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute scatter_dimension, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute use_global_device_ids) {
  odsState.addOperands(operand);
  odsState.addAttribute(getScatterDimensionAttrName(odsState.name), scatter_dimension);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  if (use_global_device_ids) {
    odsState.addAttribute(getUseGlobalDeviceIdsAttrName(odsState.name), use_global_device_ids);
  }
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void ReduceScatterOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute scatter_dimension, ::mlir::Attribute replica_groups, /*optional*/::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute use_global_device_ids) {
  odsState.addOperands(operand);
  odsState.addAttribute(getScatterDimensionAttrName(odsState.name), scatter_dimension);
  odsState.addAttribute(getReplicaGroupsAttrName(odsState.name), replica_groups);
  if (channel_handle) {
    odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  }
  if (use_global_device_ids) {
    odsState.addAttribute(getUseGlobalDeviceIdsAttrName(odsState.name), use_global_device_ids);
  }
  (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ReduceScatterOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReduceScatterOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_replica_groups;
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'replica_groups'");
    if (namedAttrIt->getName() == getReplicaGroupsAttrName()) {
      tblgen_replica_groups = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_scatter_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'scatter_dimension'");
    if (namedAttrIt->getName() == getScatterDimensionAttrName()) {
      tblgen_scatter_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_use_global_device_ids;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getUseGlobalDeviceIdsAttrName()) {
      tblgen_use_global_device_ids = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_scatter_dimension, "scatter_dimension")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_replica_groups, "replica_groups")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_use_global_device_ids, "use_global_device_ids")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "computation", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReduceScatterOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReduceScatterOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in reduce_scatter");
  return *version;
}
mlir::vhlo::Version ReduceScatterOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in reduce_scatter");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReduceScatterOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReduceWindowOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReduceWindowOpV1GenericAdaptorBase::ReduceWindowOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.reduce_window", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReduceWindowOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 2;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr ReduceWindowOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ReduceWindowOpV1GenericAdaptorBase::getWindowDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, ReduceWindowOpV1::getWindowDimensionsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReduceWindowOpV1GenericAdaptorBase::getWindowDimensions() {
  auto attr = getWindowDimensionsAttr();
  return attr;
}

::mlir::Attribute ReduceWindowOpV1GenericAdaptorBase::getWindowStridesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, ReduceWindowOpV1::getWindowStridesAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1GenericAdaptorBase::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceWindowOpV1GenericAdaptorBase::getBaseDilationsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, ReduceWindowOpV1::getBaseDilationsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1GenericAdaptorBase::getBaseDilations() {
  auto attr = getBaseDilationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceWindowOpV1GenericAdaptorBase::getWindowDilationsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, ReduceWindowOpV1::getWindowDilationsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1GenericAdaptorBase::getWindowDilations() {
  auto attr = getWindowDilationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceWindowOpV1GenericAdaptorBase::getPaddingAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, ReduceWindowOpV1::getPaddingAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1GenericAdaptorBase::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Region &ReduceWindowOpV1GenericAdaptorBase::getBody() {
  return *odsRegions[0];
}

::mlir::RegionRange ReduceWindowOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
ReduceWindowOpV1Adaptor::ReduceWindowOpV1Adaptor(ReduceWindowOpV1 op) : ReduceWindowOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReduceWindowOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_window_dimensions;
  ::mlir::Attribute tblgen_base_dilations;
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_window_dilations;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reduce_window' op ""requires attribute 'window_dimensions'");
    if (namedAttrIt->getName() == ReduceWindowOpV1::getWindowDimensionsAttrName(*odsOpName)) {
      tblgen_window_dimensions = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == ReduceWindowOpV1::getBaseDilationsAttrName(*odsOpName)) {
      tblgen_base_dilations = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ReduceWindowOpV1::getPaddingAttrName(*odsOpName)) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == ReduceWindowOpV1::getWindowDilationsAttrName(*odsOpName)) {
      tblgen_window_dilations = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == ReduceWindowOpV1::getWindowStridesAttrName(*odsOpName)) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_window_dimensions && !((true)))
    return emitError(loc, "'vhlo.reduce_window' op ""attribute 'window_dimensions' failed to satisfy constraint: any attribute");

  if (tblgen_window_strides && !((true)))
    return emitError(loc, "'vhlo.reduce_window' op ""attribute 'window_strides' failed to satisfy constraint: any attribute");

  if (tblgen_base_dilations && !((true)))
    return emitError(loc, "'vhlo.reduce_window' op ""attribute 'base_dilations' failed to satisfy constraint: any attribute");

  if (tblgen_window_dilations && !((true)))
    return emitError(loc, "'vhlo.reduce_window' op ""attribute 'window_dilations' failed to satisfy constraint: any attribute");

  if (tblgen_padding && !((true)))
    return emitError(loc, "'vhlo.reduce_window' op ""attribute 'padding' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReduceWindowOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 2;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range ReduceWindowOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range ReduceWindowOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::Operation::operand_range ReduceWindowOpV1::getInitValues() {
  return getODSOperands(1);
}

::mlir::MutableOperandRange ReduceWindowOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ReduceWindowOpV1::getInitValuesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReduceWindowOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range ReduceWindowOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &ReduceWindowOpV1::getBody() {
  return (*this)->getRegion(0);
}

::mlir::Attribute ReduceWindowOpV1::getWindowDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getWindowDimensionsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReduceWindowOpV1::getWindowDimensions() {
  auto attr = getWindowDimensionsAttr();
  return attr;
}

::mlir::Attribute ReduceWindowOpV1::getWindowStridesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getWindowStridesAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceWindowOpV1::getBaseDilationsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getBaseDilationsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1::getBaseDilations() {
  auto attr = getBaseDilationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceWindowOpV1::getWindowDilationsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getWindowDilationsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1::getWindowDilations() {
  auto attr = getWindowDilationsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ReduceWindowOpV1::getPaddingAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getPaddingAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ReduceWindowOpV1::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void ReduceWindowOpV1::setWindowDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowDimensionsAttrName(), attr);
}

void ReduceWindowOpV1::setWindowStridesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowStridesAttrName(), attr);
}

void ReduceWindowOpV1::setBaseDilationsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBaseDilationsAttrName(), attr);
}

void ReduceWindowOpV1::setWindowDilationsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowDilationsAttrName(), attr);
}

void ReduceWindowOpV1::setPaddingAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPaddingAttrName(), attr);
}

::mlir::Attribute ReduceWindowOpV1::removeWindowStridesAttr() {
  return (*this)->removeAttr(getWindowStridesAttrName());
}

::mlir::Attribute ReduceWindowOpV1::removeBaseDilationsAttr() {
  return (*this)->removeAttr(getBaseDilationsAttrName());
}

::mlir::Attribute ReduceWindowOpV1::removeWindowDilationsAttr() {
  return (*this)->removeAttr(getWindowDilationsAttrName());
}

::mlir::Attribute ReduceWindowOpV1::removePaddingAttr() {
  return (*this)->removeAttr(getPaddingAttrName());
}

void ReduceWindowOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::ValueRange inputs, ::mlir::ValueRange init_values, ::mlir::Attribute window_dimensions, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute base_dilations, /*optional*/::mlir::Attribute window_dilations, /*optional*/::mlir::Attribute padding) {
  odsState.addOperands(inputs);
  odsState.addOperands(init_values);
  odsState.addAttribute(getWindowDimensionsAttrName(odsState.name), window_dimensions);
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (base_dilations) {
    odsState.addAttribute(getBaseDilationsAttrName(odsState.name), base_dilations);
  }
  if (window_dilations) {
    odsState.addAttribute(getWindowDilationsAttrName(odsState.name), window_dilations);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void ReduceWindowOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReduceWindowOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_window_dimensions;
  ::mlir::Attribute tblgen_base_dilations;
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_window_dilations;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'window_dimensions'");
    if (namedAttrIt->getName() == getWindowDimensionsAttrName()) {
      tblgen_window_dimensions = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getBaseDilationsAttrName()) {
      tblgen_base_dilations = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getPaddingAttrName()) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowDilationsAttrName()) {
      tblgen_window_dilations = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getWindowStridesAttrName()) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_dimensions, "window_dimensions")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_strides, "window_strides")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_base_dilations, "base_dilations")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_dilations, "window_dilations")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_padding, "padding")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "body", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReduceWindowOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReduceWindowOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in reduce_window");
  return *version;
}
mlir::vhlo::Version ReduceWindowOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in reduce_window");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReduceWindowOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RemOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RemOpV1GenericAdaptorBase::RemOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.remainder", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RemOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RemOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
RemOpV1Adaptor::RemOpV1Adaptor(RemOpV1 op) : RemOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RemOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RemOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RemOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RemOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value RemOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange RemOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange RemOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RemOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RemOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RemOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void RemOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void RemOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RemOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RemOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RemOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RemOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in remainder");
  return *version;
}
mlir::vhlo::Version RemOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in remainder");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RemOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReplicaIdOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReplicaIdOpV1GenericAdaptorBase::ReplicaIdOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.replica_id", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReplicaIdOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ReplicaIdOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ReplicaIdOpV1Adaptor::ReplicaIdOpV1Adaptor(ReplicaIdOpV1 op) : ReplicaIdOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReplicaIdOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReplicaIdOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ReplicaIdOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> ReplicaIdOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ReplicaIdOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

void ReplicaIdOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0) {
  odsState.addTypes(resultType0);
}

void ReplicaIdOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes) {
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ReplicaIdOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReplicaIdOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReplicaIdOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReplicaIdOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in replica_id");
  return *version;
}
mlir::vhlo::Version ReplicaIdOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in replica_id");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReplicaIdOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReshapeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReshapeOpV1GenericAdaptorBase::ReshapeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.reshape", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReshapeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ReshapeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ReshapeOpV1Adaptor::ReshapeOpV1Adaptor(ReshapeOpV1 op) : ReshapeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReshapeOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReshapeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ReshapeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ReshapeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ReshapeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReshapeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ReshapeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

void ReshapeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(resultType0);
}

void ReshapeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ReshapeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReshapeOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReshapeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReshapeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in reshape");
  return *version;
}
mlir::vhlo::Version ReshapeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in reshape");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReshapeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReturnOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReturnOpV1GenericAdaptorBase::ReturnOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.return", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReturnOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr ReturnOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ReturnOpV1Adaptor::ReturnOpV1Adaptor(ReturnOpV1 op) : ReturnOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReturnOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReturnOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range ReturnOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range ReturnOpV1::getResults() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange ReturnOpV1::getResultsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReturnOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ReturnOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

void ReturnOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::ValueRange results) {
  odsState.addOperands(results);
}

void ReturnOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 0u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReturnOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReturnOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

::mlir::ParseResult ReturnOpV1::parse(::mlir::OpAsmParser &parser, ::mlir::OperationState &result) {
  ::llvm::SmallVector<::mlir::OpAsmParser::UnresolvedOperand, 4> resultsOperands;
  ::llvm::SMLoc resultsOperandsLoc;
  (void)resultsOperandsLoc;
  ::llvm::SmallVector<::mlir::Type, 1> resultsTypes;

  resultsOperandsLoc = parser.getCurrentLocation();
  if (parser.parseOperandList(resultsOperands))
    return ::mlir::failure();
  if (parser.parseOptionalAttrDict(result.attributes))
    return ::mlir::failure();
  if (::mlir::succeeded(parser.parseOptionalColon())) {

  if (parser.parseTypeList(resultsTypes))
    return ::mlir::failure();
  }
  if (parser.resolveOperands(resultsOperands, resultsTypes, resultsOperandsLoc, result.operands))
    return ::mlir::failure();
  return ::mlir::success();
}

void ReturnOpV1::print(::mlir::OpAsmPrinter &_odsPrinter) {
  _odsPrinter << ' ';
  _odsPrinter << getResults();
  ::llvm::SmallVector<::llvm::StringRef, 2> elidedAttrs;
  _odsPrinter.printOptionalAttrDict((*this)->getAttrs(), elidedAttrs);
  if (!getResults().empty()) {
    _odsPrinter << ' ' << ":";
    _odsPrinter << ' ';
    _odsPrinter << getResults().getTypes();
  }
}

mlir::vhlo::Version ReturnOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in return");
  return *version;
}
mlir::vhlo::Version ReturnOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in return");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReturnOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ReverseOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ReverseOpV1GenericAdaptorBase::ReverseOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.reverse", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ReverseOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ReverseOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ReverseOpV1GenericAdaptorBase::getDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, ReverseOpV1::getDimensionsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ReverseOpV1GenericAdaptorBase::getDimensions() {
  auto attr = getDimensionsAttr();
  return attr;
}

} // namespace detail
ReverseOpV1Adaptor::ReverseOpV1Adaptor(ReverseOpV1 op) : ReverseOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ReverseOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.reverse' op ""requires attribute 'dimensions'");
    if (namedAttrIt->getName() == ReverseOpV1::getDimensionsAttrName(*odsOpName)) {
      tblgen_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dimensions && !((true)))
    return emitError(loc, "'vhlo.reverse' op ""attribute 'dimensions' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ReverseOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ReverseOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ReverseOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange ReverseOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ReverseOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ReverseOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ReverseOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute ReverseOpV1::getDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ReverseOpV1::getDimensions() {
  auto attr = getDimensionsAttr();
  return attr;
}

void ReverseOpV1::setDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionsAttrName(), attr);
}

void ReverseOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand, ::mlir::Attribute dimensions) {
  odsState.addOperands(operand);
  odsState.addAttribute(getDimensionsAttrName(odsState.name), dimensions);
  odsState.addTypes(result);
}

void ReverseOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute dimensions) {
  odsState.addOperands(operand);
  odsState.addAttribute(getDimensionsAttrName(odsState.name), dimensions);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ReverseOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ReverseOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimensions;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimensions'");
    if (namedAttrIt->getName() == getDimensionsAttrName()) {
      tblgen_dimensions = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimensions, "dimensions")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ReverseOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ReverseOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in reverse");
  return *version;
}
mlir::vhlo::Version ReverseOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in reverse");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ReverseOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RngBitGeneratorOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RngBitGeneratorOpV1GenericAdaptorBase::RngBitGeneratorOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.rng_bit_generator", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RngBitGeneratorOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RngBitGeneratorOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute RngBitGeneratorOpV1GenericAdaptorBase::getRngAlgorithmAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, RngBitGeneratorOpV1::getRngAlgorithmAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute RngBitGeneratorOpV1GenericAdaptorBase::getRngAlgorithm() {
  auto attr = getRngAlgorithmAttr();
  return attr;
}

} // namespace detail
RngBitGeneratorOpV1Adaptor::RngBitGeneratorOpV1Adaptor(RngBitGeneratorOpV1 op) : RngBitGeneratorOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RngBitGeneratorOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_rng_algorithm;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.rng_bit_generator' op ""requires attribute 'rng_algorithm'");
    if (namedAttrIt->getName() == RngBitGeneratorOpV1::getRngAlgorithmAttrName(*odsOpName)) {
      tblgen_rng_algorithm = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_rng_algorithm && !((true)))
    return emitError(loc, "'vhlo.rng_bit_generator' op ""attribute 'rng_algorithm' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

void RngBitGeneratorOpV1::getAsmResultNames(::mlir::OpAsmSetValueNameFn setNameFn) {
  auto resultGroup0 = getODSResults(0);
  if (!resultGroup0.empty())
    setNameFn(*resultGroup0.begin(), "output_state");
  auto resultGroup1 = getODSResults(1);
  if (!resultGroup1.empty())
    setNameFn(*resultGroup1.begin(), "output");
}

std::pair<unsigned, unsigned> RngBitGeneratorOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RngBitGeneratorOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RngBitGeneratorOpV1::getInitialState() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange RngBitGeneratorOpV1::getInitialStateMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RngBitGeneratorOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RngBitGeneratorOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RngBitGeneratorOpV1::getOutputState() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Value RngBitGeneratorOpV1::getOutput() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(1).begin());
}

::mlir::Attribute RngBitGeneratorOpV1::getRngAlgorithmAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getRngAlgorithmAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute RngBitGeneratorOpV1::getRngAlgorithm() {
  auto attr = getRngAlgorithmAttr();
  return attr;
}

void RngBitGeneratorOpV1::setRngAlgorithmAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getRngAlgorithmAttrName(), attr);
}

void RngBitGeneratorOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type output_state, ::mlir::Type output, ::mlir::Attribute rng_algorithm, ::mlir::Value initial_state) {
  odsState.addOperands(initial_state);
  odsState.addAttribute(getRngAlgorithmAttrName(odsState.name), rng_algorithm);
  odsState.addTypes(output_state);
  odsState.addTypes(output);
}

void RngBitGeneratorOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Attribute rng_algorithm, ::mlir::Value initial_state) {
  odsState.addOperands(initial_state);
  odsState.addAttribute(getRngAlgorithmAttrName(odsState.name), rng_algorithm);
  assert(resultTypes.size() == 2u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RngBitGeneratorOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 2u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RngBitGeneratorOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_rng_algorithm;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'rng_algorithm'");
    if (namedAttrIt->getName() == getRngAlgorithmAttrName()) {
      tblgen_rng_algorithm = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_rng_algorithm, "rng_algorithm")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSResults(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RngBitGeneratorOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RngBitGeneratorOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in rng_bit_generator");
  return *version;
}
mlir::vhlo::Version RngBitGeneratorOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in rng_bit_generator");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RngBitGeneratorOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RngOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RngOpV1GenericAdaptorBase::RngOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.rng", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RngOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RngOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute RngOpV1GenericAdaptorBase::getRngDistributionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, RngOpV1::getRngDistributionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute RngOpV1GenericAdaptorBase::getRngDistribution() {
  auto attr = getRngDistributionAttr();
  return attr;
}

} // namespace detail
RngOpV1Adaptor::RngOpV1Adaptor(RngOpV1 op) : RngOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RngOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_rng_distribution;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.rng' op ""requires attribute 'rng_distribution'");
    if (namedAttrIt->getName() == RngOpV1::getRngDistributionAttrName(*odsOpName)) {
      tblgen_rng_distribution = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_rng_distribution && !((true)))
    return emitError(loc, "'vhlo.rng' op ""attribute 'rng_distribution' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RngOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RngOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RngOpV1::getA() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value RngOpV1::getB() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value RngOpV1::getShape() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange RngOpV1::getAMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange RngOpV1::getBMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange RngOpV1::getShapeMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RngOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RngOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RngOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

::mlir::Attribute RngOpV1::getRngDistributionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getRngDistributionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute RngOpV1::getRngDistribution() {
  auto attr = getRngDistributionAttr();
  return attr;
}

void RngOpV1::setRngDistributionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getRngDistributionAttrName(), attr);
}

void RngOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value a, ::mlir::Value b, ::mlir::Value shape, ::mlir::Attribute rng_distribution) {
  odsState.addOperands(a);
  odsState.addOperands(b);
  odsState.addOperands(shape);
  odsState.addAttribute(getRngDistributionAttrName(odsState.name), rng_distribution);
  odsState.addTypes(result);
}

void RngOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value a, ::mlir::Value b, ::mlir::Value shape, ::mlir::Attribute rng_distribution) {
  odsState.addOperands(a);
  odsState.addOperands(b);
  odsState.addOperands(shape);
  odsState.addAttribute(getRngDistributionAttrName(odsState.name), rng_distribution);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RngOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RngOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_rng_distribution;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'rng_distribution'");
    if (namedAttrIt->getName() == getRngDistributionAttrName()) {
      tblgen_rng_distribution = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_rng_distribution, "rng_distribution")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RngOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RngOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in rng");
  return *version;
}
mlir::vhlo::Version RngOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in rng");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RngOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RoundNearestEvenOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RoundNearestEvenOpV1GenericAdaptorBase::RoundNearestEvenOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.round_nearest_even", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RoundNearestEvenOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RoundNearestEvenOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
RoundNearestEvenOpV1Adaptor::RoundNearestEvenOpV1Adaptor(RoundNearestEvenOpV1 op) : RoundNearestEvenOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RoundNearestEvenOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RoundNearestEvenOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RoundNearestEvenOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RoundNearestEvenOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange RoundNearestEvenOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RoundNearestEvenOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RoundNearestEvenOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RoundNearestEvenOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void RoundNearestEvenOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void RoundNearestEvenOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RoundNearestEvenOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RoundNearestEvenOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RoundNearestEvenOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RoundNearestEvenOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in round_nearest_even");
  return *version;
}
mlir::vhlo::Version RoundNearestEvenOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in round_nearest_even");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RoundNearestEvenOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RoundOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RoundOpV1GenericAdaptorBase::RoundOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.round_nearest_afz", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RoundOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RoundOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
RoundOpV1Adaptor::RoundOpV1Adaptor(RoundOpV1 op) : RoundOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RoundOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RoundOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RoundOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RoundOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange RoundOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RoundOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RoundOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RoundOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void RoundOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void RoundOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RoundOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RoundOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RoundOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RoundOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in round_nearest_afz");
  return *version;
}
mlir::vhlo::Version RoundOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in round_nearest_afz");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RoundOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::RsqrtOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
RsqrtOpV1GenericAdaptorBase::RsqrtOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.rsqrt", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> RsqrtOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr RsqrtOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
RsqrtOpV1Adaptor::RsqrtOpV1Adaptor(RsqrtOpV1 op) : RsqrtOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult RsqrtOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> RsqrtOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range RsqrtOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RsqrtOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange RsqrtOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> RsqrtOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range RsqrtOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value RsqrtOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void RsqrtOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void RsqrtOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void RsqrtOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult RsqrtOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult RsqrtOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version RsqrtOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in rsqrt");
  return *version;
}
mlir::vhlo::Version RsqrtOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in rsqrt");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::RsqrtOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ScatterOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ScatterOpV1GenericAdaptorBase::ScatterOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.scatter", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ScatterOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true, false, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 1) / 2;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr ScatterOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute ScatterOpV1GenericAdaptorBase::getScatterDimensionNumbersAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, ScatterOpV1::getScatterDimensionNumbersAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute ScatterOpV1GenericAdaptorBase::getScatterDimensionNumbers() {
  auto attr = getScatterDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute ScatterOpV1GenericAdaptorBase::getIndicesAreSortedAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, ScatterOpV1::getIndicesAreSortedAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ScatterOpV1GenericAdaptorBase::getIndicesAreSorted() {
  auto attr = getIndicesAreSortedAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ScatterOpV1GenericAdaptorBase::getUniqueIndicesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, ScatterOpV1::getUniqueIndicesAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> ScatterOpV1GenericAdaptorBase::getUniqueIndices() {
  auto attr = getUniqueIndicesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Region &ScatterOpV1GenericAdaptorBase::getUpdateComputation() {
  return *odsRegions[0];
}

::mlir::RegionRange ScatterOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
ScatterOpV1Adaptor::ScatterOpV1Adaptor(ScatterOpV1 op) : ScatterOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ScatterOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_scatter_dimension_numbers;
  ::mlir::Attribute tblgen_indices_are_sorted;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.scatter' op ""requires attribute 'scatter_dimension_numbers'");
    if (namedAttrIt->getName() == ScatterOpV1::getScatterDimensionNumbersAttrName(*odsOpName)) {
      tblgen_scatter_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == ScatterOpV1::getIndicesAreSortedAttrName(*odsOpName)) {
      tblgen_indices_are_sorted = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_unique_indices;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == ScatterOpV1::getUniqueIndicesAttrName(*odsOpName)) {
      tblgen_unique_indices = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_scatter_dimension_numbers && !((true)))
    return emitError(loc, "'vhlo.scatter' op ""attribute 'scatter_dimension_numbers' failed to satisfy constraint: any attribute");

  if (tblgen_indices_are_sorted && !((true)))
    return emitError(loc, "'vhlo.scatter' op ""attribute 'indices_are_sorted' failed to satisfy constraint: any attribute");

  if (tblgen_unique_indices && !((true)))
    return emitError(loc, "'vhlo.scatter' op ""attribute 'unique_indices' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ScatterOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true, false, true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 1) / 2;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range ScatterOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range ScatterOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::Value ScatterOpV1::getScatterIndices() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Operation::operand_range ScatterOpV1::getUpdates() {
  return getODSOperands(2);
}

::mlir::MutableOperandRange ScatterOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ScatterOpV1::getScatterIndicesMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ScatterOpV1::getUpdatesMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ScatterOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range ScatterOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &ScatterOpV1::getUpdateComputation() {
  return (*this)->getRegion(0);
}

::mlir::Attribute ScatterOpV1::getScatterDimensionNumbersAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getScatterDimensionNumbersAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute ScatterOpV1::getScatterDimensionNumbers() {
  auto attr = getScatterDimensionNumbersAttr();
  return attr;
}

::mlir::Attribute ScatterOpV1::getIndicesAreSortedAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getIndicesAreSortedAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ScatterOpV1::getIndicesAreSorted() {
  auto attr = getIndicesAreSortedAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute ScatterOpV1::getUniqueIndicesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getUniqueIndicesAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> ScatterOpV1::getUniqueIndices() {
  auto attr = getUniqueIndicesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void ScatterOpV1::setScatterDimensionNumbersAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getScatterDimensionNumbersAttrName(), attr);
}

void ScatterOpV1::setIndicesAreSortedAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIndicesAreSortedAttrName(), attr);
}

void ScatterOpV1::setUniqueIndicesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getUniqueIndicesAttrName(), attr);
}

::mlir::Attribute ScatterOpV1::removeIndicesAreSortedAttr() {
  return (*this)->removeAttr(getIndicesAreSortedAttrName());
}

::mlir::Attribute ScatterOpV1::removeUniqueIndicesAttr() {
  return (*this)->removeAttr(getUniqueIndicesAttrName());
}

void ScatterOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::ValueRange inputs, ::mlir::Value scatter_indices, ::mlir::ValueRange updates, ::mlir::Attribute scatter_dimension_numbers, /*optional*/::mlir::Attribute indices_are_sorted, /*optional*/::mlir::Attribute unique_indices) {
  odsState.addOperands(inputs);
  odsState.addOperands(scatter_indices);
  odsState.addOperands(updates);
  odsState.addAttribute(getScatterDimensionNumbersAttrName(odsState.name), scatter_dimension_numbers);
  if (indices_are_sorted) {
    odsState.addAttribute(getIndicesAreSortedAttrName(odsState.name), indices_are_sorted);
  }
  if (unique_indices) {
    odsState.addAttribute(getUniqueIndicesAttrName(odsState.name), unique_indices);
  }
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void ScatterOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() >= 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ScatterOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_scatter_dimension_numbers;
  ::mlir::Attribute tblgen_indices_are_sorted;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'scatter_dimension_numbers'");
    if (namedAttrIt->getName() == getScatterDimensionNumbersAttrName()) {
      tblgen_scatter_dimension_numbers = namedAttrIt->getValue();
      break;
    }
    else if (namedAttrIt->getName() == getIndicesAreSortedAttrName()) {
      tblgen_indices_are_sorted = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_unique_indices;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getUniqueIndicesAttrName()) {
      tblgen_unique_indices = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_scatter_dimension_numbers, "scatter_dimension_numbers")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_indices_are_sorted, "indices_are_sorted")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_unique_indices, "unique_indices")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "update_computation", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult ScatterOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ScatterOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in scatter");
  return *version;
}
mlir::vhlo::Version ScatterOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in scatter");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ScatterOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SelectAndScatterOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SelectAndScatterOpV1GenericAdaptorBase::SelectAndScatterOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.select_and_scatter", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SelectAndScatterOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SelectAndScatterOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute SelectAndScatterOpV1GenericAdaptorBase::getWindowDimensionsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SelectAndScatterOpV1::getWindowDimensionsAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> SelectAndScatterOpV1GenericAdaptorBase::getWindowDimensions() {
  auto attr = getWindowDimensionsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute SelectAndScatterOpV1GenericAdaptorBase::getWindowStridesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SelectAndScatterOpV1::getWindowStridesAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> SelectAndScatterOpV1GenericAdaptorBase::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute SelectAndScatterOpV1GenericAdaptorBase::getPaddingAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SelectAndScatterOpV1::getPaddingAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> SelectAndScatterOpV1GenericAdaptorBase::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Region &SelectAndScatterOpV1GenericAdaptorBase::getSelect() {
  return *odsRegions[0];
}

::mlir::Region &SelectAndScatterOpV1GenericAdaptorBase::getScatter() {
  return *odsRegions[1];
}

::mlir::RegionRange SelectAndScatterOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
SelectAndScatterOpV1Adaptor::SelectAndScatterOpV1Adaptor(SelectAndScatterOpV1 op) : SelectAndScatterOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SelectAndScatterOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_window_dimensions;
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == SelectAndScatterOpV1::getPaddingAttrName(*odsOpName)) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == SelectAndScatterOpV1::getWindowDimensionsAttrName(*odsOpName)) {
      tblgen_window_dimensions = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == SelectAndScatterOpV1::getWindowStridesAttrName(*odsOpName)) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_window_dimensions && !((true)))
    return emitError(loc, "'vhlo.select_and_scatter' op ""attribute 'window_dimensions' failed to satisfy constraint: any attribute");

  if (tblgen_window_strides && !((true)))
    return emitError(loc, "'vhlo.select_and_scatter' op ""attribute 'window_strides' failed to satisfy constraint: any attribute");

  if (tblgen_padding && !((true)))
    return emitError(loc, "'vhlo.select_and_scatter' op ""attribute 'padding' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SelectAndScatterOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SelectAndScatterOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SelectAndScatterOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value SelectAndScatterOpV1::getSource() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value SelectAndScatterOpV1::getInitValue() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange SelectAndScatterOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SelectAndScatterOpV1::getSourceMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SelectAndScatterOpV1::getInitValueMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SelectAndScatterOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SelectAndScatterOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &SelectAndScatterOpV1::getSelect() {
  return (*this)->getRegion(0);
}

::mlir::Region &SelectAndScatterOpV1::getScatter() {
  return (*this)->getRegion(1);
}

::mlir::Attribute SelectAndScatterOpV1::getWindowDimensionsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getWindowDimensionsAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> SelectAndScatterOpV1::getWindowDimensions() {
  auto attr = getWindowDimensionsAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute SelectAndScatterOpV1::getWindowStridesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getWindowStridesAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> SelectAndScatterOpV1::getWindowStrides() {
  auto attr = getWindowStridesAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute SelectAndScatterOpV1::getPaddingAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getPaddingAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> SelectAndScatterOpV1::getPadding() {
  auto attr = getPaddingAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void SelectAndScatterOpV1::setWindowDimensionsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowDimensionsAttrName(), attr);
}

void SelectAndScatterOpV1::setWindowStridesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getWindowStridesAttrName(), attr);
}

void SelectAndScatterOpV1::setPaddingAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPaddingAttrName(), attr);
}

::mlir::Attribute SelectAndScatterOpV1::removeWindowDimensionsAttr() {
  return (*this)->removeAttr(getWindowDimensionsAttrName());
}

::mlir::Attribute SelectAndScatterOpV1::removeWindowStridesAttr() {
  return (*this)->removeAttr(getWindowStridesAttrName());
}

::mlir::Attribute SelectAndScatterOpV1::removePaddingAttr() {
  return (*this)->removeAttr(getPaddingAttrName());
}

void SelectAndScatterOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value source, ::mlir::Value init_value, /*optional*/::mlir::Attribute window_dimensions, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute padding) {
  odsState.addOperands(operand);
  odsState.addOperands(source);
  odsState.addOperands(init_value);
  if (window_dimensions) {
    odsState.addAttribute(getWindowDimensionsAttrName(odsState.name), window_dimensions);
  }
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  (void)odsState.addRegion();
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void SelectAndScatterOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value source, ::mlir::Value init_value, /*optional*/::mlir::Attribute window_dimensions, /*optional*/::mlir::Attribute window_strides, /*optional*/::mlir::Attribute padding) {
  odsState.addOperands(operand);
  odsState.addOperands(source);
  odsState.addOperands(init_value);
  if (window_dimensions) {
    odsState.addAttribute(getWindowDimensionsAttrName(odsState.name), window_dimensions);
  }
  if (window_strides) {
    odsState.addAttribute(getWindowStridesAttrName(odsState.name), window_strides);
  }
  if (padding) {
    odsState.addAttribute(getPaddingAttrName(odsState.name), padding);
  }
  (void)odsState.addRegion();
  (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SelectAndScatterOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 2; ++i)
    (void)odsState.addRegion();
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SelectAndScatterOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_padding;
  ::mlir::Attribute tblgen_window_dimensions;
  ::mlir::Attribute tblgen_window_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getPaddingAttrName()) {
      tblgen_padding = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowDimensionsAttrName()) {
      tblgen_window_dimensions = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getWindowStridesAttrName()) {
      tblgen_window_strides = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_dimensions, "window_dimensions")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_window_strides, "window_strides")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_padding, "padding")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "select", index++)))
        return ::mlir::failure();

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(1)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "scatter", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult SelectAndScatterOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SelectAndScatterOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in select_and_scatter");
  return *version;
}
mlir::vhlo::Version SelectAndScatterOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in select_and_scatter");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SelectAndScatterOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SelectOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SelectOpV1GenericAdaptorBase::SelectOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.select", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SelectOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SelectOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
SelectOpV1Adaptor::SelectOpV1Adaptor(SelectOpV1 op) : SelectOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SelectOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SelectOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SelectOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SelectOpV1::getPred() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value SelectOpV1::getOnTrue() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::Value SelectOpV1::getOnFalse() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(2).begin());
}

::mlir::MutableOperandRange SelectOpV1::getPredMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SelectOpV1::getOnTrueMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SelectOpV1::getOnFalseMutable() {
  auto range = getODSOperandIndexAndLength(2);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SelectOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SelectOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SelectOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void SelectOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value pred, ::mlir::Value on_true, ::mlir::Value on_false) {
  odsState.addOperands(pred);
  odsState.addOperands(on_true);
  odsState.addOperands(on_false);
  odsState.addTypes(result);
}

void SelectOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value pred, ::mlir::Value on_true, ::mlir::Value on_false) {
  odsState.addOperands(pred);
  odsState.addOperands(on_true);
  odsState.addOperands(on_false);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SelectOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 3u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SelectOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup2 = getODSOperands(2);

    for (auto v : valueGroup2) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SelectOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SelectOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in select");
  return *version;
}
mlir::vhlo::Version SelectOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in select");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SelectOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SendOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SendOpV1GenericAdaptorBase::SendOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.send", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SendOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true, false};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 1) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr SendOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute SendOpV1GenericAdaptorBase::getChannelHandleAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SendOpV1::getChannelHandleAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute SendOpV1GenericAdaptorBase::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr;
}

::mlir::Attribute SendOpV1GenericAdaptorBase::getIsHostTransferAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, SendOpV1::getIsHostTransferAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> SendOpV1GenericAdaptorBase::getIsHostTransfer() {
  auto attr = getIsHostTransferAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

} // namespace detail
SendOpV1Adaptor::SendOpV1Adaptor(SendOpV1 op) : SendOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SendOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.send' op ""requires attribute 'channel_handle'");
    if (namedAttrIt->getName() == SendOpV1::getChannelHandleAttrName(*odsOpName)) {
      tblgen_channel_handle = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_is_host_transfer;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == SendOpV1::getIsHostTransferAttrName(*odsOpName)) {
      tblgen_is_host_transfer = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_channel_handle && !((true)))
    return emitError(loc, "'vhlo.send' op ""attribute 'channel_handle' failed to satisfy constraint: any attribute");

  if (tblgen_is_host_transfer && !((true)))
    return emitError(loc, "'vhlo.send' op ""attribute 'is_host_transfer' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SendOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true, false};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 1) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range SendOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range SendOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::Value SendOpV1::getToken() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange SendOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SendOpV1::getTokenMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SendOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SendOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute SendOpV1::getChannelHandleAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getChannelHandleAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute SendOpV1::getChannelHandle() {
  auto attr = getChannelHandleAttr();
  return attr;
}

::mlir::Attribute SendOpV1::getIsHostTransferAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getIsHostTransferAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> SendOpV1::getIsHostTransfer() {
  auto attr = getIsHostTransferAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void SendOpV1::setChannelHandleAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getChannelHandleAttrName(), attr);
}

void SendOpV1::setIsHostTransferAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIsHostTransferAttrName(), attr);
}

::mlir::Attribute SendOpV1::removeIsHostTransferAttr() {
  return (*this)->removeAttr(getIsHostTransferAttrName());
}

void SendOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::ValueRange inputs, ::mlir::Value token, ::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute is_host_transfer) {
  odsState.addOperands(inputs);
  odsState.addOperands(token);
  odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  if (is_host_transfer) {
    odsState.addAttribute(getIsHostTransferAttrName(odsState.name), is_host_transfer);
  }
  odsState.addTypes(resultType0);
}

void SendOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange inputs, ::mlir::Value token, ::mlir::Attribute channel_handle, /*optional*/::mlir::Attribute is_host_transfer) {
  odsState.addOperands(inputs);
  odsState.addOperands(token);
  odsState.addAttribute(getChannelHandleAttrName(odsState.name), channel_handle);
  if (is_host_transfer) {
    odsState.addAttribute(getIsHostTransferAttrName(odsState.name), is_host_transfer);
  }
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SendOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() >= 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SendOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_channel_handle;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'channel_handle'");
    if (namedAttrIt->getName() == getChannelHandleAttrName()) {
      tblgen_channel_handle = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_is_host_transfer;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getIsHostTransferAttrName()) {
      tblgen_is_host_transfer = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_channel_handle, "channel_handle")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_is_host_transfer, "is_host_transfer")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SendOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SendOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in send");
  return *version;
}
mlir::vhlo::Version SendOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in send");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SendOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SetDimensionSizeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SetDimensionSizeOpV1GenericAdaptorBase::SetDimensionSizeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.set_dimension_size", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SetDimensionSizeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SetDimensionSizeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute SetDimensionSizeOpV1GenericAdaptorBase::getDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SetDimensionSizeOpV1::getDimensionAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute SetDimensionSizeOpV1GenericAdaptorBase::getDimension() {
  auto attr = getDimensionAttr();
  return attr;
}

} // namespace detail
SetDimensionSizeOpV1Adaptor::SetDimensionSizeOpV1Adaptor(SetDimensionSizeOpV1 op) : SetDimensionSizeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SetDimensionSizeOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.set_dimension_size' op ""requires attribute 'dimension'");
    if (namedAttrIt->getName() == SetDimensionSizeOpV1::getDimensionAttrName(*odsOpName)) {
      tblgen_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dimension && !((true)))
    return emitError(loc, "'vhlo.set_dimension_size' op ""attribute 'dimension' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SetDimensionSizeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SetDimensionSizeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SetDimensionSizeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value SetDimensionSizeOpV1::getSize() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange SetDimensionSizeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SetDimensionSizeOpV1::getSizeMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SetDimensionSizeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SetDimensionSizeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute SetDimensionSizeOpV1::getDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute SetDimensionSizeOpV1::getDimension() {
  auto attr = getDimensionAttr();
  return attr;
}

void SetDimensionSizeOpV1::setDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionAttrName(), attr);
}

void SetDimensionSizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value size, ::mlir::Attribute dimension) {
  odsState.addOperands(operand);
  odsState.addOperands(size);
  odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  odsState.addTypes(resultType0);
}

void SetDimensionSizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value size, ::mlir::Attribute dimension) {
  odsState.addOperands(operand);
  odsState.addOperands(size);
  odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SetDimensionSizeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SetDimensionSizeOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dimension'");
    if (namedAttrIt->getName() == getDimensionAttrName()) {
      tblgen_dimension = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension, "dimension")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SetDimensionSizeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SetDimensionSizeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in set_dimension_size");
  return *version;
}
mlir::vhlo::Version SetDimensionSizeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in set_dimension_size");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SetDimensionSizeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ShiftLeftOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ShiftLeftOpV1GenericAdaptorBase::ShiftLeftOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.shift_left", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ShiftLeftOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ShiftLeftOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ShiftLeftOpV1Adaptor::ShiftLeftOpV1Adaptor(ShiftLeftOpV1 op) : ShiftLeftOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ShiftLeftOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ShiftLeftOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ShiftLeftOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ShiftLeftOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ShiftLeftOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange ShiftLeftOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ShiftLeftOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ShiftLeftOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ShiftLeftOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ShiftLeftOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ShiftLeftOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void ShiftLeftOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ShiftLeftOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ShiftLeftOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ShiftLeftOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ShiftLeftOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in shift_left");
  return *version;
}
mlir::vhlo::Version ShiftLeftOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in shift_left");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ShiftLeftOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ShiftRightArithmeticOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ShiftRightArithmeticOpV1GenericAdaptorBase::ShiftRightArithmeticOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.shift_right_arithmetic", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ShiftRightArithmeticOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ShiftRightArithmeticOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ShiftRightArithmeticOpV1Adaptor::ShiftRightArithmeticOpV1Adaptor(ShiftRightArithmeticOpV1 op) : ShiftRightArithmeticOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ShiftRightArithmeticOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ShiftRightArithmeticOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ShiftRightArithmeticOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ShiftRightArithmeticOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ShiftRightArithmeticOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange ShiftRightArithmeticOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ShiftRightArithmeticOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ShiftRightArithmeticOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ShiftRightArithmeticOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ShiftRightArithmeticOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ShiftRightArithmeticOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void ShiftRightArithmeticOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ShiftRightArithmeticOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ShiftRightArithmeticOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ShiftRightArithmeticOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ShiftRightArithmeticOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in shift_right_arithmetic");
  return *version;
}
mlir::vhlo::Version ShiftRightArithmeticOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in shift_right_arithmetic");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ShiftRightArithmeticOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::ShiftRightLogicalOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
ShiftRightLogicalOpV1GenericAdaptorBase::ShiftRightLogicalOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.shift_right_logical", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> ShiftRightLogicalOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr ShiftRightLogicalOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
ShiftRightLogicalOpV1Adaptor::ShiftRightLogicalOpV1Adaptor(ShiftRightLogicalOpV1 op) : ShiftRightLogicalOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult ShiftRightLogicalOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ShiftRightLogicalOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ShiftRightLogicalOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ShiftRightLogicalOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value ShiftRightLogicalOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange ShiftRightLogicalOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange ShiftRightLogicalOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> ShiftRightLogicalOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ShiftRightLogicalOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value ShiftRightLogicalOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void ShiftRightLogicalOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void ShiftRightLogicalOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void ShiftRightLogicalOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult ShiftRightLogicalOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult ShiftRightLogicalOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version ShiftRightLogicalOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in shift_right_logical");
  return *version;
}
mlir::vhlo::Version ShiftRightLogicalOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in shift_right_logical");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::ShiftRightLogicalOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SignOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SignOpV1GenericAdaptorBase::SignOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.sign", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SignOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SignOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
SignOpV1Adaptor::SignOpV1Adaptor(SignOpV1 op) : SignOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SignOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SignOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SignOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SignOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange SignOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SignOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SignOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SignOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void SignOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void SignOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SignOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SignOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SignOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SignOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in sign");
  return *version;
}
mlir::vhlo::Version SignOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in sign");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SignOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SineOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SineOpV1GenericAdaptorBase::SineOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.sine", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SineOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SineOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
SineOpV1Adaptor::SineOpV1Adaptor(SineOpV1 op) : SineOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SineOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SineOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SineOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SineOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange SineOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SineOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SineOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SineOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void SineOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void SineOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SineOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SineOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SineOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SineOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in sine");
  return *version;
}
mlir::vhlo::Version SineOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in sine");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SineOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SliceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SliceOpV1GenericAdaptorBase::SliceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.slice", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SliceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SliceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute SliceOpV1GenericAdaptorBase::getStartIndicesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 1, SliceOpV1::getStartIndicesAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute SliceOpV1GenericAdaptorBase::getStartIndices() {
  auto attr = getStartIndicesAttr();
  return attr;
}

::mlir::Attribute SliceOpV1GenericAdaptorBase::getLimitIndicesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 2, SliceOpV1::getLimitIndicesAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute SliceOpV1GenericAdaptorBase::getLimitIndices() {
  auto attr = getLimitIndicesAttr();
  return attr;
}

::mlir::Attribute SliceOpV1GenericAdaptorBase::getStridesAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 0, SliceOpV1::getStridesAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute SliceOpV1GenericAdaptorBase::getStrides() {
  auto attr = getStridesAttr();
  return attr;
}

} // namespace detail
SliceOpV1Adaptor::SliceOpV1Adaptor(SliceOpV1 op) : SliceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SliceOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_limit_indices;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.slice' op ""requires attribute 'limit_indices'");
    if (namedAttrIt->getName() == SliceOpV1::getLimitIndicesAttrName(*odsOpName)) {
      tblgen_limit_indices = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_start_indices;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.slice' op ""requires attribute 'start_indices'");
    if (namedAttrIt->getName() == SliceOpV1::getStartIndicesAttrName(*odsOpName)) {
      tblgen_start_indices = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.slice' op ""requires attribute 'strides'");
    if (namedAttrIt->getName() == SliceOpV1::getStridesAttrName(*odsOpName)) {
      tblgen_strides = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_start_indices && !((true)))
    return emitError(loc, "'vhlo.slice' op ""attribute 'start_indices' failed to satisfy constraint: any attribute");

  if (tblgen_limit_indices && !((true)))
    return emitError(loc, "'vhlo.slice' op ""attribute 'limit_indices' failed to satisfy constraint: any attribute");

  if (tblgen_strides && !((true)))
    return emitError(loc, "'vhlo.slice' op ""attribute 'strides' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SliceOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SliceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SliceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange SliceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SliceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SliceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute SliceOpV1::getStartIndicesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 1, getStartIndicesAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute SliceOpV1::getStartIndices() {
  auto attr = getStartIndicesAttr();
  return attr;
}

::mlir::Attribute SliceOpV1::getLimitIndicesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 2, getLimitIndicesAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute SliceOpV1::getLimitIndices() {
  auto attr = getLimitIndicesAttr();
  return attr;
}

::mlir::Attribute SliceOpV1::getStridesAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 0, getStridesAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute SliceOpV1::getStrides() {
  auto attr = getStridesAttr();
  return attr;
}

void SliceOpV1::setStartIndicesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getStartIndicesAttrName(), attr);
}

void SliceOpV1::setLimitIndicesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLimitIndicesAttrName(), attr);
}

void SliceOpV1::setStridesAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getStridesAttrName(), attr);
}

void SliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute start_indices, ::mlir::Attribute limit_indices, ::mlir::Attribute strides) {
  odsState.addOperands(operand);
  odsState.addAttribute(getStartIndicesAttrName(odsState.name), start_indices);
  odsState.addAttribute(getLimitIndicesAttrName(odsState.name), limit_indices);
  odsState.addAttribute(getStridesAttrName(odsState.name), strides);
  odsState.addTypes(resultType0);
}

void SliceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute start_indices, ::mlir::Attribute limit_indices, ::mlir::Attribute strides) {
  odsState.addOperands(operand);
  odsState.addAttribute(getStartIndicesAttrName(odsState.name), start_indices);
  odsState.addAttribute(getLimitIndicesAttrName(odsState.name), limit_indices);
  odsState.addAttribute(getStridesAttrName(odsState.name), strides);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SliceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SliceOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_limit_indices;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'limit_indices'");
    if (namedAttrIt->getName() == getLimitIndicesAttrName()) {
      tblgen_limit_indices = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_start_indices;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'start_indices'");
    if (namedAttrIt->getName() == getStartIndicesAttrName()) {
      tblgen_start_indices = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_strides;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'strides'");
    if (namedAttrIt->getName() == getStridesAttrName()) {
      tblgen_strides = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_start_indices, "start_indices")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_limit_indices, "limit_indices")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_strides, "strides")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SliceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SliceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in slice");
  return *version;
}
mlir::vhlo::Version SliceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in slice");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SliceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SortOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SortOpV1GenericAdaptorBase::SortOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.sort", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SortOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr SortOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute SortOpV1GenericAdaptorBase::getDimensionAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SortOpV1::getDimensionAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> SortOpV1GenericAdaptorBase::getDimension() {
  auto attr = getDimensionAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute SortOpV1GenericAdaptorBase::getIsStableAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, SortOpV1::getIsStableAttrName(*odsOpName)).dyn_cast_or_null<::mlir::Attribute>();
  return attr;
}

::std::optional<::mlir::Attribute> SortOpV1GenericAdaptorBase::getIsStable() {
  auto attr = getIsStableAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Region &SortOpV1GenericAdaptorBase::getComparator() {
  return *odsRegions[0];
}

::mlir::RegionRange SortOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
SortOpV1Adaptor::SortOpV1Adaptor(SortOpV1 op) : SortOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SortOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  ::mlir::Attribute tblgen_is_stable;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == SortOpV1::getDimensionAttrName(*odsOpName)) {
      tblgen_dimension = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == SortOpV1::getIsStableAttrName(*odsOpName)) {
      tblgen_is_stable = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (tblgen_dimension && !((true)))
    return emitError(loc, "'vhlo.sort' op ""attribute 'dimension' failed to satisfy constraint: any attribute");

  if (tblgen_is_stable && !((true)))
    return emitError(loc, "'vhlo.sort' op ""attribute 'is_stable' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SortOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range SortOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range SortOpV1::getInputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange SortOpV1::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SortOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range SortOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &SortOpV1::getComparator() {
  return (*this)->getRegion(0);
}

::mlir::Attribute SortOpV1::getDimensionAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getDimensionAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> SortOpV1::getDimension() {
  auto attr = getDimensionAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

::mlir::Attribute SortOpV1::getIsStableAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getIsStableAttrName()).dyn_cast_or_null<::mlir::Attribute>();
}

::std::optional<::mlir::Attribute> SortOpV1::getIsStable() {
  auto attr = getIsStableAttr();
  return attr ? ::std::optional<::mlir::Attribute>(attr) : (::std::nullopt);
}

void SortOpV1::setDimensionAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimensionAttrName(), attr);
}

void SortOpV1::setIsStableAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getIsStableAttrName(), attr);
}

::mlir::Attribute SortOpV1::removeDimensionAttr() {
  return (*this)->removeAttr(getDimensionAttrName());
}

::mlir::Attribute SortOpV1::removeIsStableAttr() {
  return (*this)->removeAttr(getIsStableAttrName());
}

void SortOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultType0, ::mlir::ValueRange inputs, /*optional*/::mlir::Attribute dimension, /*optional*/::mlir::Attribute is_stable) {
  odsState.addOperands(inputs);
  if (dimension) {
    odsState.addAttribute(getDimensionAttrName(odsState.name), dimension);
  }
  if (is_stable) {
    odsState.addAttribute(getIsStableAttrName(odsState.name), is_stable);
  }
  (void)odsState.addRegion();
  odsState.addTypes(resultType0);
}

void SortOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SortOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_dimension;
  ::mlir::Attribute tblgen_is_stable;
  while (true) {
    if (namedAttrIt == namedAttrRange.end()) {
      break;
    }
    else if (namedAttrIt->getName() == getDimensionAttrName()) {
      tblgen_dimension = namedAttrIt->getValue();
    }
    else if (namedAttrIt->getName() == getIsStableAttrName()) {
      tblgen_is_stable = namedAttrIt->getValue();
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dimension, "dimension")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_is_stable, "is_stable")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "comparator", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult SortOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SortOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in sort");
  return *version;
}
mlir::vhlo::Version SortOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in sort");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SortOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SqrtOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SqrtOpV1GenericAdaptorBase::SqrtOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.sqrt", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SqrtOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SqrtOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
SqrtOpV1Adaptor::SqrtOpV1Adaptor(SqrtOpV1 op) : SqrtOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SqrtOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SqrtOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SqrtOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SqrtOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange SqrtOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SqrtOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SqrtOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SqrtOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void SqrtOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void SqrtOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SqrtOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SqrtOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SqrtOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SqrtOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in sqrt");
  return *version;
}
mlir::vhlo::Version SqrtOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in sqrt");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SqrtOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::SubtractOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
SubtractOpV1GenericAdaptorBase::SubtractOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.subtract", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> SubtractOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr SubtractOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
SubtractOpV1Adaptor::SubtractOpV1Adaptor(SubtractOpV1 op) : SubtractOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult SubtractOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> SubtractOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range SubtractOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SubtractOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value SubtractOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange SubtractOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange SubtractOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> SubtractOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range SubtractOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value SubtractOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void SubtractOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void SubtractOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void SubtractOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult SubtractOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult SubtractOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version SubtractOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in subtract");
  return *version;
}
mlir::vhlo::Version SubtractOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in subtract");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::SubtractOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::TanhOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
TanhOpV1GenericAdaptorBase::TanhOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.tanh", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> TanhOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr TanhOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
TanhOpV1Adaptor::TanhOpV1Adaptor(TanhOpV1 op) : TanhOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult TanhOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> TanhOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range TanhOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TanhOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange TanhOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> TanhOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range TanhOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TanhOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void TanhOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void TanhOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void TanhOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult TanhOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult TanhOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version TanhOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in tanh");
  return *version;
}
mlir::vhlo::Version TanhOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in tanh");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TanhOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::TorchIndexSelectOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
TorchIndexSelectOpV1GenericAdaptorBase::TorchIndexSelectOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.torch_index_select", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> TorchIndexSelectOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr TorchIndexSelectOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute TorchIndexSelectOpV1GenericAdaptorBase::getDimAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 0, TorchIndexSelectOpV1::getDimAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TorchIndexSelectOpV1GenericAdaptorBase::getDim() {
  auto attr = getDimAttr();
  return attr;
}

::mlir::Attribute TorchIndexSelectOpV1GenericAdaptorBase::getBatchDimsAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 1, TorchIndexSelectOpV1::getBatchDimsAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TorchIndexSelectOpV1GenericAdaptorBase::getBatchDims() {
  auto attr = getBatchDimsAttr();
  return attr;
}

} // namespace detail
TorchIndexSelectOpV1Adaptor::TorchIndexSelectOpV1Adaptor(TorchIndexSelectOpV1 op) : TorchIndexSelectOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult TorchIndexSelectOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_batch_dims;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.torch_index_select' op ""requires attribute 'batch_dims'");
    if (namedAttrIt->getName() == TorchIndexSelectOpV1::getBatchDimsAttrName(*odsOpName)) {
      tblgen_batch_dims = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_dim;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.torch_index_select' op ""requires attribute 'dim'");
    if (namedAttrIt->getName() == TorchIndexSelectOpV1::getDimAttrName(*odsOpName)) {
      tblgen_dim = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_dim && !((true)))
    return emitError(loc, "'vhlo.torch_index_select' op ""attribute 'dim' failed to satisfy constraint: any attribute");

  if (tblgen_batch_dims && !((true)))
    return emitError(loc, "'vhlo.torch_index_select' op ""attribute 'batch_dims' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> TorchIndexSelectOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range TorchIndexSelectOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TorchIndexSelectOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value TorchIndexSelectOpV1::getIndex() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange TorchIndexSelectOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange TorchIndexSelectOpV1::getIndexMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> TorchIndexSelectOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range TorchIndexSelectOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute TorchIndexSelectOpV1::getDimAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 0, getDimAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TorchIndexSelectOpV1::getDim() {
  auto attr = getDimAttr();
  return attr;
}

::mlir::Attribute TorchIndexSelectOpV1::getBatchDimsAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 1, getBatchDimsAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TorchIndexSelectOpV1::getBatchDims() {
  auto attr = getBatchDimsAttr();
  return attr;
}

void TorchIndexSelectOpV1::setDimAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getDimAttrName(), attr);
}

void TorchIndexSelectOpV1::setBatchDimsAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getBatchDimsAttrName(), attr);
}

void TorchIndexSelectOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Value index, ::mlir::Attribute dim, ::mlir::Attribute batch_dims) {
  odsState.addOperands(operand);
  odsState.addOperands(index);
  odsState.addAttribute(getDimAttrName(odsState.name), dim);
  odsState.addAttribute(getBatchDimsAttrName(odsState.name), batch_dims);
  odsState.addTypes(resultType0);
}

void TorchIndexSelectOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Value index, ::mlir::Attribute dim, ::mlir::Attribute batch_dims) {
  odsState.addOperands(operand);
  odsState.addOperands(index);
  odsState.addAttribute(getDimAttrName(odsState.name), dim);
  odsState.addAttribute(getBatchDimsAttrName(odsState.name), batch_dims);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void TorchIndexSelectOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult TorchIndexSelectOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_batch_dims;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'batch_dims'");
    if (namedAttrIt->getName() == getBatchDimsAttrName()) {
      tblgen_batch_dims = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_dim;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'dim'");
    if (namedAttrIt->getName() == getDimAttrName()) {
      tblgen_dim = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_dim, "dim")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_batch_dims, "batch_dims")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult TorchIndexSelectOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version TorchIndexSelectOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in torch_index_select");
  return *version;
}
mlir::vhlo::Version TorchIndexSelectOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in torch_index_select");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TorchIndexSelectOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::TraceOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
TraceOpV1GenericAdaptorBase::TraceOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.trace", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> TraceOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr TraceOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute TraceOpV1GenericAdaptorBase::getTagAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, TraceOpV1::getTagAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TraceOpV1GenericAdaptorBase::getTag() {
  auto attr = getTagAttr();
  return attr;
}

} // namespace detail
TraceOpV1Adaptor::TraceOpV1Adaptor(TraceOpV1 op) : TraceOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult TraceOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_tag;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.trace' op ""requires attribute 'tag'");
    if (namedAttrIt->getName() == TraceOpV1::getTagAttrName(*odsOpName)) {
      tblgen_tag = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_tag && !((true)))
    return emitError(loc, "'vhlo.trace' op ""attribute 'tag' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> TraceOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range TraceOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TraceOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange TraceOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> TraceOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range TraceOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute TraceOpV1::getTagAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getTagAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TraceOpV1::getTag() {
  auto attr = getTagAttr();
  return attr;
}

void TraceOpV1::setTagAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getTagAttrName(), attr);
}

void TraceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Value operand, ::mlir::Attribute tag) {
  odsState.addOperands(operand);
  odsState.addAttribute(getTagAttrName(odsState.name), tag);
}

void TraceOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute tag) {
  odsState.addOperands(operand);
  odsState.addAttribute(getTagAttrName(odsState.name), tag);
  assert(resultTypes.size() == 0u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void TraceOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 0u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult TraceOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_tag;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'tag'");
    if (namedAttrIt->getName() == getTagAttrName()) {
      tblgen_tag = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_tag, "tag")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult TraceOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version TraceOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in trace");
  return *version;
}
mlir::vhlo::Version TraceOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in trace");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TraceOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::TransposeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
TransposeOpV1GenericAdaptorBase::TransposeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.transpose", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> TransposeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr TransposeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute TransposeOpV1GenericAdaptorBase::getPermutationAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, TransposeOpV1::getPermutationAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TransposeOpV1GenericAdaptorBase::getPermutation() {
  auto attr = getPermutationAttr();
  return attr;
}

} // namespace detail
TransposeOpV1Adaptor::TransposeOpV1Adaptor(TransposeOpV1 op) : TransposeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult TransposeOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_permutation;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.transpose' op ""requires attribute 'permutation'");
    if (namedAttrIt->getName() == TransposeOpV1::getPermutationAttrName(*odsOpName)) {
      tblgen_permutation = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_permutation && !((true)))
    return emitError(loc, "'vhlo.transpose' op ""attribute 'permutation' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> TransposeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range TransposeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TransposeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange TransposeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> TransposeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range TransposeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute TransposeOpV1::getPermutationAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getPermutationAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TransposeOpV1::getPermutation() {
  auto attr = getPermutationAttr();
  return attr;
}

void TransposeOpV1::setPermutationAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getPermutationAttrName(), attr);
}

void TransposeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute permutation) {
  odsState.addOperands(operand);
  odsState.addAttribute(getPermutationAttrName(odsState.name), permutation);
  odsState.addTypes(resultType0);
}

void TransposeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute permutation) {
  odsState.addOperands(operand);
  odsState.addAttribute(getPermutationAttrName(odsState.name), permutation);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void TransposeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult TransposeOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_permutation;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'permutation'");
    if (namedAttrIt->getName() == getPermutationAttrName()) {
      tblgen_permutation = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_permutation, "permutation")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult TransposeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version TransposeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in transpose");
  return *version;
}
mlir::vhlo::Version TransposeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in transpose");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TransposeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::TriangularSolveOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
TriangularSolveOpV1GenericAdaptorBase::TriangularSolveOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.triangular_solve", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> TriangularSolveOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr TriangularSolveOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getLeftSideAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 3, TriangularSolveOpV1::getLeftSideAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getLeftSide() {
  auto attr = getLeftSideAttr();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getLowerAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 1, odsAttrs.end() - 2, TriangularSolveOpV1::getLowerAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getLower() {
  auto attr = getLowerAttr();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getUnitDiagonalAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 3, odsAttrs.end() - 0, TriangularSolveOpV1::getUnitDiagonalAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getUnitDiagonal() {
  auto attr = getUnitDiagonalAttr();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getTransposeAAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 2, odsAttrs.end() - 1, TriangularSolveOpV1::getTransposeAAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1GenericAdaptorBase::getTransposeA() {
  auto attr = getTransposeAAttr();
  return attr;
}

} // namespace detail
TriangularSolveOpV1Adaptor::TriangularSolveOpV1Adaptor(TriangularSolveOpV1 op) : TriangularSolveOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult TriangularSolveOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_left_side;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.triangular_solve' op ""requires attribute 'left_side'");
    if (namedAttrIt->getName() == TriangularSolveOpV1::getLeftSideAttrName(*odsOpName)) {
      tblgen_left_side = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_lower;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.triangular_solve' op ""requires attribute 'lower'");
    if (namedAttrIt->getName() == TriangularSolveOpV1::getLowerAttrName(*odsOpName)) {
      tblgen_lower = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_transpose_a;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.triangular_solve' op ""requires attribute 'transpose_a'");
    if (namedAttrIt->getName() == TriangularSolveOpV1::getTransposeAAttrName(*odsOpName)) {
      tblgen_transpose_a = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_unit_diagonal;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.triangular_solve' op ""requires attribute 'unit_diagonal'");
    if (namedAttrIt->getName() == TriangularSolveOpV1::getUnitDiagonalAttrName(*odsOpName)) {
      tblgen_unit_diagonal = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_left_side && !((true)))
    return emitError(loc, "'vhlo.triangular_solve' op ""attribute 'left_side' failed to satisfy constraint: any attribute");

  if (tblgen_lower && !((true)))
    return emitError(loc, "'vhlo.triangular_solve' op ""attribute 'lower' failed to satisfy constraint: any attribute");

  if (tblgen_unit_diagonal && !((true)))
    return emitError(loc, "'vhlo.triangular_solve' op ""attribute 'unit_diagonal' failed to satisfy constraint: any attribute");

  if (tblgen_transpose_a && !((true)))
    return emitError(loc, "'vhlo.triangular_solve' op ""attribute 'transpose_a' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> TriangularSolveOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range TriangularSolveOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TriangularSolveOpV1::getA() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value TriangularSolveOpV1::getB() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange TriangularSolveOpV1::getAMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange TriangularSolveOpV1::getBMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> TriangularSolveOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range TriangularSolveOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute TriangularSolveOpV1::getLeftSideAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 3, getLeftSideAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TriangularSolveOpV1::getLeftSide() {
  auto attr = getLeftSideAttr();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1::getLowerAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 1, (*this)->getAttrs().end() - 2, getLowerAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TriangularSolveOpV1::getLower() {
  auto attr = getLowerAttr();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1::getUnitDiagonalAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 3, (*this)->getAttrs().end() - 0, getUnitDiagonalAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TriangularSolveOpV1::getUnitDiagonal() {
  auto attr = getUnitDiagonalAttr();
  return attr;
}

::mlir::Attribute TriangularSolveOpV1::getTransposeAAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 2, (*this)->getAttrs().end() - 1, getTransposeAAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute TriangularSolveOpV1::getTransposeA() {
  auto attr = getTransposeAAttr();
  return attr;
}

void TriangularSolveOpV1::setLeftSideAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLeftSideAttrName(), attr);
}

void TriangularSolveOpV1::setLowerAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getLowerAttrName(), attr);
}

void TriangularSolveOpV1::setUnitDiagonalAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getUnitDiagonalAttrName(), attr);
}

void TriangularSolveOpV1::setTransposeAAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getTransposeAAttrName(), attr);
}

void TriangularSolveOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value a, ::mlir::Value b, ::mlir::Attribute left_side, ::mlir::Attribute lower, ::mlir::Attribute unit_diagonal, ::mlir::Attribute transpose_a) {
  odsState.addOperands(a);
  odsState.addOperands(b);
  odsState.addAttribute(getLeftSideAttrName(odsState.name), left_side);
  odsState.addAttribute(getLowerAttrName(odsState.name), lower);
  odsState.addAttribute(getUnitDiagonalAttrName(odsState.name), unit_diagonal);
  odsState.addAttribute(getTransposeAAttrName(odsState.name), transpose_a);
  odsState.addTypes(resultType0);
}

void TriangularSolveOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value a, ::mlir::Value b, ::mlir::Attribute left_side, ::mlir::Attribute lower, ::mlir::Attribute unit_diagonal, ::mlir::Attribute transpose_a) {
  odsState.addOperands(a);
  odsState.addOperands(b);
  odsState.addAttribute(getLeftSideAttrName(odsState.name), left_side);
  odsState.addAttribute(getLowerAttrName(odsState.name), lower);
  odsState.addAttribute(getUnitDiagonalAttrName(odsState.name), unit_diagonal);
  odsState.addAttribute(getTransposeAAttrName(odsState.name), transpose_a);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void TriangularSolveOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult TriangularSolveOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_left_side;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'left_side'");
    if (namedAttrIt->getName() == getLeftSideAttrName()) {
      tblgen_left_side = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_lower;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'lower'");
    if (namedAttrIt->getName() == getLowerAttrName()) {
      tblgen_lower = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_transpose_a;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'transpose_a'");
    if (namedAttrIt->getName() == getTransposeAAttrName()) {
      tblgen_transpose_a = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }
  ::mlir::Attribute tblgen_unit_diagonal;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'unit_diagonal'");
    if (namedAttrIt->getName() == getUnitDiagonalAttrName()) {
      tblgen_unit_diagonal = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_left_side, "left_side")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_lower, "lower")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_unit_diagonal, "unit_diagonal")))
    return ::mlir::failure();

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_transpose_a, "transpose_a")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult TriangularSolveOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version TriangularSolveOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in triangular_solve");
  return *version;
}
mlir::vhlo::Version TriangularSolveOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in triangular_solve");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TriangularSolveOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::TupleOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
TupleOpV1GenericAdaptorBase::TupleOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.tuple", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> TupleOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr TupleOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
TupleOpV1Adaptor::TupleOpV1Adaptor(TupleOpV1 op) : TupleOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult TupleOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> TupleOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range TupleOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range TupleOpV1::getVal() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange TupleOpV1::getValMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> TupleOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range TupleOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value TupleOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void TupleOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::ValueRange val) {
  odsState.addOperands(val);
  odsState.addTypes(result);
}

void TupleOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult TupleOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult TupleOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version TupleOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in tuple");
  return *version;
}
mlir::vhlo::Version TupleOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in tuple");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::TupleOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::UnaryEinsumOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
UnaryEinsumOpV1GenericAdaptorBase::UnaryEinsumOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.unary_einsum", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> UnaryEinsumOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr UnaryEinsumOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Attribute UnaryEinsumOpV1GenericAdaptorBase::getEinsumConfigAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  auto attr = ::mlir::impl::getAttrFromSortedRange(odsAttrs.begin() + 0, odsAttrs.end() - 0, UnaryEinsumOpV1::getEinsumConfigAttrName(*odsOpName)).cast<::mlir::Attribute>();
  return attr;
}

::mlir::Attribute UnaryEinsumOpV1GenericAdaptorBase::getEinsumConfig() {
  auto attr = getEinsumConfigAttr();
  return attr;
}

} // namespace detail
UnaryEinsumOpV1Adaptor::UnaryEinsumOpV1Adaptor(UnaryEinsumOpV1 op) : UnaryEinsumOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult UnaryEinsumOpV1Adaptor::verify(::mlir::Location loc) {
  auto namedAttrRange = odsAttrs;
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_einsum_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitError(loc, "'vhlo.unary_einsum' op ""requires attribute 'einsum_config'");
    if (namedAttrIt->getName() == UnaryEinsumOpV1::getEinsumConfigAttrName(*odsOpName)) {
      tblgen_einsum_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (tblgen_einsum_config && !((true)))
    return emitError(loc, "'vhlo.unary_einsum' op ""attribute 'einsum_config' failed to satisfy constraint: any attribute");
  return ::mlir::success();
}

std::pair<unsigned, unsigned> UnaryEinsumOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range UnaryEinsumOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value UnaryEinsumOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange UnaryEinsumOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> UnaryEinsumOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range UnaryEinsumOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Attribute UnaryEinsumOpV1::getEinsumConfigAttr() {
  return ::mlir::impl::getAttrFromSortedRange((*this)->getAttrs().begin() + 0, (*this)->getAttrs().end() - 0, getEinsumConfigAttrName()).cast<::mlir::Attribute>();
}

::mlir::Attribute UnaryEinsumOpV1::getEinsumConfig() {
  auto attr = getEinsumConfigAttr();
  return attr;
}

void UnaryEinsumOpV1::setEinsumConfigAttr(::mlir::Attribute attr) {
  (*this)->setAttr(getEinsumConfigAttrName(), attr);
}

void UnaryEinsumOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type resultType0, ::mlir::Value operand, ::mlir::Attribute einsum_config) {
  odsState.addOperands(operand);
  odsState.addAttribute(getEinsumConfigAttrName(odsState.name), einsum_config);
  odsState.addTypes(resultType0);
}

void UnaryEinsumOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand, ::mlir::Attribute einsum_config) {
  odsState.addOperands(operand);
  odsState.addAttribute(getEinsumConfigAttrName(odsState.name), einsum_config);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void UnaryEinsumOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult UnaryEinsumOpV1::verifyInvariantsImpl() {
  auto namedAttrRange = (*this)->getAttrs();
  auto namedAttrIt = namedAttrRange.begin();
  ::mlir::Attribute tblgen_einsum_config;
  while (true) {
    if (namedAttrIt == namedAttrRange.end())
      return emitOpError("requires attribute 'einsum_config'");
    if (namedAttrIt->getName() == getEinsumConfigAttrName()) {
      tblgen_einsum_config = namedAttrIt->getValue();
      break;
    }
    ++namedAttrIt;
  }

  if (::mlir::failed(__mlir_ods_local_attr_constraint_VhloOps0(*this, tblgen_einsum_config, "einsum_config")))
    return ::mlir::failure();
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult UnaryEinsumOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version UnaryEinsumOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in unary_einsum");
  return *version;
}
mlir::vhlo::Version UnaryEinsumOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in unary_einsum");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::UnaryEinsumOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::UniformDequantizeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
UniformDequantizeOpV1GenericAdaptorBase::UniformDequantizeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.uniform_dequantize", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> UniformDequantizeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr UniformDequantizeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
UniformDequantizeOpV1Adaptor::UniformDequantizeOpV1Adaptor(UniformDequantizeOpV1 op) : UniformDequantizeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult UniformDequantizeOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> UniformDequantizeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range UniformDequantizeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value UniformDequantizeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange UniformDequantizeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> UniformDequantizeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range UniformDequantizeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value UniformDequantizeOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void UniformDequantizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void UniformDequantizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void UniformDequantizeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult UniformDequantizeOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult UniformDequantizeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version UniformDequantizeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in uniform_dequantize");
  return *version;
}
mlir::vhlo::Version UniformDequantizeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in uniform_dequantize");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::UniformDequantizeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::UniformQuantizeOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
UniformQuantizeOpV1GenericAdaptorBase::UniformQuantizeOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.uniform_quantize", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> UniformQuantizeOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr UniformQuantizeOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
UniformQuantizeOpV1Adaptor::UniformQuantizeOpV1Adaptor(UniformQuantizeOpV1 op) : UniformQuantizeOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult UniformQuantizeOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> UniformQuantizeOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range UniformQuantizeOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value UniformQuantizeOpV1::getOperand() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::MutableOperandRange UniformQuantizeOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> UniformQuantizeOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range UniformQuantizeOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value UniformQuantizeOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void UniformQuantizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value operand) {
  odsState.addOperands(operand);
  odsState.addTypes(result);
}

void UniformQuantizeOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value operand) {
  odsState.addOperands(operand);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void UniformQuantizeOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 1u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult UniformQuantizeOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult UniformQuantizeOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version UniformQuantizeOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in uniform_quantize");
  return *version;
}
mlir::vhlo::Version UniformQuantizeOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in uniform_quantize");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::UniformQuantizeOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::WhileOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
WhileOpV1GenericAdaptorBase::WhileOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.while", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> WhileOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperandsSize - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::DictionaryAttr WhileOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

::mlir::Region &WhileOpV1GenericAdaptorBase::getCond() {
  return *odsRegions[0];
}

::mlir::Region &WhileOpV1GenericAdaptorBase::getBody() {
  return *odsRegions[1];
}

::mlir::RegionRange WhileOpV1GenericAdaptorBase::getRegions() {
  return odsRegions;
}

} // namespace detail
WhileOpV1Adaptor::WhileOpV1Adaptor(WhileOpV1 op) : WhileOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult WhileOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> WhileOpV1::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range WhileOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range WhileOpV1::getOperand() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange WhileOpV1::getOperandMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> WhileOpV1::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range WhileOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &WhileOpV1::getCond() {
  return (*this)->getRegion(0);
}

::mlir::Region &WhileOpV1::getBody() {
  return (*this)->getRegion(1);
}

void WhileOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 2; ++i)
    (void)odsState.addRegion();
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult WhileOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "cond", index++)))
        return ::mlir::failure();

    for (auto &region : ::llvm::MutableArrayRef((*this)->getRegion(1)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_VhloOps0(*this, region, "body", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult WhileOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version WhileOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in while");
  return *version;
}
mlir::vhlo::Version WhileOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in while");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::WhileOpV1)

namespace mlir {
namespace vhlo {

//===----------------------------------------------------------------------===//
// ::mlir::vhlo::XorOpV1 definitions
//===----------------------------------------------------------------------===//

namespace detail {
XorOpV1GenericAdaptorBase::XorOpV1GenericAdaptorBase(::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsAttrs(attrs), odsRegions(regions) {  if (odsAttrs)
    odsOpName.emplace("vhlo.xor", odsAttrs.getContext());
}

std::pair<unsigned, unsigned> XorOpV1GenericAdaptorBase::getODSOperandIndexAndLength(unsigned index, unsigned odsOperandsSize) {
  return {index, 1};
}

::mlir::DictionaryAttr XorOpV1GenericAdaptorBase::getAttributes() {
  return odsAttrs;
}

} // namespace detail
XorOpV1Adaptor::XorOpV1Adaptor(XorOpV1 op) : XorOpV1Adaptor(op->getOperands(), op->getAttrDictionary(), op->getRegions()) {}

::mlir::LogicalResult XorOpV1Adaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> XorOpV1::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range XorOpV1::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value XorOpV1::getLhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(0).begin());
}

::mlir::Value XorOpV1::getRhs() {
  return ::llvm::cast<::mlir::Value>(*getODSOperands(1).begin());
}

::mlir::MutableOperandRange XorOpV1::getLhsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange XorOpV1::getRhsMutable() {
  auto range = getODSOperandIndexAndLength(1);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> XorOpV1::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range XorOpV1::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Value XorOpV1::getResult() {
  return ::llvm::cast<::mlir::Value>(*getODSResults(0).begin());
}

void XorOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::Type result, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  odsState.addTypes(result);
}

void XorOpV1::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::Value lhs, ::mlir::Value rhs) {
  odsState.addOperands(lhs);
  odsState.addOperands(rhs);
  assert(resultTypes.size() == 1u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void XorOpV1::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 2u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  assert(resultTypes.size() == 1u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult XorOpV1::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
    auto valueGroup1 = getODSOperands(1);

    for (auto v : valueGroup1) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_VhloOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult XorOpV1::verifyInvariants() {
  return verifyInvariantsImpl();
}

mlir::vhlo::Version XorOpV1::getMinVersion() {
  auto version = mlir::vhlo::Version::fromString("0.3.0");
  if (failed(version)) llvm_unreachable("invalid version 0.3.0 in xor");
  return *version;
}
mlir::vhlo::Version XorOpV1::getMaxVersion() {
  if (!strcmp("current", "current")) return VhloDialect::getCurrentVersion();
  auto version = mlir::vhlo::Version::fromString("current");
  if (failed(version)) llvm_unreachable("invalid version current in xor");
  return *version;
}
} // namespace vhlo
} // namespace mlir
MLIR_DEFINE_EXPLICIT_TYPE_ID(::mlir::vhlo::XorOpV1)


#endif  // GET_OP_CLASSES

