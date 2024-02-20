$(window).scroll(function() {
      $('nav').toggleClass('scrolled', $(this).scrollTop() > 50);
      $("#newsletter-alert").hide(200);
      console.log("SCROLLED");
    });

    var fixedCls = '.navbar-fixed-top,.navbar-fixed-bottom';
    var oldSSB = $.fn.modal.Constructor.prototype.setScrollbar;
    $.fn.modal.Constructor.prototype.setScrollbar = function () {
        oldSSB.apply(this);
        if (this.bodyIsOverflowing && this.scrollbarWidth)
            $(fixedCls).css('padding-right', this.scrollbarWidth);
    }

    var oldRSB = $.fn.modal.Constructor.prototype.resetScrollbar;
    $.fn.modal.Constructor.prototype.resetScrollbar = function () {
        oldRSB.apply(this);
        $(fixedCls).css('padding-right', '');
    }

     //Trigger searchbar open on click
    $('#nav-search-ani.search-ani').hover(function() {
      $('#nav-search-ani.search-ani').css({
        'width': '180px',
        'cursor': 'pointer'
      });
      $('#nav-search.search').css({
        'display': 'block'
      });
      $('#nav-fa-search.fa-search').css({
        'background': '#07051a',
        'color': '#fff'
      });
    });

    $('#foot-search-ani.search-ani').hover(function() {
      $('#foot-search-ani.search-ani').css({
        'width': '180px',
        'cursor': 'pointer'
      });
      $('#foot-search.search').css({
        'display': 'block'
      });
      $('#foot-fa-search.fa-search').css({
        'background': '#07051a',
        'color': '#fff'
      });
    });

    $('label.menu-icon').click(function() {
    $('nav').toggleClass('clicked');
    console.log("YAY");
    });
