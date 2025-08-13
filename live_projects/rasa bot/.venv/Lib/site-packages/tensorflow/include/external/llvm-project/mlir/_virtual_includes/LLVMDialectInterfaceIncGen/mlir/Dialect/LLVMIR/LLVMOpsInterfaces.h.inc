/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Interface Declarations                                                     *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace LLVM {
class FastmathFlagsInterface;
namespace detail {
struct FastmathFlagsInterfaceInterfaceTraits {
  struct Concept {
    /// The methods defined by the interface.
    FastmathFlagsAttr (*getFastmathAttr)(const Concept *impl, ::mlir::Operation *);
    StringRef (*getFastmathAttrName)();
  };
  template<typename ConcreteOp>
  class Model : public Concept {
  public:
    using Interface = ::mlir::LLVM::FastmathFlagsInterface;
    Model() : Concept{getFastmathAttr, getFastmathAttrName} {}

    static inline FastmathFlagsAttr getFastmathAttr(const Concept *impl, ::mlir::Operation *tablegen_opaque_val);
    static inline StringRef getFastmathAttrName();
  };
  template<typename ConcreteOp>
  class FallbackModel : public Concept {
  public:
    using Interface = ::mlir::LLVM::FastmathFlagsInterface;
    FallbackModel() : Concept{getFastmathAttr, getFastmathAttrName} {}

    static inline FastmathFlagsAttr getFastmathAttr(const Concept *impl, ::mlir::Operation *tablegen_opaque_val);
    static inline StringRef getFastmathAttrName();
  };
  template<typename ConcreteModel, typename ConcreteOp>
  class ExternalModel : public FallbackModel<ConcreteModel> {
  public:
    using ConcreteEntity = ConcreteOp;
    FastmathFlagsAttr getFastmathAttr(::mlir::Operation *tablegen_opaque_val) const;
    static StringRef getFastmathAttrName();
  };
};template <typename ConcreteOp>
struct FastmathFlagsInterfaceTrait;

} // namespace detail
class FastmathFlagsInterface : public ::mlir::OpInterface<FastmathFlagsInterface, detail::FastmathFlagsInterfaceInterfaceTraits> {
public:
  using ::mlir::OpInterface<FastmathFlagsInterface, detail::FastmathFlagsInterfaceInterfaceTraits>::OpInterface;
  template <typename ConcreteOp>
  struct Trait : public detail::FastmathFlagsInterfaceTrait<ConcreteOp> {};
  /// Returns a FastmathFlagsAttr attribute for the operation
  FastmathFlagsAttr getFastmathAttr();
  /// Returns the name of the FastmathFlagsAttr attribute
  ///                          for the operation
  StringRef getFastmathAttrName();
};
namespace detail {
  template <typename ConcreteOp>
  struct FastmathFlagsInterfaceTrait : public ::mlir::OpInterface<FastmathFlagsInterface, detail::FastmathFlagsInterfaceInterfaceTraits>::Trait<ConcreteOp> {
    /// Returns a FastmathFlagsAttr attribute for the operation
    FastmathFlagsAttr getFastmathAttr() {
      ConcreteOp op = cast<ConcreteOp>(this->getOperation());
        return op.getFastmathFlagsAttr();
    }
    /// Returns the name of the FastmathFlagsAttr attribute
    ///                          for the operation
    static StringRef getFastmathAttrName() {
      return "fastmathFlags";
    }
  };
}// namespace detail
} // namespace LLVM
} // namespace mlir
namespace mlir {
namespace LLVM {
template<typename ConcreteOp>
FastmathFlagsAttr detail::FastmathFlagsInterfaceInterfaceTraits::Model<ConcreteOp>::getFastmathAttr(const Concept *impl, ::mlir::Operation *tablegen_opaque_val) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getFastmathAttr();
}
template<typename ConcreteOp>
StringRef detail::FastmathFlagsInterfaceInterfaceTraits::Model<ConcreteOp>::getFastmathAttrName() {
  return ConcreteOp::getFastmathAttrName();
}
template<typename ConcreteOp>
FastmathFlagsAttr detail::FastmathFlagsInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getFastmathAttr(const Concept *impl, ::mlir::Operation *tablegen_opaque_val) {
  return static_cast<const ConcreteOp *>(impl)->getFastmathAttr(tablegen_opaque_val);
}
template<typename ConcreteOp>
StringRef detail::FastmathFlagsInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getFastmathAttrName() {
  return ConcreteOp::getFastmathAttrName();
}
template<typename ConcreteModel, typename ConcreteOp>
FastmathFlagsAttr detail::FastmathFlagsInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::getFastmathAttr(::mlir::Operation *tablegen_opaque_val) const {
ConcreteOp op = cast<ConcreteOp>(this->getOperation());
        return op.getFastmathFlagsAttr();
}
template<typename ConcreteModel, typename ConcreteOp>
StringRef detail::FastmathFlagsInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::getFastmathAttrName() {
return "fastmathFlags";
}
} // namespace LLVM
} // namespace mlir
