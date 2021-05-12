# @version^0.2.0

# define Curve Point on the first curve (G1) struct
struct G1Point:
    X: uint256
    Y: uint256

struct G2Point:
    X: uint256[2]
    Y: uint256[2]

@view
@external
def P1() -> G1Point:
    return G1Point({X: 1, Y:2})

@view
@external
def P2() -> G2Point:
    return G2Point({
        X:[11559732032986387107991004021392285783925812861821192530917403151452391805634,
            10857046999023057135944570762232829481370756359578518086990519993285655852781],
        Y:[4082367875863433681332203403145435568316851327593401208105741076214120093531,
            8495653923123431417604973247489272438418190587263600148770280649306958101930]
    })