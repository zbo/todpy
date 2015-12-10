$(document).ready(function(){
  console.log("page document ready");
});
function getEndingFromUrl(){
  return window.location.pathname.split('/')
}
