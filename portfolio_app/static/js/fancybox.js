	
  $(function(){
  
    $(".single-image").fancybox({
      openEffect : 'elastic',   //'fade', 'elastic'
        closeEffect	: 'elastic',
        openSpeed:'normal', //ms, slow, normal, fast (default 250ms)
        closeSpeed:'normal',
        helpers : {
          title : {
            type : 'inside' //'float', 'inside', 'outside' or 'over'
          },
          overlay : {
            closeClick : true  // if true, se cierra al hacer click fuera de la imagen
               }
        },
        padding:11
        
    });
    
    $(".gallery-image").fancybox({
      openEffect : 'fade', 
        closeEffect	: 'fade',
        closeBtn: false,
        helpers : {
          title : {
            type : 'over' //'float', 'inside', 'outside' or 'over'
          },
          thumbs : {
                width: 50
            },
            buttons	: {},
            overlay : {
                css : {
                    'background' : 'rgba(0,0,0,0.5)'
                }
            }
        
        }
                  
    });
    
    
    $(".fancyOther").fancybox({
      width		: '70%',
      height		: '70%',
      maxWidth	: 800,
      maxHeight	: 600,
      fitToView	: false,
      autoSize	: false,
      closeClick	: false,
      openEffect	: 'none',
      closeEffect	: 'none'
    });
    
    
    $(".fancyOther2").click(function(){
      $.fancybox( '<div><h1>Lorem Lipsum</h1><p>Lorem lipsum</p></div>', {
            title : 'Custom Title',
            width		: '70%',
        height		: '70%',
        maxWidth	: 800,
        maxHeight	: 600,
        fitToView	: false,
        autoSize	: false,
        closeClick	: false	 
      });
    });
    
    
    $(".fancyMedia").fancybox({	
      helpers : {
        media : {}
      }
    });
    
    $(".fancyMediaMapa").fancybox({	
      helpers : {
        media : {}
      },
       width		: '100%',
      height		: '100%'
      
    });

    
    
  
    
  });
  
  