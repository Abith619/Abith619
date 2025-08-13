/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Interface Definitions                                                      *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

/// Returns a FastmathFlagsAttr attribute for the operation
FastmathFlagsAttr mlir::LLVM::FastmathFlagsInterface::getFastmathAttr() {
      return getImpl()->getFastmathAttr(getImpl(), getOperation());
  }
/// Returns the name of the FastmathFlagsAttr attribute
///                          for the operation
StringRef mlir::LLVM::FastmathFlagsInterface::getFastmathAttrName() {
      return getImpl()->getFastmathAttrName();
  }
