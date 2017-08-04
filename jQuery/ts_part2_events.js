// $('h1').click(function(){
//     console.log('There was a click')
// })
//
// $('li').click(function(){
//     console.log('any li was clicked')
// })
//
// $('h1').click(function(){
//     $(this).text("I was changed")
// })
//
//KEY PRESS
// $('input').eq(0).keypress(function(event){
//     //$('h3').toggleClass('turnBlue');
//     //console.log(event);
//     if (event.which === 13){
//         $('h3').toggleClass('turnBlue');
//     }
// })
//
//on()
// $('h1').on('mouseenter', function(){
//     $(this).toggleClass('turnBlue')
// })
//
//animations and effects
$('input').eq(1).on('click', function(){
    $('.container').fadeOut(3000)
    $('.container').fadeIn(3000)
    $('.container').slideUp(3000)
})
