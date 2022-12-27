// create a dictionary of result 
var result = {};


$(document).ready(function(){
    $("#submit").click(function(){
        var q1 = $("input[name='q1']:checked").val();
        var q2 = $("input[name='q2']:checked").val();
        var q3 = $("input[name='q3']:checked").val();
        var q4 = $("input[name='q4']:checked").val();
        var q5 = $("input[name='q5']:checked").val();
        var q6 = $("input[name='q6']:checked").val();
        var total = parseInt(q1) + parseInt(q2) + parseInt(q3) + parseInt(q4) + parseInt(q5) + parseInt(q6);
        if (total >= 3){
            alert("You are at risk of depression. Please seek help.");
            // result['depression'] = "true";
            // alert(result['depression']);
            window.location.href = "face?dep=true";
        }
        else{
            alert("You are not at risk of depression.");
            window.location.href = "face";
        }
    });
});

// if /face is called, then the result dictionary is sent to the server
// get the url of the current page
var url = window.location.href;
// if the url contains /face
if (url.includes("/face")){
    // send the result dictionary to the server
    console.log(result);
}