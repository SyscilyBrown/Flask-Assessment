class  list_of_conversions {
    resp = await axios.get("/conversionoutput", { params: { conversion_input: conversion_input, conversion_output: conversion_output, amount: amount}});

    
    
    


}

//if result = "ok", just return okay
//if result = "invalid-conversion" return {{conversion}} is invalid 