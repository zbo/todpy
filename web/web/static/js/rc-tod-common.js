function active_nav_path(path){
    //debugger
    if(path.substr(path.length-1)=='/'){
        path=path.substr(0,path.length-1)
    }
    filter="a[href='"+path+"']"
    $(".sidebar").find(filter).closest("li").addClass("active");
}