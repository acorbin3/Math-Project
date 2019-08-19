Math library utilities

--Floor--
TODO

--Sine--
TODO

--Cosine--
TODO

--Square Root--
TODO

--Power--
Strategy: Ensure to test a few cases of the base when exponent is 0 even though the base doesnt matter
Math_TC_1. When exponent is equal to 0 and base is 0, return value of 1
Math_TC_2. When exponent is equal to 0 and base is 10, return value of 1

Strategy: Ensure to test when base is > 0 and exponent is > 0
Math_TC_3. When exponent is 2 and base is 2, return value 4
Math_TC_4. When exponent is 5 and base is 3, return value 243

Strategy: Ensure to test when exponent is < 0
Math_TC_5. When the base is 4 and exponent is -4, return value 0.00390625
Math_TC_6. When the base is 2 and exponent is -7, return value 0.0078125

Strategy: Ensure to test error cases
Math_TC_7. when base is zero and exponent is less than 0, raise an error that there is an invalid input


--New Section--
--TODO : Add new section