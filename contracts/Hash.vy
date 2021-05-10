# @version ^0.2.0
@external
@view
def foo(_value: Bytes[100]) -> bytes32:
    return keccak256(_value)