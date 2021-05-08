# @version ^0.2.0
@external
@view
def foo(hash: bytes32, v: uint256, r:uint256, s:uint256) -> address:
    return ecrecover(hash, v, r, s)