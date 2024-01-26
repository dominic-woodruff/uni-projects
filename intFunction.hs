--Dominic Woodruff

--Representation of F(x, y, z) using ints
fFunctionInt :: Integer -> Integer  -> Integer -> Integer
fFunctionInt x y z = (2 + x) `div` (3 * y - z)

--Representation of F(x, y, z) using doubles
fFunctionDouble :: Double -> Double -> Double -> Double
fFunctionDouble x y z = (2 + x) / (3 * y - z)