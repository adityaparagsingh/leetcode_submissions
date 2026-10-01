/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    
  if(Array.isArray(obj)){
        for(let i = 0; i < obj.length; i++){
            return false;
        }
        return true;
    }
    for(let key in obj){
        return false;
    }
    return true;
};