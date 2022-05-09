odoo.define('code_backend_theme.SidebarMenu', function (require) {
    "use strict";
    //require('web.dom_ready');
    const config = require("web.config");
    const Menu = require("web.Menu");
    const SideBar = require("code_backend_theme.SideBar");
   // var Menu = require('web.Menu');
    //var UserMenu = require('web.UserMenu');
    //var Menu = require('web.Menu');

    Menu.include({
        start() {
            var res = this._super.apply(this, arguments);
            this.sidebar_apps = this.$('.sidebar_panel');
            this._sideBar = new SideBar(this, this.menu_data);
            var sideBar = this._sideBar.appendTo(this.sidebar_apps);
            return res, sideBar
        },        
    }); 
    $(document).ready(function(){   
        $('.sidebar ul.sidebar_menu li a#Apps').removeAttr('href');
        $('.sidebar ul.sidebar_menu li a#Settings').removeAttr('href');        
        // add logo on header
        // let headerLogo = $('#header_logo').html();
        // console.log(headerLogo);
        // $(window).on('load', function(){
        //     $('.nabar_logo').addClass('headerLogo');
        // });


        $('.sidebar div > div ul li a.nav-toggle').on('click', function(e){
            e.stopPropagation();
            
           let menuName = $(this).attr('id');
            hideMenu(menuName);

            
            $('.sidebar div > div ul li > a').removeClass('active');
            $(this).addClass('active');

            $('.o_sub_menu_content').addClass('active');
            // add overlay
            if($('.submenu_overlay').length > 0){
                $('.submenu_overlay').remove();
            }
            $('.o_main_content').append('<div class="submenu_overlay"></div>');
            if( gMenuName == $(this).attr('id')){
                $('.o_sub_menu_content').removeClass('active');
                $('.submenu_overlay').remove();
                gMenuName = '';
            }else{
                gMenuName = $(this).attr('id');
            }
        });  
    });


  


    $(".sidebar_menu li").click(function(){
        $("a.nav-link").addClass("blue");    
      });

    $('.sidebar_menu li a.nav-toggle').on('click', function(e){
        e.stopPropagation();         
       let menuName = $(this).attr('id'); 
        hideMenu(menuName);
    });

    function hideMenu(menuName){
        if(menuName == 'Settings'){
        }
    }

    $(document).on("click", "#closeSidebar", function(event) {
        $("#sidebar_panel").css({'display':'block'});
        $(".o_action_manager").css({'margin-left': '120px','transition':'all .1s linear'});
        $(".top_heading").css({'margin-left': '100px','transition':'all .1s linear'});

        //add class in navbar
        var navbar = $(".o_main_navbar");
        var navbar_id = navbar.data("id");
        $("nav").addClass(navbar_id);
        navbar.addClass("small_nav");

        //add class in action-manager
        var action_manager = $(".o_action_manager");
        var action_manager_id = action_manager.data("id");
        $("div").addClass(action_manager_id);
        action_manager.addClass("sidebar_margin");

        //add class in top_heading
        var top_head = $(".top_heading");
        var top_head_id = top_head.data("id");
        $("div").addClass(top_head_id);
        top_head.addClass("sidebar_margin");

        $("#closeSidebar").hide();
        $("#openSidebar").show();
    });
    
    $(document).on("click", "#openSidebar", function(event){
        if($(".o_action_manager").hasClass('sub_overlay')) {
            $(".o_action_manager").removeClass('sub_overlay'); 
        }
        $("#sidebar_panel").css({'display':'none'});
        $(".o_sub_menu_content").css({'display':'none'});
        $(".o_action_manager").css({'margin-left': '0px'});
        $(".top_heading").css({'margin-left': '0px'});

        //remove class in navbar
        var navbar = $(".o_main_navbar");
        var navbar_id = navbar.data("id");
        $("nav").removeClass(navbar_id);
        navbar.removeClass("small_nav");

        //remove class in action-manager
        var action_manager = $(".o_action_manager");
        var action_manager_id = action_manager.data("id");
        $("div").removeClass(action_manager_id);
        action_manager.removeClass("sidebar_margin");

        //remove class in top_heading
        var top_head = $(".top_heading");
        var top_head_id = top_head.data("id");
        $("div").removeClass(top_head_id);
        top_head.removeClass("sidebar_margin");

        
        $("#openSidebar").hide();
        $("#closeSidebar").show();
    });

    $(document).on("click", ".sidebar_menu a", function(event) {        
        event.stopPropagation();
        var menu = $(".sidebar_menu a");
        var menuli = $(".o_sub_menu_content li");
        var $this = $(this); 
        var id = $this.data("id");
        var menuID = $this[0].dataset.menuId; 
            $("header").removeClass().addClass(id);
            menu.removeClass("active");
            $this.addClass("active");
            menu.css({'color':'#fff'});
            menuli.css(
                {
                'color':'#fff',
               'list-style':'none'
            });
            if( menuID == '5')
            {             
           $(".o_action_manager").toggleClass('sub_overlay');
           $(".o_sub_menu_content").toggle();
           $(".sidebar_panel").css({'overflow':'visible'});
           $(".o_sub_menu_content").css(
               {'position':'absolute',
               'top':'65px','left':'120px',
               'width':'100%','height':'100%',
               'background-color':'#fff',
               'z-index':'9999',
               'background':'#0f172a', 
               'transition' : 'all 0.1s linear 0s',
                'width':'260px'
            });
    
            //sidebar close on menu-item click
            $("#sidebar_panel").css({'display':'block'});
            $(".o_action_manager").css({'margin-left': '120px'});
            $(".top_heading").css({'margin-left': '100px'});
            $("#closeSidebar").hide();
            $("#openSidebar").show();
        }

        else {
            remove_overlay();
        }


        //remove class in navbar
        // var navbar = $(".o_main_navbar");
        // var navbar_id = navbar.data("id");
        // $("nav").addClass(navbar_id);
        // navbar.addClass("small_nav");

        //remove class in action-manager
        // var action_manager = $(".o_action_manager");
        // var action_manager_id = action_manager.data("id");
        // $("div").addClass(action_manager_id);
        // action_manager.addClass("sidebar_margin");

        //remove class in top_heading
        // var top_head = $(".top_heading");
        // var top_head_id = top_head.data("id");
        // $("div").addClass(top_head_id);
        // top_head.addClass("sidebar_margin");
    });

    
    $(document).on("click", ".o_sub_menu_content a", function(event) { 
        remove_overlay();         
        var $this = $(this); 
        var menuID = $this[0].dataset.menuId; 
        if(menuID == 5 ) {
            $(".o_sub_menu_content").toggle();
        }        
     });
 
     $(document).on("click", ".sub_overlay", function() { 
            remove_overlay();
            $(".o_sub_menu_content").toggle();
    });

    $(document).on("click", ".o_sub_menu_content a", function(event) { 
        $('.sidebar_menu li:nth-child(5) a').addClass('active');
     });

function remove_overlay() {
    if($(".o_action_manager").hasClass('sub_overlay')) {
        $(".o_action_manager").removeClass('sub_overlay'); 
    }
}


});